#!/usr/bin/env python3
"""
██████╗ ██╗   ██╗██╗  ██╗██╗   ██╗
██╔══██╗██║   ██║██║  ██║╚██╗ ██╔╝
██████╔╝██║   ██║███████║ ╚████╔╝ 
██╔══██╗██║   ██║╚════██║  ╚██╔╝  
██████╔╝╚██████╔╝     ██║   ██║   
╚═════╝  ╚═════╝      ╚═╝   ╚═╝   
BLU3Y | TikTok Glass Ultra Pro - المولد الكامل للموقع الزجاجي الأزرق
"""

import os
import json
import random

# =====================================================================
# إعدادات Firebase
# =====================================================================
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

# =====================================================================
# إعدادات Cloudinary
# =====================================================================
CLOUD_NAME = "dmla61v7n"
UPLOAD_PRESET = "so2_mk"
CLOUDINARY_COLLECTION_URL = "https://collection.cloudinary.com/dmla61v7n"

# =====================================================================
# إعدادات الأدمن
# =====================================================================
ADMIN_EMAILS = ['jasim28v@gmail.com']

# =====================================================================
# الشخصيات الكارتونية (20 شخصية)
# =====================================================================
CARTOON_AVATARS = [
    {"name": "الأسد الشجاع", "emoji": "🦁", "color": "#FF6B35", "bg": "linear-gradient(135deg, #FF6B35, #FFD700)"},
    {"name": "الأرنب الذكي", "emoji": "🐰", "color": "#00D2FF", "bg": "linear-gradient(135deg, #00D2FF, #3A7BD5)"},
    {"name": "الثعلب الماكر", "emoji": "🦊", "color": "#FF4500", "bg": "linear-gradient(135deg, #FF4500, #FF8C00)"},
    {"name": "الباندا اللطيف", "emoji": "🐼", "color": "#2C3E50", "bg": "linear-gradient(135deg, #2C3E50, #BDC3C7)"},
    {"name": "القط المدهش", "emoji": "🐱", "color": "#8E44AD", "bg": "linear-gradient(135deg, #8E44AD, #3498DB)"},
    {"name": "الدب القوي", "emoji": "🐻", "color": "#8B4513", "bg": "linear-gradient(135deg, #8B4513, #D2691E)"},
    {"name": "النمر السريع", "emoji": "🐯", "color": "#FFA500", "bg": "linear-gradient(135deg, #FFA500, #FF0000)"},
    {"name": "القرد المرح", "emoji": "🐵", "color": "#A0522D", "bg": "linear-gradient(135deg, #A0522D, #DEB887)"},
    {"name": "الكلب الوفي", "emoji": "🐶", "color": "#D4A574", "bg": "linear-gradient(135deg, #D4A574, #8B6914)"},
    {"name": "الحصان النبيل", "emoji": "🐴", "color": "#C0C0C0", "bg": "linear-gradient(135deg, #C0C0C0, #708090)"},
    {"name": "التنين الأسطوري", "emoji": "🐲", "color": "#00FF00", "bg": "linear-gradient(135deg, #006400, #00FF00)"},
    {"name": "وحيد القرن", "emoji": "🦄", "color": "#FF69B4", "bg": "linear-gradient(135deg, #FF69B4, #9B59B6)"},
    {"name": "النسر الجريء", "emoji": "🦅", "color": "#FFFFFF", "bg": "linear-gradient(135deg, #8B0000, #FF6347)"},
    {"name": "السلحفاة الحكيمة", "emoji": "🐢", "color": "#228B22", "bg": "linear-gradient(135deg, #228B22, #90EE90)"},
    {"name": "الدولفين المرح", "emoji": "🐬", "color": "#1E90FF", "bg": "linear-gradient(135deg, #000080, #1E90FF)"},
    {"name": "الفراشة الساحرة", "emoji": "🦋", "color": "#DA70D6", "bg": "linear-gradient(135deg, #DA70D6, #FF1493)"},
    {"name": "البومة الذكية", "emoji": "🦉", "color": "#8B4513", "bg": "linear-gradient(135deg, #8B4513, #F4A460)"},
    {"name": "التمساح القوي", "emoji": "🐊", "color": "#006400", "bg": "linear-gradient(135deg, #006400, #32CD32)"},
    {"name": "الحوت الأزرق", "emoji": "🐋", "color": "#4169E1", "bg": "linear-gradient(135deg, #000080, #4169E1)"},
    {"name": "الفيل العظيم", "emoji": "🐘", "color": "#808080", "bg": "linear-gradient(135deg, #808080, #A9A9A9)"}
]

# =====================================================================
# ألوان غلاف الملف الشخصي (Cover Colors)
# =====================================================================
COVER_COLORS = [
    "linear-gradient(135deg, #0a2463, #1e3a8a, #3b82f6)",
    "linear-gradient(135deg, #1e3a8a, #3b82f6, #60a5fa)",
    "linear-gradient(135deg, #0f172a, #1e3a8a, #2563eb)",
    "linear-gradient(135deg, #1e40af, #3b82f6, #93c5fd)",
    "linear-gradient(135deg, #172554, #2563eb, #60a5fa)",
]

# =====================================================================
# إنشاء ملف firebase-config.js
# =====================================================================
def create_firebase_config():
    content = f'''// ========== Firebase Configuration ==========
// Generated by BLU3Y Glass System

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

// Initialize Firebase
firebase.initializeApp(firebaseConfig);
const auth = firebase.auth();
const db = firebase.database();
const storage = firebase.storage();

// Cloudinary Configuration
const CLOUD_NAME = "{CLOUD_NAME}";
const UPLOAD_PRESET = "{UPLOAD_PRESET}";
const CLOUDINARY_COLLECTION_URL = "{CLOUDINARY_COLLECTION_URL}";

console.log('💙 BLU3Y Glass Firebase + Cloudinary Ready');
'''
    write_file("firebase-config.js", content)
    print("✅ firebase-config.js تم إنشاؤه بنجاح")

