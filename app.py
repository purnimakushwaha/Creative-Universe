import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# APPLICATION URLS
# ==========================================

DRAWING_URL = "https://ai-drawing-studio.streamlit.app/"
MOODSPARK_URL = "https://moodspark-pe81.onrender.com/"

# ==========================================
# SESSION STATE
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "Home"


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #100c28,
        #211746,
        #102b43
    );
    color: white;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: #15112b;
}

[data-testid="stSidebar"] * {
    color: white;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: white !important;
}

p {
    color: #d8d5ed;
}

.hero {
    text-align: center;
    padding: 45px 10px 35px 10px;
}

.hero-title {
    font-size: 48px;
    font-weight: 800;
    line-height: 1.3;
}

.hero-subtitle {
    color: #d8d5ed;
    font-size: 18px;
    line-height: 1.8;
    max-width: 750px;
    margin: 15px auto;
}

.badge {
    display: inline-block;
    background: rgba(180, 150, 255, 0.12);
    border: 1px solid rgba(180, 150, 255, 0.4);
    border-radius: 30px;
    padding: 8px 18px;
    color: #d9c8ff;
    font-size: 13px;
    letter-spacing: 1px;
}

.app-card {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(210, 195, 255, 0.25);
    border-radius: 22px;
    padding: 28px 22px;
    text-align: center;
    min-height: 280px;
    margin-bottom: 15px;
}

.app-icon {
    font-size: 52px;
}

.app-title {
    color: white;
    font-size: 25px;
    font-weight: 750;
    margin: 12px 0;
}

.app-description {
    color: #d8d5ed;
    line-height: 1.8;
    font-size: 15px;
}

.section-heading {
    text-align: center;
    font-size: 32px;
    font-weight: 750;
    margin-top: 25px;
    margin-bottom: 10px;
}

.section-subtitle {
    text-align: center;
    color: #c6c1df;
    margin-bottom: 28px;
}

.info-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(210, 195, 255, 0.2);
    border-radius: 18px;
    padding: 24px;
    margin: 15px 0;
}

.info-title {
    color: #cbbaff;
    font-size: 21px;
    font-weight: 700;
    margin-bottom: 10px;
}

.info-description {
    color: #d8d5ed;
    line-height: 1.8;
}

.step-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(210, 195, 255, 0.18);
    border-radius: 18px;
    padding: 22px 14px;
    text-align: center;
    min-height: 165px;
}

.step-icon {
    font-size: 35px;
}

.step-title {
    color: white;
    font-size: 19px;
    font-weight: 700;
    margin: 10px 0;
}

.step-description {
    color: #d0cbe4;
    font-size: 14px;
    line-height: 1.7;
}

.footer {
    text-align: center;
    color: #aaa5c7;
    padding: 30px 10px 10px 10px;
    margin-top: 35px;
    border-top: 1px solid rgba(255, 255, 255, 0.15);
    line-height: 1.9;
}

