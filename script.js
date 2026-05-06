// 💎 CRYSTΔL Core Script
let currentUser=null,currentUserData=null,currentShareUrl=null;
let allUsers={},allVideos=[],allSounds={};
let isMuted=true,currentFeed='forYou';

// ===== AUTH CHECK =====
auth.onAuthStateChanged(async u=>{
    if(!u){window.location.replace('auth.html');return}
    currentUser=u;
    const snap=await db.ref('users/'+u.uid).get();
    if(snap.exists())currentUserData={uid:u.uid,...snap.val()};
    loadUsers();loadVideos();
    db.ref('presence/'+u.uid).set(true);
    db.ref('presence/'+u.uid).onDisconnect().remove();
});

function loadUsers(){db.ref('users').on('value',s=>{allUsers=s.val()||{}})}

function loadVideos(){
    db.ref('videos').on('value',s=>{
        const data=s.val();
        if(!data){allVideos=[];renderVideos();return}
        allVideos=[];allSounds={};
        Object.keys(data).forEach(k=>{const v={id:k,...data[k]};allVideos.push(v);if(v.music)allSounds[v.music]=(allSounds[v.music]||0)+1});
        allVideos.sort((a,b)=>(b.timestamp||0)-(a.timestamp||0));
        renderVideos();
    });
}

function renderVideos(){
    const c=document.getElementById('videosWrap');if(!c)return;
    c.innerHTML='';
    let fv=currentFeed==='forYou'?allVideos:allVideos.filter(v=>currentUserData?.following?.[v.sender]);
    if(!fv.length){c.innerHTML='<div class="load-center"><div class="spinner"></div><span>لا توجد فيديوهات</span></div>';return}
    fv.forEach(v=>{
        const liked=v.likedBy&&v.likedBy[currentUser?.uid];
        const user=allUsers[v.sender]||{username:v.senderName||'user'};
        const following=currentUserData?.following&&currentUserData.following[v.sender];
        const cc=v.comments?Object.keys(v.comments).length:0;
        const cap=(v.description||'').replace(/#(\w+)/g,'<span class="tag" onclick="searchTag(\'$1\')">#$1</span>');
        const avUrl=user.avatarUrl||(DICEBEAR_URL+'?seed='+v.sender);
        const div=document.createElement('div');div.className='vid-card';
        div.innerHTML=`
            <video loop playsinline muted data-src="${v.url}" poster="${v.thumbnail||''}"></video>
            <div class="vid-info">
                <div class="author-row">
                    <div class="author-avatar" onclick="window.location.href='profile.html'"><img src="${avUrl}"></div>
                    <div class="author-name">
                        <span onclick="window.location.href='profile.html'">@${user.username}</span>
                        ${user.isVerified?'<span class="badge">✅</span>':''}
                        ${currentUser?.uid!==v.sender?`<button class="btn-follow" onclick="toggleFollow('${v.sender}',this)">${following?'متابع':'متابعة'}</button>`:''}
                    </div>
                </div>
                <div class="caption">${cap}</div>
                <div class="music" onclick="searchSound('${v.music||'Original Sound'}')"><i class="fas fa-music"></i> ${v.music||'Original Sound'}</div>
            </div>
            <div class="side-btns">
                <button class="sbtn" onclick="toggleMute()"><i class="fas ${isMuted?'fa-volume-mute':'fa-volume-up'}"></i></button>
                <button class="sbtn like-btn ${liked?'liked':''}" onclick="toggleLike('${v.id}',this)"><i class="fas fa-heart"></i><span class="cnt">${v.likes||0}</span></button>
                <button class="sbtn" onclick="openComments('${v.id}')"><i class="fas fa-comment"></i><span class="cnt">${cc}</span></button>
                <button class="sbtn" onclick="openShare('${v.url}')"><i class="fas fa-share"></i></button>
            </div>`;
        const ve=div.querySelector('video');
        ve.addEventListener('dblclick',e=>{e.stopPropagation();const lb=div.querySelector('.like-btn');if(lb){toggleLike(v.id,lb);showHeart(e.clientX,e.clientY)}});
        c.appendChild(div);
    });
    initObs();
}

function showHeart(x,y){const h=document.createElement('div');h.className='heart-fly';h.innerHTML='❤️';h.style.left=(x-40)+'px';h.style.top=(y-40)+'px';document.body.appendChild(h);setTimeout(()=>h.remove(),800)}

function initObs(){
    const ob=new IntersectionObserver(entries=>{entries.forEach(e=>{const v=e.target.querySelector('video');if(e.isIntersecting){if(!v.src)v.src=v.dataset.src;v.muted=isMuted;v.play().catch(()=>{})}else v.pause()})},{threshold:0.65});
    document.querySelectorAll('.vid-card').forEach(s=>ob.observe(s));
}

function toggleMute(){isMuted=!isMuted;document.querySelectorAll('video').forEach(v=>v.muted=isMuted);document.querySelectorAll('.side-btns .sbtn:first-child i').forEach(b=>b.className=isMuted?'fas fa-volume-mute':'fas fa-volume-up')}

function switchFeed(f){currentFeed=f;document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));event.target.classList.add('active');renderVideos()}

