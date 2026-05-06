// 💎 CRYSTΔL TIKTOK 2026 - Core Script
const ADMIN_EMAILS=['jasim28v@gmail.com'];
let isAdmin=false,currentUser=null,currentUserData=null,currentVideoId=null;
let currentShareUrl=null,allUsers={},allVideos=[],allSounds={};
let isMuted=true,viewingProfileUserId=null,currentFeed='forYou';
let selectedVideoFile=null,currentChatUserId=null;

// ===== AUTH =====
function logout(){auth.signOut();location.replace('login.html')}
function checkAdminStatus(){
    if(currentUser&&ADMIN_EMAILS.includes(currentUser.email)){isAdmin=true;return true}
    isAdmin=false;return false
}

// ===== LOAD USER DATA =====
async function loadUserData(){
    const snap=await db.ref('users/'+currentUser.uid).get();
    if(snap.exists())currentUserData={uid:currentUser.uid,...snap.val()}
}
db.ref('users').on('value',s=>{allUsers=s.val()||{}});

// ===== VIDEOS =====
db.ref('videos').on('value',s=>{
    const data=s.val();
    if(!data){allVideos=[];renderVideos();return}
    allVideos=[];allSounds={};
    Object.keys(data).forEach(k=>{
        const v={id:k,...data[k]};allVideos.push(v);
        if(v.music)allSounds[v.music]=(allSounds[v.music]||0)+1
    });
    allVideos.sort((a,b)=>(b.timestamp||0)-(a.timestamp||0));
    renderVideos()
});