.stButton > button {
    border-radius: 12px;
    min-height: 45px;
    border: 1px solid #8e7bdb;
    background: linear-gradient(90deg, #6746c3, #4269c7);
    color: white;
    font-weight: 650;
}

.stButton > button:hover {
    border-color: white;
    color: white;
}

.stLinkButton > a {
    border-radius: 12px;
    border: 1px solid #a994ff;
    background: linear-gradient(90deg, #7957e8, #527ce8);
    color: white !important;
    font-weight: 700;
}

iframe {
    border-radius: 12px;
}

@media (max-width: 768px) {
    .hero-title {
        font-size: 35px;
    }

    .hero-subtitle {
        font-size: 16px;
    }

    .section-heading {
        font-size: 27px;
    }

    .app-card {
        min-height: auto;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

with st.sidebar:
    st.title("🌌 Creative Universe")
    st.caption("Your creative space")

    st.divider()

    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

    if st.button("🎨 AI Drawing Studio", use_container_width=True):
        st.session_state.page = "Drawing"
        st.rerun()

    if st.button("🌈 MoodSpark", use_container_width=True):
        st.session_state.page = "MoodSpark"
        st.rerun()

    st.divider()

    st.caption("Create • Explore • Discover")


# ==========================================
# HOME PAGE
# ==========================================

if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="badge">✦ CREATE · EXPLORE · DISCOVER ✦</div>

        <div class="hero-title">
            Welcome to<br>
            <span style="color:#bdaaff;">Creative Universe 🌌</span>
        </div>

        <div class="hero-subtitle">
            A universe where imagination meets creativity.
            Explore art, discover your emotions, and give your
            ideas a place to grow.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">✨ Explore Our Universe</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">Choose an experience to get started.</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="app-card">
            <div class="app-icon">🎨</div>
            <div class="app-title">AI Drawing Studio</div>
            <div class="app-description">
                Explore your imagination and discover
                your artistic side. Turn your ideas into
                creative experiences.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🎨 Open AI Drawing Studio",
            use_container_width=True,
            key="home_drawing"
        ):
            st.session_state.page = "Drawing"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="app-card">
            <div class="app-icon">🌈</div>
            <div class="app-title">MoodSpark</div>
            <div class="app-description">
                Explore your mood, reflect on your feelings,
                and make space for positivity in your day.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🌈 Open MoodSpark",
            use_container_width=True,
            key="home_moodspark"
        ):
            st.session_state.page = "MoodSpark"
            st.rerun()

    st.markdown("---")

    st.markdown(
        '<div class="section-heading">💫 About Our Universe</div>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="info-card">
        <div class="info-title">🌠 Two experiences, one destination</div>
        <div class="info-description">
            Creative Universe connects two projects in one dashboard.
            AI Drawing Studio offers an artistic experience, while
            MoodSpark provides a space for mood reflection.
            <br><br>
            Choose either experience from the Home page or sidebar.
            You can return here whenever you want.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-heading">🚀 Get Started</div>',
        unsafe_allow_html=True
    )

    step1, step2, step3 = st.columns(3, gap="medium")

    with step1:
        st.markdown("""
        <div class="step-card">
            <div class="step-icon">🌌</div>
            <div class="step-title">Explore</div>
            <div class="step-description">
                Choose an application.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with step2:
        st.markdown("""
        <div class="step-card">
            <div class="step-icon">🎨</div>
            <div class="step-title">Create</div>
            <div class="step-description">
                Explore your creativity.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with step3:
        st.markdown("""
        <div class="step-card">
            <div class="step-icon">💜</div>
            <div class="step-title">Discover</div>
            <div class="step-description">
                Enjoy your own creative journey.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        🌌 ✨ 🎨 🌈<br>
        <b>Creative Universe</b><br>
        Dashboard collaboration: Purnima Kushwaha &amp; Kritika<br>
        AI Drawing Studio: Purnima Kushwaha<br>
        MoodSpark: Kritika<br><br>
        Keep imagining. Keep creating. ✨
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# AI DRAWING STUDIO PAGE
# ==========================================

elif st.session_state.page == "Drawing":

    if st.button("← Back to Home", key="drawing_back"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🎨 AI Drawing Studio")

    st.write(
        "Welcome to AI Drawing Studio. "
        "If the embedded application does not load, use the button below."
    )

    st.link_button(
        "↗ Open AI Drawing Studio Directly",
        DRAWING_URL,
        use_container_width=True
    )

    st.divider()

    try:
        st.components.v1.iframe(
            DRAWING_URL,
            height=850,
            scrolling=True
        )
    except Exception:
        st.warning(
            "The Drawing Studio could not be embedded. "
            "Please use the direct-open button above."
        )

    st.caption(
        "If the embedded page remains blank or displays a browser error, "
        "the hosted app may not allow iframe embedding."
    )


# ==========================================
# MOODSPARK PAGE
# ==========================================

elif st.session_state.page == "MoodSpark":

    if st.button("← Back to Home", key="moodspark_back"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🌈 MoodSpark")

    st.write(
        "Welcome to MoodSpark. Explore the application below."
    )

    st.link_button(
        "↗ Open MoodSpark Directly",
        MOODSPARK_URL,
        use_container_width=True
    )

    st.divider()

    try:
        st.components.v1.iframe(
            MOODSPARK_URL,
            height=850,
            scrolling=True
        )
    except Exception:
        st.warning(
            "MoodSpark could not be embedded. "
            "Please use the direct-open button above."
        )

    st.caption(
        "If the embedded page remains blank, "
        "the hosted app may not allow iframe embedding."
    )
