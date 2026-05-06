// ========== BLU3Y Glass Script ==========
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
function addHashtags(text) { if (!text) return ''; return text.replace(/#(\w+)/g, '<span class="hashtag" onclick="searchHashtag('$1')">#$1</span>'); }
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
    const colorOptions = COVER_COLORS.map((c, i) => `
${i+1}. ${c.substring(0, 30)}...`).join('');
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