async function toggleLike(vid,btn){
    if(!currentUser)return;
    const ref=db.ref('videos/'+vid);const snap=await ref.get();const v=snap.val();if(!v)return;
    let l=v.likes||0,lb=v.likedBy||{};
    if(lb[currentUser.uid]){l--;delete lb[currentUser.uid]}else{l++;lb[currentUser.uid]=true;addNotif(v.sender,'like')}
    await ref.update({likes:l,likedBy:lb});btn.classList.toggle('liked');const cs=btn.querySelector('.cnt');if(cs)cs.innerText=l;
}

async function toggleFollow(uid,btn){
    if(!currentUser||currentUser.uid===uid)return;
    const ur=db.ref('users/'+currentUser.uid+'/following/'+uid);const tr=db.ref('users/'+uid+'/followers/'+currentUser.uid);
    const snap=await ur.get();
    if(snap.exists()){await ur.remove();await tr.remove();btn.innerText='متابعة';addNotif(uid,'unfollow')}else{await ur.set(true);await tr.set(true);btn.innerText='متابع';addNotif(uid,'follow')}
}

async function openComments(vid){
    const snap=await db.ref('videos/'+vid+'/comments').get();const cs=snap.val()||{};
    let html='<div style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(5,5,16,0.97);backdrop-filter:blur(40px);z-index:400;overflow-y:auto"><div style="padding:16px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.08);position:sticky;top:0;background:rgba(5,5,16,0.8);backdrop-filter:blur(20px)"><h3 style="font-weight:700">💬 التعليقات</h3><button onclick="this.closest(\'div\').parentElement.remove()" style="background:rgba(255,255,255,0.08);border:none;color:#fff;width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:18px"><i class="fas fa-times"></i></button></div><div style="padding:16px">';
    Object.values(cs).reverse().forEach(c=>{const u=allUsers[c.userId]||{username:c.username||'user'};html+=`<div style="display:flex;gap:10px;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.05)"><img src="${u.avatarUrl||(DICEBEAR_URL+'?seed='+c.userId)}" style="width:36px;height:36px;border-radius:50%"><div><div style="font-weight:600">@${u.username}</div><div style="font-size:13px;opacity:0.8;margin-top:2px">${c.text}</div></div></div>`)});
    html+=`</div><div style="display:flex;gap:8px;padding:12px;background:rgba(5,5,16,0.9);position:sticky;bottom:0"><input type="text" id="cmtInput" placeholder="أضف تعليقاً..." style="flex:1;padding:12px 16px;border-radius:30px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);color:#fff;font-size:14px;outline:none"><button onclick="addCmt('${vid}')" style="background:linear-gradient(135deg,#6366f1,#06b6d4);border:none;color:#fff;padding:12px 20px;border-radius:30px;font-weight:700;cursor:pointer">نشر</button></div></div>`;
    document.body.insertAdjacentHTML('beforeend',html);
}
window.addCmt=async function(vid){const inp=document.getElementById('cmtInput');if(!inp||!inp.value.trim())return;await db.ref('videos/'+vid+'/comments').push({userId:currentUser.uid,username:currentUserData?.username,text:inp.value,timestamp:Date.now()});document.querySelector('[style*="z-index:400"]').remove();openComments(vid)};

function openShare(url){
    currentShareUrl=url;
    let html='<div style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(5,5,16,0.97);backdrop-filter:blur(40px);z-index:400;overflow-y:auto"><div style="padding:16px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.08)"><h3 style="font-weight:700">📤 مشاركة</h3><button onclick="this.closest(\'div\').parentElement.remove()" style="background:rgba(255,255,255,0.08);border:none;color:#fff;width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:18px"><i class="fas fa-times"></i></button></div><div style="padding:16px">';
    html+=`<div onclick="copyLink()" style="display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid rgba(255,255,255,0.05);cursor:pointer"><i class="fas fa-link" style="color:#6366f1;font-size:20px"></i><span>نسخ الرابط</span></div>`;
    html+=`<div onclick="shareWA()" style="display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid rgba(255,255,255,0.05);cursor:pointer"><i class="fab fa-whatsapp" style="color:#25D366;font-size:20px"></i><span>WhatsApp</span></div>`;
    html+=`<div onclick="shareTG()" style="display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid rgba(255,255,255,0.05);cursor:pointer"><i class="fab fa-telegram" style="color:#0088cc;font-size:20px"></i><span>Telegram</span></div>`;
    html+=`<div onclick="downloadVid()" style="display:flex;align-items:center;gap:12px;padding:14px;cursor:pointer"><i class="fas fa-download" style="color:#06b6d4;font-size:20px"></i><span>تنزيل</span></div></div></div>`;
    document.body.insertAdjacentHTML('beforeend',html);
}
window.copyLink=function(){navigator.clipboard.writeText(currentShareUrl);showToast();closePanel()};
window.shareWA=function(){window.open('https://wa.me/?text='+encodeURIComponent(currentShareUrl));closePanel()};
window.shareTG=function(){window.open('https://t.me/share/url?url='+encodeURIComponent(currentShareUrl));closePanel()};
window.downloadVid=function(){window.open(currentShareUrl);closePanel()};
function closePanel(){const p=document.querySelector('[style*="z-index:400"]');if(p)p.remove()}
function showToast(){const t=document.getElementById('toast');if(t){t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2000)}}

