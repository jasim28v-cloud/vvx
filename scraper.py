#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════╗
║            💎 CRYSTΔL TIKTØK 2026              ║
║         TikTok Ultra Pro - Crystal Glass        ║
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

CARTOON_AVATARS = [
    {"emoji": "🦁", "name": "الأسد", "bg": "linear-gradient(135deg, #FF6B35, #FFD700)"},
    {"emoji": "🐰", "name": "الأرنب", "bg": "linear-gradient(135deg, #00D2FF, #7B68EE)"},
    {"emoji": "🦊", "name": "الثعلب", "bg": "linear-gradient(135deg, #FF4500, #FF8C00)"},
    {"emoji": "🐼", "name": "الباندا", "bg": "linear-gradient(135deg, #2C3E50, #BDC3C7)"},
    {"emoji": "🐱", "name": "القط", "bg": "linear-gradient(135deg, #8E44AD, #3498DB)"},
    {"emoji": "🐻", "name": "الدب", "bg": "linear-gradient(135deg, #8B4513, #D2691E)"},
    {"emoji": "🐯", "name": "النمر", "bg": "linear-gradient(135deg, #FFA500, #FF0000)"},
    {"emoji": "🐵", "name": "القرد", "bg": "linear-gradient(135deg, #A0522D, #DEB887)"},
    {"emoji": "🐶", "name": "الكلب", "bg": "linear-gradient(135deg, #D4A574, #8B6914)"},
    {"emoji": "🦄", "name": "يونيكورن", "bg": "linear-gradient(135deg, #FF69B4, #9B59B6)"},
    {"emoji": "🐲", "name": "التنين", "bg": "linear-gradient(135deg, #006400, #00FF00)"},
    {"emoji": "🦅", "name": "النسر", "bg": "linear-gradient(135deg, #8B0000, #FF6347)"},
    {"emoji": "🐬", "name": "الدولفين", "bg": "linear-gradient(135deg, #000080, #1E90FF)"},
    {"emoji": "🦋", "name": "الفراشة", "bg": "linear-gradient(135deg, #DA70D6, #FF1493)"},
    {"emoji": "🦉", "name": "البومة", "bg": "linear-gradient(135deg, #8B4513, #F4A460)"},
    {"emoji": "🐘", "name": "الفيل", "bg": "linear-gradient(135deg, #808080, #A9A9A9)"}
]

def write(filename, content):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  ✅ {filename}")

# ============================================
# firebase-config.js
# ============================================
def build_firebase_config():
    return f'''// 💎 CRYSTΔL Firebase Config
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
'''

