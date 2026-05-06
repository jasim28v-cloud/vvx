#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════╗
║     💎 CRYSTΔL TIKTØK 2026 - Crystal Glass     ║
║          Big Smile Avatars - 8 Files            ║
║              جميع الملفات في ملف واحد            ║
╚══════════════════════════════════════════════════╝
"""

import os

# ============================================
# الإعدادات
# ============================================
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
ADMIN_EMAILS = ['jasim28v@gmail.com']
DICEBEAR_URL = "https://api.dicebear.com/7.x/big-smile/svg"

COVER_COLORS = [
    "linear-gradient(135deg, #6366f1, #06b6d4, #3b82f6)",
    "linear-gradient(135deg, #8b5cf6, #6366f1, #06b6d4)",
    "linear-gradient(135deg, #1e1b4b, #0e7490, #06b6d4)",
    "linear-gradient(135deg, #3b82f6, #06b6d4, #8b5cf6)",
    "linear-gradient(135deg, #06b6d4, #6366f1, #1e1b4b)",
]

def write(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ {filename}")

# ============================================
# firebase-config.js
# ============================================
def build_firebase_config():
    return f'''// 💎 CRYSTΔL Firebase + Cloudinary + DiceBear Config
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
const storage = firebase.storage();
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";
const DICEBEAR_URL = "{DICEBEAR_URL}";
const COVER_COLORS = {COVER_COLORS};
'''

# ============================================
# auth.html (تسجيل دخول + اشتراك - بدون شخصيات)
# ============================================
def build_auth():
    return '''<!DOCTYPE html>
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
        body{
            min-height:100vh;
            background:radial-gradient(ellipse at top, #1a1a2e, #0f0f1a, #000);
            display:flex;align-items:center;justify-content:center;
            font-family:'Segoe UI',sans-serif;overflow:hidden;
        }
        .bg-orb{
            position:fixed;border-radius:50%;filter:blur(130px);opacity:0.35;
            animation:orbFloat 20s infinite alternate;
        }
        .bg-orb:nth-child(1){width:400px;height:400px;background:#6366f1;top:-100px;left:-100px}
        .bg-orb:nth-child(2){width:350px;height:350px;background:#06b6d4;bottom:-100px;right:-100px;animation-delay:5s}
        .bg-orb:nth-child(3){width:300px;height:300px;background:#8b5cf6;top:50%;left:50%;animation-delay:10s}
        @keyframes orbFloat{0%{transform:translate(0,0) scale(1)}100%{transform:translate(50px,-50px) scale(1.3)}}
        .card{
            position:relative;z-index:1;width:90%;max-width:410px;
            background:rgba(255,255,255,0.03);
            backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
            border-radius:32px;padding:36px 24px;
            border:1px solid rgba(255,255,255,0.1);
            box-shadow:0 30px 70px rgba(0,0,0,0.5),inset 0 0 30px rgba(255,255,255,0.02);
            animation:fadeUp 0.8s ease;
        }
        @keyframes fadeUp{from{opacity:0;transform:translateY(40px)}to{opacity:1;transform:translateY(0)}}
        .logo{
            width:70px;height:70px;margin:0 auto 20px;
            background:linear-gradient(135deg, rgba(99,102,241,0.3), rgba(6,182,212,0.3));
            border-radius:20px;display:flex;align-items:center;justify-content:center;
            font-size:36px;border:1px solid rgba(255,255,255,0.15);
            box-shadow:0 15px 40px rgba(99,102,241,0.2);
        }
        h1{text-align:center;font-size:36px;font-weight:900;background:linear-gradient(to bottom, #fff, #a5b4fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:4px}
        .sub{text-align:center;color:rgba(255,255,255,0.5);font-size:13px;margin-bottom:20px}
        .tabs{display:flex;gap:4px;background:rgba(255,255,255,0.04);border-radius:40px;padding:4px;margin-bottom:24px}
        .tab{flex:1;padding:12px;background:none;border:none;color:rgba(255,255,255,0.5);cursor:pointer;border-radius:40px;font-size:14px;transition:all 0.3s;font-weight:500}
        .tab.active{background:linear-gradient(135deg, #6366f1, #06b6d4);color:#fff;box-shadow:0 8px 20px rgba(99,102,241,0.3)}
        .form{display:none;animation:fadeIn 0.4s ease}
        .form.active{display:block}
        @keyframes fadeIn{from{opacity:0}to{opacity:1}}
        input{
            width:100%;padding:15px 18px;margin:8px 0;
            border-radius:50px;background:rgba(255,255,255,0.04);
            border:1px solid rgba(255,255,255,0.1);color:#fff;
            font-size:14px;outline:none;transition:all 0.4s;
        }
        input:focus{border-color:rgba(99,102,241,0.6);box-shadow:0 0 20px rgba(99,102,241,0.1);background:rgba(255,255,255,0.07)}
        input::placeholder{color:rgba(255,255,255,0.3)}
        button{
            width:100%;padding:15px;margin-top:18px;
            background:linear-gradient(135deg, #6366f1, #06b6d4);
            border:none;border-radius:50px;color:#fff;
            font-weight:bold;font-size:15px;cursor:pointer;
            box-shadow:0 10px 30px rgba(99,102,241,0.3);
            transition:all 0.3s;
        }
        button:hover{transform:translateY(-2px);box-shadow:0 20px 40px rgba(99,102,241,0.4)}
        button:active{transform:scale(0.97)}
        .msg{text-align:center;color:#fca5a5;font-size:13px;margin-top:12px;min-height:20px}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div><div class="bg-orb"></div>
    <div class="card">
        <div class="logo">💎</div>
        <h1>CRYSTΔL</h1>
        <p class="sub">TikTok 2026 Ultra Pro</p>
        <div class="tabs">
            <button class="tab active" onclick="switchTab('login')">دخول</button>
            <button class="tab" onclick="switchTab('register')">اشتراك</button>
        </div>
        <div id="formLogin" class="form active">
            <input type="email" id="loginEmail" placeholder="📧 البريد الإلكتروني">
            <input type="password" id="loginPass" placeholder="🔒 كلمة المرور">
            <button onclick="doLogin()">🚀 تسجيل الدخول</button>
            <div class="msg" id="loginMsg"></div>
        </div>
        <div id="formRegister" class="form">
            <input type="text" id="regName" placeholder="👤 اسم المستخدم">
            <input type="email" id="regEmail" placeholder="📧 البريد الإلكتروني">
            <input type="password" id="regPass" placeholder="🔒 كلمة المرور (6 أحرف)">
            <button onclick="doRegister()">🎨 إنشاء حساب</button>
            <div class="msg" id="regMsg"></div>
        </div>
    </div>
    <script src="firebase-config.js"></script>
    <script>
        function switchTab(type){
            document.querySelectorAll('.tab').forEach(t=>t.classList.remove('active'));
            event.target.classList.add('active');
            document.querySelectorAll('.form').forEach(f=>f.classList.remove('active'));
            document.getElementById('form'+(type==='login'?'Login':'Register')).classList.add('active');
        }
        async function doLogin(){
            const e=document.getElementById('loginEmail').value,p=document.getElementById('loginPass').value,m=document.getElementById('loginMsg');
            if(!e||!p){m.innerText='املأ جميع الحقول';return}
            m.innerText='';
            try{await auth.signInWithEmailAndPassword(e,p);location.replace('index.html')}
            catch(err){m.innerText='❌ بيانات غير صحيحة'}
        }
        async function doRegister(){
            const u=document.getElementById('regName').value,e=document.getElementById('regEmail').value,p=document.getElementById('regPass').value,m=document.getElementById('regMsg');
            if(!u||!e||!p){m.innerText='املأ جميع الحقول';return}
            if(p.length<6){m.innerText='❌ كلمة المرور 6 أحرف على الأقل';return}
            m.innerText='';
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
                location.replace('index.html');
            }catch(err){
                if(err.code==='auth/email-already-in-use')m.innerText='❌ البريد مستخدم بالفعل';
                else m.innerText='❌ حدث خطأ';
            }
        }
        document.querySelectorAll('input').forEach(i=>i.addEventListener('keydown',e=>{if(e.key==='Enter'){if(document.getElementById('formLogin').classList.contains('active'))doLogin();else doRegister()}}));
    </script>
</body>
</html>'''

# ============================================
# index.html (التطبيق الرئيسي)
# ============================================
def build_index():
    return '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>💎 CRYSTΔL | الرئيسية</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(255,255,255,0.08);--accent:#6366f1;--accent2:#06b6d4;--bg:#050510}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;height:100vh;overflow:hidden;-webkit-tap-highlight-color:transparent;user-select:none}
        #mainApp{height:100vh;position:relative}
        
        /* TOP BAR */
        .topbar{position:fixed;top:0;left:0;right:0;z-index:100;display:flex;justify-content:space-between;align-items:center;padding:12px 20px;background:rgba(5,5,16,0.7);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);border-bottom:1px solid var(--border)}
        .logo-icon{width:36px;height:36px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:10px;display:flex;align-items:center;justify-content:center;font-weight:900;font-size:14px;box-shadow:0 8px 20px rgba(99,102,241,0.4)}
        .logo-text{font-weight:800;font-size:17px;background:linear-gradient(to bottom,#fff,#a5b4fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-left:8px}
        .tabs{display:flex;gap:4px;background:var(--glass);border-radius:30px;padding:3px}
        .tab{background:none;border:none;color:rgba(255,255,255,0.5);padding:7px 16px;cursor:pointer;border-radius:25px;font-size:13px;font-weight:500;transition:all 0.3s}
        .tab.active{background:rgba(99,102,241,0.2);color:#fff}
        .top-icons{display:flex;gap:16px}
        .top-icon{background:none;border:none;color:rgba(255,255,255,0.7);font-size:18px;cursor:pointer;transition:color 0.3s}
        .top-icon:hover{color:#a5b4fc}
        
        /* VIDEOS */
        .videos-wrap{height:100vh;overflow-y:scroll;scroll-snap-type:y mandatory;scrollbar-width:none;-ms-overflow-style:none}
        .videos-wrap::-webkit-scrollbar{display:none}
        .vid-card{height:100vh;scroll-snap-align:start;position:relative;background:#000}
        .vid-card video{width:100%;height:100%;object-fit:cover}
        
        /* INFO */
        .vid-info{position:absolute;bottom:90px;left:14px;right:80px;z-index:20;text-shadow:0 2px 10px rgba(0,0,0,0.8)}
        .author-row{display:flex;align-items:center;gap:10px;margin-bottom:6px}
        .author-avatar{width:46px;height:46px;border-radius:50%;display:flex;align-items:center;justify-content:center;overflow:hidden;cursor:pointer;border:2px solid rgba(255,255,255,0.3);box-shadow:0 8px 20px rgba(0,0,0,0.4)}
        .author-avatar img{width:100%;height:100%;object-fit:cover}
        .author-name{font-weight:700;font-size:15px;cursor:pointer;display:flex;align-items:center;gap:6px;flex-wrap:wrap}
        .badge{color:#a5b4fc;font-size:12px}
        .btn-follow{background:linear-gradient(135deg,var(--accent),var(--accent2));padding:5px 14px;border-radius:20px;font-size:11px;font-weight:700;border:none;color:#fff;cursor:pointer;box-shadow:0 4px 15px rgba(99,102,241,0.3)}
        .caption{font-size:14px;margin-bottom:5px;line-height:1.4}
        .tag{color:var(--accent2);cursor:pointer;font-weight:500}
        .music{font-size:12px;opacity:0.8;display:flex;align-items:center;gap:6px;cursor:pointer}
        
        /* SIDE */
        .side-btns{position:absolute;right:14px;bottom:130px;display:flex;flex-direction:column;gap:22px;z-index:20}
        .sbtn{display:flex;flex-direction:column;align-items:center;gap:3px;background:none;border:none;color:#fff;cursor:pointer;font-size:10px;transition:transform 0.15s}
        .sbtn:active{transform:scale(0.85)}
        .sbtn i{font-size:28px;filter:drop-shadow(0 3px 8px rgba(0,0,0,0.5))}
        .sbtn.liked i{color:var(--accent)}
        .sbtn .cnt{font-weight:700;font-size:11px}
        
        /* BOTTOM */
        .nav-bottom{position:fixed;bottom:0;left:0;right:0;display:flex;justify-content:space-around;align-items:center;padding:8px 0 20px;background:rgba(5,5,16,0.8);backdrop-filter:blur(30px);-webkit-backdrop-filter:blur(30px);z-index:100;border-top:1px solid var(--border)}
        .nav-item{display:flex;flex-direction:column;align-items:center;gap:3px;background:none;border:none;color:rgba(255,255,255,0.5);font-size:10px;cursor:pointer;transition:all 0.3s}
        .nav-item i{font-size:22px}
        .nav-item.active{color:#a5b4fc}
        .btn-add{width:48px;height:48px;background:linear-gradient(135deg,var(--accent),var(--accent2));border-radius:50%;display:flex;align-items:center;justify-content:center;margin-top:-24px;cursor:pointer;box-shadow:0 10px 30px rgba(99,102,241,0.5);border:none;color:#fff;font-size:20px}
        
        /* HEART */
        .heart-fly{position:fixed;font-size:80px;color:var(--accent);pointer-events:none;z-index:1000;animation:fly 0.8s ease-out forwards}
        @keyframes fly{0%{transform:scale(0.5) translateY(0);opacity:1}100%{transform:scale(1.5) translateY(-120px);opacity:0}}
        
        /* TOAST */
        .toast{position:fixed;bottom:100px;left:50%;transform:translateX(-50%);background:rgba(5,5,16,0.9);padding:10px 22px;border-radius:50px;z-index:1000;opacity:0;transition:opacity 0.3s;pointer-events:none;border:1px solid var(--border);font-size:13px}
        .toast.show{opacity:1}
        
        /* SPINNER */
        .spinner{width:32px;height:32px;border:3px solid rgba(99,102,241,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:0 auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .load-center{display:flex;align-items:center;justify-content:center;height:100vh;gap:10px;flex-direction:column;color:rgba(255,255,255,0.5)}
    </style>
</head>
<body>

<div id="mainApp">
    <!-- TOP BAR -->
    <div class="topbar">
        <div style="display:flex;align-items:center"><div class="logo-icon">💎</div><span class="logo-text">CRYSTΔL</span></div>
        <div class="tabs"><button class="tab" onclick="switchFeed('following')">متابَعين</button><button class="tab active" onclick="switchFeed('forYou')">لك</button></div>
        <div class="top-icons"><i class="fas fa-search top-icon" onclick="openSearch()"></i><i class="fas fa-bell top-icon" onclick="openNotifs()"></i></div>
    </div>
    
    <!-- VIDEOS -->
    <div class="videos-wrap" id="videosWrap"><div class="load-center"><div class="spinner"></div><span>💎 جاري التحميل...</span></div></div>
    
    <!-- BOTTOM -->
    <div class="nav-bottom">
        <button class="nav-item active" onclick="navTo('home')"><i class="fas fa-home"></i><span>الرئيسية</span></button>
        <button class="nav-item" onclick="navTo('search')"><i class="fas fa-search"></i><span>بحث</span></button>
        <button class="btn-add" onclick="window.location.href='upload.html'"><i class="fas fa-plus"></i></button>
        <button class="nav-item" onclick="window.location.href='chat.html'"><i class="fas fa-envelope"></i><span>رسائل</span></button>
        <button class="nav-item" onclick="window.location.href='profile.html'"><i class="fas fa-user"></i><span>ملفي</span></button>
    </div>
    
    <!-- TOAST -->
    <div id="toast" class="toast">✅ تم النسخ</div>
</div>

<script src="firebase-config.js"></script>
<script src="script.js"></script>
</body>
</html>'''

# ============================================
# profile.html (الملف الشخصي)
# ============================================
def build_profile():
    return '''<!DOCTYPE html>
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
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(255,255,255,0.08);--accent:#6366f1;--accent2:#06b6d4;--bg:#050510}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .cover{height:220px;position:relative;display:flex;align-items:flex-end;justify-content:center;padding-bottom:40px}
        .btn-back{position:fixed;top:16px;right:16px;background:rgba(0,0,0,0.5);backdrop-filter:blur(10px);width:42px;height:42px;border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;z-index:50;border:1px solid rgba(255,255,255,0.15);color:#fff;font-size:18px}
        .btn-cover{position:absolute;top:16px;left:16px;background:rgba(0,0,0,0.4);backdrop-filter:blur(10px);border:1px solid rgba(255,255,255,0.15);color:#fff;padding:8px 16px;border-radius:20px;font-size:12px;cursor:pointer;z-index:50}
        .avatar-lg{width:110px;height:110px;border-radius:50%;display:flex;align-items:center;justify-content:center;overflow:hidden;border:4px solid rgba(255,255,255,0.3);box-shadow:0 12px 40px rgba(0,0,0,0.5);cursor:pointer;position:relative;z-index:2}
        .avatar-lg img{width:100%;height:100%;object-fit:cover}
        .stats{display:flex;justify-content:center;gap:35px;margin:20px 0}
        .stat-val{font-size:22px;font-weight:700;color:#a5b4fc}
        .stat-lbl{font-size:11px;opacity:0.5;margin-top:2px}
        .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:3px;padding:0 12px}
        .thumb{aspect-ratio:9/16;background:rgba(255,255,255,0.03);border-radius:8px;display:flex;align-items:center;justify-content:center;cursor:pointer;position:relative;overflow:hidden;transition:transform 0.2s}
        .thumb:hover{transform:scale(1.03)}
        .thumb i{font-size:24px;color:rgba(255,255,255,0.6);z-index:1}
        .thumb img.thb{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.5}
        .btn{background:rgba(255,255,255,0.08);border:1px solid var(--border);padding:10px 24px;border-radius:30px;color:#fff;cursor:pointer;font-size:14px;margin:4px;transition:all 0.3s}
        .btn:hover{background:rgba(255,255,255,0.15)}
        .btn-primary{background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;box-shadow:0 8px 20px rgba(99,102,241,0.3)}
        .btn-primary:hover{box-shadow:0 12px 28px rgba(99,102,241,0.5)}
        .spinner{width:32px;height:32px;border:3px solid rgba(99,102,241,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .load-center{display:flex;align-items:center;justify-content:center;min-height:80vh;flex-direction:column;gap:12px;color:rgba(255,255,255,0.5)}
    </style>
</head>
<body>
<div class="load-center" id="loader"><div class="spinner"></div><span>💎 تحميل الملف...</span></div>

<div id="profileContent" style="display:none">
    <div class="cover" id="profileCover"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><button class="btn-cover" onclick="changeCover()"><i class="fas fa-palette"></i> تغيير الغلاف</button><div class="avatar-lg" id="avatarDisplay" onclick="document.getElementById('avatarInput').click()"><img src="" alt="avatar"></div></div>
    <input type="file" id="avatarInput" accept="image/*" style="display:none" onchange="uploadAvatar(this)">
    <div style="text-align:center;padding:0 20px">
        <h2 id="nameDisplay" style="font-size:22px;font-weight:700;margin-top:8px"></h2>
        <p id="bioDisplay" style="font-size:13px;opacity:0.5;margin-top:4px"></p>
        <div class="stats"><div style="text-align:center"><div class="stat-val" id="statFollowing">0</div><div class="stat-lbl">يتابع</div></div><div style="text-align:center"><div class="stat-val" id="statFollowers">0</div><div class="stat-lbl">متابع</div></div><div style="text-align:center"><div class="stat-val" id="statLikes">0</div><div class="stat-lbl">إعجابات</div></div></div>
        <div id="actionsBar" style="margin:12px 0"></div>
    </div>
    <div style="padding:16px"><h3 style="font-weight:700;margin-bottom:12px">🎬 فيديوهاتي</h3><div class="grid" id="videosGrid"></div></div>
    
    <!-- Admin Section -->
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
        await loadEverything();
        await loadProfile();
        document.getElementById('loader').style.display='none';
        document.getElementById('profileContent').style.display='block';
    });
    
    async function loadEverything(){
        const us=await db.ref('users').once('value');allUsers=us.val()||{};
        const vs=await db.ref('videos').once('value');allVideos=Object.entries(vs.val()||{}).map(([k,v])=>({id:k,...v}));
    }
    
    async function loadProfile(){
        const u=allUsers[profileUserId]||currentUserData;
        if(!u)return;
        document.getElementById('nameDisplay').innerHTML='@'+(u.username||'مستخدم')+(u.isVerified?' <span style="color:#a5b4fc">✅</span>':'');
        document.getElementById('bioDisplay').innerText=u.bio||'';
        document.getElementById('statFollowing').innerText=Object.keys(u.following||{}).length;
        document.getElementById('statFollowers').innerText=Object.keys(u.followers||{}).length;
        const uvs=allVideos.filter(v=>v.sender===profileUserId);
        document.getElementById('statLikes').innerText=uvs.reduce((s,v)=>s+(v.likes||0),0);
        document.getElementById('profileCover').style.background=u.coverColor||COVER_COLORS[0];
        const avImg=document.querySelector('#avatarDisplay img');
        avImg.src=u.avatarUrl||(DICEBEAR_URL+'?seed='+profileUserId);
        const g=document.getElementById('videosGrid');g.innerHTML='';
        if(!uvs.length)g.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px;grid-column:1/-1">لا توجد فيديوهات بعد</div>';
        else uvs.forEach(v=>{const d=document.createElement('div');d.className='thumb';d.innerHTML=`<i class="fas fa-play"></i>${v.thumbnail?`<img src="${v.thumbnail}" class="thb">`:''}`;d.onclick=()=>window.open(v.url,'_blank');g.appendChild(d)});
        const ab=document.getElementById('actionsBar');ab.innerHTML=`
            <button class="btn btn-primary" onclick="openEdit()"><i class="fas fa-edit"></i> تعديل</button>
            <button class="btn" onclick="auth.signOut();window.location.href='auth.html'"><i class="fas fa-sign-out-alt"></i> خروج</button>
        `;
        if(currentUserData?.email==='jasim28v@gmail.com')await loadAdmin();
    }
    
    async function loadAdmin(){
        document.getElementById('adminSection').style.display='block';
        const us=allUsers,vs={};allVideos.forEach(v=>vs[v.id]=v);
        const tl=Object.values(vs).reduce((s,v)=>s+(v.likes||0),0);
        const bu=Object.values(us).filter(u=>u.banned).length;
        const vu=Object.values(us).filter(u=>u.isVerified).length;
        document.getElementById('adminSection').innerHTML=`
            <div style="margin-top:20px;padding:16px;background:rgba(99,102,241,0.05);border-radius:16px;border:1px solid rgba(99,102,241,0.15)">
                <h3 style="color:#a5b4fc;font-weight:700;margin-bottom:12px">🛡️ لوحة الأدمن</h3>
                <div style="display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-bottom:16px">
                    <div style="background:rgba(0,0,0,0.3);border-radius:10px;padding:10px;text-align:center"><div style="font-size:20px;font-weight:700;color:#a5b4fc">${Object.keys(us).length}</div><div style="font-size:10px;opacity:0.5">مستخدمين</div></div>
                    <div style="background:rgba(0,0,0,0.3);border-radius:10px;padding:10px;text-align:center"><div style="font-size:20px;font-weight:700;color:#a5b4fc">${Object.keys(vs).length}</div><div style="font-size:10px;opacity:0.5">فيديوهات</div></div>
                    <div style="background:rgba(0,0,0,0.3);border-radius:10px;padding:10px;text-align:center"><div style="font-size:20px;font-weight:700;color:#a5b4fc">${tl}</div><div style="font-size:10px;opacity:0.5">إعجابات</div></div>
                    <div style="background:rgba(0,0,0,0.3);border-radius:10px;padding:10px;text-align:center"><div style="font-size:20px;font-weight:700;color:#a5b4fc">${bu}</div><div style="font-size:10px;opacity:0.5">محظورين</div></div>
                    <div style="background:rgba(0,0,0,0.3);border-radius:10px;padding:10px;text-align:center"><div style="font-size:20px;font-weight:700;color:#a5b4fc">${vu}</div><div style="font-size:10px;opacity:0.5">موثقين</div></div>
                </div>
                <h4 style="font-weight:700;margin-bottom:8px;color:#fbbf24">✅ توثيق</h4>
                <div style="max-height:200px;overflow-y:auto">${Object.entries(us).slice(0,10).map(([id,u])=>`<div style="display:flex;justify-content:space-between;align-items:center;background:rgba(0,0,0,0.3);padding:8px;border-radius:10px;margin-bottom:6px"><div style="display:flex;align-items:center;gap:8px"><img src="${u.avatarUrl||(DICEBEAR_URL+'?seed='+id)}" style="width:32px;height:32px;border-radius:50%"><span>@${u.username||'?'} ${u.isVerified?'<span style="color:#a5b4fc">✅</span>':''}</span></div><button style="background:rgba(251,191,36,0.2);border:none;color:#fbbf24;padding:5px 12px;border-radius:20px;font-size:11px;cursor:pointer" onclick="toggleVerify('${id}')">${u.isVerified?'إلغاء':'توثيق'}</button></div>`).join('')}</div>
                <h4 style="font-weight:700;margin:16px 0 8px">🗑️ حذف فيديوهات</h4>
                <div style="max-height:200px;overflow-y:auto">${Object.entries(vs).reverse().slice(0,10).map(([id,v])=>`<div style="display:flex;justify-content:space-between;align-items:center;background:rgba(0,0,0,0.3);padding:8px;border-radius:10px;margin-bottom:6px"><div style="display:flex;align-items:center;gap:8px"><i class="fas fa-video"></i><span style="font-size:13px">${(v.description||'فيديو').substring(0,30)}</span></div><button style="background:rgba(239,68,68,0.2);border:none;color:#f87171;padding:5px 12px;border-radius:20px;font-size:11px;cursor:pointer" onclick="delVid('${id}')">حذف</button></div>`).join('')}</div>
            </div>`;
        window.toggleVerify=async(id)=>{if(confirm('تأكيد؟')){const r=db.ref('users/'+id);const s=await r.once('value');const d=s.val();await r.update({isVerified:!d.isVerified});alert('✅');loadProfile()}};
        window.delVid=async(id)=>{if(confirm('حذف؟')){await db.ref('videos/'+id).remove();alert('✅');loadProfile()}};
    }
    
    function openEdit(){
        const u=allUsers[profileUserId]||currentUserData;
        const name=prompt('اسم المستخدم:',u?.username||'');
        const bio=prompt('السيرة الذاتية:',u?.bio||'');
        if(name!==null&&bio!==null){
            db.ref('users/'+profileUserId).update({username:name,bio:bio});
            loadProfile();
        }
    }
    
    async function changeCover(){
        const idx=prompt(`اختر غلاف (1-${COVER_COLORS.length}):`);
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
    
    function changeAvatar(){document.getElementById('avatarInput').click()}
</script>
</body>
</html>'''

# ============================================
# admin.html (لوحة الأدمن منفصلة)
# ============================================
def build_admin():
    return '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 CRYSTΔL | لوحة الأدمن</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(255,255,255,0.08);--accent:#6366f1;--accent2:#06b6d4;--bg:#050510}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;padding:16px;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;margin-bottom:20px}
        .btn-back{background:rgba(255,255,255,0.08);border:1px solid var(--border);width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:18px}
        h1{font-size:24px;font-weight:800;background:linear-gradient(to bottom,#fff,#a5b4fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
        .card{background:rgba(255,255,255,0.03);border:1px solid var(--border);border-radius:20px;padding:16px;margin-bottom:16px;backdrop-filter:blur(20px)}
        .card h3{color:#a5b4fc;margin-bottom:12px;font-size:16px}
        .stats{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-bottom:16px}
        .stat-box{background:rgba(0,0,0,0.3);border-radius:10px;padding:10px;text-align:center}
        .stat-num{font-size:22px;font-weight:700;color:#a5b4fc}
        .stat-label{font-size:10px;opacity:0.5;margin-top:2px}
        .list{max-height:300px;overflow-y:auto}
        .item{display:flex;justify-content:space-between;align-items:center;background:rgba(0,0,0,0.3);padding:10px;border-radius:12px;margin-bottom:6px;gap:10px}
        .item-info{display:flex;align-items:center;gap:8px;overflow:hidden}
        .item-avatar{width:36px;height:36px;border-radius:50%;overflow:hidden;flex-shrink:0}
        .item-avatar img{width:100%;height:100%;object-fit:cover}
        .item-name{font-weight:600;font-size:14px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
        .btn-sm{padding:6px 14px;border-radius:20px;font-size:11px;cursor:pointer;border:none;font-weight:600}
        .btn-verify{background:rgba(251,191,36,0.2);color:#fbbf24}
        .btn-delete{background:rgba(239,68,68,0.2);color:#f87171}
        .btn-ban{background:rgba(239,68,68,0.2);color:#f87171}
        .btn-unban{background:rgba(34,197,94,0.2);color:#4ade80}
        .spinner{width:32px;height:32px;border:3px solid rgba(99,102,241,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .load-center{display:flex;align-items:center;justify-content:center;min-height:80vh;flex-direction:column;gap:12px;color:rgba(255,255,255,0.5)}
    </style>
</head>
<body>
<div class="load-center" id="loader"><div class="spinner"></div><span>💎 تحميل لوحة الأدمن...</span></div>
<div id="content" style="display:none">
    <div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h1>🛡️ لوحة الأدمن</h1></div>
    <div id="adminContent"></div>
</div>

<script src="firebase-config.js"></script>
<script>
    const ADMIN_EMAILS=['jasim28v@gmail.com'];
    let currentUser=null;
    
    auth.onAuthStateChanged(async u=>{
        if(!u){window.location.href='auth.html';return}
        currentUser=u;
        if(!ADMIN_EMAILS.includes(u.email)){alert('غير مصرح');window.location.href='index.html';return}
        await loadAdmin();
        document.getElementById('loader').style.display='none';
        document.getElementById('content').style.display='block';
    });
    
    async function loadAdmin(){
        const us=await db.ref('users').once('value');const users=us.val()||{};
        const vs=await db.ref('videos').once('value');const videos=vs.val()||{};
        const tl=Object.values(videos).reduce((s,v)=>s+(v.likes||0),0);
        const bu=Object.values(users).filter(u=>u.banned).length;
        const vu=Object.values(users).filter(u=>u.isVerified).length;
        document.getElementById('adminContent').innerHTML=`
            <div class="card">
                <h3>📊 إحصائيات</h3>
                <div class="stats">
                    <div class="stat-box"><div class="stat-num">${Object.keys(users).length}</div><div class="stat-label">مستخدمين</div></div>
                    <div class="stat-box"><div class="stat-num">${Object.keys(videos).length}</div><div class="stat-label">فيديوهات</div></div>
                    <div class="stat-box"><div class="stat-num">${tl}</div><div class="stat-label">إعجابات</div></div>
                    <div class="stat-box"><div class="stat-num">${bu}</div><div class="stat-label">محظورين</div></div>
                    <div class="stat-box"><div class="stat-num">${vu}</div><div class="stat-label">موثقين</div></div>
                </div>
            </div>
            <div class="card"><h3>✅ توثيق الحسابات</h3><div class="list">${Object.entries(users).slice(0,20).map(([id,u])=>`<div class="item"><div class="item-info"><div class="item-avatar"><img src="${u.avatarUrl||(DICEBEAR_URL+'?seed='+id)}"></div><div class="item-name">@${u.username||'?'} ${u.isVerified?'<span style="color:#a5b4fc">✅</span>':''}</div></div><button class="btn-sm btn-verify" onclick="toggleV('${id}')">${u.isVerified?'إلغاء':'توثيق'}</button></div>`).join('')}</div></div>
            <div class="card"><h3>🗑️ حذف فيديوهات</h3><div class="list">${Object.entries(videos).reverse().slice(0,15).map(([id,v])=>`<div class="item"><div class="item-info"><i class="fas fa-video"></i><span style="font-size:13px">${(v.description||'فيديو').substring(0,35)}</span></div><button class="btn-sm btn-delete" onclick="delV('${id}')">حذف</button></div>`).join('')}</div></div>
            <div class="card"><h3>👥 إدارة المستخدمين</h3><div class="list">${Object.entries(users).slice(0,15).map(([id,u])=>`<div class="item"><div class="item-info"><div class="item-avatar"><img src="${u.avatarUrl||(DICEBEAR_URL+'?seed='+id)}"></div><div class="item-name">@${u.username||'?'} ${u.banned?'<span style="background:#ef4444;padding:1px 6px;border-radius:8px;font-size:9px">محظور</span>':''} ${u.isVerified?'<span style="color:#a5b4fc">✅</span>':''}</div></div><div>${u.banned?`<button class="btn-sm btn-unban" onclick="unban('${id}')">إلغاء الحظر</button>`:`<button class="btn-sm btn-ban" onclick="ban('${id}')">حظر</button>`}<button class="btn-sm btn-delete" style="margin-right:4px" onclick="delU('${id}')">حذف</button></div></div>`).join('')}</div></div>`;
        window.toggleV=async(id)=>{if(confirm('تأكيد؟')){const r=await db.ref('users/'+id).once('value');const d=r.val();await db.ref('users/'+id).update({isVerified:!d.isVerified});alert('✅');loadAdmin()}};
        window.delV=async(id)=>{if(confirm('حذف الفيديو؟')){await db.ref('videos/'+id).remove();alert('✅');loadAdmin()}};
        window.ban=async(id)=>{if(confirm('حظر المستخدم؟')){await db.ref('users/'+id+'/banned').set(true);alert('✅');loadAdmin()}};
        window.unban=async(id)=>{if(confirm('إلغاء الحظر؟')){await db.ref('users/'+id+'/banned').remove();alert('✅');loadAdmin()}};
        window.delU=async(id)=>{if(confirm('حذف المستخدم؟')){await db.ref('users/'+id).remove();const vs=await db.ref('videos').once('value');Object.entries(vs.val()||{}).forEach(([k,v])=>{if(v.sender===id)db.ref('videos/'+k).remove()});alert('✅');loadAdmin()}};
    }
</script>
</body>
</html>'''

# ============================================
# chat.html (الدردشة)
# ============================================
def build_chat():
    return '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 CRYSTΔL | الدردشة</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-storage-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(255,255,255,0.08);--accent:#6366f1;--accent2:#06b6d4;--bg:#050510}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;height:100vh;display:flex;flex-direction:column}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(5,5,16,0.8);backdrop-filter:blur(20px)}
        .btn-back{background:rgba(255,255,255,0.08);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        .chat-avatar{width:40px;height:40px;border-radius:50%;overflow:hidden;background:linear-gradient(135deg,var(--accent),var(--accent2));display:flex;align-items:center;justify-content:center}
        .chat-avatar img{width:100%;height:100%;object-fit:cover}
        .msgs{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px}
        .bubble{max-width:80%;padding:10px 16px;border-radius:20px;word-break:break-word;font-size:14px}
        .bubble.sent{background:linear-gradient(135deg,var(--accent),var(--accent2));align-self:flex-end;color:#fff;border-bottom-right-radius:6px}
        .bubble.received{background:rgba(255,255,255,0.06);align-self:flex-start;border-bottom-left-radius:6px}
        .bubble img{max-width:200px;max-height:200px;border-radius:12px;cursor:pointer}
        .bubble .time{font-size:9px;opacity:0.5;margin-top:4px;text-align:left}
        .input-bar{display:flex;gap:10px;padding:12px;background:rgba(5,5,16,0.9);border-top:1px solid var(--border);align-items:center}
        .input-bar input{flex:1;padding:12px 16px;border-radius:30px;background:var(--glass);border:1px solid var(--border);color:#fff;font-size:14px;outline:none}
        .input-bar input:focus{border-color:var(--accent)}
        .btn-send{width:42px;height:42px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:50%;color:#fff;cursor:pointer;font-size:18px;display:flex;align-items:center;justify-content:center}
        .btn-attach{width:38px;height:38px;background:var(--glass);border:1px solid var(--border);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;color:#fff}
        .conv-item{display:flex;align-items:center;gap:12px;padding:14px;border-bottom:1px solid var(--border);cursor:pointer;transition:background 0.2s}
        .conv-item:hover{background:rgba(255,255,255,0.03)}
        .spinner{width:32px;height:32px;border:3px solid rgba(99,102,241,0.2);border-top-color:var(--accent);border-radius:50%;animation:spin 0.7s linear infinite;margin:30px auto}
        @keyframes spin{to{transform:rotate(360deg)}}
        .load-center{display:flex;align-items:center;justify-content:center;flex:1;flex-direction:column;gap:12px;color:rgba(255,255,255,0.5)}
    </style>
</head>
<body>
<div class="load-center" id="loader"><div class="spinner"></div><span>💎 تحميل...</span></div>

<!-- CONVERSATIONS -->
<div id="convView" style="display:none;flex:1;flex-direction:column;overflow:hidden">
    <div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2 style="font-size:18px;font-weight:700">💬 المحادثات</h2></div>
    <div id="convList" style="flex:1;overflow-y:auto"></div>
</div>

<!-- CHAT -->
<div id="chatView" style="display:none;flex:1;flex-direction:column;overflow:hidden">
    <div class="header"><button class="btn-back" onclick="showConvs()"><i class="fas fa-arrow-right"></i></button><div class="chat-avatar" id="chatAvatar"><span style="font-size:20px">👤</span></div><h3 id="chatName" style="font-size:16px;font-weight:700">محادثة</h3></div>
    <div class="msgs" id="msgsList"></div>
    <div class="input-bar">
        <div class="btn-attach" onclick="document.getElementById('imgInput').click()"><i class="fas fa-image"></i></div>
        <input type="file" id="imgInput" accept="image/*" style="display:none" onchange="sendImg(this)">
        <input type="text" id="msgInput" placeholder="اكتب رسالة..." onkeydown="if(event.key==='Enter')sendMsg()">
        <button class="btn-send" onclick="sendMsg()"><i class="fas fa-paper-plane"></i></button>
    </div>
</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser=null,allUsers={},chatUserId=null;
    
    auth.onAuthStateChanged(async u=>{
        if(!u){window.location.href='auth.html';return}
        currentUser=u;
        const us=await db.ref('users').once('value');allUsers=us.val()||{};
        document.getElementById('loader').style.display='none';
        showConvs();
    });
    
    function showConvs(){
        document.getElementById('chatView').style.display='none';
        document.getElementById('convView').style.display='flex';
        chatUserId=null;
        loadConvs();
    }
    
    async function loadConvs(){
        const cl=document.getElementById('convList');cl.innerHTML='';
        const snap=await db.ref('private_messages').once('value');
        const all=snap.val()||{};
        const found=new Set();
        Object.keys(all).forEach(cid=>{
            const[u1,u2]=cid.split('_');
            const other=u1===currentUser.uid?u2:u2===currentUser.uid?u1:null;
            if(other&&!found.has(other)&&allUsers[other])found.add(other)
        });
        if(!found.size){cl.innerHTML='<div style="text-align:center;opacity:0.5;padding:40px">لا توجد محادثات</div>';return}
        found.forEach(uid=>{
            const u=allUsers[uid];
            const d=document.createElement('div');d.className='conv-item';
            d.innerHTML=`<div class="chat-avatar"><img src="${u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid)}"></div><div><div style="font-weight:600">@${u?.username||'مستخدم'} ${u?.isVerified?'<span style="color:#a5b4fc">✅</span>':''}</div><div style="font-size:12px;opacity:0.5">💬 اضغط للمحادثة</div></div>`;
            d.onclick=()=>openChat(uid);
            cl.appendChild(d);
        });
    }
    
    async function openChat(uid){
        chatUserId=uid;
        const u=allUsers[uid];
        document.getElementById('chatName').innerText='@'+(u?.username||'مستخدم');
        const ca=document.getElementById('chatAvatar');ca.innerHTML='';
        const img=document.createElement('img');img.src=u?.avatarUrl||(DICEBEAR_URL+'?seed='+uid);ca.appendChild(img);
        document.getElementById('convView').style.display='none';
        document.getElementById('chatView').style.display='flex';
        await loadMsgs();
    }
    
    function getChatId(){return[currentUser.uid,chatUserId].sort().join('_')}
    
    async function loadMsgs(){
        const ml=document.getElementById('msgsList');ml.innerHTML='';
        if(!chatUserId)return;
        const snap=await db.ref('private_messages/'+getChatId()).once('value');
        const ms=snap.val()||{};
        Object.values(ms).sort((a,b)=>a.timestamp-b.timestamp).forEach(m=>{
            const sent=m.senderId===currentUser.uid;
            const d=document.createElement('div');d.className='bubble '+(sent?'sent':'received');
            d.innerHTML=`${m.type==='image'?`<img src="${m.imageUrl}" onclick="window.open('${m.imageUrl}')">`:m.text}<div class="time">${new Date(m.timestamp).toLocaleTimeString()}</div>`;
            ml.appendChild(d);
        });
        ml.scrollTop=ml.scrollHeight;
    }
    
    async function sendMsg(){
        const inp=document.getElementById('msgInput');
        const txt=inp.value.trim();if(!txt||!chatUserId)return;
        await db.ref('private_messages/'+getChatId()).push({senderId:currentUser.uid,text:txt,type:'text',timestamp:Date.now()});
        inp.value='';await loadMsgs();
    }
    
    async function sendImg(inp){
        const file=inp.files[0];if(!file||!chatUserId)return;
        const fd=new FormData();fd.append('file',file);fd.append('upload_preset',UPLOAD_PRESET);
        const res=await fetch('https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/image/upload',{method:'POST',body:fd});
        const data=await res.json();
        await db.ref('private_messages/'+getChatId()).push({senderId:currentUser.uid,imageUrl:data.secure_url,type:'image',timestamp:Date.now()});
        inp.value='';await loadMsgs();
    }
    
    db.ref('private_messages').on('child_changed',()=>{if(chatUserId)loadMsgs()});
    db.ref('private_messages').on('child_added',()=>{if(chatUserId)loadMsgs()});
</script>
</body>
</html>'''

# ============================================
# upload.html (رفع الفيديو)
# ============================================
def build_upload():
    return '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 CRYSTΔL | رفع فيديو</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{--glass:rgba(255,255,255,0.03);--border:rgba(255,255,255,0.08);--accent:#6366f1;--accent2:#06b6d4;--bg:#050510}
        *{margin:0;padding:0;box-sizing:border-box}
        body{font-family:'Segoe UI',sans-serif;background:var(--bg);color:#fff;min-height:100vh;overflow-y:auto}
        .header{display:flex;align-items:center;gap:12px;padding:16px;border-bottom:1px solid var(--border);background:rgba(5,5,16,0.8);backdrop-filter:blur(20px);position:sticky;top:0;z-index:10}
        .btn-back{background:rgba(255,255,255,0.08);border:1px solid var(--border);width:38px;height:38px;border-radius:50%;display:flex;align-items:center;justify-content:center;color:#fff;cursor:pointer;font-size:16px}
        h2{font-size:18px;font-weight:700}
        .container{max-width:500px;margin:0 auto;padding:20px}
        .dropzone{border:2px dashed rgba(99,102,241,0.3);border-radius:20px;padding:50px 20px;text-align:center;cursor:pointer;background:var(--glass);transition:all 0.3s;margin-bottom:20px}
        .dropzone:hover{border-color:var(--accent);background:rgba(99,102,241,0.05)}
        .dropzone i{font-size:48px;color:var(--accent);margin-bottom:12px}
        .dropzone p{font-size:15px;margin-bottom:4px}
        .dropzone span{font-size:11px;opacity:0.5}
        .dropzone video{width:100%;max-height:250px;object-fit:contain;margin-top:12px;border-radius:12px;display:none}
        .form-card{background:var(--glass);border:1px solid var(--border);border-radius:20px;padding:20px}
        .form-card label{display:block;font-size:13px;opacity:0.7;margin-bottom:6px;margin-top:12px}
        .form-card textarea,.form-card input{width:100%;padding:14px 16px;border-radius:16px;background:rgba(255,255,255,0.04);border:1px solid var(--border);color:#fff;font-size:14px;outline:none;resize:none;font-family:'Segoe UI',sans-serif}
        .form-card textarea:focus,.form-card input:focus{border-color:var(--accent)}
        .form-card textarea{min-height:80px}
        .progress-wrap{display:none;margin:16px 0}
        .progress-bar{background:rgba(255,255,255,0.1);border-radius:30px;height:6px;overflow:hidden}
        .progress-fill{background:linear-gradient(90deg,var(--accent),var(--accent2));height:100%;border-radius:30px;transition:width 0.3s;width:0%}
        .progress-text{text-align:center;font-size:12px;margin-top:6px;color:#a5b4fc}
        .btn-upload{width:100%;padding:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));border:none;border-radius:30px;color:#fff;font-weight:700;font-size:15px;cursor:pointer;box-shadow:0 10px 25px rgba(99,102,241,0.3);margin-top:16px;transition:all 0.3s}
        .btn-upload:hover{transform:translateY(-1px);box-shadow:0 14px 32px rgba(99,102,241,0.4)}
        .btn-upload:disabled{opacity:0.5;pointer-events:none}
        .status{text-align:center;margin-top:12px;font-size:13px}
    </style>
</head>
<body>
<div class="header"><button class="btn-back" onclick="window.location.href='index.html'"><i class="fas fa-arrow-right"></i></button><h2>📤 رفع فيديو جديد</h2></div>
<div class="container">
    <div class="dropzone" onclick="document.getElementById('videoFile').click()">
        <i class="fas fa-cloud-upload-alt"></i>
        <p>اضغط لاختيار فيديو</p>
        <span>MP4, MOV - حتى 100MB</span>
        <video id="preview" controls></video>
    </div>
    <input type="file" id="videoFile" accept="video/*" style="display:none" onchange="onFilePick(this)">
    <div class="form-card">
        <label>🎬 وصف الفيديو</label>
        <textarea id="vidDesc" placeholder="اكتب وصفاً... #هاشتاقات"></textarea>
        <label>🎵 الموسيقى</label>
        <input type="text" id="vidMusic" placeholder="Original Sound">
        <div class="progress-wrap" id="progressWrap"><div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div><div class="progress-text" id="progressText">0%</div></div>
        <button class="btn-upload" id="uploadBtn" onclick="upload()">🚀 رفع الفيديو</button>
        <div class="status" id="status"></div>
    </div>
</div>

<script src="firebase-config.js"></script>
<script>
    let currentUser=null,currentUserData=null,selectedFile=null;
    
    auth.onAuthStateChanged(async u=>{
        if(!u)window.location.href='auth.html';
        currentUser=u;
        const snap=await db.ref('users/'+u.uid).get();
        if(snap.exists())currentUserData={uid:u.uid,...snap.val()};
    });
    
    function onFilePick(inp){
        const f=inp.files[0];
        if(!f||!f.type.startsWith('video/')){alert('اختر فيديو صحيح');return}
        if(f.size>100*1024*1024){alert('أقل من 100MB');return}
        selectedFile=f;
        const r=new FileReader();r.onload=e=>{const v=document.getElementById('preview');v.src=e.target.result;v.style.display='block'};r.readAsDataURL(f);
    }
    
    async function upload(){
        if(!selectedFile){alert('اختر فيديو');return}
        if(!currentUser){alert('سجل دخول');return}
        const desc=document.getElementById('vidDesc').value;
        const music=document.getElementById('vidMusic').value||'Original Sound';
        const pw=document.getElementById('progressWrap');pw.style.display='block';
        const pf=document.getElementById('progressFill');pf.style.width='0%';
        const pt=document.getElementById('progressText');pt.innerText='0%';
        const st=document.getElementById('status');st.innerHTML='';
        const btn=document.getElementById('uploadBtn');btn.disabled=true;
        const fd=new FormData();fd.append('file',selectedFile);fd.append('upload_preset',UPLOAD_PRESET);
        const xhr=new XMLHttpRequest();
        xhr.open('POST','https://api.cloudinary.com/v1_1/'+CLOUD_NAME+'/video/upload');
        xhr.upload.onprogress=e=>{if(e.lengthComputable){const p=Math.round(e.loaded/e.total*100);pf.style.width=p+'%';pt.innerText=p+'%'}};
        xhr.onload=async()=>{
            const r=JSON.parse(xhr.responseText);
            await db.ref('videos/').push({url:r.secure_url,thumbnail:r.secure_url.replace('.mp4','.jpg'),description:desc,music:music,sender:currentUser.uid,senderName:currentUserData?.username,likes:0,likedBy:{},comments:{},timestamp:Date.now()});
            st.innerHTML='✅ تم الرفع بنجاح!';st.style.color='#4ade80';
            setTimeout(()=>window.location.href='index.html',1500);
        };
        xhr.onerror=()=>{st.innerHTML='❌ فشل الرفع';btn.disabled=false;st.style.color='#f87171'};
        xhr.send(fd);
    }
</script>
</body>
</html>'''

# ============================================
# script.js (المنطق المشترك)
# ============================================
def build_script():
    return r'''// 💎 CRYSTΔL Core Script
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
'''

# ============================================
# MAIN
# ============================================
def main():
    print("╔══════════════════════════════════════╗")
    print("║  💎 CRYSTΔL TIKTØK 2026 GENERATOR  ║")
    print("║     Big Smile Avatars - 8 Files     ║")
    print("╚══════════════════════════════════════╝")
    print()
    
    write("firebase-config.js", build_firebase_config())
    write("auth.html", build_auth())
    write("index.html", build_index())
    write("profile.html", build_profile())
    write("admin.html", build_admin())
    write("chat.html", build_chat())
    write("upload.html", build_upload())
    write("script.js", build_script())
    
    print()
    print("══════════════════════════════════════")
    print("  ✅ 8 ملفات جاهزة!")
    print("  📂 auth.html | index.html")
    print("  📂 profile.html | admin.html")
    print("  📂 chat.html | upload.html")
    print("  📂 firebase-config.js | script.js")
    print("  🎨 Big Smile Avatars عشوائية")
    print("  💎 تصميم كريستالي شفاف")
    print("══════════════════════════════════════")

if __name__ == "__main__":
    main()
