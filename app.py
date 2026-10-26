import streamlit as st
import streamlit.components.v1 as components

# =====================================================
# PAGE CONFIGURATION
# =====================================================
st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded",
)

# =====================================================
# DEPLOYED APPLICATION URLS
# =====================================================
DRAWING_URL = "https://ai-drawing-studio.streamlit.app/"
MOODSPARK_URL = "https://moodspark-pe81.onrender.com"

# =====================================================
# SESSION STATE / NAVIGATION
# =====================================================
if "page" not in st.session_state:
    st.session_state.page = "Home"


def navigate_to(page_name):
    st.session_state.page = page_name


def show_embedded_app(url, title):
    """Try to display the remote app inside the dashboard."""
    st.markdown(f"### {title}")
    st.caption(
        "The app is being displayed inside Creative Universe. "
        "If the panel stays blank or shows a security error, that site's "
        "hosting settings may block embedding. Use the fallback button below."
    )
    components.iframe(url, height=780, scrolling=True)
    st.write("")
    st.link_button(
        f"If the app does not load, open {title} directly ↗",
        url,
        use_container_width=True,
    )


# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Orbitron:wght@500;600;700;800&display=swap');

    .stApp {
        background:
            radial-gradient(circle at 10% 10%, #172554 0%, transparent 35%),
            radial-gradient(circle at 90% 20%, #312e81 0%, transparent 30%),
            linear-gradient(135deg, #080d1b, #10172a 55%, #080d1b);
        color: #f8fafc;
        font-family: 'Inter', sans-serif;
    }
    [data-testid="stSidebar"] {
        background: #0b1120;
        border-right: 1px solid rgba(148,163,184,0.18);
    }
    [data-testid="stSidebar"] * { color: #e2e8f0; }
    .hero {
        padding: 42px 24px;
        text-align: center;
        border: 1px solid rgba(148,163,184,0.22);
        border-radius: 24px;
        background: linear-gradient(135deg, rgba(30,41,59,0.95), rgba(49,46,129,0.65));
        margin-bottom: 32px;
    }
    .hero-icon { font-size: 48px; margin-bottom: 12px; }
    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(28px,5vw,44px);
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 16px;
    }
    .hero-subtitle {
        color: #cbd5e1;
        font-size: 16px;
        line-height: 1.8;
        max-width: 680px;
        margin: 0 auto;
    }
    .section-title { font-size: 25px; font-weight: 800; color: #ffffff; margin-bottom: 8px; }
    .section-description { color: #a5b4fc; font-size: 14px; margin-bottom: 24px; }
    .app-card {
        box-sizing: border-box;
        min-height: 260px;
        padding: 25px;
        border-radius: 20px;
        background: rgba(15,23,42,0.92);
        border: 1px solid rgba(148,163,184,0.22);
        margin-bottom: 15px;
    }
    .drawing-card { border-top: 4px solid #8b5cf6; }
    .mood-card { border-top: 4px solid #06b6d4; }
    .card-icon { font-size: 38px; margin-bottom: 14px; }
    .card-title { font-size: 22px; font-weight: 800; color: #ffffff; margin-bottom: 12px; }
    .card-description { font-size: 14px; line-height: 1.8; color: #cbd5e1; margin-bottom: 18px; }
    .feature-tag {
        display: inline-block; padding: 6px 10px; margin: 4px 3px 4px 0;
        border-radius: 20px; font-size: 11px; color: #e0e7ff;
        background: rgba(99,102,241,0.18); border: 1px solid rgba(129,140,248,0.28);
    }
    .launch-link {
        display:flex;align-items:center;justify-content:center;min-height:46px;padding:10px 14px;
        width:100%;box-sizing:border-box;border-radius:10px;font-weight:700;text-decoration:none;
        color:#fff;background:linear-gradient(90deg,#6366f1,#8b5cf6);
        border:1px solid rgba(255,255,255,.18);margin:6px 0 15px;
    }
    .launch-link:hover {color:#fff;border-color:#c4b5fd;filter:brightness(1.08)}
    .info-box {
        padding: 18px; border-radius: 14px; background: rgba(30,41,59,0.80);
        border: 1px solid rgba(148,163,184,0.20); color: #cbd5e1;
        font-size: 14px; line-height: 1.8; margin-bottom: 20px;
    }
    .footer {
        text-align: center; color: #94a3b8; font-size: 12px;
        padding: 25px 10px; margin-top: 35px;
        border-top: 1px solid rgba(148,163,184,0.18);
    }
    div.stButton > button, div.stLinkButton > a {
        width: 100%; box-sizing: border-box; border-radius: 10px;
        font-weight: 600; min-height: 44px; transition: 0.2s ease;
        justify-content: center;
    }
    div.stLinkButton > a {
        background: linear-gradient(90deg, #6366f1, #8b5cf6);
        border: 1px solid rgba(255,255,255,0.18); color: #ffffff;
    }
    div.stLinkButton > a:hover { border-color: #c4b5fd; color: #ffffff; }
    div.stButton > button:hover { border-color: #818cf8; color: #c4b5fd; }
    #MainMenu, footer { visibility: hidden; }
    </style>
    """,
    unsafe_allow_html=True,
)

# =====================================================
# SIDEBAR — STAYS VISIBLE WHEN SWITCHING PROJECTS
# =====================================================
with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center;padding:20px 5px;">
            <div style="font-size:44px;">🌌</div>
            <div style="font-family:Orbitron,sans-serif;font-size:21px;font-weight:800;color:#ffffff;">CREATIVE</div>
            <div style="font-size:12px;color:#a5b4fc;letter-spacing:4px;">UNIVERSE</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("---")
    st.caption("NAVIGATION")
    if st.button("🏠 Home", key="nav_home", use_container_width=True):
        navigate_to("Home")
        st.rerun()
    if st.button("🎨 AI Drawing Studio", key="nav_drawing", use_container_width=True):
        navigate_to("AI Drawing Studio")
        st.rerun()
    if st.button("✨ MoodSpark", key="nav_moodspark", use_container_width=True):
        navigate_to("MoodSpark")
        st.rerun()
    st.markdown("---")
    st.markdown("### 💡 Explore")
    st.caption("Discover creativity, express yourself, and explore new ideas.")
    st.markdown("---")
    st.caption("Dashboard collaboration: Purnima & Kritika")

# =====================================================
# HOME PAGE
# =====================================================
if st.session_state.page == "Home":
    st.markdown(
        """
        <div class="hero">
            <div class="hero-icon">🌌</div>
            <div class="hero-title">Creative Universe</div>
            <div class="hero-subtitle">Your personal space to create, explore, and express. Discover creative tools designed to turn your imagination into something meaningful.</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="section-title">Explore Your Creative Space</div>', unsafe_allow_html=True)
    st.markdown('<div class="section-description">Open AI Drawing Studio in its own tab, or explore MoodSpark right here. Both projects keep their own code and identity.</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")
    with col1:
        st.markdown(
            """
            <div class="app-card drawing-card">
                <div class="card-icon">🎨</div>
                <div class="card-title">AI Drawing Studio</div>
                <div class="card-description">Bring your imagination to life with drawing challenges, digital art, and AI-powered creative feedback.</div>
                <span class="feature-tag">AI Creativity</span><span class="feature-tag">Digital Art</span><span class="feature-tag">Visual Ideas</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<a class="launch-link" href="{DRAWING_URL}" target="_blank" rel="noopener noreferrer">🎨 Open AI Drawing Studio in a new tab ↗</a>',
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="app-card mood-card">
                <div class="card-icon">✨</div>
                <div class="card-title">MoodSpark</div>
                <div class="card-description">Explore mood-focused experience, inspiration, and positive moments.</div>
                <span class="feature-tag">Mood &amp; Inspiration</span><span class="feature-tag">Self-Expression</span><span class="feature-tag">Positive Vibes</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if st.button("✨ Open MoodSpark inside dashboard", key="home_explore_moodspark", use_container_width=True):
            navigate_to("MoodSpark")
            st.rerun()
        st.link_button("Open MoodSpark directly ↗", MOODSPARK_URL, use_container_width=True)

    st.markdown(
        '<div class="footer">🌌 Creative Universe · Dashboard collaboration: Purnima Kushwaha &amp; Kritika<br><br>AI Drawing Studio by Purnima · MoodSpark by Kritika</div>',
        unsafe_allow_html=True,
    )

# =====================================================
# EMBEDDED PROJECT PAGES
# =====================================================
elif st.session_state.page == "AI Drawing Studio":
    st.markdown(
        '<div class="hero"><div class="hero-icon">🎨</div><div class="hero-title">AI Drawing Studio</div><div class="hero-subtitle">Your personal drawing space opens in a separate tab, so you can return here any time.</div></div>',
        unsafe_allow_html=True,
    )
    st.markdown(f'<a class="launch-link" href="{DRAWING_URL}" target="_blank" rel="noopener noreferrer">🎨 Launch AI Drawing Studio ↗</a>', unsafe_allow_html=True)
    st.info("If you open the studio in another tab, this dashboard stays available in its original tab.")

elif st.session_state.page == "MoodSpark":
    st.markdown(
        '<div class="hero"><div class="hero-icon">✨</div><div class="hero-title">MoodSpark</div><div class="hero-subtitle">Explore Kritika’s project from the Creative Universe dashboard.</div></div>',
        unsafe_allow_html=True,
    )
    show_embedded_app(MOODSPARK_URL, "MoodSpark")