# ============================================
# login.html
# ============================================
def build_login():
    return '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 CRYSTΔL | دخول</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            min-height:100vh;
            background: radial-gradient(ellipse at top, #1a1a2e, #0f0f1a, #000);
            display:flex;align-items:center;justify-content:center;
            font-family:'Segoe UI',sans-serif;
            overflow:hidden;
        }
        .bg-orb{
            position:fixed;border-radius:50%;filter:blur(120px);opacity:0.4;
            animation:orbFloat 20s infinite alternate;
        }
        .bg-orb:nth-child(1){width:400px;height:400px;background:#6366f1;top:-100px;left:-100px;}
        .bg-orb:nth-child(2){width:350px;height:350px;background:#06b6d4;bottom:-100px;right:-100px;animation-delay:5s;}
        .bg-orb:nth-child(3){width:300px;height:300px;background:#8b5cf6;top:50%;left:50%;animation-delay:10s;}
        @keyframes orbFloat{
            0%{transform:translate(0,0) scale(1)}
            100%{transform:translate(40px,-40px) scale(1.2)}
        }
        .card{
            position:relative;z-index:1;
            width:90%;max-width:400px;
            background:rgba(255,255,255,0.03);
            backdrop-filter:blur(40px);
            -webkit-backdrop-filter:blur(40px);
            border-radius:32px;
            padding:40px 28px;
            border:1px solid rgba(255,255,255,0.1);
            box-shadow:0 30px 70px rgba(0,0,0,0.5),inset 0 0 30px rgba(255,255,255,0.02);
            animation:fadeUp 0.8s ease;
        }
        @keyframes fadeUp{
            from{opacity:0;transform:translateY(40px)}
            to{opacity:1;transform:translateY(0)}
        }
        .logo{
            width:70px;height:70px;margin:0 auto 20px;
            background:linear-gradient(135deg, rgba(99,102,241,0.3), rgba(6,182,212,0.3));
            border-radius:20px;display:flex;align-items:center;justify-content:center;
            font-size:36px;border:1px solid rgba(255,255,255,0.15);
            box-shadow:0 15px 40px rgba(99,102,241,0.2);
        }
        h1{
            text-align:center;font-size:38px;font-weight:900;
            background:linear-gradient(to bottom, #fff, #a5b4fc);
            -webkit-background-clip:text;-webkit-text-fill-color:transparent;
            margin-bottom:6px;
        }
        .sub{text-align:center;color:rgba(255,255,255,0.5);font-size:13px;margin-bottom:28px}
        input{
            width:100%;padding:16px 20px;margin:8px 0;
            border-radius:50px;
            background:rgba(255,255,255,0.04);
            border:1px solid rgba(255,255,255,0.1);
            color:#fff;font-size:14px;outline:none;
            transition:all 0.4s;
        }
        input:focus{
            border-color:rgba(99,102,241,0.6);
            box-shadow:0 0 20px rgba(99,102,241,0.1);
            background:rgba(255,255,255,0.07);
        }
        input::placeholder{color:rgba(255,255,255,0.3)}
        button{
            width:100%;padding:16px;margin-top:20px;
            background:linear-gradient(135deg, #6366f1, #06b6d4);
            border:none;border-radius:50px;
            color:#fff;font-weight:bold;font-size:15px;cursor:pointer;
            box-shadow:0 10px 30px rgba(99,102,241,0.3);
            transition:all 0.3s;
        }
        button:hover{transform:translateY(-2px);box-shadow:0 20px 40px rgba(99,102,241,0.4)}
        button:active{transform:scale(0.97)}
        .msg{text-align:center;color:#fca5a5;font-size:13px;margin-top:12px;min-height:20px}
        .link{text-align:center;margin-top:20px;color:rgba(255,255,255,0.6);font-size:14px}
        .link a{color:#a5b4fc;text-decoration:none;font-weight:600}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div><div class="bg-orb"></div>
    <div class="card">
        <div class="logo">💎</div>
        <h1>CRYSTΔL</h1>
        <p class="sub">TikTok 2026 Ultra</p>
        <input type="email" id="email" placeholder="📧 البريد الإلكتروني">
        <input type="password" id="pass" placeholder="🔒 كلمة المرور">
        <button onclick="doLogin()">🚀 دخول</button>
        <div class="msg" id="msg"></div>
        <div class="link">جديد هنا؟ <a href="signup.html">إنشاء حساب</a></div>
    </div>
    <script src="firebase-config.js"></script>
    <script>
        async function doLogin(){
            const e=document.getElementById('email').value,p=document.getElementById('pass').value,m=document.getElementById('msg');
            if(!e||!p){m.innerText='املأ جميع الحقول';return}
            m.innerText='';
            try{
                await auth.signInWithEmailAndPassword(e,p);
                location.replace('index.html');
            }catch(err){
                m.innerText='❌ بيانات غير صحيحة';
            }
        }
        document.querySelectorAll('input').forEach(i=>i.addEventListener('keydown',e=>{if(e.key==='Enter')doLogin()}));
    </script>
</body>
</html>'''

# ============================================
# signup.html
# ============================================
def build_signup():
    import json
    avatars = json.dumps(CARTOON_AVATARS, ensure_ascii=False)
    return f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>💎 CRYSTΔL | اشتراك</title>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        *{{margin:0;padding:0;box-sizing:border-box}}
        body{{
            min-height:100vh;
            background:radial-gradient(ellipse at top, #1a1a2e, #0f0f1a, #000);
            display:flex;align-items:center;justify-content:center;
            font-family:'Segoe UI',sans-serif;padding:20px;
        }}
        .bg-orb{{
            position:fixed;border-radius:50%;filter:blur(120px);opacity:0.4;
            animation:orbFloat 20s infinite alternate;
        }}
        .bg-orb:nth-child(1){{width:400px;height:400px;background:#6366f1;top:-100px;left:-100px;}}
        .bg-orb:nth-child(2){{width:350px;height:350px;background:#06b6d4;bottom:-100px;right:-100px;animation-delay:5s;}}
        @keyframes orbFloat{{
            0%{{transform:translate(0,0) scale(1)}}
            100%{{transform:translate(40px,-40px) scale(1.2)}}
        }}
        .card{{
            position:relative;z-index:1;width:90%;max-width:420px;
            background:rgba(255,255,255,0.03);
            backdrop-filter:blur(40px);-webkit-backdrop-filter:blur(40px);
            border-radius:32px;padding:32px 24px;
            border:1px solid rgba(255,255,255,0.1);
            box-shadow:0 30px 70px rgba(0,0,0,0.5);
            animation:fadeUp 0.8s ease;max-height:90vh;overflow-y:auto;
        }}
        @keyframes fadeUp{{from{{opacity:0;transform:translateY(40px)}}to{{opacity:1;transform:translateY(0)}}}}
        .logo{{
            width:60px;height:60px;margin:0 auto 20px;
            background:linear-gradient(135deg, rgba(99,102,241,0.3), rgba(6,182,212,0.3));
            border-radius:18px;display:flex;align-items:center;justify-content:center;
            font-size:30px;border:1px solid rgba(255,255,255,0.15);
        }}
        h1{{text-align:center;font-size:32px;font-weight:900;background:linear-gradient(to bottom, #fff, #a5b4fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent}}
        .sub{{text-align:center;color:rgba(255,255,255,0.5);font-size:12px;margin-bottom:20px}}
        .avatar-section{{text-align:center;margin-bottom:16px}}
        .avatar-preview{{
            width:70px;height:70px;margin:0 auto 8px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:38px;border:2px solid rgba(255,255,255,0.2);
            transition:all 0.4s;
        }}
        .avatar-grid{{
            display:grid;grid-template-columns:repeat(4,1fr);gap:6px;
            max-height:120px;overflow-y:auto;padding:8px;
            background:rgba(255,255,255,0.02);border-radius:16px;
            border:1px solid rgba(255,255,255,0.05);
        }}
        .avatar-grid::-webkit-scrollbar{{width:3px}}
        .avatar-grid::-webkit-scrollbar-thumb{{background:rgba(99,102,241,0.5);border-radius:10px}}
        .av{{
            width:100%;aspect-ratio:1;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:24px;cursor:pointer;border:2px solid transparent;
            transition:all 0.3s;
        }}
        .av:hover{{transform:scale(1.1);border-color:rgba(255,255,255,0.3)}}
        .av.sel{{border-color:#6366f1!important;box-shadow:0 0 20px rgba(99,102,241,0.5);transform:scale(1.1)}}
        .av.sel::after{{content:'✅';position:absolute;top:-4px;right:-4px;font-size:10px}}
        input{{
            width:100%;padding:14px 18px;margin:6px 0;
            border-radius:50px;background:rgba(255,255,255,0.04);
            border:1px solid rgba(255,255,255,0.1);color:#fff;
            font-size:14px;outline:none;transition:all 0.4s;
        }}
        input:focus{{border-color:rgba(99,102,241,0.6);background:rgba(255,255,255,0.07)}}
        input::placeholder{{color:rgba(255,255,255,0.3)}}
        button{{
            width:100%;padding:14px;margin-top:16px;
            background:linear-gradient(135deg, #6366f1, #06b6d4);
            border:none;border-radius:50px;color:#fff;
            font-weight:bold;font-size:15px;cursor:pointer;
            box-shadow:0 10px 30px rgba(99,102,241,0.3);
        }}
        button:hover{{transform:translateY(-2px)}}
        .msg{{text-align:center;color:#fca5a5;font-size:13px;margin-top:10px;min-height:20px}}
        .link{{text-align:center;margin-top:16px;color:rgba(255,255,255,0.6);font-size:13px}}
        .link a{{color:#a5b4fc;text-decoration:none;font-weight:600}}
    </style>
</head>
<body>
    <div class="bg-orb"></div><div class="bg-orb"></div>
    <div class="card">
        <div class="logo">💎</div>
        <h1>CRYSTΔL</h1>
        <p class="sub">اختر شخصيتك الكارتونية</p>
        <div class="avatar-section">
            <div class="avatar-preview" id="preview">🎭</div>
            <p style="color:rgba(255,255,255,0.5);font-size:11px;margin-bottom:8px" id="avname">اختر شخصية</p>
            <div class="avatar-grid" id="grid"></div>
        </div>
        <input type="text" id="uname" placeholder="👤 اسم المستخدم">
        <input type="email" id="email" placeholder="📧 البريد الإلكتروني">
        <input type="password" id="pass" placeholder="🔒 كلمة المرور (6+)">
        <button onclick="doReg()">🚀 إنشاء حساب</button>
        <div class="msg" id="msg"></div>
        <div class="link">لديك حساب؟ <a href="login.html">تسجيل دخول</a></div>
    </div>
    <script src="firebase-config.js"></script>
    <script>
        const AVATARS={avatars};let sel=null;
        function renderAvatars(){{
            const g=document.getElementById('grid');g.innerHTML='';
            AVATARS.forEach((a,i)=>{{
                const d=document.createElement('div');d.className='av';
                d.style.background=a.bg;d.innerHTML=a.emoji;d.title=a.name;
                d.onclick=()=>select(a,d);
                g.appendChild(d);
            }});
        }}
        function select(a,el){{
            document.querySelectorAll('.av').forEach(x=>x.classList.remove('sel'));
            el.classList.add('sel');sel=a;
            document.getElementById('preview').innerHTML=a.emoji;
            document.getElementById('preview').style.background=a.bg;
            document.getElementById('avname').innerText=a.name;
        }}
        renderAvatars();
        setTimeout(()=>{{const r=AVATARS[Math.floor(Math.random()*AVATARS.length)];document.querySelectorAll('.av').forEach((el,i)=>{{if(AVATARS[i].name===r.name)select(r,el)}});}},300);
        async function doReg(){{
            const u=document.getElementById('uname').value,e=document.getElementById('email').value,p=document.getElementById('pass').value,m=document.getElementById('msg');
            if(!u||!e||!p){{m.innerText='املأ جميع الحقول';return}}
            if(p.length<6){{m.innerText='كلمة المرور 6 أحرف على الأقل';return}}
            if(!sel){{m.innerText='اختر شخصية كارتونية';return}}
            m.innerText='';
            try{{
                const uc=await auth.createUserWithEmailAndPassword(e,p);
                await db.ref('users/'+uc.user.uid).set({{
                    username:u,email:e,bio:'',avatarUrl:'',
                    cartoonAvatar:{{emoji:sel.emoji,name:sel.name,bg:sel.bg}},
                    followers:{{}},following:{{}},totalLikes:0,
                    isVerified:false,createdAt:Date.now()
                }});
                location.replace('index.html');
            }}catch(err){{
                if(err.code==='auth/email-already-in-use')m.innerText='❌ البريد مستخدم';
                else m.innerText='❌ حدث خطأ';
            }}
        }}
        document.querySelectorAll('input').forEach(i=>i.addEventListener('keydown',e=>{{if(e.key==='Enter')doReg()}}));
    </script>
</body>
</html>'''

# ============================================
# index.html (CRYSTAL TIKTOK 2026)
# ============================================
def build_index():
    return '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>💎 CRYSTΔL | TikTok 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-storage-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        :root{
            --glass: rgba(255,255,255,0.03);
            --glass-border: rgba(255,255,255,0.08);
            --glass-hover: rgba(255,255,255,0.06);
            --accent: #6366f1;
            --accent2: #06b6d4;
            --bg: #050510;
        }
        *{margin:0;padding:0;box-sizing:border-box}
        body{
            font-family:'Segoe UI',sans-serif;
            background:var(--bg);
            color:#fff;
            height:100vh;width:100vw;
            overflow:hidden;
            -webkit-tap-highlight-color:transparent;
            user-select:none;
        }
        
        /* ===== MAIN APP ===== */
        #mainApp{display:none;height:100vh;width:100vw;position:relative}
        
        /* ===== TOP BAR ===== */
        .topbar{
            position:fixed;top:0;left:0;right:0;z-index:100;
            display:flex;justify-content:space-between;align-items:center;
            padding:14px 20px;
            background:rgba(5,5,16,0.7);
            backdrop-filter:blur(30px);
            -webkit-backdrop-filter:blur(30px);
            border-bottom:1px solid var(--glass-border);
        }
        .logo-symbol{
            width:36px;height:36px;
            background:linear-gradient(135deg, var(--accent), var(--accent2));
            border-radius:10px;display:flex;align-items:center;justify-content:center;
            font-weight:900;font-size:14px;color:#fff;
            box-shadow:0 8px 20px rgba(99,102,241,0.4);
        }
        .tabs{display:flex;gap:4px;background:var(--glass);border-radius:30px;padding:3px}
        .tab{
            background:none;border:none;color:rgba(255,255,255,0.6);
            padding:7px 16px;cursor:pointer;border-radius:25px;
            font-size:13px;font-weight:500;transition:all 0.3s;
        }
        .tab.active{background:rgba(99,102,241,0.2);color:#fff}
        .top-icons{display:flex;gap:18px}
        .top-icon{background:none;border:none;color:rgba(255,255,255,0.7);font-size:18px;cursor:pointer}
        
        /* ===== VIDEOS ===== */
        .videos-container{
            height:100vh;overflow-y:scroll;
            scroll-snap-type:y mandatory;
            scrollbar-width:none;
            -ms-overflow-style:none;
        }
        .videos-container::-webkit-scrollbar{display:none}
        .video-item{
            height:100vh;scroll-snap-align:start;
            position:relative;background:#000;
        }
        .video-item video{width:100%;height:100%;object-fit:cover}
        
        /* ===== VIDEO INFO ===== */
        .video-info{
            position:absolute;bottom:90px;left:16px;right:80px;z-index:20;
            text-shadow:0 2px 10px rgba(0,0,0,0.8);
        }
        .author-row{display:flex;align-items:center;gap:10px;margin-bottom:8px}
        .author-avatar{
            width:48px;height:48px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:24px;cursor:pointer;
            border:2px solid rgba(255,255,255,0.4);
            box-shadow:0 8px 20px rgba(0,0,0,0.4);
            overflow:hidden;
        }
        .author-avatar img{width:100%;height:100%;object-fit:cover}
        .author-name{
            font-weight:700;font-size:15px;cursor:pointer;
            display:flex;align-items:center;gap:6px;flex-wrap:wrap;
        }
        .badge-verified{color:#a5b4fc;font-size:12px}
        .btn-follow{
            background:linear-gradient(135deg, var(--accent), var(--accent2));
            padding:5px 14px;border-radius:20px;font-size:11px;font-weight:700;
            border:none;color:#fff;cursor:pointer;
            box-shadow:0 4px 15px rgba(99,102,241,0.3);
        }
        .caption{font-size:14px;margin-bottom:6px;line-height:1.5}
        .hashtag{color:var(--accent2);cursor:pointer;font-weight:500}
        .music-info{font-size:12px;opacity:0.8;display:flex;align-items:center;gap:6px;cursor:pointer}
        
        /* ===== SIDE ACTIONS ===== */
        .side-actions{
            position:absolute;right:14px;bottom:130px;
            display:flex;flex-direction:column;gap:22px;z-index:20;
        }
        .side-btn{
            display:flex;flex-direction:column;align-items:center;gap:3px;
            background:none;border:none;color:#fff;cursor:pointer;
            font-size:10px;transition:transform 0.15s;
        }
        .side-btn:active{transform:scale(0.85)}
        .side-btn i{font-size:30px;filter:drop-shadow(0 3px 8px rgba(0,0,0,0.5))}
        .side-btn.liked i{color:var(--accent)}
        .side-btn .count{font-weight:700;font-size:11px}
        
        /* ===== BOTTOM NAV ===== */
        .bottom-nav{
            position:fixed;bottom:0;left:0;right:0;
            display:flex;justify-content:space-around;align-items:center;
            padding:8px 0 20px;
            background:rgba(5,5,16,0.8);
            backdrop-filter:blur(30px);
            -webkit-backdrop-filter:blur(30px);
            z-index:100;
            border-top:1px solid var(--glass-border);
        }
        .nav-item{
            display:flex;flex-direction:column;align-items:center;gap:3px;
            background:none;border:none;color:rgba(255,255,255,0.5);
            font-size:10px;cursor:pointer;transition:all 0.3s;
        }
        .nav-item i{font-size:22px}
        .nav-item.active{color:#a5b4fc}
        .btn-create{
            width:48px;height:48px;
            background:linear-gradient(135deg, var(--accent), var(--accent2));
            border-radius:50%;display:flex;align-items:center;justify-content:center;
            margin-top:-24px;cursor:pointer;
            box-shadow:0 10px 30px rgba(99,102,241,0.5);
            border:none;color:#fff;font-size:20px;
            transition:transform 0.3s;
        }
        .btn-create:hover{transform:scale(1.08)}
        
        /* ===== PANELS ===== */
        .panel{
            position:fixed;top:0;left:0;right:0;bottom:0;
            background:rgba(5,5,16,0.95);
            backdrop-filter:blur(40px);
            -webkit-backdrop-filter:blur(40px);
            z-index:300;
            transform:translateX(100%);
            transition:transform 0.35s cubic-bezier(0.2,0.9,0.4,1.1);
            overflow-y:auto;
        }
        .panel.open{transform:translateX(0)}
        .panel-header{
            display:flex;justify-content:space-between;align-items:center;
            padding:18px 20px;
            border-bottom:1px solid var(--glass-border);
            position:sticky;top:0;
            background:rgba(5,5,16,0.8);
            backdrop-filter:blur(20px);
            z-index:10;
        }
        .panel-header h3{font-size:18px;font-weight:700}
        .btn-close{
            background:rgba(255,255,255,0.08);border:none;
            color:#fff;width:38px;height:38px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            cursor:pointer;font-size:18px;transition:all 0.3s;
        }
        .btn-close:hover{background:rgba(255,255,255,0.15)}
        
        /* ===== PROFILE ===== */
        .profile-cover{
            height:200px;position:relative;
            background:linear-gradient(135deg, #1e1b4b, #0e7490, #6366f1);
            display:flex;align-items:flex-end;justify-content:center;
            padding-bottom:30px;
        }
        .btn-back{
            position:absolute;top:16px;right:16px;
            background:rgba(0,0,0,0.5);backdrop-filter:blur(10px);
            width:42px;height:42px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            cursor:pointer;z-index:20;border:1px solid rgba(255,255,255,0.15);
            color:#fff;font-size:18px;
        }
        .profile-avatar-lg{
            width:100px;height:100px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:50px;border:4px solid rgba(255,255,255,0.3);
            box-shadow:0 12px 40px rgba(0,0,0,0.4);
            overflow:hidden;cursor:pointer;
        }
        .profile-avatar-lg img{width:100%;height:100%;object-fit:cover}
        .profile-stats{
            display:flex;justify-content:center;gap:30px;
            margin:20px 0;
        }
        .stat-num{font-size:20px;font-weight:700;color:#a5b4fc}
        .stat-label{font-size:11px;opacity:0.5;margin-top:4px}
        .videos-grid{
            display:grid;grid-template-columns:repeat(3,1fr);gap:3px;
            margin-top:20px;padding:0 12px;
        }
        .video-thumb{
            aspect-ratio:9/16;background:rgba(255,255,255,0.03);
            border-radius:6px;display:flex;align-items:center;justify-content:center;
            cursor:pointer;position:relative;overflow:hidden;
            transition:transform 0.2s;
        }
        .video-thumb:hover{transform:scale(1.03)}
        .video-thumb i{
            font-size:28px;color:rgba(255,255,255,0.7);
            z-index:1;filter:drop-shadow(0 2px 6px rgba(0,0,0,0.5));
        }
        .video-thumb img.thumb-bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:0.6}
        
        /* ===== MISC ===== */
        .toast{
            position:fixed;bottom:100px;left:50%;transform:translateX(-50%);
            background:rgba(5,5,16,0.9);padding:10px 22px;border-radius:50px;
            z-index:1000;opacity:0;transition:opacity 0.3s;pointer-events:none;
            border:1px solid var(--glass-border);font-size:13px;
        }
        .toast.show{opacity:1}
        .heart-anim{
            position:fixed;font-size:80px;color:var(--accent);
            pointer-events:none;z-index:1000;
            animation:floatUp 0.8s ease-out forwards;
        }
        @keyframes floatUp{
            0%{transform:scale(0.5) translateY(0);opacity:1}
            100%{transform:scale(1.5) translateY(-120px);opacity:0}
        }
        .spinner{
            width:36px;height:36px;border:3px solid rgba(99,102,241,0.2);
            border-top-color:var(--accent);border-radius:50%;
            animation:spin 0.7s linear infinite;
        }
        @keyframes spin{to{transform:rotate(360deg)}}
        .loading-center{
            display:flex;align-items:center;justify-content:center;
            height:100vh;gap:12px;flex-direction:column;color:rgba(255,255,255,0.6);
        }
        
        /* ===== INPUTS ===== */
        .input-glass{
            width:100%;padding:14px 18px;border-radius:50px;
            background:var(--glass);border:1px solid var(--glass-border);
            color:#fff;font-size:14px;outline:none;transition:all 0.4s;
        }
        .input-glass:focus{border-color:rgba(99,102,241,0.5);background:var(--glass-hover)}
        .input-glass::placeholder{color:rgba(255,255,255,0.3)}
        .btn-glass{
            background:linear-gradient(135deg, var(--accent), var(--accent2));
            border:none;border-radius:50px;color:#fff;font-weight:700;
            padding:12px 24px;cursor:pointer;font-size:14px;
            box-shadow:0 8px 25px rgba(99,102,241,0.3);
            transition:all 0.3s;
        }
        .btn-glass:hover{transform:translateY(-1px);box-shadow:0 12px 30px rgba(99,102,241,0.4)}
        
        /* ===== SEARCH ===== */
        .search-result{
            display:flex;align-items:center;gap:12px;padding:14px;
            border-bottom:1px solid var(--glass-border);cursor:pointer;
            transition:background 0.2s;
        }
        .search-result:hover{background:var(--glass-hover)}
        .search-avatar{
            width:44px;height:44px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:22px;overflow:hidden;
        }
        .search-avatar img{width:100%;height:100%;object-fit:cover}
        
        /* ===== COMMENTS ===== */
        .comment-row{
            display:flex;gap:12px;padding:12px 0;
            border-bottom:1px solid var(--glass-border);
        }
        .comment-avatar{
            width:38px;height:38px;border-radius:50%;
            display:flex;align-items:center;justify-content:center;
            font-size:18px;overflow:hidden;flex-shrink:0;
        }
        .comment-avatar img{width:100%;height:100%;object-fit:cover}
        
        /* ===== ADMIN ===== */
        .admin-section{
            margin-top:20px;padding:16px;
            background:rgba(99,102,241,0.05);
            border-radius:20px;border:1px solid rgba(99,102,241,0.15);
        }
        .admin-stats{display:grid;grid-template-columns:repeat(5,1fr);gap:8px;margin-bottom:20px}
        .admin-stat-card{
            background:rgba(0,0,0,0.3);border-radius:12px;
            padding:10px;text-align:center;
        }
        .admin-stat-num{font-size:22px;font-weight:700;color:#a5b4fc}
        .admin-stat-label{font-size:10px;opacity:0.5;margin-top:4px}
        .admin-list{max-height:280px;overflow-y:auto}
        .admin-item{
            display:flex;justify-content:space-between;align-items:center;
            background:rgba(0,0,0,0.3);padding:10px;border-radius:12px;margin-bottom:8px;
        }
        .admin-btn-danger{
            background:rgba(239,68,68,0.2);border:none;color:#f87171;
            padding:5px 12px;border-radius:20px;font-size:11px;cursor:pointer;
        }
        .admin-btn-warn{
            background:rgba(251,191,36,0.2);border:none;color:#fbbf24;
            padding:5px 12px;border-radius:20px;font-size:11px;cursor:pointer;
        }
        .banned-tag{
            background:#ef4444;padding:2px 6px;border-radius:10px;
            font-size:9px;margin-left:5px;
        }
        
        /* ===== CHAT ===== */
        .msg-bubble{
            max-width:80%;padding:10px 16px;border-radius:20px;
            word-break:break-word;font-size:14px;
        }
        .msg-bubble.sent{background:linear-gradient(135deg, var(--accent), var(--accent2));color:#fff;align-self:flex-end}
        .msg-bubble.received{background:rgba(255,255,255,0.06);color:#fff;align-self:flex-start}
    </style>
</head>
<body>

<!-- ===== MAIN APP ===== -->
<div id="mainApp">
    <!-- TOP BAR -->
    <div class="topbar">
        <div style="display:flex;align-items:center;gap:10px">
            <div class="logo-symbol">💎</div>
            <span style="font-weight:800;font-size:18px;background:linear-gradient(to bottom,#fff,#a5b4fc);-webkit-background-clip:text;-webkit-text-fill-color:transparent">CRYSTΔL</span>
        </div>
        <div class="tabs">
            <button class="tab" onclick="switchFeed('following')">متابَعين</button>
            <button class="tab active" onclick="switchFeed('forYou')">لك</button>
        </div>
        <div class="top-icons">
            <i class="fas fa-search top-icon" onclick="openSearch()"></i>
            <i class="fas fa-bell top-icon" onclick="openNotifications()"></i>
        </div>
    </div>
    
    <!-- VIDEOS CONTAINER -->
    <div class="videos-container" id="videosContainer">
        <div class="loading-center"><div class="spinner"></div><span>💎 جاري التحميل...</span></div>
    </div>
    
    <!-- BOTTOM NAV -->
    <div class="bottom-nav">
        <button class="nav-item active" onclick="switchTab('home')"><i class="fas fa-home"></i><span>الرئيسية</span></button>
        <button class="nav-item" onclick="switchTab('search')"><i class="fas fa-search"></i><span>بحث</span></button>
        <button class="btn-create" onclick="openUpload()"><i class="fas fa-plus"></i></button>
        <button class="nav-item" onclick="openConversations()"><i class="fas fa-envelope"></i><span>رسائل</span></button>
        <button class="nav-item" onclick="openMyProfile()"><i class="fas fa-user"></i><span>ملفي</span></button>
    </div>
    
    <!-- TOAST -->
    <div id="toast" class="toast">✅ تم النسخ</div>

    <!-- ===== SHARE PANEL ===== -->
    <div id="sharePanel" class="panel">
        <div class="panel-header"><h3>📤 مشاركة</h3><button class="btn-close" onclick="closeShare()"><i class="fas fa-times"></i></button></div>
        <div style="padding:16px">
            <div class="search-result" onclick="copyLink()"><i class="fas fa-link" style="color:#6366f1;font-size:20px"></i><span>نسخ الرابط</span></div>
            <div class="search-result" onclick="shareWA()"><i class="fab fa-whatsapp" style="color:#25D366;font-size:20px"></i><span>WhatsApp</span></div>
            <div class="search-result" onclick="shareTG()"><i class="fab fa-telegram" style="color:#0088cc;font-size:20px"></i><span>Telegram</span></div>
            <div class="search-result" onclick="downloadVid()"><i class="fas fa-download" style="color:#06b6d4;font-size:20px"></i><span>تنزيل</span></div>
        </div>
    </div>

    <!-- ===== COMMENTS PANEL ===== -->
    <div id="commentsPanel" class="panel">
        <div class="panel-header"><h3>💬 التعليقات</h3><button class="btn-close" onclick="closeComments()"><i class="fas fa-times"></i></button></div>
        <div id="commentsList" style="padding:16px"></div>
        <div style="display:flex;gap:10px;padding:16px;background:rgba(5,5,16,0.9);position:sticky;bottom:0">
            <input type="text" id="commentInput" class="input-glass" style="flex:1" placeholder="أضف تعليقاً...">
            <button class="btn-glass" onclick="addComment()">نشر</button>
        </div>
    </div>

    <!-- ===== SEARCH PANEL ===== -->
    <div id="searchPanel" class="panel">
        <div class="panel-header"><h3>🔍 بحث</h3><button class="btn-close" onclick="closeSearch()"><i class="fas fa-times"></i></button></div>
        <div style="padding:16px"><input type="text" id="searchInput" class="input-glass" placeholder="ابحث عن مستخدمين، فيديوهات، هاشتاقات..." onkeyup="doSearch()"></div>
        <div id="searchResults" style="padding:16px"></div>
    </div>

    <!-- ===== NOTIFICATIONS PANEL ===== -->
    <div id="notificationsPanel" class="panel">
        <div class="panel-header"><h3>🔔 الإشعارات</h3><button class="btn-close" onclick="closeNotifications()"><i class="fas fa-times"></i></button></div>
        <div id="notificationsList" style="padding:16px"></div>
    </div>

    <!-- ===== UPLOAD PANEL ===== -->
    <div id="uploadPanel" class="panel">
        <div class="panel-header"><h3>📤 رفع فيديو</h3><button class="btn-close" onclick="closeUpload()"><i class="fas fa-times"></i></button></div>
        <div style="max-width:500px;margin:0 auto;padding:20px">
            <div id="dropZone" onclick="document.getElementById('videoFile').click()" style="border:2px dashed rgba(99,102,241,0.3);border-radius:20px;padding:50px 20px;text-align:center;cursor:pointer;background:var(--glass);transition:all 0.3s">
                <i class="fas fa-cloud-upload-alt" style="font-size:48px;color:#6366f1;margin-bottom:12px"></i>
                <p>اضغط لاختيار فيديو</p>
                <span style="font-size:11px;opacity:0.5">MP4 - حتى 100MB</span>
                <video id="videoPreview" style="display:none;width:100%;max-height:250px;object-fit:contain;margin-top:12px;border-radius:12px" controls></video>
            </div>
            <input type="file" id="videoFile" accept="video/*" style="display:none" onchange="onFilePicked(this)">
            <div style="background:var(--glass);border-radius:20px;padding:20px;margin-top:16px;border:1px solid var(--glass-border)">
                <label style="font-size:13px;opacity:0.7;margin-bottom:6px;display:block">وصف الفيديو</label>
                <textarea id="vidDesc" class="input-glass" style="border-radius:16px;min-height:70px;resize:none" placeholder="اكتب وصفاً... #هاشتاق"></textarea>
                <label style="font-size:13px;opacity:0.7;margin-bottom:6px;display:block;margin-top:12px">الموسيقى</label>
                <input type="text" id="vidMusic" class="input-glass" placeholder="Original Sound">
                <div id="progressBar" style="display:none;margin:16px 0">
                    <div style="background:rgba(255,255,255,0.1);border-radius:30px;height:6px">
                        <div id="progressFill" style="background:linear-gradient(90deg,#6366f1,#06b6d4);width:0%;height:100%;border-radius:30px;transition:width 0.3s"></div>
                    </div>
                    <p id="progressText" style="text-align:center;font-size:12px;margin-top:6px;color:#a5b4fc">0%</p>
                </div>
                <button class="btn-glass" id="uploadBtn" onclick="uploadVideo()" style="width:100%;padding:14px">🚀 رفع الفيديو</button>
                <p id="uploadStatus" style="text-align:center;margin-top:10px;font-size:13px"></p>
            </div>
        </div>
    </div>

    <!-- ===== PROFILE PANEL ===== -->
    <div id="profilePanel" class="panel">
        <div class="btn-back" onclick="closeProfile()"><i class="fas fa-arrow-right"></i></div>
        <div class="profile-cover" id="profileCover">
            <div class="profile-avatar-lg" id="profileAvatarDisplay" onclick="changeAvatar()" style="background:linear-gradient(135deg,#6366f1,#06b6d4)">👤</div>
        </div>
        <div style="text-align:center;padding:0 20px">
            <h2 id="profileNameDisplay" style="font-size:22px;font-weight:700;margin-top:8px"></h2>
            <p id="profileBioDisplay" style="font-size:13px;opacity:0.5;margin-top:4px"></p>
            <div class="profile-stats">
                <div style="text-align:center"><div class="stat-num" id="profileFollowing">0</div><div class="stat-label">يتابع</div></div>
                <div style="text-align:center"><div class="stat-num" id="profileFollowers">0</div><div class="stat-label">متابع</div></div>
                <div style="text-align:center"><div class="stat-num" id="profileLikes">0</div><div class="stat-label">إعجابات</div></div>
            </div>
            <div id="profileActions" style="margin:12px 0"></div>
        </div>
        <div style="padding:16px">
            <h4 style="font-weight:700;margin-bottom:12px">🎬 فيديوهاتي</h4>
            <div id="profileVideosList" class="videos-grid"></div>
        </div>
    </div>

    <!-- ===== EDIT PROFILE PANEL ===== -->
    <div id="editProfilePanel" class="panel">
        <div class="panel-header"><h3>✏️ تعديل الملف</h3><button class="btn-close" onclick="closeEditProfile()"><i class="fas fa-times"></i></button></div>
        <div style="text-align:center;padding:20px" onclick="changeAvatar()">
            <div class="profile-avatar-lg" id="editAvatarDisplay" style="background:linear-gradient(135deg,#6366f1,#06b6d4);margin:0 auto">👤</div>
            <p style="font-size:11px;opacity:0.5;margin-top:8px">اضغط لتغيير الصورة</p>
        </div>
        <input type="file" id="avatarInput" accept="image/*" style="display:none" onchange="uploadAvatar(this)">
        <div style="padding:20px">
            <input type="text" id="editUsername" class="input-glass" placeholder="اسم المستخدم" style="margin-bottom:12px">
            <textarea id="editBio" class="input-glass" style="border-radius:16px;min-height:80px;resize:none;margin-bottom:12px" placeholder="السيرة الذاتية"></textarea>
            <button class="btn-glass" onclick="saveProfile()" style="width:100%;padding:14px">💾 حفظ</button>
        </div>
    </div>

    <!-- ===== CHAT PANEL ===== -->
    <div id="chatPanel" class="panel">
        <div class="panel-header">
            <div style="display:flex;align-items:center;gap:12px">
                <div id="chatAvatar" style="width:40px;height:40px;border-radius:50%;background:linear-gradient(135deg,#6366f1,#06b6d4);display:flex;align-items:center;justify-content:center;font-size:20px">👤</div>
                <h3 id="chatName">محادثة</h3>
            </div>
            <button class="btn-close" onclick="closeChat()"><i class="fas fa-times"></i></button>
        </div>
        <div id="messagesList" style="flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:8px"></div>
        <div style="display:flex;gap:10px;padding:16px;background:rgba(5,5,16,0.9);border-top:1px solid var(--glass-border)">
            <div onclick="document.getElementById('chatImageInput').click()" style="width:42px;height:42px;background:var(--glass);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer;border:1px solid var(--glass-border)"><i class="fas fa-image"></i></div>
            <input type="file" id="chatImageInput" accept="image/*" style="display:none" onchange="sendChatImage(this)">
            <input type="text" id="chatMsgInput" class="input-glass" style="flex:1" placeholder="اكتب رسالة...">
            <button onclick="sendChatMsg()" style="width:42px;height:42px;background:linear-gradient(135deg,#6366f1,#06b6d4);border:none;border-radius:50%;color:#fff;cursor:pointer"><i class="fas fa-paper-plane"></i></button>
        </div>
    </div>

    <!-- ===== CONVERSATIONS PANEL ===== -->
    <div id="conversationsPanel" class="panel">
        <div class="panel-header"><h3>💬 المحادثات</h3><button class="btn-close" onclick="closeConversations()"><i class="fas fa-times"></i></button></div>
        <div id="conversationsList" style="padding:16px"></div>
    </div>
</div>

<script src="firebase-config.js"></script>
<script src="script.js"></script>
</body>
</html>'''

# ============================================
# script.js
# ============================================
def build_script():
    return r'''// 💎 CRYSTΔL TIKTOK 2026 - Core Script
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
'''

# ============================================
# MAIN
# ============================================
def main():
    print("╔══════════════════════════════════════╗")
    print("║  💎 CRYSTΔL TIKTØK 2026 GENERATOR  ║")
    print("╚══════════════════════════════════════╝")
    print()
    
    write("firebase-config.js", build_firebase_config())
    write("login.html", build_login())
    write("signup.html", build_signup())
    write("index.html", build_index())
    write("script.js", build_script())
    
    print()
    print("══════════════════════════════════════")
    print("  ✅ جميع الملفات جاهزة!")
    print("  📂 login.html | signup.html | index.html")
    print("  📂 firebase-config.js | script.js")
    print("  🔥 Firebase: gomlf-c26ce")
    print("  ☁️  Cloudinary: dmla61v7n / so2_mk")
    print("  👑 Admin: jasim28v@gmail.com")
    print("══════════════════════════════════════")

if __name__ == "__main__":
    main()
