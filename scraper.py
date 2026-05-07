#!/usr/bin/env python3
"""
💎 CRYSTΔL 2026 - FINAL VERSION
كل الصفحات مستقلة 100% - بدون أخطاء
"""

import os

FIREBASE_CONFIG = {
    "apiKey": "AIzaSyDBguT0T_TR0IVRCqjd-5_yGO3MEGrV7FI",
    "authDomain": "gomlf-c26ce.firebaseapp.com",
    "databaseURL": "https://gomlf-c26ce-default-rtdb.firebaseio.com",
    "projectId": "gomlf-c26ce",
    "storageBucket": "gomlf-c26ce.firebasestorage.app",
    "messagingSenderId": "18853650392",
    "appId": "1:18853650392:web:80bf57c23a28158671dcad",
    "measurementId": "G-8XNVS6EYPE"
}

CLOUD_NAME = "dmla61v7n"
UPLOAD_PRESET = "so2_mk"
ADMIN_EMAILS_JS = "['jasim28v@gmail.com']"
DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg"
COVER_COLORS_JS = """["linear-gradient(135deg, #6366f1, #06b6d4, #3b82f6)","linear-gradient(135deg, #8b5cf6, #6366f1, #06b6d4)","linear-gradient(135deg, #1e1b4b, #0e7490, #06b6d4)","linear-gradient(135deg, #3b82f6, #06b6d4, #8b5cf6)","linear-gradient(135deg, #06b6d4, #6366f1, #1e1b4b)"]"""

