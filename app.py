import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# CREATIVE UNIVERSE - MAIN DASHBOARD
# ==========================================

st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App URLs
DRAWING_URL = "https://ai-drawing-studio.streamlit.app/"
MOODSPARK_URL = "https://moodspark-pe81.onrender.com/"

# Session state
if "page" not in st.session_state:
    st.session_state.page = "Home"


def navigate_to(page):
    st.session_state.page = page


# ==========================================
# ATTRACTIVE GALAXY BACKGROUND AND CSS
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(ellipse at 15% 20%,
            rgba(125, 60, 255, 0.35), transparent 35%),
        radial-gradient(ellipse at 85% 30%,
            rgba(0, 200, 255, 0.25), transparent 35%),
        radial-gradient(ellipse at 50% 90%,
            rgba(255, 0, 170, 0.22), transparent 40%),
        linear-gradient(135deg,
            #070719 0%, #11103b 35%,
            #1b1045 65%, #08091e 100%);
    background-attachment: fixed;
    color: white;
    font-family: 'Poppins', sans-serif;
}

/* Animated star background */
.stApp::before {
    content: "";
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
    background-image:
        radial-gradient(2px 2px at 20px 30px,
            white, transparent),
        radial-gradient(2px 2px at 100px 150px,
            #b8c7ff, transparent),
        radial-gradient(1px 1px at 200px 80px,
            white, transparent),
        radial-gradient(2px 2px at 300px 250px,
            #d5b8ff, transparent),
        radial-gradient(1px 1px at 400px 100px,
            white, transparent),
        radial-gradient(2px 2px at 500px 350px,
            #83eaff, transparent);
    background-size: 550px 400px;
    animation: starDrift 35s linear infinite;
    opacity: 0.65;
}

@keyframes starDrift {
    from { transform: translateY(0); }
    to { transform: translateY(-400px); }
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    background: transparent;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        rgba(16, 12, 48, 0.98),
        rgba(10, 15, 40, 0.98)
    );
    border-right: 1px solid rgba(157, 120, 255, 0.55);
    box-shadow: 5px 0 30px rgba(90, 50, 255, 0.15);
}

[data-testid="stSidebar"] * {
    color: #f4f0ff;
}

/* Main heading */
.hero-title {
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(34px, 5vw, 66px);
    font-weight: 800;
    text-align: center;
    letter-spacing: 2px;
    line-height: 1.3;
    background: linear-gradient(
        90deg,
        #ffffff,
        #c8a8ff,
        #77e8ff,
        #ffffff
    );
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    filter: drop-shadow(0 0 15px rgba(148, 90, 255, 0.75));
    margin-top: 25px;
    margin-bottom: 15px;
}

.hero-subtitle {
    text-align: center;
    color: #dcdcff;
    font-size: 17px;
    line-height: 1.9;
    letter-spacing: 1px;
    margin-bottom: 35px;
}

.section-title {
    font-family: 'Orbitron', sans-serif;
    text-align: center;
    font-size: 25px;
    color: #e3d8ff;
    margin: 35px 0 25px;
    text-shadow: 0 0 16px rgba(145, 100, 255, 0.55);
}

/* Description */
.app-description {
    color: #e0e3ff;
    font-size: 15px;
    line-height: 1.8;
    min-height: 70px;
}

/* Glass-effect cards */
.credit-box {
    background: linear-gradient(
        135deg,
        rgba(116, 75, 220, 0.22),
        rgba(0, 190, 255, 0.12)
    );
    border: 1px solid rgba(183, 155, 255, 0.45);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    box-shadow: 0 0 25px rgba(108, 66, 255, 0.15);
    transition: all 0.3s ease;
}

.credit-box:hover {
    border-color: #a997ff;
    box-shadow: 0 0 30px rgba(137, 100, 255, 0.35);
    transform: translateY(-4px);
}

.credit-box h3 {
    font-family: 'Orbitron', sans-serif;
    color: #d8c7ff;
}

/* Photos */
[data-testid="stImage"] img {
    border-radius: 18px;
    border: 1px solid rgba(176, 146, 255, 0.45);
    box-shadow: 0 0 22px rgba(113, 75, 255, 0.2);
    transition: all 0.35s ease;
}

[data-testid="stImage"] img:hover {
    box-shadow: 0 0 30px rgba(95, 205, 255, 0.4);
}

/* Buttons */
div.stButton > button,
div.stLinkButton > a {
    width: 100%;
    border-radius: 12px;
    border: 1px solid rgba(198, 171, 255, 0.65);
    background: linear-gradient(
        115deg,
        #7652e8,
        #5538ba,
        #2878ce
    );
    color: white;
    font-weight: 600;
    padding: 0.7rem 1rem;
    transition: all 0.25s ease;
}

div.stButton > button:hover,
div.stLinkButton > a:hover {
    border-color: white;
    box-shadow: 0 0 22px rgba(126, 100, 255, 0.55);
    transform: translateY(-2px);
    color: white;
}

/* Alerts */
[data-testid="stAlert"] {
    background: rgba(74, 58, 145, 0.23);
    border: 1px solid rgba(166, 145, 255, 0.4);
    border-radius: 14px;
}

/* Footer */
.footer-text {
    text-align: center;
    color: #c5c8ed;
    font-size: 13px;
    padding: 35px 0 15px;
    letter-spacing: 1px;
}

.small-note {
    color: #c8cbed;
    font-size: 13px;
    line-height: 1.7;
}

@media (prefers-reduced-motion: reduce) {
    .stApp::before {
        animation: none;
    }

    * {
        transition: none !important;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("""
    <div style="text-align:center; padding:15px 0 20px;">
        <div style="font-size:48px;">🌌</div>
        <h2 style="font-family:Orbitron,sans-serif;color:#d9caff;margin-bottom:0;">
            CREATIVE
        </h2>
        <h2 style="font-family:Orbitron,sans-serif;color:#a99aff;margin-top:0;">
            UNIVERSE
        </h2>
        <p style="color:#c7c9ed;font-size:13px;">
            Explore your imagination
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🧭 Navigation")

    if st.button("🏠 Home", key="nav_home",
                 use_container_width=True):
        navigate_to("Home")
        st.rerun()

    if st.button("🎨 AI Drawing Studio", key="nav_drawing",
                 use_container_width=True):
        navigate_to("AI Drawing Studio")
        st.rerun()

    if st.button("✨ MoodSpark", key="nav_moodspark",
                 use_container_width=True):
        navigate_to("MoodSpark")
        st.rerun()

    st.markdown("---")
    st.markdown("### 👩‍💻 Project Team")

    st.markdown("**Purnima Kushwaha**")
    st.caption("AI Drawing Studio")

    st.markdown("**Kritika**")
    st.caption("MoodSpark")

    st.markdown("---")

    st.markdown("""
    <p class="small-note">
    A shared space for creativity, imagination,
    and exploring new ideas.
    </p>
    """, unsafe_allow_html=True)


# ==========================================
# HOME PAGE
# ==========================================

if st.session_state.page == "Home":

    st.markdown("""
    <h1 class="hero-title">CREATIVE UNIVERSE</h1>

    <p class="hero-subtitle">
        ✦ Where imagination meets innovation ✦<br>
        Discover. Create. Express.
    </p>
    """, unsafe_allow_html=True)

    st.markdown(
        '<h2 class="section-title">🚀 Explore Our Universe</h2>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    # AI DRAWING STUDIO
    with col1:

        st.image(
            "https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=1000&q=85",
            use_container_width=True
        )

        st.markdown("### 🎨 AI Drawing Studio")

        st.markdown("""
        <p class="app-description">
        Turn your imagination into art. Explore your creative
        side and bring your ideas to life with AI-powered drawing.
        </p>
        """, unsafe_allow_html=True)

        if st.button(
            "🎨 Enter Drawing Studio",
            key="home_drawing",
            use_container_width=True
        ):
            navigate_to("AI Drawing Studio")
            st.rerun()

        st.link_button(
            "↗ Open Drawing Studio Directly",
            DRAWING_URL,
            use_container_width=True
        )

    # MOODSPARK
    with col2:

        st.image(
            "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?auto=format&fit=crop&w=1000&q=85",
            use_container_width=True
        )

        st.markdown("### ✨ MoodSpark")

        st.markdown("""
        <p class="app-description">
        Explore a space designed around moods and self-expression.
        Take a moment, discover your feelings, and explore MoodSpark.
        </p>
        """, unsafe_allow_html=True)

        if st.button(
            "✨ Enter MoodSpark",
            key="home_moodspark",
            use_container_width=True
        ):
            navigate_to("MoodSpark")
            st.rerun()

        st.link_button(
            "↗ Open MoodSpark Directly",
            MOODSPARK_URL,
            use_container_width=True
        )

    # ABOUT SECTION
    st.markdown("---")

    st.markdown(
        '<h2 class="section-title">🌠 About Creative Universe</h2>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="credit-box">
        <h3>Two Ideas. One Universe.</h3>
        <p>
        Creative Universe brings two independent applications together
        in one dashboard, making it easier to discover and explore
        both projects.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # CREATOR CREDITS
    st.markdown(
        '<h2 class="section-title">💜 Meet the Creators</h2>',
        unsafe_allow_html=True
    )

    credit1, credit2 = st.columns(2, gap="large")

    with credit1:
        st.markdown("""
        <div class="credit-box">
            <div style="font-size:35px;">👩‍💻</div>
            <h3>Purnima Kushwaha</h3>
            <p>Creator of AI Drawing Studio</p>
        </div>
        """, unsafe_allow_html=True)

    with credit2:
        st.markdown("""
        <div class="credit-box">
            <div style="font-size:35px;">👩‍💻</div>
            <h3>Kritika</h3>
            <p>Creator of MoodSpark</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer-text">
        🌌 CREATIVE UNIVERSE<br>
        Made with creativity, curiosity, and code.
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# AI DRAWING STUDIO PAGE
# ==========================================

elif st.session_state.page == "AI Drawing Studio":

    st.markdown("""
    <h1 class="hero-title">🎨 AI Drawing Studio</h1>
    <p class="hero-subtitle">
        Turn your imagination into art
    </p>
    """, unsafe_allow_html=True)

    if st.button(
        "⬅️ Back to Home",
        key="drawing_home",
        use_container_width=True
    ):
        navigate_to("Home")
        st.rerun()

    st.markdown("---")

    st.info(
        "If the embedded app does not load, use the direct-open button below."
    )

    st.link_button(
        "↗ Open AI Drawing Studio in a New Tab",
        DRAWING_URL,
        use_container_width=True
    )

    components.iframe(
        DRAWING_URL + "?embed=true",
        height=850,
        scrolling=True
    )

    st.markdown("""
    <div class="footer-text">
        AI Drawing Studio · Created by Purnima Kushwaha
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# MOODSPARK PAGE
# ==========================================

elif st.session_state.page == "MoodSpark":

    st.markdown("""
    <h1 class="hero-title">✨ MoodSpark</h1>
    <p class="hero-subtitle">
        Explore moods. Discover moments.
    </p>
    """, unsafe_allow_html=True)

    if st.button(
        "⬅️ Back to Home",
        key="moodspark_home",
        use_container_width=True
    ):
        navigate_to("Home")
        st.rerun()

    st.markdown("---")

    st.info(
        "If MoodSpark does not load inside the dashboard, open it directly."
    )

    st.link_button(
        "↗ Open MoodSpark in a New Tab",
        MOODSPARK_URL,
        use_container_width=True
    )

    components.iframe(
        MOODSPARK_URL,
        height=850,
        scrolling=True
    )

    st.markdown("""
    <div class="footer-text">
        MoodSpark · Created by Kritika
    </div>
    """, unsafe_allow_html=True)