function renderVideos(){
    const c=document.getElementById('videosContainer');if(!c)return;
    c.innerHTML='';
    let fv=currentFeed==='forYou'?allVideos:allVideos.filter(v=>currentUserData?.following?.[v.sender]);
    if(!fv.length){c.innerHTML='<div class="loading-center"><div class="spinner"></div><span>لا توجد فيديوهات</span></div>';return}
    fv.forEach(v=>{
        const liked=v.likedBy&&v.likedBy[currentUser?.uid];
        const user=allUsers[v.sender]||{username:v.senderName||'user',cartoonAvatar:null};
        const following=currentUserData?.following&&currentUserData.following[v.sender];
        const cc=v.comments?Object.keys(v.comments).length:0;
        const cap=(v.description||'').replace(/#(\w+)/g,'<span class="hashtag" onclick="searchTag(\'$1\')">#$1</span>');
        const avHtml=user.cartoonAvatar?`<span style="font-size:28px">${user.cartoonAvatar.emoji}</span>`:(user.avatarUrl?`<img src="${user.avatarUrl}">`:(user.username?.charAt(0)||'👤'));
        const div=document.createElement('div');div.className='video-item';
        div.innerHTML=`
            <video loop playsinline muted data-src="${v.url}" poster="${v.thumbnail||''}"></video>
            <div class="video-info">
                <div class="author-row">
                    <div class="author-avatar" onclick="viewProfile('${v.sender}')" style="background:${user.cartoonAvatar?.bg||'linear-gradient(135deg,#6366f1,#06b6d4)'}">${avHtml}</div>
                    <div class="author-name">
                        <span onclick="viewProfile('${v.sender}')">@${user.username}</span>
                        ${user.isVerified?'<span class="badge-verified">✅</span>':''}
                        ${currentUser?.uid!==v.sender?`<button class="btn-follow" onclick="toggleFollow('${v.sender}',this)">${following?'متابع':'متابعة'}</button>`:''}
                    </div>
                </div>
                <div class="caption">${cap}</div>
                <div class="music-info" onclick="searchBySound('${v.music||'Original Sound'}')"><i class="fas fa-music"></i> ${v.music||'Original Sound'}</div>
            </div>
            <div class="side-actions">
                <button class="side-btn" onclick="toggleMute()"><i class="fas ${isMuted?'fa-volume-mute':'fa-volume-up'}"></i></button>
                <button class="side-btn like-btn ${liked?'liked':''}" onclick="toggleLike('${v.id}',this)"><i class="fas fa-heart"></i><span class="count">${v.likes||0}</span></button>
                <button class="side-btn" onclick="openComments('${v.id}')"><i class="fas fa-comment"></i><span class="count">${cc}</span></button>
                <button class="side-btn" onclick="openShare('${v.url}')"><i class="fas fa-share"></i></button>
            </div>`;
        const ve=div.querySelector('video');
        ve.addEventListener('dblclick',e=>{
            e.stopPropagation();
            const lb=div.querySelector('.like-btn');
            if(lb){toggleLike(v.id,lb);showHeart(e.clientX,e.clientY)}
        });
        c.appendChild(div)
    });
    initObserver()
}

function showHeart(x,y){
    const h=document.createElement('div');h.className='heart-anim';h.innerHTML='❤️';
    h.style.left=(x-40)+'px';h.style.top=(y-40)+'px';
    document.body.appendChild(h);setTimeout(()=>h.remove(),800)
}

function initObserver(){
    const ob=new IntersectionObserver(entries=>{
        entries.forEach(e=>{
            const v=e.target.querySelector('video');
            if(e.isIntersecting){
                if(!v.src)v.src=v.dataset.src;
                v.muted=isMuted;v.play().catch(()=>{})
            }else{v.pause()}
        })
    },{threshold:0.65});
    document.querySelectorAll('.video-item').forEach(s=>ob.observe(s))
}

function toggleMute(){
    isMuted=!isMuted;
    document.querySelectorAll('video').forEach(v=>v.muted=isMuted);
    document.querySelectorAll('.side-actions .side-btn:first-child i').forEach(b=>b.className=isMuted?'fas fa-volume-mute':'fas fa-volume-up')
}

function switchFeed(f){
    currentFeed=f;
    document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
    event.target.classList.add('active');renderVideos()
}

// ===== LIKES =====
async function toggleLike(vid,btn){
    if(!currentUser)return;
    const ref=db.ref('videos/'+vid);
    const snap=await ref.get();const v=snap.val();if(!v)return;
    let l=v.likes||0,lb=v.likedBy||{};
    if(lb[currentUser.uid]){l--;delete lb[currentUser.uid]}
    else{l++;lb[currentUser.uid]=true;addNotif(v.sender,'like')}
    await ref.update({likes:l,likedBy:lb});
    btn.classList.toggle('liked');
    const cs=btn.querySelector('.count');if(cs)cs.innerText=l
}

// ===== FOLLOW =====
async function toggleFollow(uid,btn){
    if(!currentUser||currentUser.uid===uid)return;
    const ur=db.ref('users/'+currentUser.uid+'/following/'+uid);
    const tr=db.ref('users/'+uid+'/followers/'+currentUser.uid);
    const snap=await ur.get();
    if(snap.exists()){
        await ur.remove();await tr.remove();
        btn.innerText='متابعة';addNotif(uid,'unfollow')
    }else{
        await ur.set(true);await tr.set(true);
        btn.innerText='متابع';addNotif(uid,'follow')
    }
    if(viewingProfileUserId===uid)loadProfile(uid)
}

// ===== COMMENTS =====
async function openComments(vid){
    currentVideoId=vid;
    const panel=document.getElementById('commentsPanel');
    const snap=await db.ref('videos/'+vid+'/comments').get();
    const cs=snap.val()||{};
    const ct=document.getElementById('commentsList');ct.innerHTML='';
    Object.values(cs).reverse().forEach(c=>{
        const user=allUsers[c.userId]||{username:c.username||'user',cartoonAvatar:null};
        const av=user.cartoonAvatar?`<span style="font-size:24px">${user.cartoonAvatar.emoji}</span>`:(user.avatarUrl?`<img src="${user.avatarUrl}">`:(user.username?.charAt(0)||'👤'));
        ct.innerHTML+=`<div class="comment-row"><div class="comment-avatar" style="background:${user.cartoonAvatar?.bg||'linear-gradient(135deg,#6366f1,#06b6d4)'}">${av}</div><div><div style="font-weight:700">@${user.username}</div><div style="font-size:13px;opacity:0.8;margin-top:2px">${c.text}</div></div></div>`
    });
    panel.classList.add('open')
}
function closeComments(){document.getElementById('commentsPanel').classList.remove('open')}
async function addComment(){
    const inp=document.getElementById('commentInput');
    if(!inp.value.trim()||!currentVideoId)return;
    await db.ref('videos/'+currentVideoId+'/comments').push({
        userId:currentUser.uid,username:currentUserData?.username,
        text:inp.value,timestamp:Date.now()
    });
    inp.value='';openComments(currentVideoId)
}

// ===== SHARE =====
function openShare(url){currentShareUrl=url;document.getElementById('sharePanel').classList.add('open')}
function closeShare(){document.getElementById('sharePanel').classList.remove('open')}
function copyLink(){navigator.clipboard.writeText(currentShareUrl);showToast();closeShare()}
function shareWA(){window.open('https://wa.me/?text='+encodeURIComponent(currentShareUrl));closeShare()}
function shareTG(){window.open('https://t.me/share/url?url='+encodeURIComponent(currentShareUrl));closeShare()}
function downloadVid(){window.open(currentShareUrl);closeShare()}
function showToast(){
    const t=document.getElementById('toast');t.classList.add('show');
    setTimeout(()=>t.classList.remove('show'),2000)
}

// ===== NOTIFICATIONS =====
async function addNotif(target,type){
    if(target===currentUser.uid)return;
    const from=currentUserData?.username||'مستخدم';
    const msgs={like:'💙 أعجب بفيديوك',comment:'💬 علق على فيديو',follow:'👋 بدأ بمتابعتك',unfollow:'توقف عن متابعتك'};
    await db.ref('notifications/'+target).push({
        type,from,msg:msgs[type],timestamp:Date.now(),read:false
    })
}
async function openNotifications(){
    const panel=document.getElementById('notificationsPanel');
    const snap=await db.ref('notifications/'+currentUser.uid).once('value');
    const ns=snap.val()||{};
    const ct=document.getElementById('notificationsList');ct.innerHTML='';
    Object.values(ns).reverse().forEach(n=>{
        ct.innerHTML+=`<div style="display:flex;gap:12px;padding:12px 0;border-bottom:1px solid rgba(255,255,255,0.05)">
            <i class="fas ${n.type==='like'?'fa-heart':n.type==='follow'?'fa-user-plus':'fa-comment'}" style="color:#6366f1;font-size:20px;margin-top:4px"></i>
            <div><div style="font-weight:600">${n.from}</div><div style="font-size:12px;opacity:0.6">${n.msg}</div></div></div>`
    });
    panel.classList.add('open')
}
function closeNotifications(){document.getElementById('notificationsPanel').classList.remove('open')}

// ===== SEARCH =====
function openSearch(){document.getElementById('searchPanel').classList.add('open')}
function closeSearch(){document.getElementById('searchPanel').classList.remove('open')}
function searchTag(tag){document.getElementById('searchInput').value='#'+tag;openSearch();doSearch()}
function searchBySound(s){document.getElementById('searchInput').value=s;openSearch();doSearch()}
function doSearch(){
    const q=document.getElementById('searchInput').value.toLowerCase();
    const rd=document.getElementById('searchResults');
    if(!q){rd.innerHTML='';return}
    const users=Object.values(allUsers).filter(u=>u.username?.toLowerCase().includes(q));
    const vids=allVideos.filter(v=>(v.description||'').toLowerCase().includes(q)||(v.music||'').toLowerCase().includes(q));
    rd.innerHTML=`
        ${users.length?`<div style="margin-bottom:20px"><h4 style="font-size:12px;opacity:0.5;margin-bottom:8px">👥 مستخدمين</h4>${users.map(u=>`<div class="search-result" onclick="viewProfile('${u.uid}')"><div class="search-avatar" style="background:${u.cartoonAvatar?.bg||'linear-gradient(135deg,#6366f1,#06b6d4)'}">${u.cartoonAvatar?.emoji||(u.username?.charAt(0)||'👤')}</div><div>@${u.username} ${u.isVerified?'<span class="badge-verified">✅</span>':''}</div></div>`).join('')}</div>`:''}
        ${vids.length?`<div><h4 style="font-size:12px;opacity:0.5;margin-bottom:8px">🎬 فيديوهات</h4>${vids.map(v=>`<div class="search-result" onclick="playVideo('${v.url}')"><i class="fas fa-play-circle" style="font-size:24px;color:#6366f1"></i><div>${(v.description||'فيديو').substring(0,50)}</div></div>`).join('')}</div>`:''}
        ${!users.length&&!vids.length?'<div style="text-align:center;opacity:0.5;padding:30px">لا توجد نتائج</div>':''}`
}

// ===== PROFILE =====
async function viewProfile(uid){
    if(!uid)return;viewingProfileUserId=uid;
    await loadProfile(uid);document.getElementById('profilePanel').classList.add('open')
}
async function loadProfile(uid){
    const snap=await db.ref('users/'+uid).get();const u=snap.val();if(!u)return;
    const ad=document.getElementById('profileAvatarDisplay');
    if(u.cartoonAvatar){
        ad.innerHTML=`<span style="font-size:52px">${u.cartoonAvatar.emoji}</span>`;
        ad.style.background=u.cartoonAvatar.bg
    }else if(u.avatarUrl){
        ad.innerHTML=`<img src="${u.avatarUrl}" style="width:100%;height:100%;object-fit:cover;border-radius:50%">`;
        ad.style.background='white'
    }else{ad.innerHTML=u.username?.charAt(0)||'👤';ad.style.background='linear-gradient(135deg,#6366f1,#06b6d4)'}
    let nd=document.getElementById('profileNameDisplay');nd.innerText=u.username||'مستخدم';
    if(u.isVerified)nd.innerHTML+=' <span class="badge-verified">✅</span>';
    document.getElementById('profileBioDisplay').innerText=u.bio||'';
    document.getElementById('profileFollowing').innerText=Object.keys(u.following||{}).length;
    document.getElementById('profileFollowers').innerText=Object.keys(u.followers||{}).length;
    const uvs=allVideos.filter(v=>v.sender===uid);
    document.getElementById('profileLikes').innerText=uvs.reduce((s,v)=>s+(v.likes||0),0);
    const vc=document.getElementById('profileVideosList');vc.innerHTML='';
    if(!uvs.length)vc.innerHTML='<div style="text-align:center;opacity:0.5;padding:30px">لا توجد فيديوهات</div>';
    else uvs.forEach(v=>{
        const t=document.createElement('div');t.className='video-thumb';
        t.innerHTML=`<i class="fas fa-play"></i>${v.thumbnail?`<img src="${v.thumbnail}" class="thumb-bg">`:''}`;
        t.onclick=()=>playVideo(v.url);vc.appendChild(t)
    });
    const aa=document.getElementById('profileActions');aa.innerHTML='';
    if(uid===currentUser?.uid){
        aa.innerHTML=`<button class="btn-follow" onclick="openEditProfile()" style="margin:5px">✏️ تعديل</button>
        <button style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);padding:8px 20px;border-radius:30px;color:#fff;cursor:pointer;margin:5px" onclick="logout()">🚪 خروج</button>`;
        if(isAdmin)renderAdminPanel(aa)
    }else{
        const isF=currentUserData?.following&&currentUserData.following[uid];
        aa.innerHTML=`<button class="btn-follow" onclick="toggleFollow('${uid}',this)">${isF?'متابع':'متابعة'}</button>
        <button style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.2);padding:8px 20px;border-radius:30px;color:#fff;cursor:pointer;margin:5px" onclick="openChat('${uid}')">💬 رسالة</button>`
    }
}
function openMyProfile(){if(currentUser)viewProfile(currentUser.uid)}
function closeProfile(){document.getElementById('profilePanel').classList.remove('open');viewingProfileUserId=null}
function openEditProfile(){
    document.getElementById('editUsername').value=currentUserData?.username||'';
    document.getElementById('editBio').value=currentUserData?.bio||'';
    const ea=document.getElementById('editAvatarDisplay');
    if(currentUserData?.cartoonAvatar){ea.innerHTML=`<span style="font-size:52px">${currentUserData.cartoonAvatar.emoji}</span>`;ea.style.background=currentUserData.cartoonAvatar.bg}
    else if(currentUserData?.avatarUrl){ea.innerHTML=`<img src="${currentUserData.avatarUrl}" style="width:100%;height:100%;object-fit:cover;border-radius:50%">`;ea.style.background='white'}
    else{ea.innerHTML=currentUserData?.username?.charAt(0)||'👤';ea.style.background='linear-gradient(135deg,#6366f1,#06b6d4)'}
    document.getElementById('editProfilePanel').classList.add('open')
}
function closeEditProfile(){document.getElementById('editProfilePanel').classList.remove('open')}
async function saveProfile(){
    const uname=document.getElementById('editUsername').value;
    const bio=document.getElementById('editBio').value;
    await db.ref('users/'+currentUser.uid).update({username:uname,bio:bio});
    currentUserData.username=uname;currentUserData.bio=bio;
    closeEditProfile();
    if(viewingProfileUserId===currentUser.uid)loadProfile(currentUser.uid);
    renderVideos()
}
function changeAvatar(){document.getElementById('avatarInput').click()}
async function uploadAvatar(inp){
    const file=inp.files[0];if(!file)return;
    const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);
    const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{method:'POST',body:fd});
    const data=await res.json();
    await db.ref('users/'+currentUser.uid+'/avatarUrl').set(data.secure_url);
    await db.ref('users/'+currentUser.uid+'/cartoonAvatar').set(null);
    currentUserData.avatarUrl=data.secure_url;currentUserData.cartoonAvatar=null;
    if(viewingProfileUserId===currentUser.uid)loadProfile(currentUser.uid);
    renderVideos()
}
function playVideo(url){window.open(url,'_blank')}