# =====================================================================
# إنشاء ملف login.html (تسجيل الدخول منفصل)
# =====================================================================
def create_login_html():
    content = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>BLU3Y | تسجيل الدخول</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            min-height: 100vh;
            background: linear-gradient(135deg, #0a2463, #1e3a8a, #3b82f6, #60a5fa);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 20px;
            overflow-x: hidden;
        }
        @keyframes gradientShift {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        
        /* جزيئات عائمة */
        .particles {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
        }
        .particle {
            position: absolute;
            background: rgba(255,255,255,0.15);
            border-radius: 50%;
            animation: floatUp 8s infinite;
        }
        @keyframes floatUp {
            0% { transform: translateY(100vh) scale(0); opacity: 0; }
            50% { opacity: 0.5; }
            100% { transform: translateY(-10vh) scale(1); opacity: 0; }
        }
        
        /* بطاقة زجاجية */
        .glass-card {
            position: relative;
            z-index: 1;
            width: 100%;
            max-width: 420px;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border-radius: 40px;
            padding: 40px 32px;
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 25px 60px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.1);
            animation: cardEntry 0.8s cubic-bezier(0.2, 0.9, 0.4, 1);
        }
        @keyframes cardEntry {
            from { opacity: 0; transform: translateY(50px) scale(0.9); }
            to { opacity: 1; transform: translateY(0) scale(1); }
        }
        .glass-card h1 {
            text-align: center;
            font-size: 42px;
            font-weight: 900;
            background: linear-gradient(to bottom, #fff, #93c5fd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
            letter-spacing: 2px;
        }
        .glass-card .subtitle {
            text-align: center;
            color: rgba(255,255,255,0.6);
            font-size: 13px;
            margin-bottom: 32px;
        }
        .glass-input {
            width: 100%;
            padding: 16px 20px;
            margin: 10px 0;
            border-radius: 50px;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.15);
            color: white;
            font-size: 15px;
            transition: all 0.4s;
            outline: none;
        }
        .glass-input:focus {
            background: rgba(255,255,255,0.12);
            border-color: rgba(59, 130, 246, 0.6);
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.2);
        }
        .glass-input::placeholder { color: rgba(255,255,255,0.4); }
        .glass-btn {
            width: 100%;
            padding: 16px;
            margin-top: 20px;
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            border: none;
            border-radius: 50px;
            color: white;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3);
            letter-spacing: 1px;
        }
        .glass-btn:hover {
            transform: translateY(-2px);
            box-shadow: 0 15px 40px rgba(59, 130, 246, 0.5);
        }
        .glass-btn:active { transform: scale(0.98); }
        .link-text {
            text-align: center;
            margin-top: 24px;
            color: rgba(255,255,255,0.7);
            font-size: 14px;
        }
        .link-text a {
            color: #93c5fd;
            text-decoration: none;
            font-weight: 600;
            transition: color 0.3s;
        }
        .link-text a:hover { color: #fff; }
        .error-msg {
            text-align: center;
            color: #fca5a5;
            font-size: 13px;
            margin-top: 12px;
            min-height: 20px;
        }
        .loading-dots {
            display: inline-flex;
            gap: 4px;
        }
        .loading-dots span {
            width: 8px;
            height: 8px;
            background: white;
            border-radius: 50%;
            animation: bounce 0.5s infinite alternate;
        }
        .loading-dots span:nth-child(2) { animation-delay: 0.15s; }
        .loading-dots span:nth-child(3) { animation-delay: 0.3s; }
        @keyframes bounce {
            to { transform: translateY(-8px); opacity: 0.5; }
        }
        .logo-icon {
            width: 70px;
            height: 70px;
            margin: 0 auto 20px;
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            border-radius: 22px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 36px;
            box-shadow: 0 15px 35px rgba(59, 130, 246, 0.4);
        }
    </style>
</head>
<body>
    <div class="particles" id="particles"></div>
    
    <div class="glass-card">
        <div class="logo-icon">💎</div>
        <h1>BLU3Y</h1>
        <p class="subtitle">TikTok Glass Ultra Pro</p>
        <input type="email" id="loginEmail" class="glass-input" placeholder="📧 البريد الإلكتروني">
        <input type="password" id="loginPassword" class="glass-input" placeholder="🔒 كلمة المرور">
        <button class="glass-btn" onclick="login()">
            <span id="loginBtnText">دخول</span>
            <span id="loginBtnLoader" style="display:none">
                <span class="loading-dots"><span></span><span></span><span></span></span>
            </span>
        </button>
        <div class="error-msg" id="loginMsg"></div>
        <div class="link-text">
            ليس لديك حساب؟ <a href="signup.html">إنشاء حساب جديد</a>
        </div>
    </div>

    <script src="firebase-config.js"></script>
    <script>
        // جزيئات عائمة
        function createParticles() {
            const container = document.getElementById('particles');
            for (let i = 0; i < 30; i++) {
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.width = (Math.random() * 8 + 2) + 'px';
                particle.style.height = particle.style.width;
                particle.style.animationDuration = (Math.random() * 6 + 6) + 's';
                particle.style.animationDelay = Math.random() * 8 + 's';
                container.appendChild(particle);
            }
        }
        createParticles();

        // تسجيل الدخول
        async function login() {
            const email = document.getElementById('loginEmail').value;
            const password = document.getElementById('loginPassword').value;
            const msg = document.getElementById('loginMsg');
            const btnText = document.getElementById('loginBtnText');
            const btnLoader = document.getElementById('loginBtnLoader');
            
            if (!email || !password) { msg.innerText = 'الرجاء ملء جميع الحقول'; return; }
            
            btnText.style.display = 'none';
            btnLoader.style.display = 'inline';
            msg.innerText = '';
            
            try {
                await auth.signInWithEmailAndPassword(email, password);
                window.location.href = 'index.html';
            } catch (error) {
                btnText.style.display = 'inline';
                btnLoader.style.display = 'none';
                if (error.code === 'auth/user-not-found') msg.innerText = '❌ لا يوجد حساب بهذا البريد';
                else if (error.code === 'auth/wrong-password') msg.innerText = '❌ كلمة المرور غير صحيحة';
                else if (error.code === 'auth/invalid-email') msg.innerText = '❌ بريد إلكتروني غير صالح';
                else msg.innerText = '❌ حدث خطأ، حاول مرة أخرى';
            }
        }

        document.querySelectorAll('.glass-input').forEach(input => {
            input.addEventListener('keydown', function(e) {
                if (e.key === 'Enter') login();
            });
        });
    </script>
</body>
</html>'''
    write_file("login.html", content)
    print("✅ login.html تم إنشاؤه بنجاح")

# =====================================================================
# إنشاء ملف signup.html (الاشتراك منفصل مع الشخصيات الكارتونية)
# =====================================================================
def create_signup_html():
    avatars_json = json.dumps(CARTOON_AVATARS, ensure_ascii=False)
    content = f'''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>BLU3Y | إنشاء حساب</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            min-height: 100vh;
            background: linear-gradient(135deg, #0a2463, #1e3a8a, #3b82f6, #60a5fa);
            background-size: 400% 400%;
            animation: gradientShift 15s ease infinite;
            display: flex;
            align-items: center;
            justify-content: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            padding: 20px;
            overflow-y: auto;
        }}
        @keyframes gradientShift {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        .particles {{
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 0;
        }}
        .particle {{
            position: absolute;
            background: rgba(255,255,255,0.12);
            border-radius: 50%;
            animation: floatUp 8s infinite;
        }}
        @keyframes floatUp {{
            0% {{ transform: translateY(100vh) scale(0); opacity: 0; }}
            50% {{ opacity: 0.4; }}
            100% {{ transform: translateY(-10vh) scale(1); opacity: 0; }}
        }}
        .glass-card {{
            position: relative;
            z-index: 1;
            width: 100%;
            max-width: 460px;
            background: rgba(255, 255, 255, 0.08);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            border-radius: 40px;
            padding: 32px 24px;
            border: 1px solid rgba(255,255,255,0.2);
            box-shadow: 0 25px 60px rgba(0,0,0,0.3), inset 0 1px 0 rgba(255,255,255,0.1);
            animation: cardEntry 0.8s cubic-bezier(0.2, 0.9, 0.4, 1);
        }}
        @keyframes cardEntry {{
            from {{ opacity: 0; transform: translateY(50px) scale(0.9); }}
            to {{ opacity: 1; transform: translateY(0) scale(1); }}
        }}
        .glass-card h1 {{
            text-align: center;
            font-size: 36px;
            font-weight: 900;
            background: linear-gradient(to bottom, #fff, #93c5fd);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 6px;
        }}
        .glass-card .subtitle {{
            text-align: center;
            color: rgba(255,255,255,0.6);
            font-size: 13px;
            margin-bottom: 20px;
        }}
        .glass-input {{
            width: 100%;
            padding: 14px 18px;
            margin: 8px 0;
            border-radius: 50px;
            background: rgba(255,255,255,0.06);
            border: 1px solid rgba(255,255,255,0.15);
            color: white;
            font-size: 14px;
            transition: all 0.4s;
            outline: none;
        }}
        .glass-input:focus {{
            background: rgba(255,255,255,0.12);
            border-color: rgba(59, 130, 246, 0.6);
            box-shadow: 0 0 25px rgba(59, 130, 246, 0.2);
        }}
        .glass-input::placeholder {{ color: rgba(255,255,255,0.4); }}
        .glass-btn {{
            width: 100%;
            padding: 16px;
            margin-top: 20px;
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            border: none;
            border-radius: 50px;
            color: white;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
            transition: all 0.3s;
            box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3);
        }}
        .glass-btn:hover {{
            transform: translateY(-2px);
            box-shadow: 0 15px 40px rgba(59, 130, 246, 0.5);
        }}
        .glass-btn:active {{ transform: scale(0.98); }}
        .link-text {{
            text-align: center;
            margin-top: 20px;
            color: rgba(255,255,255,0.7);
            font-size: 14px;
        }}
        .link-text a {{
            color: #93c5fd;
            text-decoration: none;
            font-weight: 600;
        }}
        .error-msg {{
            text-align: center;
            color: #fca5a5;
            font-size: 13px;
            margin-top: 10px;
            min-height: 20px;
        }}
        
        /* أفاتار كارتونية */
        .avatar-section {{
            text-align: center;
            margin-bottom: 16px;
        }}
        .avatar-label {{
            color: rgba(255,255,255,0.7);
            font-size: 13px;
            margin-bottom: 12px;
            display: block;
        }}
        .avatar-grid {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 8px;
            max-height: 160px;
            overflow-y: auto;
            padding: 8px;
            background: rgba(255,255,255,0.04);
            border-radius: 20px;
            border: 1px solid rgba(255,255,255,0.08);
        }}
        .avatar-grid::-webkit-scrollbar {{ width: 3px; }}
        .avatar-grid::-webkit-scrollbar-thumb {{ background: rgba(59,130,246,0.5); border-radius: 10px; }}
        .avatar-option {{
            width: 100%;
            aspect-ratio: 1;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 28px;
            cursor: pointer;
            transition: all 0.3s;
            border: 3px solid transparent;
            position: relative;
        }}
        .avatar-option:hover {{
            transform: scale(1.1);
            border-color: rgba(255,255,255,0.3);
        }}
        .avatar-option.selected {{
            border-color: #3b82f6 !important;
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);
            transform: scale(1.1);
        }}
        .avatar-option.selected::after {{
            content: '✅';
            position: absolute;
            top: -5px;
            right: -5px;
            font-size: 12px;
        }}
        .selected-avatar-preview {{
            width: 80px;
            height: 80px;
            margin: 0 auto 10px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 44px;
            border: 3px solid rgba(255,255,255,0.3);
            box-shadow: 0 10px 30px rgba(59, 130, 246, 0.3);
            transition: all 0.5s;
        }}
        .loading-dots {{
            display: inline-flex;
            gap: 4px;
        }}
        .loading-dots span {{
            width: 8px;
            height: 8px;
            background: white;
            border-radius: 50%;
            animation: bounce 0.5s infinite alternate;
        }}
        .loading-dots span:nth-child(2) {{ animation-delay: 0.15s; }}
        .loading-dots span:nth-child(3) {{ animation-delay: 0.3s; }}
        @keyframes bounce {{
            to {{ transform: translateY(-8px); opacity: 0.5; }}
        }}
        .logo-icon {{
            width: 60px;
            height: 60px;
            margin: 0 auto 16px;
            background: linear-gradient(135deg, #3b82f6, #1d4ed8);
            border-radius: 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 30px;
            box-shadow: 0 12px 28px rgba(59, 130, 246, 0.4);
        }}
    </style>
</head>
<body>
    <div class="particles" id="particles"></div>
    
    <div class="glass-card">
        <div class="logo-icon">💎</div>
        <h1>BLU3Y</h1>
        <p class="subtitle">اختر شخصيتك الكارتونية</p>
        
        <div class="avatar-section">
            <div class="selected-avatar-preview" id="selectedAvatarPreview">🎭</div>
            <span class="avatar-label" id="selectedAvatarName">اختر شخصية</span>
            <div class="avatar-grid" id="avatarGrid"></div>
        </div>
        
        <input type="text" id="regName" class="glass-input" placeholder="👤 اسم المستخدم">
        <input type="email" id="regEmail" class="glass-input" placeholder="📧 البريد الإلكتروني">
        <input type="password" id="regPass" class="glass-input" placeholder="🔒 كلمة المرور (6 أحرف)">
        
        <button class="glass-btn" onclick="register()">
            <span id="regBtnText">🚀 إنشاء حساب</span>
            <span id="regBtnLoader" style="display:none">
                <span class="loading-dots"><span></span><span></span><span></span></span>
            </span>
        </button>
        <div class="error-msg" id="regMsg"></div>
        <div class="link-text">
            لديك حساب بالفعل؟ <a href="login.html">تسجيل الدخول</a>
        </div>
    </div>

    <script src="firebase-config.js"></script>
    <script>
        const CARTOON_AVATARS = {avatars_json};
        let selectedAvatar = null;

        // جزيئات
        function createParticles() {{
            const container = document.getElementById('particles');
            for (let i = 0; i < 30; i++) {{
                const particle = document.createElement('div');
                particle.className = 'particle';
                particle.style.left = Math.random() * 100 + '%';
                particle.style.width = (Math.random() * 6 + 2) + 'px';
                particle.style.height = particle.style.width;
                particle.style.animationDuration = (Math.random() * 6 + 6) + 's';
                particle.style.animationDelay = Math.random() * 8 + 's';
                container.appendChild(particle);
            }}
        }}
        createParticles();

        // عرض الأفاتارات
        function renderAvatars() {{
            const grid = document.getElementById('avatarGrid');
            grid.innerHTML = '';
            CARTOON_AVATARS.forEach((avatar, index) => {{
                const div = document.createElement('div');
                div.className = 'avatar-option';
                div.style.background = avatar.bg;
                div.innerHTML = avatar.emoji;
                div.title = avatar.name;
                div.onclick = () => selectAvatar(avatar, div);
                grid.appendChild(div);
            }});
        }}

        function selectAvatar(avatar, element) {{
            document.querySelectorAll('.avatar-option').forEach(a => a.classList.remove('selected'));
            element.classList.add('selected');
            selectedAvatar = avatar;
            document.getElementById('selectedAvatarPreview').innerHTML = avatar.emoji;
            document.getElementById('selectedAvatarPreview').style.background = avatar.bg;
            document.getElementById('selectedAvatarName').innerText = avatar.name;
        }}

        renderAvatars();
        // اختيار عشوائي افتراضي
        const randomAvatar = CARTOON_AVATARS[Math.floor(Math.random() * CARTOON_AVATARS.length)];
        setTimeout(() => {{
            const firstOption = document.querySelector('.avatar-option');
            if (firstOption) selectAvatar(randomAvatar, firstOption);
            document.querySelectorAll('.avatar-option').forEach((el, i) => {{
                if (CARTOON_AVATARS[i].name === randomAvatar.name) selectAvatar(randomAvatar, el);
            }});
        }}, 300);

        // التسجيل
        async function register() {{
            const username = document.getElementById('regName').value;
            const email = document.getElementById('regEmail').value;
            const password = document.getElementById('regPass').value;
            const msg = document.getElementById('regMsg');
            const btnText = document.getElementById('regBtnText');
            const btnLoader = document.getElementById('regBtnLoader');

            if (!username || !email || !password) {{ msg.innerText = 'الرجاء ملء جميع الحقول'; return; }}
            if (password.length < 6) {{ msg.innerText = '❌ كلمة المرور 6 أحرف على الأقل'; return; }}
            if (!selectedAvatar) {{ msg.innerText = '❌ الرجاء اختيار شخصية كارتونية'; return; }}

            btnText.style.display = 'none';
            btnLoader.style.display = 'inline';
            msg.innerText = '';

            try {{
                const userCredential = await auth.createUserWithEmailAndPassword(email, password);
                await db.ref(`users/${{userCredential.user.uid}}`).set({{
                    username,
                    email,
                    bio: '',
                    avatarUrl: '',
                    coverColor: COVER_COLORS[Math.floor(Math.random() * COVER_COLORS.length)],
                    cartoonAvatar: {{
                        emoji: selectedAvatar.emoji,
                        name: selectedAvatar.name,
                        bg: selectedAvatar.bg
                    }},
                    followers: {{}},
                    following: {{}},
                    totalLikes: 0,
                    isVerified: false,
                    verifiedAt: null,
                    verifiedBy: null,
                    createdAt: Date.now()
                }});
                window.location.href = 'index.html';
            }} catch (error) {{
                btnText.style.display = 'inline';
                btnLoader.style.display = 'none';
                if (error.code === 'auth/email-already-in-use') msg.innerText = '❌ البريد الإلكتروني مستخدم بالفعل';
                else if (error.code === 'auth/weak-password') msg.innerText = '❌ كلمة المرور ضعيفة جداً';
                else msg.innerText = '❌ حدث خطأ، حاول مرة أخرى';
            }}
        }}

        const COVER_COLORS = {json.dumps(COVER_COLORS, ensure_ascii=False)};

        document.querySelectorAll('.glass-input').forEach(input => {{
            input.addEventListener('keydown', function(e) {{
                if (e.key === 'Enter') register();
            }});
        }});
    </script>
</body>
</html>'''
    write_file("signup.html", content)
    print("✅ signup.html تم إنشاؤه بنجاح (مع الشخصيات الكارتونية)")

# =====================================================================
# إنشاء ملف script.js (المنطق الكامل للموقع الزجاجي)
# =====================================================================
def create_script_js():
    content = '''// ========== BLU3Y Glass Script ==========
const ADMIN_EMAILS = ['jasim28v@gmail.com'];
let isAdmin = false;

// ========== المتغيرات العامة ==========
let currentUser = null;
let currentUserData = null;
let currentVideoId = null;
let currentShareUrl = null;
let allUsers = {};
let allVideos = [];
let allSounds = {};
let isMuted = true;
let viewingProfileUserId = null;
let currentFeed = 'forYou';

// ========== ألوان الغلاف ==========
const COVER_COLORS = [
    "linear-gradient(135deg, #0a2463, #1e3a8a, #3b82f6)",
    "linear-gradient(135deg, #1e3a8a, #3b82f6, #60a5fa)",
    "linear-gradient(135deg, #0f172a, #1e3a8a, #2563eb)",
    "linear-gradient(135deg, #1e40af, #3b82f6, #93c5fd)",
    "linear-gradient(135deg, #172554, #2563eb, #60a5fa)",
];

// ========== المصادقة ==========
function logout() { auth.signOut(); window.location.href = 'login.html'; }

// ========== التحقق من الأدمن ==========
function checkAdminStatus() {
    if (currentUser && ADMIN_EMAILS.includes(currentUser.email)) {
        isAdmin = true;
        return true;
    }
    isAdmin = false;
    return false;
}

// ========== توثيق الحسابات ==========
async function toggleVerifyUser(userId) {
    if (!isAdmin) return;
    const userRef = db.ref(`users/${userId}`);
    const snap = await userRef.once('value');
    const userData = snap.val();
    if (!userData) return;
    const newVerifiedStatus = !userData.isVerified;
    if (confirm(newVerifiedStatus ? 'توثيق هذا المستخدم؟' : 'إلغاء توثيق هذا المستخدم؟')) {
        await userRef.update({
            isVerified: newVerifiedStatus,
            verifiedAt: newVerifiedStatus ? Date.now() : null,
            verifiedBy: newVerifiedStatus ? currentUser.uid : null
        });
        alert(newVerifiedStatus ? '✅ تم توثيق الحساب' : '❌ تم إلغاء التوثيق');
        if (viewingProfileUserId === userId) await loadProfileData(userId);
        location.reload();
    }
}

// ========== لوحة الأدمن ==========
async function renderAdminPanel() {
    if (!isAdmin) return '';
    const usersSnap = await db.ref('users').once('value');
    const users = usersSnap.val() || {};
    const videosSnap = await db.ref('videos').once('value');
    const videos = videosSnap.val() || {};
    const totalLikes = Object.values(videos).reduce((sum, v) => sum + (v.likes || 0), 0);
    const bannedUsers = Object.values(users).filter(u => u.banned).length;
    const verifiedUsers = Object.values(users).filter(u => u.isVerified).length;
    
    return `
        <div class="admin-panel-section">
            <h3 class="admin-title"><i class="fas fa-shield-alt"></i> لوحة تحكم الأدمن</h3>
            <div class="admin-stats">
                <div class="admin-stat-card"><div class="admin-stat-number">${Object.keys(users).length}</div><div class="admin-stat-label">مستخدمين</div></div>
                <div class="admin-stat-card"><div class="admin-stat-number">${Object.keys(videos).length}</div><div class="admin-stat-label">فيديوهات</div></div>
                <div class="admin-stat-card"><div class="admin-stat-number">${totalLikes}</div><div class="admin-stat-label">إعجابات</div></div>
                <div class="admin-stat-card"><div class="admin-stat-number">${bannedUsers}</div><div class="admin-stat-label">محظورين</div></div>
                <div class="admin-stat-card"><div class="admin-stat-number">${verifiedUsers}</div><div class="admin-stat-label">موثقين</div></div>
            </div>
            
            <div style="margin-bottom:20px">
                <h4 style="font-weight:bold;margin-bottom:12px;color:#60a5fa"><i class="fas fa-check-circle"></i> توثيق الحسابات</h4>
                <div class="admin-list">
                    ${Object.entries(users).slice(0, 20).filter(([uid, u]) => !u.banned).map(([uid, u]) => `
                        <div class="admin-item">
                            <div class="admin-item-info">
                                <div class="admin-item-avatar" style="background:${u.cartoonAvatar?.bg || 'linear-gradient(135deg, #3b82f6, #1d4ed8)'}">
                                    ${u.cartoonAvatar?.emoji || u.avatarUrl ? `<img src="${u.avatarUrl}" style="width:100%;height:100%;object-fit:cover;border-radius:50%;">` : (u.username?.charAt(0) || '👤')}
                                </div>
                                <div class="admin-item-text">
                                    <div class="admin-item-name">
                                        @${u.username}
                                        ${u.isVerified ? '<span style="color:#60a5fa;">✅</span>' : ''}
                                    </div>
                                    <div class="admin-item-email">${u.email || ''}</div>
                                </div>
                            </div>
                            <button class="admin-verify-btn" onclick="toggleVerifyUser('${uid}')">
                                ${u.isVerified ? 'إلغاء التوثيق' : 'توثيق'}
                            </button>
                        </div>
                    `).join('')}
                </div>
            </div>
            
            <div style="margin-bottom:20px">
                <h4 style="font-weight:bold;margin-bottom:12px">🗑️ حذف فيديوهات</h4>
                <div class="admin-list">
                    ${Object.entries(videos).reverse().slice(0, 15).map(([id, v]) => `
                        <div class="admin-item">
                            <div class="admin-item-info">
                                <div class="admin-item-avatar"><i class="fas fa-video"></i></div>
                                <div class="admin-item-text">
                                    <div class="admin-item-name">${v.description?.substring(0, 35) || 'فيديو'}</div>
                                    <div class="admin-item-email">@${v.senderName || 'user'}</div>
                                </div>
                            </div>
                            <button class="admin-delete-btn" onclick="adminDeleteVideo('${id}')">حذف</button>
                        </div>
                    `).join('')}
                </div>
            </div>
            
            <div>
                <h4 style="font-weight:bold;margin-bottom:12px">👥 إدارة المستخدمين</h4>
                <div class="admin-list">
                    ${Object.entries(users).slice(0, 15).map(([uid, u]) => `
                        <div class="admin-item">
                            <div class="admin-item-info">
                                <div class="admin-item-avatar" style="background:${u.cartoonAvatar?.bg || 'linear-gradient(135deg, #3b82f6, #1d4ed8)'}">
                                    ${u.cartoonAvatar?.emoji || (u.username?.charAt(0) || 'U')}
                                </div>
                                <div class="admin-item-text">
                                    <div class="admin-item-name">
                                        @${u.username}
                                        ${u.banned ? '<span class="banned-tag">محظور</span>' : ''}
                                        ${u.isVerified ? '<span style="color:#60a5fa;">✅</span>' : ''}
                                    </div>
                                    <div class="admin-item-email">${u.email || ''}</div>
                                </div>
                            </div>
                            <div>
                                ${!u.banned ? `<button class="admin-ban-btn" onclick="adminBanUser('${uid}')">حظر</button>` : `<button class="admin-ban-btn unban" onclick="adminUnbanUser('${uid}')">إلغاء</button>`}
                                <button class="admin-delete-btn" onclick="adminDeleteUser('${uid}')">حذف</button>
                            </div>
                        </div>
                    `).join('')}
                </div>
            </div>
        </div>
    `;
}

async function adminDeleteVideo(videoId) { if (!isAdmin) return; if (confirm('حذف الفيديو؟')) { await db.ref(`videos/${videoId}`).remove(); alert('✅ تم الحذف'); location.reload(); } }
async function adminBanUser(userId) { if (!isAdmin) return; if (confirm('حظر المستخدم؟')) { await db.ref(`users/${userId}/banned`).set(true); alert('✅ تم الحظر'); location.reload(); } }
async function adminUnbanUser(userId) { if (!isAdmin) return; if (confirm('إلغاء الحظر؟')) { await db.ref(`users/${userId}/banned`).remove(); alert('✅ تم إلغاء الحظر'); location.reload(); } }
async function adminDeleteUser(userId) { if (!isAdmin) return; if (confirm('حذف المستخدم وجميع فيديوهاته؟')) { const videosSnap = await db.ref('videos').once('value'); const videos = videosSnap.val() || {}; Object.entries(videos).forEach(([id, v]) => { if (v.sender === userId) db.ref(`videos/${id}`).remove(); }); await db.ref(`users/${userId}`).remove(); alert('✅ تم الحذف'); location.reload(); } }

// ========== تحميل البيانات ==========
async function loadUserData() { const snap = await db.ref(`users/${currentUser.uid}`).get(); if (snap.exists()) currentUserData = { uid: currentUser.uid, ...snap.val() }; }
db.ref('users').on('value', s => { allUsers = s.val() || {}; });

// ========== فيديوهات ==========
db.ref('videos').on('value', (s) => {
    const data = s.val();
    if (!data) { allVideos = []; renderVideos(); return; }
    allVideos = []; allSounds = {};
    Object.keys(data).forEach(key => { const v = { id: key, ...data[key] }; allVideos.push(v); if (v.music) allSounds[v.music] = (allSounds[v.music] || 0) + 1; });
    allVideos.sort((a, b) => (b.timestamp || 0) - (a.timestamp || 0));
    renderVideos(); renderSoundsList();
});

function renderVideos() {
    const container = document.getElementById('videosContainer'); if (!container) return;
    container.innerHTML = '';
    let filteredVideos = currentFeed === 'forYou' ? allVideos : allVideos.filter(v => currentUserData?.following?.[v.sender]);
    if (filteredVideos.length === 0) { container.innerHTML = '<div class="loading"><div class="spinner"></div><span>' + (currentFeed === 'forYou' ? 'لا توجد فيديوهات' : 'تابع مستخدمين لرؤية فيديوهاتهم') + '</span></div>'; return; }
    filteredVideos.forEach(video => {
        const isLiked = video.likedBy && video.likedBy[currentUser?.uid];
        const user = allUsers[video.sender] || { username: video.senderName || 'user', avatarUrl: '', cartoonAvatar: null };
        const isFollowing = currentUserData?.following && currentUserData.following[video.sender];
        const commentsCount = video.comments ? Object.keys(video.comments).length : 0;
        const caption = addHashtags(video.description || '');
        const avatarHtml = user.cartoonAvatar ? `<span style="font-size:32px;">${user.cartoonAvatar.emoji}</span>` : (user.avatarUrl ? `<img src="${user.avatarUrl}">` : (user.username?.charAt(0)?.toUpperCase() || '👤'));
        const isVerified = user.isVerified || false;
        const div = document.createElement('div'); div.className = 'video-item';
        div.innerHTML = `
            <video loop playsinline muted data-src="${video.url}" poster="${video.thumbnail || ''}"></video>
            <div class="video-info">
                <div class="author-info">
                    <div class="author-avatar glass-avatar" onclick="viewProfile('${video.sender}')" style="background:${user.cartoonAvatar?.bg || 'linear-gradient(135deg, #3b82f6, #1d4ed8)'}">${avatarHtml}</div>
                    <div class="author-name"><span onclick="viewProfile('${video.sender}')">@${user.username}</span>${isVerified ? '<span class="verified-badge">✅</span>' : ''}${currentUser?.uid !== video.sender ? `<button class="follow-btn" onclick="toggleFollow('${video.sender}', this)">${isFollowing ? 'متابع' : 'متابعة'}</button>` : ''}</div>
                </div>
                <div class="video-caption">${caption}</div>
                <div class="video-music" onclick="searchBySound('${video.music || 'Original Sound'}')"><i class="fas fa-music"></i> ${video.music || 'Original Sound'}</div>
            </div>
            <div class="side-actions">
                <button class="side-btn" onclick="toggleGlobalMute()"><i class="fas ${isMuted ? 'fa-volume-mute' : 'fa-volume-up'}"></i></button>
                <button class="side-btn like-btn ${isLiked ? 'active' : ''}" onclick="toggleLike('${video.id}', this)"><i class="fas fa-heart"></i><span class="count">${video.likes || 0}</span></button>
                <button class="side-btn" onclick="openComments('${video.id}')"><i class="fas fa-comment"></i><span class="count">${commentsCount}</span></button>
                <button class="side-btn" onclick="openShare('${video.url}')"><i class="fas fa-share"></i></button>
            </div>
        `;
        const videoEl = div.querySelector('video');
        videoEl.addEventListener('dblclick', (e) => { e.stopPropagation(); const likeBtn = div.querySelector('.like-btn'); if (likeBtn) { toggleLike(video.id, likeBtn); showHeartAnimation(e.clientX, e.clientY); } });
        container.appendChild(div);
    });
    initVideoObserver();
}

function showHeartAnimation(x, y) { const heart = document.createElement('div'); heart.className = 'heart-animation'; heart.innerHTML = '❤️'; heart.style.left = (x - 40) + 'px'; heart.style.top = (y - 40) + 'px'; document.body.appendChild(heart); setTimeout(() => heart.remove(), 800); }
function initVideoObserver() { const observer = new IntersectionObserver((entries) => { entries.forEach(entry => { const video = entry.target.querySelector('video'); if (entry.isIntersecting) { if (!video.src) video.src = video.dataset.src; video.muted = isMuted; video.play().catch(() => {}); } else video.pause(); }); }, { threshold: 0.65 }); document.querySelectorAll('.video-item').forEach(seg => observer.observe(seg)); }
function toggleGlobalMute() { isMuted = !isMuted; document.querySelectorAll('video').forEach(v => v.muted = isMuted); const btns = document.querySelectorAll('.side-actions .side-btn:first-child i'); btns.forEach(btn => btn.className = isMuted ? 'fas fa-volume-mute' : 'fas fa-volume-up'); }
function switchFeed(feed) { currentFeed = feed; document.querySelectorAll('.top-tab').forEach(t => t.classList.remove('active')); event.target.classList.add('active'); renderVideos(); }

// ========== الهاشتاجات ==========
function addHashtags(text) { if (!text) return ''; return text.replace(/#(\w+)/g, '<span class="hashtag" onclick="searchHashtag(\'$1\')">#$1</span>'); }
function searchHashtag(tag) { document.getElementById('searchInput').value = '#' + tag; openSearch(); searchAll(); }

// ========== الإعجاب ==========
async function toggleLike(videoId, btn) { if (!currentUser) return; const videoRef = db.ref(`videos/${videoId}`); const snap = await videoRef.get(); const video = snap.val(); if (!video) return; let likes = video.likes || 0; let likedBy = video.likedBy || {}; if (likedBy[currentUser.uid]) { likes--; delete likedBy[currentUser.uid]; } else { likes++; likedBy[currentUser.uid] = true; await addNotification(video.sender, 'like', currentUser.uid); } await videoRef.update({ likes, likedBy }); btn.classList.toggle('active'); const countSpan = btn.querySelector('.count'); if (countSpan) countSpan.innerText = likes; }

// ========== المتابعة ==========
async function toggleFollow(userId, btn) { if (!currentUser || currentUser.uid === userId) return; const userRef = db.ref(`users/${currentUser.uid}/following/${userId}`); const targetRef = db.ref(`users/${userId}/followers/${currentUser.uid}`); const snap = await userRef.get(); if (snap.exists()) { await userRef.remove(); await targetRef.remove(); btn.innerText = 'متابعة'; await addNotification(userId, 'unfollow', currentUser.uid); } else { await userRef.set(true); await targetRef.set(true); btn.innerText = 'متابع'; await addNotification(userId, 'follow', currentUser.uid); } if (viewingProfileUserId === userId) await loadProfileData(userId); }

// ========== التعليقات ==========
async function openComments(videoId) { currentVideoId = videoId; const panel = document.getElementById('commentsPanel'); const commentsRef = db.ref(`videos/${videoId}/comments`); const snap = await commentsRef.get(); const comments = snap.val() || {}; const container = document.getElementById('commentsList'); container.innerHTML = ''; Object.values(comments).reverse().forEach(c => { const user = allUsers[c.userId] || { username: c.username || 'user', avatarUrl: '', cartoonAvatar: null }; const avatarHtml = user.cartoonAvatar ? `<span style="font-size:28px;">${user.cartoonAvatar.emoji}</span>` : (user.avatarUrl ? `<img src="${user.avatarUrl}">` : (user.username?.charAt(0)?.toUpperCase() || '👤')); container.innerHTML += `<div class="comment-item"><div class="comment-avatar" style="background:${user.cartoonAvatar?.bg || 'linear-gradient(135deg, #3b82f6, #1d4ed8)'}">${avatarHtml}</div><div><div class="font-bold">@${user.username}</div><div class="text-sm mt-1">${c.text}</div></div></div>`; }); panel.classList.add('open'); }
function closeComments() { document.getElementById('commentsPanel').classList.remove('open'); }
async function addComment() { const input = document.getElementById('commentInput'); if (!input.value.trim() || !currentVideoId) return; await db.ref(`videos/${currentVideoId}/comments`).push({ userId: currentUser.uid, username: currentUserData?.username, text: input.value, timestamp: Date.now() }); input.value = ''; openComments(currentVideoId); }

// ========== المشاركة ==========
function openShare(url) { currentShareUrl = url; document.getElementById('sharePanel').classList.add('open'); }
function closeShare() { document.getElementById('sharePanel').classList.remove('open'); }
function copyLink() { navigator.clipboard.writeText(currentShareUrl); showToast(); closeShare(); }
function shareToWhatsApp() { window.open(`https://wa.me/?text=${encodeURIComponent(currentShareUrl)}`, '_blank'); closeShare(); }
function shareToTelegram() { window.open(`https://t.me/share/url?url=${encodeURIComponent(currentShareUrl)}`, '_blank'); closeShare(); }
function downloadVideo() { window.open(currentShareUrl, '_blank'); closeShare(); }
function showToast() { const t = document.getElementById('copyToast'); t.classList.add('show'); setTimeout(() => t.classList.remove('show'), 2000); }

// ========== الإشعارات ==========
async function addNotification(targetUserId, type, fromUserId) { if (targetUserId === fromUserId) return; const fromUser = allUsers[fromUserId] || { username: 'مستخدم' }; const messages = { like: 'أعجب بفيديوك 💙', comment: 'علق على فيديو 📝', follow: 'بدأ بمتابعتك 👋', unfollow: 'توقف عن متابعتك' }; await db.ref(`notifications/${targetUserId}`).push({ type, fromUserId, fromUsername: fromUser.username, message: messages[type], timestamp: Date.now(), read: false }); }
async function openNotifications() { const panel = document.getElementById('notificationsPanel'); const snap = await db.ref(`notifications/${currentUser.uid}`).once('value'); const notifs = snap.val() || {}; const container = document.getElementById('notificationsList'); container.innerHTML = ''; Object.values(notifs).reverse().forEach(n => { container.innerHTML += `<div class="notification-item"><i class="fas ${n.type === 'like' ? 'fa-heart text-red-400' : n.type === 'comment' ? 'fa-comment text-blue-400' : 'fa-user-plus text-green-400'}"></i><div><div>${n.fromUsername}</div><div class="text-xs opacity-60">${n.message}</div></div></div>`; if (!n.read) db.ref(`notifications/${currentUser.uid}/${Object.keys(notifs).find(k => notifs[k] === n)}/read`).set(true); }); panel.classList.add('open'); }
function closeNotifications() { document.getElementById('notificationsPanel').classList.remove('open'); }

// ========== البحث ==========
function openSearch() { document.getElementById('searchPanel').classList.add('open'); }
function closeSearch() { document.getElementById('searchPanel').classList.remove('open'); }
function searchAll() { const query = document.getElementById('searchInput').value.toLowerCase(); const resultsDiv = document.getElementById('searchResults'); if (!query) { resultsDiv.innerHTML = ''; return; } const users = Object.values(allUsers).filter(u => u.username.toLowerCase().includes(query)); const videos = allVideos.filter(v => v.description?.toLowerCase().includes(query) || v.music?.toLowerCase().includes(query)); const hashtags = [...new Set(allVideos.flatMap(v => (v.description?.match(/#\w+/g) || []).filter(h => h.toLowerCase().includes(query))))]; resultsDiv.innerHTML = `${users.length ? `<div class="mb-5"><h4 class="search-section-title">👥 مستخدمين</h4>${users.map(u => `<div class="search-result" onclick="viewProfile('${u.uid}')"><div class="search-avatar" style="background:${u.cartoonAvatar?.bg || 'linear-gradient(135deg, #3b82f6, #1d4ed8)'}">${u.cartoonAvatar?.emoji || (u.username?.charAt(0)?.toUpperCase() || '👤')}</div><div>@${u.username} ${u.isVerified ? '<span style="color:#60a5fa;">✅</span>' : ''}</div></div>`).join('')}</div>` : ''}${hashtags.length ? `<div class="mb-5"><h4 class="search-section-title"># هاشتاقات</h4>${hashtags.map(h => `<div class="search-result" onclick="searchHashtag('${h.substring(1)}')"><i class="fas fa-hashtag text-blue-400 w-8 text-xl"></i><div>${h}</div></div>`).join('')}</div>` : ''}${videos.length ? `<div><h4 class="search-section-title">🎬 فيديوهات</h4>${videos.map(v => `<div class="search-result" onclick="playVideo('${v.url}')"><i class="fas fa-video w-8 text-xl text-blue-400"></i><div>${(v.description || 'فيديو').substring(0, 40)}</div></div>`).join('')}</div>` : ''}`; }

// ========== الأصوات ==========
function openSounds() { document.getElementById('soundsPanel').classList.add('open'); }
function closeSounds() { document.getElementById('soundsPanel').classList.remove('open'); }
function renderSoundsList() { const container = document.getElementById('soundsList'); if (!container) return; const sortedSounds = Object.entries(allSounds).sort((a, b) => b[1] - a[1]); container.innerHTML = sortedSounds.map(([name, count]) => `<div class="sound-item" onclick="searchBySound('${name}')"><div class="sound-icon"><i class="fas fa-music"></i></div><div class="sound-info"><div class="sound-name">${name}</div><div class="sound-count">${count} فيديو</div></div></div>`).join(''); }
function searchBySound(soundName) { document.getElementById('searchInput').value = soundName; closeSounds(); openSearch(); searchAll(); }

// ========== الملف الشخصي ==========
async function viewProfile(userId) { if (!userId) return; viewingProfileUserId = userId; await loadProfileData(userId); document.getElementById('profilePanel').classList.add('open'); }

async function loadProfileData(userId) {
    const userSnap = await db.ref(`users/${userId}`).get(); const user = userSnap.val(); if (!user) return;
    
    // تحديث غلاف الملف الشخصي
    const coverEl = document.getElementById('profileCover');
    if (coverEl && user.coverColor) {
        coverEl.style.background = user.coverColor;
    }
    
    const avatarDisplay = document.getElementById('profileAvatarDisplay');
    if (user.cartoonAvatar) {
        avatarDisplay.innerHTML = `<span style="font-size:56px;">${user.cartoonAvatar.emoji}</span>`;
        avatarDisplay.style.background = user.cartoonAvatar.bg;
    } else if (user.avatarUrl && user.avatarUrl !== '') {
        avatarDisplay.innerHTML = `<img src="${user.avatarUrl}" style="width:100%;height:100%;object-fit:cover;border-radius:50%;">`;
        avatarDisplay.style.background = 'white';
    } else {
        avatarDisplay.innerHTML = user.username?.charAt(0)?.toUpperCase() || '👤';
        avatarDisplay.style.background = 'linear-gradient(135deg, #3b82f6, #1d4ed8)';
    }
    
    const nameDisplay = document.getElementById('profileNameDisplay');
    nameDisplay.innerText = user.username || 'مستخدم';
    if (user.isVerified) {
        nameDisplay.innerHTML += ' <span class="verified-badge">✅</span>';
    }
    
    document.getElementById('profileBioDisplay').innerText = user.bio || '';
    document.getElementById('profileFollowing').innerText = Object.keys(user.following || {}).length;
    document.getElementById('profileFollowers').innerText = Object.keys(user.followers || {}).length;
    
    const userVideos = allVideos.filter(v => v.sender === userId);
    const totalLikes = userVideos.reduce((sum, v) => sum + (v.likes || 0), 0);
    document.getElementById('profileLikes').innerText = totalLikes;
    
    // عرض الفيديوهات في الشبكة
    const container = document.getElementById('profileVideosList');
    container.innerHTML = '';
    if (userVideos.length === 0) {
        container.innerHTML = '<div class="text-center text-gray-400 py-10">لا توجد فيديوهات بعد</div>';
    } else {
        userVideos.forEach(v => {
            const thumb = document.createElement('div');
            thumb.className = 'video-thumb';
            thumb.innerHTML = `<i class="fas fa-play"></i>${v.thumbnail ? `<img src="${v.thumbnail}" class="thumb-bg">` : ''}`;
            thumb.onclick = () => playVideo(v.url);
            container.appendChild(thumb);
        });
    }
    
    const actionsDiv = document.getElementById('profileActions');
    actionsDiv.innerHTML = '';
    
    if (userId === currentUser?.uid) {
        actionsDiv.innerHTML = `
            <button class="edit-profile-btn" onclick="openEditProfile()"><i class="fas fa-edit"></i> تعديل الملف</button>
            <button class="logout-btn" onclick="logout()"><i class="fas fa-sign-out-alt"></i> تسجيل خروج</button>
        `;
        if (isAdmin) {
            const adminPanel = await renderAdminPanel();
            actionsDiv.innerHTML += adminPanel;
        }
    } else {
        const isFollowing = currentUserData?.following && currentUserData.following[userId];
        actionsDiv.innerHTML = `<button class="follow-btn" onclick="toggleFollow('${userId}', this)">${isFollowing ? 'متابع' : 'متابعة'}</button>`;
        addMessageButtonInProfile(userId);
    }
}

function openMyProfile() { if (currentUser) viewProfile(currentUser.uid); }
function closeProfile() { document.getElementById('profilePanel').classList.remove('open'); viewingProfileUserId = null; }

// ========== تغيير غلاف الملف الشخصي ==========
async function changeCoverColor() {
    if (!currentUser) return;
    const currentCover = currentUserData?.coverColor || COVER_COLORS[0];
    const colorOptions = COVER_COLORS.map((c, i) => `\n${i+1}. ${c.substring(0, 30)}...`).join('');
    const choice = prompt(`اختر لون الغلاف (1-${COVER_COLORS.length}):${colorOptions}`);
    if (choice && !isNaN(choice) && choice >= 1 && choice <= COVER_COLORS.length) {
        const newCover = COVER_COLORS[choice - 1];
        await db.ref(`users/${currentUser.uid}/coverColor`).set(newCover);
        currentUserData.coverColor = newCover;
        if (viewingProfileUserId === currentUser.uid) await loadProfileData(currentUser.uid);
    }
}

function openEditProfile() {
    document.getElementById('editUsername').value = currentUserData?.username || '';
    document.getElementById('editBio').value = currentUserData?.bio || '';
    const editAvatar = document.getElementById('editAvatarDisplay');
    if (currentUserData?.cartoonAvatar) {
        editAvatar.innerHTML = `<span style="font-size:56px;">${currentUserData.cartoonAvatar.emoji}</span>`;
        editAvatar.style.background = currentUserData.cartoonAvatar.bg;
    } else if (currentUserData?.avatarUrl) {
        editAvatar.innerHTML = `<img src="${currentUserData.avatarUrl}" style="width:100%;height:100%;object-fit:cover;border-radius:50%;">`;
        editAvatar.style.background = 'white';
    } else {
        editAvatar.innerHTML = currentUserData?.username?.charAt(0)?.toUpperCase() || '👤';
        editAvatar.style.background = 'linear-gradient(135deg, #3b82f6, #1d4ed8)';
    }
    document.getElementById('editProfilePanel').classList.add('open');
}

function closeEditProfile() { document.getElementById('editProfilePanel').classList.remove('open'); }

async function saveProfile() {
    const newUsername = document.getElementById('editUsername').value;
    const newBio = document.getElementById('editBio').value;
    await db.ref(`users/${currentUser.uid}`).update({ username: newUsername, bio: newBio });
    currentUserData.username = newUsername;
    currentUserData.bio = newBio;
    closeEditProfile();
    if (viewingProfileUserId === currentUser.uid) await loadProfileData(currentUser.uid);
    renderVideos();
}

function changeAvatar() { document.getElementById('avatarInput').click(); }

async function uploadAvatar(input) {
    const file = input.files[0];
    if (!file) return;
    const fd = new FormData(); fd.append('file', file); fd.append('upload_preset', UPLOAD_PRESET);
    const res = await fetch(`https://api.cloudinary.com/v1_1/${CLOUD_NAME}/image/upload`, { method: 'POST', body: fd });
    const data = await res.json();
    await db.ref(`users/${currentUser.uid}/avatarUrl`).set(data.secure_url);
    await db.ref(`users/${currentUser.uid}/cartoonAvatar`).set(null);
    currentUserData.avatarUrl = data.secure_url;
    currentUserData.cartoonAvatar = null;
    if (viewingProfileUserId === currentUser.uid) await loadProfileData(currentUser.uid);
    renderVideos();
}

function playVideo(url) { window.open(url, '_blank'); }

// ========== الدردشة ==========
let currentChatUserId = null;
async function openConversations() { /* ... نفس الكود السابق ... */ }
function closeConversations() { document.getElementById('conversationsPanel').classList.remove('open'); }
async function openPrivateChat(otherUserId) { /* ... */ }
function closePrivateChat() { document.getElementById('privateChatPanel').classList.remove('open'); currentChatUserId = null; }
async function loadPrivateMessages(otherUserId) { /* ... */ }
async function sendPrivateMessage() { /* ... */ }
async function sendChatImage(input) { /* ... */ }
function addMessageButtonInProfile(userId) { /* ... */ }
function getChatId(uid1, uid2) { return uid1 < uid2 ? `${uid1}_${uid2}` : `${uid2}_${uid1}`; }

// ========== رفع الفيديو ==========
let selectedVideoFile = null;
let popularHashtags = ['تيك_توك', 'ترند', 'اكسبلور', 'فن', 'موسيقى', 'ضحك', 'رياضة', 'طبخ', 'سفر', 'تحدي'];
let popularMusics = ['Original Sound', 'موسيقى هادئة', 'ريمكس ترند'];

function openUploadPanel() { document.getElementById('uploadPanel').classList.add('open'); resetUploadForm(); }
function closeUploadPanel() { document.getElementById('uploadPanel').classList.remove('open'); resetUploadForm(); }
// ... (باقي دوال الرفع كما في الموقع السابق) ...

function switchTab(tab) {
    document.querySelectorAll('.nav-item').forEach(t => t.classList.remove('active'));
    if (event.target.closest('.nav-item')) event.target.closest('.nav-item').classList.add('active');
    if (tab === 'search') openSearch();
    if (tab === 'notifications') openNotifications();
    if (tab === 'home') { closeSearch(); closeNotifications(); closeProfile(); closeSounds(); closeUploadPanel(); closeConversations(); closePrivateChat(); }
}

// ========== مراقبة المستخدم ==========
auth.onAuthStateChanged(async (user) => {
    if (user) {
        currentUser = user; await loadUserData(); checkAdminStatus();
        document.getElementById('loginScreen').style.display = 'none';
        document.getElementById('mainApp').style.display = 'block';
        const presenceRef = db.ref('presence/' + user.uid); presenceRef.set(true); presenceRef.onDisconnect().remove();
    } else {
        window.location.href = 'login.html';
    }
});

console.log('💙 BLU3Y Glass System Ready');
'''
    write_file("script.js", content)
    print("✅ script.js تم إنشاؤه بنجاح")

# =====================================================================
# إنشاء ملف index.html (الموقع الرئيسي الزجاجي)
# =====================================================================
def create_index_html():
    content = '''<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>BLU3Y | Glass TikTok</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://upload-widget.cloudinary.com/global/all.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-database-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-auth-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/10.7.0/firebase-storage-compat.js"></script>
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { 
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; 
            background: linear-gradient(135deg, #0a0a1a, #0f172a, #1e293b);
            color: #fff; 
            overflow: hidden; 
            height: 100vh; 
        }
        
        /* شاشة التحميل */
        #loginScreen { 
            position: fixed; inset: 0; z-index: 1000; 
            background: linear-gradient(135deg, #0a2463, #1e3a8a, #3b82f6);
            display: flex; align-items: center; justify-content: center; 
        }
        
        /* التطبيق الرئيسي */
        #mainApp { display: none; height: 100vh; position: relative; }
        
        /* شريط علوي زجاجي */
        .top-bar { 
            position: fixed; top: 0; left: 0; right: 0; 
            display: flex; justify-content: space-between; align-items: center; 
            padding: 12px 20px; z-index: 100; 
            background: rgba(15, 23, 42, 0.7);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(59, 130, 246, 0.15);
        }
        .logo { display: flex; align-items: center; gap: 8px; }
        .logo-icon { 
            width: 34px; height: 34px; 
            background: linear-gradient(135deg, #3b82f6, #1d4ed8); 
            border-radius: 10px; display: flex; align-items: center; justify-content: center; 
            font-weight: bold; box-shadow: 0 4px 15px rgba(59, 130, 246, 0.4);
        }
        .logo-text { font-weight: 800; font-size: 18px; background: linear-gradient(to bottom, #fff, #93c5fd); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .top-tabs { display: flex; gap: 12px; background: rgba(255,255,255,0.05); padding: 4px; border-radius: 30px; }
        .top-tab { background: none; border: none; color: rgba(255,255,255,0.6); font-weight: 500; padding: 6px 14px; cursor: pointer; border-radius: 20px; font-size: 13px; transition: all 0.3s; }
        .top-tab.active { color: #fff; background: rgba(59, 130, 246, 0.3); }
        .top-icons { display: flex; gap: 16px; }
        .top-icon { background: none; border: none; color: rgba(255,255,255,0.8); font-size: 18px; cursor: pointer; transition: color 0.3s; }
        .top-icon:hover { color: #60a5fa; }
        
        /* حاوية الفيديوهات */
        .videos-container { height: 100vh; overflow-y: scroll; scroll-snap-type: y mandatory; scrollbar-width: none; }
        .videos-container::-webkit-scrollbar { display: none; }
        .video-item { height: 100vh; scroll-snap-align: start; position: relative; background: #000; }
        .video-item video { width: 100%; height: 100%; object-fit: cover; }
        
        .video-info { position: absolute; bottom: 100px; left: 16px; right: 80px; z-index: 20; }
        .author-info { display: flex; align-items: center; gap: 12px; margin-bottom: 8px; }
        .author-avatar { 
            width: 50px; height: 50px; border-radius: 50%; 
            display: flex; align-items: center; justify-content: center; 
            font-size: 22px; cursor: pointer; 
            border: 2px solid rgba(255,255,255,0.4);
            box-shadow: 0 8px 20px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        .author-avatar img { width: 100%; height: 100%; object-fit: cover; }
        .author-name { font-weight: bold; font-size: 15px; cursor: pointer; display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
        .verified-badge { color: #60a5fa; font-size: 13px; }
        .follow-btn { 
            background: linear-gradient(135deg, #3b82f6, #2563eb); 
            padding: 5px 14px; border-radius: 20px; font-size: 11px; 
            font-weight: bold; cursor: pointer; border: none; color: white;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
        }
        .video-caption { font-size: 14px; margin-bottom: 6px; line-height: 1.4; }
        .video-music { font-size: 12px; opacity: 0.8; display: flex; align-items: center; gap: 6px; cursor: pointer; }
        .hashtag { color: #60a5fa; cursor: pointer; font-weight: 500; }
        
        /* الأزرار الجانبية */
        .side-actions { position: absolute; right: 12px; bottom: 130px; display: flex; flex-direction: column; gap: 22px; z-index: 20; }
        .side-btn { display: flex; flex-direction: column; align-items: center; gap: 4px; background: none; border: none; color: white; cursor: pointer; font-size: 10px; transition: transform 0.2s; }
        .side-btn:active { transform: scale(0.85); }
        .side-btn i { font-size: 30px; filter: drop-shadow(0 2px 6px rgba(0,0,0,0.4)); }
        .side-btn.active i { color: #3b82f6; }
        .side-btn .count { font-weight: bold; font-size: 11px; }
        
        /* شريط سفلي زجاجي */
        .bottom-nav { 
            position: fixed; bottom: 0; left: 0; right: 0; 
            display: flex; justify-content: space-around; align-items: center; 
            padding: 10px 0 22px; 
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(25px);
            -webkit-backdrop-filter: blur(25px);
            z-index: 100; 
            border-top: 1px solid rgba(59, 130, 246, 0.15);
        }
        .nav-item { display: flex; flex-direction: column; align-items: center; gap: 3px; background: none; border: none; color: rgba(255,255,255,0.5); cursor: pointer; font-size: 10px; transition: all 0.3s; }
        .nav-item i { font-size: 22px; }
        .nav-item.active { color: #60a5fa; }
        .create-btn { 
            width: 50px; height: 50px; 
            background: linear-gradient(135deg, #3b82f6, #1d4ed8); 
            border-radius: 50%; display: flex; align-items: center; justify-content: center; 
            margin-top: -26px; cursor: pointer; 
            box-shadow: 0 8px 25px rgba(59, 130, 246, 0.5);
            transition: transform 0.3s;
        }
        .create-btn:hover { transform: scale(1.08); }
        
        /* اللوحات */
        .share-panel, .comments-panel, .search-panel, .notifications-panel, .profile-panel, .edit-profile-panel, .sounds-panel, .upload-panel, .private-chat-panel, .conversations-panel {
            position: fixed; top: 0; left: 0; right: 0; bottom: 0; 
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(30px);
            -webkit-backdrop-filter: blur(30px);
            z-index: 300; 
            transform: translateX(100%); 
            transition: 0.35s cubic-bezier(0.2, 0.9, 0.4, 1.1); 
            overflow-y: auto;
        }
        .share-panel.open, .comments-panel.open, .search-panel.open, .notifications-panel.open, .profile-panel.open, .edit-profile-panel.open, .sounds-panel.open, .upload-panel.open, .private-chat-panel.open, .conversations-panel.open {
            transform: translateX(0);
        }
        .panel-header { 
            display: flex; justify-content: space-between; align-items: center; 
            padding: 20px; 
            border-bottom: 1px solid rgba(59, 130, 246, 0.1); 
            position: sticky; top: 0; 
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(20px);
            z-index: 10; 
        }
        .close-btn { 
            background: rgba(255,255,255,0.1); 
            border: none; color: white; font-size: 20px; cursor: pointer; 
            width: 40px; height: 40px; border-radius: 50%; 
            display: flex; align-items: center; justify-content: center;
            transition: background 0.3s;
        }
        .close-btn:hover { background: rgba(255,255,255,0.2); }
        
        /* غلاف الملف الشخصي */
        .profile-cover {
            height: 180px;
            position: relative;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            padding-bottom: 30px;
        }
        .change-cover-btn {
            position: absolute;
            top: 15px;
            right: 15px;
            background: rgba(0,0,0,0.5);
            border: 1px solid rgba(255,255,255,0.2);
            color: white;
            padding: 6px 12px;
            border-radius: 20px;
            font-size: 11px;
            cursor: pointer;
            backdrop-filter: blur(10px);
        }
        .profile-avatar-large { 
            width: 100px; height: 100px; border-radius: 50%; 
            display: flex; align-items: center; justify-content: center; 
            font-size: 48px; 
            border: 4px solid rgba(255,255,255,0.3);
            box-shadow: 0 12px 30px rgba(0,0,0,0.4);
            overflow: hidden;
            cursor: pointer;
        }
        .profile-avatar-large img { width: 100%; height: 100%; object-fit: cover; }
        .profile-stats { display: flex; justify-content: center; gap: 35px; margin: 20px 0; }
        .stat { text-align: center; }
        .stat-number { font-size: 20px; font-weight: bold; color: #93c5fd; }
        .stat-label { font-size: 11px; opacity: 0.6; margin-top: 4px; }
        .edit-profile-btn, .logout-btn { 
            background: rgba(59, 130, 246, 0.2); 
            border: 1px solid rgba(59, 130, 246, 0.3); 
            padding: 10px 24px; border-radius: 40px; color: white; 
            margin: 5px; cursor: pointer; font-size: 13px;
            transition: all 0.3s;
        }
        .edit-profile-btn:hover, .logout-btn:hover { background: rgba(59, 130, 246, 0.4); }
        .follow-btn { background: linear-gradient(135deg, #3b82f6, #2563eb); border: none; }
        .videos-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 3px; margin-top: 20px; padding: 0 12px; }
        .video-thumb { 
            aspect-ratio: 9/16; 
            background: rgba(255,255,255,0.05); 
            border-radius: 8px;
            display: flex; align-items: center; justify-content: center; 
            cursor: pointer; 
            position: relative;
            overflow: hidden;
            transition: transform 0.2s;
        }
        .video-thumb:hover { transform: scale(1.03); }
        .video-thumb i { 
            position: absolute; 
            font-size: 28px; 
            color: rgba(255,255,255,0.8);
            z-index: 1;
            filter: drop-shadow(0 2px 6px rgba(0,0,0,0.5));
        }
        .thumb-bg {
            position: absolute;
            inset: 0;
            width: 100%;
            height: 100%;
            object-fit: cover;
            opacity: 0.7;
        }
        .back-btn { 
            position: absolute; top: 20px; right: 20px; 
            background: rgba(0,0,0,0.5); 
            width: 44px; height: 44px; border-radius: 50%; 
            display: flex; align-items: center; justify-content: center; 
            cursor: pointer; z-index: 20;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.2);
        }
        
        /* إضافات */
        .copy-toast { position: fixed; bottom: 100px; left: 50%; transform: translateX(-50%); background: rgba(15,23,42,0.9); padding: 12px 24px; border-radius: 50px; z-index: 1000; opacity: 0; transition: opacity 0.3s; pointer-events: none; border: 1px solid rgba(59,130,246,0.3); }
        .copy-toast.show { opacity: 1; }
        .heart-animation { position: fixed; font-size: 80px; color: #3b82f6; pointer-events: none; z-index: 1000; animation: heartFloat 0.8s ease-out forwards; }
        @keyframes heartFloat { 0% { transform: scale(0.5) translateY(0); opacity: 1; } 100% { transform: scale(1.5) translateY(-100px); opacity: 0; } }
        .loading { display: flex; align-items: center; justify-content: center; height: 100vh; color: #93c5fd; gap: 12px; flex-direction: column; }
        .spinner { width: 36px; height: 36px; border: 3px solid rgba(59,130,246,0.2); border-top-color: #3b82f6; border-radius: 50%; animation: spin 0.8s linear infinite; }
        @keyframes spin { to { transform: rotate(360deg); } }
        .search-input { width: 100%; padding: 14px 18px; border-radius: 30px; background: rgba(255,255,255,0.05); border: 1px solid rgba(59,130,246,0.2); color: white; margin-bottom: 20px; outline: none; }
        .search-section-title { font-size: 12px; opacity: 0.5; margin-bottom: 8px; }
        .comment-item { display: flex; gap: 12px; padding: 12px 0; border-bottom: 1px solid rgba(255,255,255,0.05); }
        .comment-avatar { width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; overflow: hidden; }
        .admin-panel-section { margin-top: 20px; padding: 16px; background: rgba(59,130,246,0.08); border-radius: 20px; border: 1px solid rgba(59,130,246,0.2); }
        .admin-stats { display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; margin-bottom: 20px; }
        .admin-stat-card { background: rgba(0,0,0,0.3); border-radius: 12px; padding: 10px; text-align: center; }
        .admin-stat-number { font-size: 22px; font-weight: bold; color: #60a5fa; }
        .admin-stat-label { font-size: 10px; opacity: 0.5; margin-top: 4px; }
        .banned-tag { background: #ef4444; padding: 2px 6px; border-radius: 12px; font-size: 9px; margin-left: 5px; }
    </style>
</head>
<body>

<!-- شاشة تحميل -->
<div id="loginScreen">
    <div style="text-align:center">
        <div class="spinner"></div>
        <p style="margin-top:16px;color:rgba(255,255,255,0.7)">💙 جاري التحميل...</p>
    </div>
</div>

<!-- التطبيق الرئيسي -->
<div id="mainApp">
    <div class="top-bar">
        <div class="logo"><div class="logo-icon">💎</div><span class="logo-text">BLU3Y</span></div>
        <div class="top-tabs">
            <button class="top-tab" onclick="switchFeed('following')">متابَعين</button>
            <button class="top-tab active" onclick="switchFeed('forYou')">لك</button>
        </div>
        <div class="top-icons">
            <i class="fas fa-search top-icon" onclick="openSearch()"></i>
            <i class="fas fa-music top-icon" onclick="openSounds()"></i>
        </div>
    </div>

    <div class="videos-container" id="videosContainer"><div class="loading"><div class="spinner"></div><span>جاري التحميل...</span></div></div>

    <div class="bottom-nav">
        <button class="nav-item active" onclick="switchTab('home')"><i class="fas fa-home"></i><span>الرئيسية</span></button>
        <button class="nav-item" onclick="switchTab('search')"><i class="fas fa-search"></i><span>بحث</span></button>
        <div class="create-btn" onclick="openUploadPanel()"><i class="fas fa-plus"></i></div>
        <button class="nav-item" onclick="openConversations()"><i class="fas fa-envelope"></i><span>الرسائل</span></button>
        <button class="nav-item" onclick="openMyProfile()"><i class="fas fa-user"></i><span>الملف</span></button>
    </div>

    <div id="copyToast" class="copy-toast">✅ تم نسخ الرابط</div>

    <!-- لوحة المشاركة -->
    <div id="sharePanel" class="share-panel"><div class="panel-header"><h3>مشاركة</h3><button class="close-btn" onclick="closeShare()"><i class="fas fa-times"></i></button></div><div class="share-option p-4" onclick="copyLink()"><i class="fas fa-link text-blue-400"></i><span>نسخ الرابط</span></div><div class="share-option p-4" onclick="shareToWhatsApp()"><i class="fab fa-whatsapp text-green-400"></i><span>WhatsApp</span></div><div class="share-option p-4" onclick="shareToTelegram()"><i class="fab fa-telegram text-blue-400"></i><span>Telegram</span></div><div class="share-option p-4" onclick="downloadVideo()"><i class="fas fa-download"></i><span>تنزيل</span></div></div>

    <!-- لوحة التعليقات -->
    <div id="commentsPanel" class="comments-panel"><div class="panel-header"><h3>التعليقات</h3><button class="close-btn" onclick="closeComments()"><i class="fas fa-times"></i></button></div><div id="commentsList" class="p-4"></div><div class="add-comment p-4" style="display:flex;gap:12px;background:rgba(255,255,255,0.05);border-radius:30px;margin:16px"><input type="text" id="commentInput" class="search-input" style="flex:1;margin:0" placeholder="أضف تعليقاً..."><button onclick="addComment()" class="follow-btn">نشر</button></div></div>

    <!-- لوحة البحث -->
    <div id="searchPanel" class="search-panel"><div class="panel-header"><h3>بحث</h3><button class="close-btn" onclick="closeSearch()"><i class="fas fa-times"></i></button></div><div class="p-4"><input type="text" id="searchInput" class="search-input" placeholder="🔍 بحث..." onkeyup="searchAll()"></div><div id="searchResults" class="p-4"></div></div>

    <!-- لوحة الأصوات -->
    <div id="soundsPanel" class="sounds-panel"><div class="panel-header"><h3>🎵 الأصوات</h3><button class="close-btn" onclick="closeSounds()"><i class="fas fa-times"></i></button></div><div id="soundsList" class="p-2"></div></div>

    <!-- لوحة الإشعارات -->
    <div id="notificationsPanel" class="notifications-panel"><div class="panel-header"><h3>🔔 الإشعارات</h3><button class="close-btn" onclick="closeNotifications()"><i class="fas fa-times"></i></button></div><div id="notificationsList" class="p-4"></div></div>

    <!-- لوحة الرفع -->
    <div id="uploadPanel" class="upload-panel">
        <div class="panel-header"><h3>📤 رفع فيديو</h3><button class="close-btn" onclick="closeUploadPanel()"><i class="fas fa-times"></i></button></div>
        <div class="p-4" style="max-width:500px;margin:0 auto">
            <div onclick="document.getElementById('videoFileInput').click()" style="background:rgba(255,255,255,0.05);border:2px dashed rgba(59,130,246,0.3);border-radius:20px;padding:60px 20px;text-align:center;cursor:pointer;margin-bottom:20px">
                <i class="fas fa-cloud-upload-alt" style="font-size:48px;color:#3b82f6;margin-bottom:12px"></i>
                <p>اضغط لاختيار فيديو</p>
                <span style="font-size:12px;opacity:0.5">MP4, MOV - حتى 100MB</span>
                <video id="videoPreview" style="width:100%;max-height:250px;object-fit:contain;display:none;margin-top:12px;border-radius:12px" controls></video>
            </div>
            <input type="file" id="videoFileInput" accept="video/*" style="display:none" onchange="selectVideoFile(this)">
            <div style="background:rgba(255,255,255,0.05);border-radius:20px;padding:20px">
                <div style="margin-bottom:16px"><label style="display:block;margin-bottom:8px;font-size:13px;opacity:0.7">وصف الفيديو</label><textarea id="videoDescription" class="search-input" style="min-height:70px;resize:none" placeholder="اكتب وصفاً... استخدم # للهاشتاقات"></textarea></div>
                <div style="margin-bottom:16px"><label style="display:block;margin-bottom:8px;font-size:13px;opacity:0.7">الموسيقى</label><input type="text" id="videoMusic" class="search-input" style="margin:0" placeholder="Original Sound"></div>
                <div id="uploadProgressBar" style="display:none;margin:16px 0"><div style="background:rgba(255,255,255,0.1);border-radius:30px;height:6px"><div id="progressFill" style="background:#3b82f6;width:0%;height:100%;border-radius:30px;transition:width 0.3s"></div></div><p id="progressText" style="text-align:center;font-size:12px;margin-top:6px;color:#60a5fa">0%</p></div>
                <button class="follow-btn" id="uploadSubmitBtn" onclick="uploadVideoWithDetails()" style="width:100%;padding:14px">رفع الفيديو 🚀</button>
                <div id="uploadStatus" style="text-align:center;margin-top:12px;font-size:13px"></div>
            </div>
        </div>
    </div>

    <!-- صفحة الملف الشخصي -->
    <div id="profilePanel" class="profile-panel">
        <div class="back-btn" onclick="closeProfile()"><i class="fas fa-arrow-right"></i></div>
        <div class="profile-cover" id="profileCover">
            <button class="change-cover-btn" onclick="changeCoverColor()"><i class="fas fa-palette"></i> تغيير الغلاف</button>
            <div class="profile-avatar-large" id="profileAvatarDisplay" onclick="changeAvatar()">👤</div>
        </div>
        <div style="text-align:center;padding:0 20px">
            <h2 id="profileNameDisplay" class="mt-3 text-xl font-bold"></h2>
            <p id="profileBioDisplay" class="text-sm opacity-60 mt-1"></p>
            <div class="profile-stats">
                <div class="stat"><div class="stat-number" id="profileFollowing">0</div><div class="stat-label">يتابع</div></div>
                <div class="stat"><div class="stat-number" id="profileFollowers">0</div><div class="stat-label">متابع</div></div>
                <div class="stat"><div class="stat-number" id="profileLikes">0</div><div class="stat-label">إعجابات</div></div>
            </div>
            <div id="profileActions"></div>
        </div>
        <div class="p-4"><h4 class="mb-3 font-bold">🎬 فيديوهاتي</h4><div id="profileVideosList" class="videos-grid"></div></div>
    </div>

    <!-- لوحة تعديل الملف الشخصي -->
    <div id="editProfilePanel" class="edit-profile-panel">
        <div class="panel-header"><h3>تعديل الملف</h3><button class="close-btn" onclick="closeEditProfile()"><i class="fas fa-times"></i></button></div>
        <div style="text-align:center;padding:20px" onclick="changeAvatar()">
            <div class="profile-avatar-large" id="editAvatarDisplay">👤</div>
            <p style="font-size:11px;opacity:0.5;margin-top:8px">اضغط لتغيير الصورة</p>
        </div>
        <input type="file" id="avatarInput" accept="image/*" style="display:none" onchange="uploadAvatar(this)">
        <div class="p-4">
            <input type="text" id="editUsername" class="search-input" placeholder="اسم المستخدم" style="margin-bottom:12px">
            <textarea id="editBio" class="search-input" style="min-height:80px;resize:none;margin-bottom:12px" placeholder="السيرة الذاتية"></textarea>
            <button onclick="saveProfile()" class="follow-btn" style="width:100%;padding:14px">💾 حفظ التغييرات</button>
        </div>
    </div>

    <!-- لوحة الدردشة -->
    <div id="privateChatPanel" class="private-chat-panel">
        <div class="panel-header">
            <div style="display:flex;align-items:center;gap:12px">
                <div id="chatAvatarDisplay" style="width:42px;height:42px;border-radius:50%;background:#3b82f6;display:flex;align-items:center;justify-content:center">👤</div>
                <h3 id="chatUserName">محادثة</h3>
            </div>
            <button class="close-btn" onclick="closePrivateChat()"><i class="fas fa-times"></i></button>
        </div>
        <div id="privateMessagesList" style="flex:1;overflow-y:auto;padding:16px"></div>
        <div style="display:flex;gap:12px;padding:16px;background:rgba(255,255,255,0.05);align-items:center">
            <div onclick="document.getElementById('chatImageInput').click()" style="width:40px;height:40px;background:rgba(255,255,255,0.1);border-radius:50%;display:flex;align-items:center;justify-content:center;cursor:pointer"><i class="fas fa-image"></i></div>
            <input type="file" id="chatImageInput" accept="image/*" style="display:none" onchange="sendChatImage(this)">
            <input type="text" id="privateMessageInput" class="search-input" style="flex:1;margin:0" placeholder="اكتب رسالة...">
            <button onclick="sendPrivateMessage()" style="width:40px;height:40px;background:#3b82f6;border:none;border-radius:50%;color:white;cursor:pointer"><i class="fas fa-paper-plane"></i></button>
        </div>
    </div>

    <!-- قائمة المحادثات -->
    <div id="conversationsPanel" class="conversations-panel">
        <div class="panel-header"><h3>المحادثات</h3><button class="close-btn" onclick="closeConversations()"><i class="fas fa-times"></i></button></div>
        <div id="conversationsList" style="padding:16px"></div>
    </div>
</div>

<script src="firebase-config.js"></script>
<script src="script.js"></script>
</body>
</html>'''
    write_file("index.html", content)
    print("✅ index.html تم إنشاؤه بنجاح (زجاجي أزرق)")

# =====================================================================
# دالة مساعدة
# =====================================================================
def write_file(filename, content):
    os.makedirs(os.path.dirname(filename) if os.path.dirname(filename) else '.', exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# =====================================================================
# التشغيل الرئيسي
# =====================================================================
def main():
    print("=" * 60)
    print("💎 BLU3Y Glass System - بدء إنشاء الملفات...")
    print("=" * 60)
    
    create_firebase_config()
    create_login_html()
    create_signup_html()
    create_script_js()
    create_index_html()
    
    print("=" * 60)
    print("✅ تم إنشاء جميع الملفات بنجاح!")
    print("📁 الملفات المنشأة:")
    print("   ├── login.html (تسجيل الدخول - زجاجي)")
    print("   ├── signup.html (الاشتراك - مع شخصيات كارتونية)")
    print("   ├── index.html (الموقع الرئيسي - زجاجي أزرق)")
    print("   ├── firebase-config.js (إعدادات Firebase + Cloudinary)")
    print("   └── script.js (المنطق الكامل)")
    print()
    print("👾 20 شخصية كارتونية متاحة عند التسجيل")
    print("💙 تصميم زجاجي أزرق شفاف")
    print("🎨 غلاف ملف شخصي قابل للتغيير")
    print("📂 ملفات منفصلة لتسجيل الدخول والاشتراك")
    print("🔥 Firebase: gomlf-c26ce")
    print("☁️ Cloudinary: dmla61v7n / so2_mk")
    print("👑 الأدمن: jasim28v@gmail.com")
    print("=" * 60)

if __name__ == "__main__":
    main()