def write(fname, content):
    with open(fname, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ {fname}")

# ============================================
# 1. firebase-config.js
# ============================================
def make_config():
    return f"""// 💎 CRYSTΔL Config
const firebaseConfig = {{
    apiKey: "{FIREBASE_CONFIG['apiKey']}",
    authDomain: "{FIREBASE_CONFIG['authDomain']}",
    databaseURL: "{FIREBASE_CONFIG['databaseURL']}",
    projectId: "{FIREBASE_CONFIG['projectId']}",
    storageBucket: "{FIREBASE_CONFIG['storageBucket']}",
    messagingSenderId: "{FIREBASE_CONFIG['messagingSenderId']}",
    appId: "{FIREBASE_CONFIG['appId']}",
    measurementId: "{FIREBASE_CONFIG['measurementId']}"
}};
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";
const ADMIN_EMAILS = {ADMIN_EMAILS_JS};
const DICEBEAR_URL = "{DICEBEAR_URL}";
const COVER_COLORS = {COVER_COLORS_JS};
console.log('💎 Config Ready');
"""

# ============================================
# 2. auth.html (تسجيل دخول + اشتراك - مصحح)
# ============================================
def make_auth():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 CRYSTΔL | دخول</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{min-height:100vh;background:radial-gradient(ellipse at top, #1a1a2e, #0f0f1a, #000);display:flex;align-items:center;justify-content:center;font-family:'Segoe UI',sans-serif;overflow:hidden}
        .bg-orb{position:fixed;border-radius:50%;filter:blur(130px);opacity:0.35;animation:orbFloat 20s infinite alternate}
        .bg-orb:nth-child(1){width:400px;height:400px;background:#6366f1;top:-100px;left:-100px}
        .bg-orb:nth-child(2){width:350px;height:350px;background:#06b6d4;bottom:-100px;right:-100px;animation-delay:5s}
        @keyframes orbFloat{0%{transform:translate(0,0) scale(1)}100%{transform:translate(50px,-50px) scale(1.3)}}
        .card{position:relative;z-index:1;width:90%;max-width:410px;background:rgba(255,255,255,0.03);backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);border-radius:32px;padding:36px 24px;border:1px solid rgba(255,255,255,0.1);box-shadow:0 30px 70px rgba(0,0,0,0.5);animation:fadeUp 0.8s ease}
        @keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
        .logo{width:70px;height:70px;margin:0 auto 20px;background:linear-gradient(135deg, rgba(99,102,241,0.3), rgba(6,182,212,0.3));border-radius:20px;display:flex;align-items:center;justify-content:center;font-size:36px;border:1px solid rgba(255,255,255,0.15);box-shadow:0 15px 40px rgba(99,102,241,0.2)}
        h1{text-align:center;font-size:36px;font-weight:900;background:linear-gradient(to bottom, #fff, #a5b4fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px}
        .sub{text-align:center;color:rgba(255,255,255,0.5);font-size:13px;margin-bottom:20px}
        .tabs{display:flex;gap:4px;background:rgba(255,255,255,0.04);border-radius:40px;padding:4px;margin-bottom:24px}
        .tab{flex:1;padding:12px;background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;border-radius:40px;font-size:14px;transition:all 0.3s;font-weight:500}
        .tab.active{background:linear-gradient(135deg, #6366f1, #06b6d4);color:#fff}
        .form{display:none}
        .form.active{display:block}
        input{width:100%;padding:15px 18px;margin:8px 0;border-radius:50px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);color:#fff;font-size:14px;outline:none;transition:all 0.4s}
        input:focus{border-color:rgba(99,102,241,0.6);background:rgba(255,255,255,0.07)}
        input::placeholder{color:rgba(255,255,255,0.3)}
        button{width:100%;padding:15px;margin-top:18px;background:linear-gradient(135deg, #6366f1, #06b6d4);border:none;border-radius:50px;color:#fff;font-weight:bold;font-size:15px;cursor:pointer;transition:all 0.3s;box-shadow:0 10px 30px rgba(99,102,241,0.3)}
        button:hover{transform:translateY(-2px)}
        button:disabled{opacity:0.5;pointer-events:none}
        .msg{text-align:center;color:#fca5a5;font-size:13px;margin-top:12px;min-height:20px}
        .msg.success{color:#4ade80}
    </style>
</head>
<body>
<div class="bg-orb"></div><div class="bg-orb"></div>
<div class="card">
    <div class="logo">💎</div>
    <h1>CRYSTΔL</h1>
    <p class="sub">TikTok 2026 Ultra Pro</p>
    <div class="tabs">
        <button class="tab active" id="tabLogin" onclick="switchTab('login')">دخول</button>
        <button class="tab" id="tabRegister" onclick="switchTab('register')">اشتراك</button>
    </div>
    <div id="formLogin" class="form active">
        <input type="email" id="loginEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
        <input type="password" id="loginPass" placeholder="🔒 كلمة المرور" autocomplete="current-password">
        <button id="btnLogin" onclick="doLogin()">🚀 تسجيل الدخول</button>
        <div class="msg" id="loginMsg"></div>
    </div>
    <div id="formRegister" class="form">
        <input type="text" id="regName" placeholder="👤 اسم المستخدم" autocomplete="username">
        <input type="email" id="regEmail" placeholder="📧 البريد الإلكتروني" autocomplete="email">
        <input type="password" id="regPass" placeholder="🔒 كلمة المرور (6 أحرف)" autocomplete="new-password">
        <button id="btnRegister" onclick="doRegister()">🎨 إنشاء حساب</button>
        <div class="msg" id="regMsg"></div>
    </div>
</div>
<script src="firebase-config.js"></script>
<script>
    // ========== SWITCH TAB (تم التصحيح) ==========
    function switchTab(type){
        document.getElementById('tabLogin').classList.remove('active');
        document.getElementById('tabRegister').classList.remove('active');
        document.getElementById('formLogin').classList.remove('active');
        document.getElementById('formRegister').classList.remove('active');
        document.getElementById('loginMsg').innerText='';
        document.getElementById('regMsg').innerText='';
        if(type==='login'){
            document.getElementById('tabLogin').classList.add('active');
            document.getElementById('formLogin').classList.add('active');
        } else {
            document.getElementById('tabRegister').classList.add('active');
            document.getElementById('formRegister').classList.add('active');
        }
    }
    
    // ========== LOGIN ==========
    async function doLogin(){
        const e=document.getElementById('loginEmail').value.trim();
        const p=document.getElementById('loginPass').value;
        const m=document.getElementById('loginMsg');
        const b=document.getElementById('btnLogin');
        if(!e||!p){m.innerText='❌ املأ جميع الحقول';return}
        b.disabled=true;b.innerHTML='⏳ جاري الدخول...';m.innerText='';
        try{
            await auth.signInWithEmailAndPassword(e,p);
            window.location.replace('index.html');
        }catch(err){
            b.disabled=false;b.innerHTML='🚀 تسجيل الدخول';
            if(err.code==='auth/wrong-password'||err.code==='auth/invalid-credential')m.innerText='❌ كلمة مرور خاطئة';
            else if(err.code==='auth/user-not-found')m.innerText='❌ لا يوجد حساب';
            else m.innerText='❌ خطأ: '+err.message;
        }
    }
    
    // ========== REGISTER ==========
    async function doRegister(){
        const u=document.getElementById('regName').value.trim();
        const e=document.getElementById('regEmail').value.trim();
        const p=document.getElementById('regPass').value;
        const m=document.getElementById('regMsg');
        const b=document.getElementById('btnRegister');
        if(!u||!e||!p){m.innerText='❌ املأ جميع الحقول';return}
        if(p.length<6){m.innerText='❌ كلمة المرور 6 أحرف على الأقل';return}
        b.disabled=true;b.innerHTML='⏳ جاري الإنشاء...';m.innerText='';
        try{
            const uc=await auth.createUserWithEmailAndPassword(e,p);
            const avatarUrl=DICEBEAR_URL+'?seed='+uc.user.uid;
            const coverColor=COVER_COLORS[Math.floor(Math.random()*COVER_COLORS.length)];
            await db.ref('users/'+uc.user.uid).set({
                username:u,email:e,bio:'',avatarUrl:avatarUrl,
                hasCustomAvatar:false,coverColor:coverColor,
                followers:{},following:{},totalLikes:0,
                isVerified:false,createdAt:Date.now()
            });
            m.innerText='✅ تم بنجاح!';m.className='msg success';
            setTimeout(()=>window.location.replace('index.html'),600);
        }catch(err){
            b.disabled=false;b.innerHTML='🎨 إنشاء حساب';
            if(err.code==='auth/email-already-in-use')m.innerText='❌ البريد مستخدم بالفعل';
            else if(err.code==='auth/weak-password')m.innerText='❌ كلمة مرور ضعيفة';
            else m.innerText='❌ خطأ: '+err.message;
        }
    }
    
    // Enter key
    document.querySelectorAll('input').forEach(i=>i.addEventListener('keydown',e=>{
        if(e.key==='Enter'){
            if(document.getElementById('formLogin').classList.contains('active'))doLogin();
            else doRegister();
        }
    }));
    
    // Auto-redirect if logged in
    auth.onAuthStateChanged(u=>{if(u)window.location.replace('index.html')});
    console.log('💎 Auth Ready');
</script>
</body>
</html>"""

# ============================================
# 3. index.html (الرئيسية - كود كامل بداخلها)
# ============================================
def make_index():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>💎 CRYSTΔL</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(255,255,255,0.08);--accent:#6366f1;--accent2:#06b6d4;--bg:#050510}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;height:100vh;overflow:hidden}
        #loaderScreen{position:fixed;inset:0;z-index:9999;background:radial-gradient(ellipse at top, #1a1a2e, #0f0f1a, #000);display:flex;align-items:center;justify-content:center;flex-direction:column;gap:16px}
        .spinner-big{width:48px;height:48px;border:4px solid rgba(99,102,241,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.8s linear infinite}
        @keyframes spin{to{transform:rotate(360deg)}}
        #mainApp{display:none;height:100vh;position:relative}
        .topbar{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;justify-content:space-between;align-items:center;padding:12px 20px;background:rgba(5,5,16,0.7);backdrop-filter:blur(30px);border-bottom:1px solid var(--border)}
        .logo-icon{width:36px;height:36px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:10px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:14px}
        .logo-text{font-weight:800;font-size:17px;background:linear-gradient(to bottom,#fff,#a5b4fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-left:8px}
        .tabs{display:flex;gap:4px;background:var(--glass);border-radius:30px;padding:3px}
        .tab{background:none;border:none;color:rgba(255,255,255,0.5);padding:7px 16px;cursor:pointer;border-radius:25px;font-size:13px;transition:all 0.3s}
        .tab.active{background:rgba(99,102,241,0.2);color:#fff}
        .top-icons{display:flex;gap:16px}
        .top-icon{background:none;border:none;color:rgba(255,255,255,0.7);font-size:18px;cursor:pointer}
        .videos-wrap{height:100vh;overflow-y:scroll;scroll-snap-type:y mandatory;scrollbar-width:none}
        .videos-wrap::-webkit-scrollbar{display:none}
        .vid-card{height:100vh;scroll-snap-align:start;position:relative;background:#000}
        .vid-card video{width:100%;height:100%;object-fit:cover}
        .vid-info{position:absolute;bottom:90px;left:14px;right:80px;z-index:20;text-shadow:0 2px 10px rgba(0,0,0,0.8)}
        .author-row{display:flex;align-items:center;gap:10px;margin-bottom:6px}
        .author-avatar{width:46px;height:46px;border-radius:50%;overflow:hidden;cursor:pointer;border:2px solid rgba(255,255,255,0.3)}
        .author-avatar img{width:100%;height:100%;object-fit:cover}
        .author-name{font-weight:700;font-size:15px;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
        .verified-badge{color:#60a5fa;font-size:14px}
        .btn-follow{background:linear-gradient(135deg,var(--accent),var(--accent2));padding:5px 14px;border-radius:20px;font-size:11px;font-weight:700;border:none;color:#fff;cursor:pointer}
        .caption{font-size:14px;margin-bottom:5px;line-height:1.4}
        .tag{color:var(--accent2);cursor:pointer;font-weight:500}
        .music{font-size:12px;opacity:0.8;display:flex;align-items:center;gap:6px;cursor:pointer}
        .side-btns{position:absolute;right:14px;bottom:130px;display:flex;flex-direction:column;gap:22px;z-index:20}
        .sbtn{display:flex;flex-direction:column;align-items:center;gap:3px;background:none;border:none;color:#fff;cursor:pointer;font-size:10px;transition:transform 0.15s}
        .sbtn:active{transform:scale(0.85)}
        .sbtn i{font-size:28px;filter:drop-shadow(0 3px 8px rgba(0,0,0,0.5))}
        .sbtn.liked i{color:var(--accent)}
        .nav-bottom{position:fixed;bottom:0;left:0;right:0;display:flex;justify-content:space-around;align-items:center;padding:8px 0 20px;background:rgba(5,5,16,0.8);backdrop-filter:blur(30px);z-index:100;border-top:1px solid var(--border)}
        .nav-item{display:flex;flex-direction:column;align-items:center;gap:3px;background:none;border:none;color:rgba(255,255,255,0.5);font-size:10px;cursor:pointer;text-decoration:none}
        .nav-item i{font-size:22px}
        .btn-add{width:48px;height:48px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:50%;display:flex;align-items:center;justify-content:center;margin-top:-24px;cursor:pointer;border:none;color:#fff;font-size:20px;text-decoration:none}
        .toast{position:fixed;bottom:100px;left:50%;transform:translateX(-50%);background:rgba(5,5,16,0.9);padding:10px 22px;border-radius:50px;z-index:1000;opacity:0;transition:opacity 0.3s;pointer-events:none;border:1px solid var(--border)}
        .toast.show{opacity:1}
    </style>
</head>
<body>
<div id="loaderScreen"><div class="spinner-big"></div><p style="color:rgba(255,255,255,0.6)">💎 جاري التحميل...</p></div>

<div id="mainApp">
    <div class="topbar">
        <div style="display:flex;align-items:center"><div class="logo-icon">💎</div><span class="logo-text">CRYSTΔL</span></div>
        <div class="tabs"><button class="tab" onclick="switchFeed('following')">متابَعين</button><button class="tab active" onclick="switchFeed('forYou')">لك</button></div>
        <div class="top-icons"><i class="fas fa-search top-icon" onclick="openSearch()"></i><i class="fas fa-bell top-icon" onclick="openNotifs()"></i></div>
    </div>
    <div class="videos-wrap" id="videosWrap"><div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px"><i class="fas fa-video" style="font-size:48px;opacity:0.3"></i><p>لا توجد فيديوهات</p></div></div>
    <div class="nav-bottom">
        <button class="nav-item active"><i class="fas fa-home"></i><span>الرئيسية</span></button>
        <button class="nav-item" onclick="openSearch()"><i class="fas fa-search"></i><span>بحث</span></button>
        <a href="upload.html" class="btn-add"><i class="fas fa-plus"></i></a>
        <a href="chat.html" class="nav-item"><i class="fas fa-envelope"></i><span>رسائل</span></a>
        <a href="profile.html" class="nav-item"><i class="fas fa-user"></i><span>ملفي</span></a>
    </div>
    <div id="toast" class="toast">✅ تم النسخ</div>
</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null,allUsers={},allVideos=[],isMuted=true,currentFeed='forYou',currentShareUrl=null;
    
    auth.onAuthStateChanged(async u=>{
        if(!u){window.location.replace('auth.html');return}
        currentUser=u;
        const snap=await db.ref('users/'+u.uid).get();
        if(snap.exists())currentUserData={uid:u.uid,...snap.val()};
        db.ref('users').on('value',s=>{allUsers=s.val()||{}});
        db.ref('videos').on('value',s=>{
            const data=s.val();
            allVideos=data?Object.entries(data).map(([k,v])=>({id:k,...v})).sort((a,b)=>(b.timestamp||0)-(a.timestamp||0)):[];
            renderVideos();
        });
        db.ref('presence/'+u.uid).set(true);
        db.ref('presence/'+u.uid).onDisconnect().remove();
        document.getElementById('loaderScreen').style.display='none';
        document.getElementById('mainApp').style.display='block';
    });
    
    function renderVideos(){
        const c=document.getElementById('videosWrap');
        let fv=currentFeed==='forYou'?allVideos:allVideos.filter(v=>currentUserData?.following?.[v.sender]);
        if(!fv.length){c.innerHTML='<div style="display:flex;align-items:center;justify-content:center;height:100vh;color:rgba(255,255,255,0.5);flex-direction:column;gap:12px"><i class="fas fa-video" style="font-size:48px;opacity:0.3"></i><p>لا توجد فيديوهات</p></div>';return}
        c.innerHTML='';
        fv.forEach(v=>{
            const liked=v.likedBy&&v.likedBy[currentUser?.uid];
            const user=allUsers[v.sender]||{username:v.senderName||'user'};
            const following=currentUserData?.following&&currentUserData.following[v.sender];
            const cc=v.comments?Object.keys(v.comments).length:0;
            const cap=(v.description||'').replace(/#(\w+)/g,'<span class="tag">#$1</span>');
            const avUrl=user.avatarUrl||(DICEBEAR_URL+'?seed='+v.sender);
            const div=document.createElement('div');div.className='vid-card';
            div.innerHTML=`
                <video loop playsinline muted data-src="${v.url}" poster="${v.thumbnail||''}"></video>
                <div class="vid-info">
                    <div class="author-row">
                        <div class="author-avatar" onclick="window.location.href='profile.html'"><img src="${avUrl}"></div>
                        <div class="author-name">
                            <span onclick="window.location.href='profile.html'">@${user.username}</span>
                            ${user.isVerified?'<span class="verified-badge">✅</span>':''}
                            ${currentUser?.uid!==v.sender?`<button class="btn-follow" onclick="toggleFollow('${v.sender}',this)">${following?'متابع':'متابعة'}</button>`:''}
                        </div>
                    </div>
                    <div class="caption">${cap}</div>
                    <div class="music"><i class="fas fa-music"></i> ${v.music||'Original Sound'}</div>
                </div>
                <div class="side-btns">
                    <button class="sbtn" onclick="toggleMute()"><i class="fas ${isMuted?'fa-volume-mute':'fa-volume-up'}"></i></button>
                    <button class="sbtn like-btn ${liked?'liked':''}" onclick="toggleLike('${v.id}',this)"><i class="fas fa-heart"></i><span>${v.likes||0}</span></button>
                    <button class="sbtn" onclick="openComments('${v.id}')"><i class="fas fa-comment"></i><span>${cc}</span></button>
                    <button class="sbtn" onclick="openShare('${v.url}')"><i class="fas fa-share"></i></button>
                </div>`;
            const ve=div.querySelector('video');
            ve.addEventListener('dblclick',e=>{e.stopPropagation();const lb=div.querySelector('.like-btn');if(lb)toggleLike(v.id,lb)});
            c.appendChild(div);
        });
        initObs();
    }
    
    function initObs(){
        const ob=new IntersectionObserver(entries=>{entries.forEach(e=>{const v=e.target.querySelector('video');if(e.isIntersecting){if(!v.src)v.src=v.dataset.src;v.muted=isMuted;v.play().catch(()=>{})}else v.pause()})},{threshold:0.65});
        document.querySelectorAll('.vid-card').forEach(s=>ob.observe(s));
    }
    
    function toggleMute(){isMuted=!isMuted;document.querySelectorAll('video').forEach(v=>v.muted=isMuted)}
    function switchFeed(f){currentFeed=f;document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));event.target.classList.add('active');renderVideos()}
    
    async function toggleLike(vid,btn){
        if(!currentUser)return;
        const ref=db.ref('videos/'+vid);const snap=await ref.get();const v=snap.val();if(!v)return;
        let l=v.likes||0,lb=v.likedBy||{};
        if(lb[currentUser.uid]){l--;delete lb[currentUser.uid]}else{l++;lb[currentUser.uid]=true}
        await ref.update({likes:l,likedBy:lb});btn.classList.toggle('liked');btn.querySelector('span').innerText=l;
    }
    
    async function toggleFollow(uid,btn){
        if(!currentUser||currentUser.uid===uid)return;
        const ur=db.ref('users/'+currentUser.uid+'/following/'+uid);const tr=db.ref('users/'+uid+'/followers/'+currentUser.uid);
        const snap=await ur.get();
        if(snap.exists()){await ur.remove();await tr.remove();btn.innerText='متابعة'}else{await ur.set(true);await tr.set(true);btn.innerText='متابع'}
    }
    
    function openShare(url){currentShareUrl=url;showOverlay('<h3>📤 مشاركة</h3>','<div onclick="copyL()" style="display:flex;align-items:center;gap:12px;padding:14px;cursor:pointer;border-bottom:1px solid rgba(255,255,255,0.05)"><i class="fas fa-link" style="color:#6366f1;font-size:20px"></i><span>نسخ الرابط</span></div><div onclick="shareW()" style="display:flex;align-items:center;gap:12px;padding:14px;cursor:pointer"><i class="fab fa-whatsapp" style="color:#25D366;font-size:20px"></i><span>WhatsApp</span></div>')}
    window.copyL=function(){navigator.clipboard.writeText(currentShareUrl);document.getElementById('toast').classList.add('show');setTimeout(()=>document.getElementById('toast').classList.remove('show'),2000);closeOverlay()}
    window.shareW=function(){window.open('https://wa.me/?text='+encodeURIComponent(currentShareUrl));closeOverlay()}
    
    async function openComments(vid){
        const snap=await db.ref('videos/'+vid+'/comments').get();const cs=snap.val()||{};
        let list='';Object.values(cs).reverse().forEach(c=>{const u=allUsers[c.userId]||{username:c.username||'user'};list+=`<div style="display:flex;gap:10px;padding:10px 0;border-bottom:1px solid rgba(255,255,255,0.05)"><img src="${u.avatarUrl||(DICEBEAR_URL+'?seed='+c.userId)}" style="width:36px;height:36px;border-radius:50%"><div><div style="font-weight:600">@${u.username}</div><div style="font-size:13px;opacity:0.8">${c.text}</div></div></div>`});
        showOverlay('<h3>💬 التعليقات</h3>',list+'<div style="display:flex;gap:8px;padding-top:12px"><input type="text" id="cmtInput" placeholder="أضف تعليقاً..." style="flex:1;padding:12px;border-radius:30px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);color:#fff;outline:none"><button onclick="addCmt(\''+vid+'\')" style="background:linear-gradient(135deg,#6366f1,#06b6d4);border:none;color:#fff;padding:12px 20px;border-radius:30px;font-weight:700;cursor:pointer">نشر</button></div>')
    }
    window.addCmt=async function(vid){const inp=document.getElementById('cmtInput');if(!inp||!inp.value.trim())return;await db.ref('videos/'+vid+'/comments').push({userId:currentUser.uid,username:currentUserData?.username,text:inp.value,timestamp:Date.now()});closeOverlay();openComments(vid)}
    
    function openSearch(){
        showOverlay('<h3>🔍 بحث</h3>','<input type="text" id="searchQ" onkeyup="doSearch()" placeholder="ابحث..." style="width:100%;padding:14px;border-radius:30px;background:rgba(255,255,255,0.04);border:1px solid rgba(255,255,255,0.1);color:#fff;font-size:14px;outline:none;margin-bottom:16px"><div id="searchR"></div>');
        window.doSearch=function(){const q=document.getElementById('searchQ').value.toLowerCase();const rd=document.getElementById('searchR');if(!q){rd.innerHTML='';return}const users=Object.values(allUsers).filter(u=>u.username?.toLowerCase().includes(q));const vids=allVideos.filter(v=>(v.description||'').toLowerCase().includes(q));rd.innerHTML=`${users.length?`<div style="margin-bottom:16px"><h4 style="font-size:12px;opacity:0.5">👥 مستخدمين</h4>${users.map(u=>`<div onclick="window.location.href='profile.html'" style="display:flex;align-items:center;gap:10px;padding:10px;cursor:pointer;border-bottom:1px solid rgba(255,255,255,0.05)"><img src="${u.avatarUrl||(DICEBEAR_URL+'?seed='+u.uid||u.username)}" style="width:40px;height:40px;border-radius:50%"><div>@${u.username} ${u.isVerified?'<span class="verified-badge">✅</span>':''}</div></div>`).join('')}</div>`:''}${vids.length?`<div><h4 style="font-size:12px;opacity:0.5">🎬 فيديوهات</h4>${vids.map(v=>`<div onclick="window.open('${v.url}')" style="display:flex;align-items:center;gap:10px;padding:10px;cursor:pointer;border-bottom:1px solid rgba(255,255,255,0.05)"><i class="fas fa-play-circle" style="color:#6366f1;font-size:20px"></i><span style="font-size:13px">${(v.description||'فيديو').substring(0,40)}</span></div>`).join('')}</div>`:''}${!users.length&&!vids.length?'<div style="text-align:center;opacity:0.5;padding:30px">لا نتائج</div>':''}`}
    }
    
    function openNotifs(){showOverlay('<h3>🔔 الإشعارات</h3>','<div style="text-align:center;opacity:0.5;padding:30px">لا توجد إشعارات</div>')}
    
    function showOverlay(title,content){
        const id='ov_'+Date.now();
        document.body.insertAdjacentHTML('beforeend','<div id="'+id+'" style="position:fixed;inset:0;background:rgba(5,5,16,0.97);backdrop-filter:blur(40px);z-index:400;overflow-y:auto"><div style="padding:16px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid rgba(255,255,255,0.08);position:sticky;top:0;background:rgba(5,5,16,0.8)">'+title+'<button onclick="document.getElementById(\''+id+'\').remove()" style="background:rgba(255,255,255,0.08);border:none;color:#fff;width:36px;height:36px;border-radius:50%;cursor:pointer;font-size:18px"><i class="fas fa-times"></i></button></div><div style="padding:16px">'+content+'</div></div>');
    }
    function closeOverlay(){const o=document.querySelector('[style*="z-index:400"]');if(o)o.remove()}
</script>
</body>
</html>"""

# ============================================
# 4. profile.html (ملف شخصي + أدمن)
# ============================================
def make_profile():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 CRYSTΔL | ملفي</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-storage-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(255,255,255,0.08);--accent:#6366f1;--accent2:#06b6d4;--bg:#050510}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .cover{height:220px;position:relative;display:flex;align-items:flex-end;justify-content:center;padding-bottom:40px;transition:background 0.5s}
        .btn-back{position:fixed;top:16px;right:16px;background:rgba(0,0,0,0.5);backdrop-filter:blur(10px);width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:50;border:1px solid rgba(255,255,255,0.15);color:#fff;font-size:18px}
        .btn-cover{position:absolute;top:16px;left:16px;background:rgba(0,0,0,0.4);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.15);color:#fff;padding:8px 16px;border-radius:20px;font-size:12px;cursor:pointer;z-index:50}
        .avatar-lg{width:110px;height:110px;border-radius:50%;overflow:hidden;border:4px solid rgba(255,255,255,0.3);box-shadow:0 12px 40px rgba(0,0,0,0.5);cursor:pointer;position:relative;z-index:2}
        .avatar-lg img{width:100%;height:100%;object-fit:cover}
        .stats{display:flex;justify-content:center;gap:35px;margin:20px 0}
        .stat-val{font-size:22px;font-weight:700;color:#a5b4fc}
        .stat-lbl{font-size:11px;opacity:0.5}
        .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;padding:0 12px}
        .thumb{aspect-ratio:9/16;background:rgba(255,255,255,0.03);border-radius:8px;display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden}
        .thumb i{font-size:24px;color:rgba(255,255,255,0.6);z-index:1}
        .thumb img.thb{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.5}
        .btn{background:rgba(255,255,255,0.08);border:1px solid var(--border);padding:10px 24px;border-radius:30px;color:#fff;cursor:pointer;font-size:14px;margin:4px;transition:all 0.3s}
        .btn:hover{background:rgba(255,255,255,0.15)}
        .btn-primary{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;color:#fff}
        .verified-badge{color:#60a5fa;font-size:16px;margin-right:4px}
        .admin-section{margin-top:20px;padding:16px;background:rgba(99,102,241,0.05);border-radius:16px;border:1px solid rgba(99,102,241,0.15)}
        .admin-stats{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-bottom:16px}
        .stat-card{background:rgba(0,0,0,0.3);border-radius:10px;padding:10px;text-align:center}
        .stat-num{font-size:22px;font-weight:700;color:#a5b4fc}
        .admin-item{display:flex;justify-content:space-between;align-items:center;background:rgba(0,0,0,0.3);padding:8px;border-radius:10px;margin-bottom:6px}
        .admin-btn{padding:5px 12px;border-radius:20px;font-size:11px;cursor:pointer;border:none;font-weight:600;color:#fff}
        .btn-verify{background:rgba(96,165,250,0.3);color:#60a5fa}
        .btn-delete{background:rgba(239,68,68,0.3);color:#f87171}
        .btn-ban{background:rgba(239,68,68,0.3);color:#f87171}
        .btn-unban{background:rgba(34,197,94,0.3);color:#4ade80}
        .spinner{width:32px;height:32px;border:3px solid rgba(99,102,241,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .load-center{display:flex;align-items:center;justify-content:center;min-height:80vh;flex-direction:column;gap:12px;color:rgba(255,255,255,0.5)}
    </style>
</head>
<body>
<div class="load-center" id="loader"><div class="spinner"></div><span>💎 تحميل...</span></div>
<div id="content" style="display:none">
    <div class="cover" id="profileCover">
        <button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button>
        <button class="btn-cover" onclick="changeCover()"><i class="fas fa-palette"></i> الغلاف</button>
        <div class="avatar-lg" id="avatarDisplay" onclick="document.getElementById('avatarInput').click()"><img src="" alt="avatar"></div>
    </div>
    <input type="file" id="avatarInput" accept="image/*" style="display:none" onchange="uploadAvatar(this)">
    <div style="text-align:center;padding:0 20px">
        <h2 id="nameDisplay" style="font-size:22px;font-weight:700;margin-top:8px"></h2>
        <p id="bioDisplay" style="font-size:13px;opacity:0.5;margin-top:4px"></p>
        <div class="stats"><div><div class="stat-val" id="statFollowing">0</div><div class="stat-lbl">يتابع</div></div><div><div class="stat-val" id="statFollowers">0</div><div class="stat-lbl">متابع</div></div><div><div class="stat-val" id="statLikes">0</div><div class="stat-lbl">إعجابات</div></div></div>
        <div id="actionsBar" style="margin:12px 0"></div>
    </div>
    <div style="padding:16px"><h3 style="font-weight:700;margin-bottom:12px">🎬 فيديوهاتي</h3><div class="grid" id="videosGrid"></div></div>
    <div id="adminSection" style="padding:16px;display:none"></div>
</div>

<script src="firebase-config.js"></script>
<script>
    let profileUserId=null,currentUser=null,currentUserData=null,allVideos=[],allUsers={};
    
    auth.onAuthStateChanged(async u=>{
        if(!u){window.location.href='auth.html';return}
        currentUser=u;
        const snap=await db.ref('users/'+u.uid).get();
        if(snap.exists())currentUserData={uid:u.uid,...snap.val()};
        profileUserId=u.uid;
        await loadAll();
        await loadProfile();
        document.getElementById('loader').style.display='none';
        document.getElementById('content').style.display='block';
    });
    
    async function loadAll(){
        const us=await db.ref('users').once('value');allUsers=us.val()||{};
        const vs=await db.ref('videos').once('value');allVideos=Object.entries(vs.val()||{}).map(([k,v])=>({id:k,...v}));
    }
    
    async function loadProfile(){
        const u=allUsers[profileUserId]||currentUserData;
        if(!u)return;
        document.getElementById('nameDisplay').innerHTML='@'+(u.username||'مستخدم')+(u.isVerified?' <span class="verified-badge">✅</span>':'');
        document.getElementById('bioDisplay').innerText=u.bio||'';
        document.getElementById('statFollowing').innerText=Object.keys(u.following||{}).length;
        document.getElementById('statFollowers').innerText=Object.keys(u.followers||{}).length;
        const uvs=allVideos.filter(v=>v.sender===profileUserId);
        document.getElementById('statLikes').innerText=uvs.reduce((s,v)=>s+(v.likes||0),0);
        document.getElementById('profileCover').style.background=u.coverColor||COVER_COLORS[0];
        document.querySelector('#avatarDisplay img').src=u.avatarUrl||(DICEBEAR_URL+'?seed='+profileUserId);
        const g=document.getElementById('videosGrid');g.innerHTML='';
        if(!uvs.length)g.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px;grid-column:1/-1">لا توجد فيديوهات</div>';
        else uvs.forEach(v=>{const d=document.createElement('div');d.className='thumb';d.innerHTML=`<i class="fas fa-play"></i>${v.thumbnail?`<img src="${v.thumbnail}" class="thb">`:''}`;d.onclick=()=>window.open(v.url,'_blank');g.appendChild(d)});
        document.getElementById('actionsBar').innerHTML=`
            <button class="btn btn-primary" onclick="editProfile()"><i class="fas fa-edit"></i> تعديل</button>
            <button class="btn" onclick="auth.signOut();window.location.href='auth.html'"><i class="fas fa-sign-out-alt"></i> خروج</button>
        `;
        if(ADMIN_EMAILS.includes(currentUser.email)){document.getElementById('adminSection').style.display='block';loadAdminPanel()}
    }
    
    async function loadAdminPanel(){
        const us=allUsers,vs={};allVideos.forEach(v=>vs[v.id]=v);
        const tl=Object.values(vs).reduce((s,v)=>s+(v.likes||0),0);
        const bu=Object.values(us).filter(u=>u.banned).length;
        const vu=Object.values(us).filter(u=>u.isVerified).length;
        document.getElementById('adminSection').innerHTML=`
            <div class="admin-section">
                <h3 style="color:#a5b4fc;font-weight:700;margin-bottom:12px"><i class="fas fa-shield-alt"></i> لوحة الأدمن</h3>
                <div class="admin-stats">
                    <div class="stat-card"><div class="stat-num">${Object.keys(us).length}</div><div style="font-size:10px;opacity:0.5">مستخدمين</div></div>
                    <div class="stat-card"><div class="stat-num">${Object.keys(vs).length}</div><div style="font-size:10px;opacity:0.5">فيديوهات</div></div>
                    <div class="stat-card"><div class="stat-num">${tl}</div><div style="font-size:10px;opacity:0.5">إعجابات</div></div>
                    <div class="stat-card"><div class="stat-num">${bu}</div><div style="font-size:10px;opacity:0.5">محظورين</div></div>
                    <div class="stat-card"><div class="stat-num">${vu}</div><div style="font-size:10px;opacity:0.5">موثقين ✅</div></div>
                </div>
                <h4 style="font-weight:700;margin-bottom:8px;color:#60a5fa"><i class="fas fa-check-circle"></i> توثيق</h4>
                <div style="max-height:200px;overflow-y:auto">${Object.entries(us).filter(([id,u])=>!u.banned).slice(0,20).map(([id,u])=>`
                    <div class="admin-item">
                        <div style="display:flex;align-items:center;gap:8px"><img src="${u.avatarUrl||(DICEBEAR_URL+'?seed='+id)}" style="width:32px;height:32px;border-radius:50%"><span>@${u.username||'?'} ${u.isVerified?'<span class="verified-badge">✅</span>':''}</span></div>
                        <button class="admin-btn btn-verify" onclick="toggleVerify('${id}')">${u.isVerified?'إلغاء':'توثيق'}</button>
                    </div>`).join('')}</div>
            </div>`;
        window.toggleVerify=async(id)=>{if(confirm('تأكيد؟')){const r=await db.ref('users/'+id).once('value');const d=r.val();await db.ref('users/'+id).update({isVerified:!d.isVerified});alert('✅');loadAll();loadProfile()}};
    }
    
    function editProfile(){
        const u=allUsers[profileUserId]||currentUserData;
        const name=prompt('اسم المستخدم:',u?.username||'');
        const bio=prompt('السيرة:',u?.bio||'');
        if(name!==null&&bio!==null){db.ref('users/'+profileUserId).update({username:name,bio:bio});loadAll();loadProfile()}
    }
    
    async function changeCover(){
        const idx=prompt('اختر غلاف (1-5):');
        if(idx&&idx>=1&&idx<=COVER_COLORS.length){
            const nc=COVER_COLORS[idx-1];
            await db.ref('users/'+profileUserId+'/coverColor').set(nc);
            document.getElementById('profileCover').style.background=nc;
        }
    }
    
    async function uploadAvatar(inp){
        const file=inp.files[0];if(!file)return;
        const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);
        const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{method:'POST',body:fd});
        const data=await res.json();
        await db.ref('users/'+profileUserId).update({avatarUrl:data.secure_url,hasCustomAvatar:true});
        document.querySelector('#avatarDisplay img').src=data.secure_url;
    }
</script>
</body>
</html>"""

# ============================================
# 5. upload.html (رفع فيديو)
# ============================================
def make_upload():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 CRYSTΔL | رفع</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(255,255,255,0.08);--accent:#6366f1;--accent2:#06b6d4;--bg:#050510}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(5,5,16,0.8);position:sticky;top:0;z-index:10}
        .btn-back{background:rgba(255,255,255,0.08);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .container{max-width:500px;margin:0 auto;padding:20px}
        .dropzone{border:2px dashed rgba(99,102,241,0.3);border-radius:20px;padding:50px 20px;text-align:center;cursor:pointer;background:var(--glass);margin-bottom:20px}
        .dropzone i{font-size:48px;color:var(--accent);margin-bottom:12px}
        .dropzone video{width:100%;max-height:250px;object-fit:contain;margin-top:12px;border-radius:12px;display:none}
        .form-card{background:var(--glass);border:1px solid var(--border);border-radius:20px;padding:20px}
        .form-card label{display:block;font-size:13px;opacity:0.7;margin-bottom:6px;margin-top:12px}
        .form-card textarea,.form-card input{width:100%;padding:14px 16px;border-radius:16px;background:rgba(255,255,255,0.04);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif}
        .form-card textarea{min-height:80px}
        .progress-wrap{display:none;margin:16px 0}
        .progress-bar{background:rgba(255,255,255,0.1);border-radius:30px;height:6px}
        .progress-fill{background:linear-gradient(90deg,var(--accent),var(--accent2));height:100%;border-radius:30px;width:0%}
        .progress-text{text-align:center;font-size:12px;margin-top:6px;color:#a5b4fc}
        .btn-upload{width:100%;padding:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:30px;color:#fff;font-weight:700;font-size:15px;cursor:pointer;margin-top:16px}
        .btn-upload:disabled{opacity:0.5}
        .status{text-align:center;margin-top:12px;font-size:13px}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>📤 رفع فيديو</h2></div>
<div class="container">
    <div class="dropzone" onclick="document.getElementById('videoFile').click()"><i class="fas fa-cloud-upload-alt"></i><p>اضغط لاختيار فيديو</p><span style="font-size:11px;opacity:0.5">MP4 - حتى 100MB</span><video id="preview" controls></video></div>
    <input type="file" id="videoFile" accept="video/*" style="display:none" onchange="onFilePick(this)">
    <div class="form-card">
        <label>🎬 وصف الفيديو</label>
        <textarea id="vidDesc" placeholder="اكتب وصفاً... #هاشتاقات"></textarea>
        <label>🎵 الموسيقى</label>
        <input type="text" id="vidMusic" placeholder="Original Sound">
        <div class="progress-wrap" id="progressWrap"><div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div><div class="progress-text" id="progressText">0%</div></div>
        <button class="btn-upload" id="uploadBtn" onclick="upload()">🚀 رفع</button>
        <div class="status" id="status"></div>
    </div>
</div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null,selectedFile=null;
    auth.onAuthStateChanged(async u=>{if(!u)window.location.href='auth.html';currentUser=u;const snap=await db.ref('users/'+u.uid).get();if(snap.exists())currentUserData={uid:u.uid,...snap.val()}});
    function onFilePick(inp){const f=inp.files[0];if(!f||!f.type.startsWith('video/')){alert('اختر فيديو صحيح');return}if(f.size>100*1024*1024){alert('أقل من 100MB');return}selectedFile=f;const r=new FileReader();r.onload=e=>{const v=document.getElementById('preview');v.src=e.target.result;v.style.display='block'};r.readAsDataURL(f)}
    async function upload(){
        if(!selectedFile){alert('اختر فيديو');return}if(!currentUser){alert('سجل دخول');return}
        const desc=document.getElementById('vidDesc').value;const music=document.getElementById('vidMusic').value||'Original Sound';
        const pw=document.getElementById('progressWrap');pw.style.display='block';const pf=document.getElementById('progressFill');pf.style.width='0%';const pt=document.getElementById('progressText');pt.innerText='0%';
        const st=document.getElementById('status');st.innerHTML='';const btn=document.getElementById('uploadBtn');btn.disabled=true;
        const fd=new FormData();fd.append('file',selectedFile);fd.append('upload_preset',UPLOAD_PRESET);
        const xhr=new XMLHttpRequest();xhr.open('POST','https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/video/upload');
        xhr.upload.onprogress=e=>{if(e.lengthComputable){const p=Math.round(e.loaded/e.total*100);pf.style.width=p+'%';pt.innerText=p+'%'}};
        xhr.onload=async()=>{const r=JSON.parse(xhr.responseText);await db.ref('videos/').push({url:r.secure_url,thumbnail:r.secure_url.replace('.mp4','.jpg'),description:desc,music:music,sender:currentUser.uid,senderName:currentUserData?.username,likes:0,likedBy:{},comments:{},timestamp:Date.now()});st.innerHTML='✅ تم!';st.style.color='#4ade80';setTimeout(()=>window.location.href='index.html',1500)};
        xhr.onerror=()=>{st.innerHTML='❌ فشل';btn.disabled=false;st.style.color='#f87171'};xhr.send(fd);
    }
</script>
</body>
</html>"""

# ============================================
# 6. chat.html (دردشة)
# ============================================
def make_chat():
    return """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 CRYSTΔL | دردشة</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(255,255,255,0.08);--accent:#6366f1;--accent2:#06b6d4;--bg:#050510}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;height:100vh;display:flex;flex-direction:column}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border)}
        .btn-back{background:rgba(255,255,255,0.08);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .msgs{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px}
        .bubble{max-width:80%;padding:10px 16px;border-radius:20px;word-break:break-word;font-size:14px}
        .bubble.sent{background:linear-gradient(135deg,var(--accent),var(--accent2));align-self:flex-end}
        .bubble.received{background:rgba(255,255,255,0.06);align-self:flex-start}
        .input-bar{display:flex;gap:10px;padding:12px;background:rgba(5,5,16,0.9);border-top:1px solid var(--border)}
        .input-bar input{flex:1;padding:12px 16px;border-radius:30px;background:var(--glass);border:1px solid var(--border);color:#fff;font-size:14px;outline:none}
        .btn-send{width:42px;height:42px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:50%;color:#fff;cursor:pointer;font-size:18px}
        .conv-item{display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid var(--border);cursor:pointer}
        .chat-avatar{width:40px;height:40px;border-radius:50%;overflow:hidden}
        .chat-avatar img{width:100%;height:100%;object-fit:cover}
        .spinner{width:32px;height:32px;border:3px solid rgba(99,102,241,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
    </style>
</head>
<body>
<div id="loader" style="flex:1;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px"><div class="spinner"></div><span>💎 تحميل...</span></div>
<div id="convView" style="display:none;flex:1;flex-direction:column;overflow:hidden"><div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>💬 المحادثات</h2></div><div id="convList" style="flex:1;overflow-y:auto"></div></div>
<div id="chatView" style="display:none;flex:1;flex-direction:column;overflow:hidden"><div class="header"><button class="btn-back" onclick="showConvs()"><i class="fas fa-arrow-right"></i></button><div class="chat-avatar" id="chatAvatar"></div><h3 id="chatName">محادثة</h3></div><div class="msgs" id="msgsList"></div><div class="input-bar"><input type="text" id="msgInput" placeholder="اكتب رسالة..." onkeydown="if(event.key==='Enter')sendMsg()"><button class="btn-send" onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button></div></div>
<script src="firebase-config.js"></script>
<script>
    let currentUser=null,allUsers={},chatUserId=null;
    auth.onAuthStateChanged(async u=>{if(!u){window.location.href='auth.html';return}currentUser=u;const us=await db.ref('users').once('value');allUsers=us.val()||{};document.getElementById('loader').style.display='none';showConvs()});
    function showConvs(){document.getElementById('chatView').style.display='none';document.getElementById('convView').style.display='flex';chatUserId=null;loadConvs()}
    async function loadConvs(){const cl=document.getElementById('convList');cl.innerHTML='';const snap=await db.ref('private_messages').once('value');const all=snap.val()||{};const found=new Set();Object.keys(all).forEach(cid=>{const[u1,u2]=cid.split('_');const other=u1===currentUser.uid?u2:u2===currentUser.uid?u1:null;if(other&&!found.has(other)&&allUsers[other])found.add(other)});if(!found.size){cl.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px">لا محادثات</div>';return}found.forEach(uid=>{const u=allUsers[uid];const d=document.createElement('div');d.className='conv-item';d.innerHTML=`<div class="chat-avatar"><img src="${u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}"></div><div><div style="font-weight:600">@${u?.username||'?'} ${u?.isVerified?'<span style="color:#60a5fa">✅</span>':''}</div></div>`;d.onclick=()=>openChat(uid);cl.appendChild(d)})}
    async function openChat(uid){chatUserId=uid;const u=allUsers[uid];document.getElementById('chatName').innerText='@'+(u?.username||'مستخدم');document.getElementById('chatAvatar').innerHTML=`<img src="${u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}">`;document.getElementById('convView').style.display='none';document.getElementById('chatView').style.display='flex';await loadMsgs()}
    function getChatId(){return[currentUser.uid,chatUserId].sort().join('_')}
    async function loadMsgs(){const ml=document.getElementById('msgsList');ml.innerHTML='';if(!chatUserId)return;const snap=await db.ref('private_messages/'+getChatId()).once('value');const ms=snap.val()||{};Object.values(ms).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{const sent=m.senderId===currentUser.uid;const d=document.createElement('div');d.className='bubble '+(sent?'sent':'received');d.innerHTML=`${m.type==='image'?`<img src="${m.imageUrl}" style="max-width:200px;border-radius:12px;cursor:pointer" onclick="window.open('${m.imageUrl}')">`:m.text}<div style="font-size:9px;opacity:0.5;margin-top:4px">${new Date(m.timestamp).toLocaleTimeString()}</div>`;ml.appendChild(d)});ml.scrollTop=ml.scrollHeight}
    async function sendMsg(){const inp=document.getElementById('msgInput');const txt=inp.value.trim();if(!txt||!chatUserId)return;await db.ref('private_messages/'+getChatId()).push({senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()});inp.value='';await loadMsgs()}
</script>
</body>
</html>"""

# ============================================
# MAIN
# ============================================
def main():
    print("\n💎 CRYSTΔL 2026 - FINAL BUILD\n")
    write("firebase-config.js", make_config())
    write("auth.html", make_auth())
    write("index.html", make_index())
    write("profile.html", make_profile())
    write("upload.html", make_upload())
    write("chat.html", make_chat())
    print("\n✅ 6 ملفات جاهزة - بدون أخطاء!\n")

if __name__ == "__main__":
    main()