// ===== ADMIN =====
async function renderAdminPanel(aa){
    const us=await db.ref('users').once('value');const users=us.val()||{};
    const vs=await db.ref('videos').once('value');const videos=vs.val()||{};
    const tl=Object.values(videos).reduce((s,v)=>s+(v.likes||0),0);
    const bu=Object.values(users).filter(u=>u.banned).length;
    const vu=Object.values(users).filter(u=>u.isVerified).length;
    aa.innerHTML+=`<div class="admin-section">
        <h3 style="color:#a5b4fc;font-weight:700;margin-bottom:16px">🛡️ لوحة الأدمن</h3>
        <div class="admin-stats">
            <div class="admin-stat-card"><div class="admin-stat-num">${Object.keys(users).length}</div><div class="admin-stat-label">مستخدمين</div></div>
            <div class="admin-stat-card"><div class="admin-stat-num">${Object.keys(videos).length}</div><div class="admin-stat-label">فيديوهات</div></div>
            <div class="admin-stat-card"><div class="admin-stat-num">${tl}</div><div class="admin-stat-label">إعجابات</div></div>
            <div class="admin-stat-card"><div class="admin-stat-num">${bu}</div><div class="admin-stat-label">محظورين</div></div>
            <div class="admin-stat-card"><div class="admin-stat-num">${vu}</div><div class="admin-stat-label">موثقين</div></div>
        </div>
        <h4 style="font-weight:700;margin-bottom:8px;color:#fbbf24">✅ توثيق الحسابات</h4>
        <div class="admin-list">${Object.entries(users).slice(0,15).map(([id,u])=>`
            <div class="admin-item">
                <div style="display:flex;align-items:center;gap:8px">
                    <div style="width:32px;height:32px;border-radius:50%;background:${u.cartoonAvatar?.bg||'#6366f1'};display:flex;align-items:center;justify-content:center;font-size:16px">${u.cartoonAvatar?.emoji||u.username?.charAt(0)||'👤'}</div>
                    <div>@${u.username} ${u.isVerified?'<span class="badge-verified">✅</span>':''}</div>
                </div>
                <button class="admin-btn-warn" onclick="toggleVerify('${id}')">${u.isVerified?'إلغاء':'توثيق'}</button>
            </div>`).join('')}</div>
        <h4 style="font-weight:700;margin-bottom:8px;margin-top:16px">🗑️ حذف فيديوهات</h4>
        <div class="admin-list">${Object.entries(videos).reverse().slice(0,10).map(([id,v])=>`
            <div class="admin-item">
                <div style="display:flex;align-items:center;gap:8px"><i class="fas fa-video"></i><span>${(v.description||'فيديو').substring(0,30)}</span></div>
                <button class="admin-btn-danger" onclick="adminDelVid('${id}')">حذف</button>
            </div>`).join('')}</div>
    </div>`
}
async function toggleVerify(uid){
    if(!isAdmin)return;
    const ref=db.ref('users/'+uid);const snap=await ref.once('value');const u=snap.val();
    if(!u)return;
    const st=!u.isVerified;
    if(confirm(st?'توثيق؟':'إلغاء التوثيق؟')){
        await ref.update({isVerified:st,verifiedAt:st?Date.now():null});
        alert(st?'✅ تم':'❌ تم');loadProfile(uid)
    }
}
async function adminDelVid(vid){if(!isAdmin)return;if(confirm('حذف؟')){await db.ref('videos/'+vid).remove();alert('✅');location.reload()}}