async function addNotif(target,type){
    if(target===currentUser.uid)return;
    const msgs={like:'💙 أعجب بفيديوك',comment:'💬 علق',follow:'👋 بدأ بمتابعتك',unfollow:'توقف'};
    await db.ref('notifications/'+target).push({from:currentUserData?.username||'مستخدم',msg:msgs[type],timestamp:Date.now(),read:false});
}

async function openNotifs(){
    const snap=await db.ref('notifications/'+currentUser.uid).once('value');const ns=snap.val()||{};
    let html='<div style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(5,5,16,0.97);backdrop-filter:blur(40px);z-index:400;overflow-y:auto"><div style="padding:16px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.08)"><h3 style="font-weight:700">🔔 الإشعارات</h3><button onclick="this.closest(\'div\').parentElement.remove()" style="background:rgba(255,255,255,0.08);border:none;color:#fff;width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:18px"><i class="fas fa-times"></i></button></div><div style="padding:16px">';
    Object.values(ns).reverse().forEach(n=>{html+=`<div style="display:flex;gap:12px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.05)"><i class="fas fa-bell" style="color:#6366f1;font-size:20px;margin-top:4px"></i><div><div style="font-weight:600">${n.from}</div><div style="font-size:12px;opacity:0.6">${n.msg}</div></div></div>`)});
    html+='</div></div>';document.body.insertAdjacentHTML('beforeend',html);
}

function openSearch(){
    let html='<div style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(5,5,16,0.97);backdrop-filter:blur(40px);z-index:400;overflow-y:auto"><div style="padding:16px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.08)"><h3 style="font-weight:700">🔍 بحث</h3><button onclick="this.closest(\'div\').parentElement.remove()" style="background:rgba(255,255,255,0.08);border:none;color:#fff;width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:18px"><i class="fas fa-times"></i></button></div><div style="padding:16px"><input type="text" id="searchQ" onkeyup="doSearch()" placeholder="ابحث..." style="width:100%;padding:14px 18px;border-radius:30px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);color:#fff;font-size:14px;outline:none;margin-bottom:16px"><div id="searchR"></div></div></div>';
    document.body.insertAdjacentHTML('beforeend',html);
    window.doSearch=function(){
        const q=document.getElementById('searchQ').value.toLowerCase();const rd=document.getElementById('searchR');if(!q){rd.innerHTML='';return}
        const users=Object.values(allUsers).filter(u=>u.username?.toLowerCase().includes(q));
        const vids=allVideos.filter(v=>(v.description||'').toLowerCase().includes(q)||(v.music||'').toLowerCase().includes(q));
        rd.innerHTML=`${users.length?`<div style="margin-bottom:16px"><h4 style="font-size:12px;opacity:0.5;margin-bottom:8px">👥 مستخدمين</h4>${users.map(u=>`<div onclick="window.location.href='profile.html'" style="display:flex;align-items:center;gap:10px;padding:10px;border-bottom:1px solid rgba(255,255,255,0.05);cursor:pointer"><img src="${u.avatarUrl||(DICEBEAR_URL+'?seed='+u.uid||u.username)}" style="width:40px;height:40px;border-radius:50%"><div>@${u.username} ${u.isVerified?'<span style="color:#a5b4fc">✅</span>':''}</div></div>`).join('')}</div>`:''}${vids.length?`<div><h4 style="font-size:12px;opacity:0.5;margin-bottom:8px">🎬 فيديوهات</h4>${vids.map(v=>`<div onclick="window.open('${v.url}')" style="display:flex;align-items:center;gap:10px;padding:10px;border-bottom:1px solid rgba(255,255,255,0.05);cursor:pointer"><i class="fas fa-play-circle" style="color:#6366f1;font-size:20px"></i><span style="font-size:13px">${(v.description||'فيديو').substring(0,40)}</span></div>`).join('')}</div>`:''}${!users.length&&!vids.length?'<div style="text-align:center;opacity:0.5;padding:30px">لا نتائج</div>':''}`;
    };
}

function searchTag(tag){openSearch();setTimeout(()=>{const inp=document.getElementById('searchQ');if(inp){inp.value='#'+tag;doSearch()}},300)}
function searchSound(s){openSearch();setTimeout(()=>{const inp=document.getElementById('searchQ');if(inp){inp.value=s;doSearch()}},300)}

function navTo(t){
    document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
    if(event.target.closest('.nav-item'))event.target.closest('.nav-item').classList.add('active');
    if(t==='search')openSearch();
    if(t==='notifs')openNotifs();
    if(t==='home'){const p=document.querySelector('[style*="z-index:400"]');if(p)p.remove()}
}