// ===== CHAT =====
async function openChat(uid){
    currentChatUserId=uid;
    const u=allUsers[uid];
    document.getElementById('chatName').innerText='@'+(u?.username||'مستخدم');
    document.getElementById('chatAvatar').innerHTML=u?.cartoonAvatar?.emoji||(u?.username?.charAt(0)||'👤');
    await loadMessages();document.getElementById('chatPanel').classList.add('open')
}
function closeChat(){document.getElementById('chatPanel').classList.remove('open');currentChatUserId=null}
async function loadMessages(){
    const cid=[currentUser.uid,currentChatUserId].sort().join('_');
    const snap=await db.ref('private_messages/'+cid).once('value');
    const ms=snap.val()||{};
    const ct=document.getElementById('messagesList');ct.innerHTML='';
    Object.values(ms).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{
        const sent=m.senderId===currentUser.uid;
        ct.innerHTML+=`<div class="msg-bubble ${sent?'sent':'received'}">
            ${m.type==='image'?`<img src="${m.imageUrl}" style="max-width:200px;max-height:200px;border-radius:12px;cursor:pointer" onclick="window.open('${m.imageUrl}')">`:m.text}
            <div style="font-size:9px;opacity:0.5;margin-top:4px;text-align:${sent?'left':'right'}">${new Date(m.timestamp).toLocaleTimeString()}</div>
        </div>`
    });
    ct.scrollTop=ct.scrollHeight
}
async function sendChatMsg(){
    const inp=document.getElementById('chatMsgInput');
    const txt=inp.value.trim();if(!txt||!currentChatUserId)return;
    const cid=[currentUser.uid,currentChatUserId].sort().join('_');
    const msg={senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()};
    await db.ref('private_messages/'+cid).push(msg);
    inp.value='';await loadMessages()
}
async function sendChatImage(inp){
    const file=inp.files[0];if(!file||!currentChatUserId)return;
    const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);
    const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{method:'POST',body:fd});
    const data=await res.json();
    const cid=[currentUser.uid,currentChatUserId].sort().join('_');
    await db.ref('private_messages/'+cid).push({senderId:currentUser.uid,imageUrl:data.secure_url,type:'image',timestamp:Date.now()});
    inp.value='';await loadMessages()
}
async function openConversations(){
    const panel=document.getElementById('conversationsPanel');
    const ct=document.getElementById('conversationsList');ct.innerHTML='';
    const snap=await db.ref('private_messages').once('value');
    const all=snap.val()||{};
    const found=new Set();
    Object.keys(all).forEach(cid=>{
        const[uid1,uid2]=cid.split('_');
        const other=uid1===currentUser.uid?uid2:uid2===currentUser.uid?uid1:null;
        if(other&&!found.has(other)&&allUsers[other]){found.add(other)}
    });
    found.forEach(uid=>{
        const u=allUsers[uid];
        ct.innerHTML+=`<div class="search-result" onclick="openChat('${uid}');closeConversations()">
            <div class="search-avatar" style="background:${u?.cartoonAvatar?.bg||'linear-gradient(135deg,#6366f1,#06b6d4)'}">${u?.cartoonAvatar?.emoji||(u?.username?.charAt(0)||'👤')}</div>
            <div>@${u?.username||'مستخدم'}</div>
        </div>`
    });
    if(!found.size)ct.innerHTML='<div style="text-align:center;opacity:0.5;padding:30px">لا توجد محادثات</div>';
    panel.classList.add('open')
}
function closeConversations(){document.getElementById('conversationsPanel').classList.remove('open')}

// ===== UPLOAD =====
function openUpload(){document.getElementById('uploadPanel').classList.add('open')}
function closeUpload(){document.getElementById('uploadPanel').classList.remove('open');selectedVideoFile=null}
function onFilePicked(inp){
    const file=inp.files[0];
    if(!file||!file.type.startsWith('video/')){alert('اختر فيديو صحيح');return}
    if(file.size>100*1024*1024){alert('أقل من 100MB');return}
    selectedVideoFile=file;
    const reader=new FileReader();
    reader.onload=e=>{
        const vp=document.getElementById('videoPreview');
        vp.src=e.target.result;vp.style.display='block'
    };
    reader.readAsDataURL(file)
}
async function uploadVideo(){
    if(!selectedVideoFile){alert('اختر فيديو');return}
    const desc=document.getElementById('vidDesc').value;
    const music=document.getElementById('vidMusic').value||'Original Sound';
    const pb=document.getElementById('progressBar');pb.style.display='block';
    const pf=document.getElementById('progressFill');pf.style.width='0%';
    const pt=document.getElementById('progressText');pt.innerText='0%';
    const st=document.getElementById('uploadStatus');st.innerHTML='';
    const btn=document.getElementById('uploadBtn');btn.disabled=true;btn.style.opacity='0.5';
    const fd=new FormData();fd.append('file',selectedVideoFile);fd.append('upload_preset',UPLOAD_PRESET);
    const xhr=new XMLHttpRequest();
    xhr.open('POST','https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/video/upload');
    xhr.upload.onprogress=e=>{if(e.lengthComputable){const p=Math.round(e.loaded/e.total*100);pf.style.width=p+'%';pt.innerText=p+'%'}};
    xhr.onload=async()=>{
        const r=JSON.parse(xhr.responseText);
        await db.ref('videos/').push({
            url:r.secure_url,thumbnail:r.secure_url.replace('.mp4','.jpg'),
            description:desc,music:music,
            sender:currentUser.uid,senderName:currentUserData?.username,
            likes:0,likedBy:{},comments:{},timestamp:Date.now()
        });
        st.innerHTML='✅ تم الرفع!';st.style.color='#4ade80';
        setTimeout(()=>{closeUpload();renderVideos()},1500)
    };
    xhr.onerror=()=>{st.innerHTML='❌ فشل';btn.disabled=false;btn.style.opacity='1'};
    xhr.send(fd)
}

// ===== TAB SWITCH =====
function switchTab(t){
    document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));
    if(event.target.closest('.nav-item'))event.target.closest('.nav-item').classList.add('active');
    if(t==='search')openSearch();
    if(t==='home'){
        closeSearch();closeNotifications();closeProfile();
        closeComments();closeShare();closeUpload();closeChat();closeConversations()
    }
}

// ===== AUTH STATE =====
let authChecked=false;
auth.onAuthStateChanged(async user=>{
    if(user){
        currentUser=user;await loadUserData();checkAdminStatus();
        document.getElementById('mainApp').style.display='block';
        db.ref('presence/'+user.uid).set(true);
        db.ref('presence/'+user.uid).onDisconnect().remove();
        authChecked=true;
    }else{
        if(!authChecked)location.replace('login.html');
    }
});
setTimeout(()=>{if(!currentUser&&!authChecked)location.replace('login.html')},3000);
console.log('💎 CRYSTΔL 2026 Ready');
