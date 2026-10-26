import streamlit as st

# ==================================================
# PAGE CONFIGURATION
# ==================================================

st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================================================
# APPLICATION URLS
# ==================================================

DRAWING_URL = "https://ai-drawing-studio.streamlit.app/"
MOODSPARK_URL = "https://moodspark-pe81.onrender.com/"

# ==================================================
# SESSION STATE
# ==================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"


def navigate_to(page_name):
    st.session_state.page = page_name


# ==================================================
# CUSTOM CSS
# ==================================================

st.markdown(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Orbitron:wght@500;600;700;800&display=swap'
    );

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                #172554 0%,
                transparent 35%
            ),
            radial-gradient(
                circle at 90% 20%,
                #312e81 0%,
                transparent 30%
            ),
            linear-gradient(
                135deg,
                #080d1b,
                #10172a 55%,
                #080d1b
            );
        color: #f8fafc;
    }

    [data-testid="stSidebar"] {
        background: #0b1120;
        border-right: 1px solid rgba(148, 163, 184, 0.15);
    }

    [data-testid="stSidebar"] * {
        color: #e2e8f0;
    }

    .hero {
        padding: 38px 20px;
        text-align: center;
        border: 1px solid rgba(148, 163, 184, 0.20);
        border-radius: 24px;
        background: linear-gradient(
            135deg,
            rgba(30, 41, 59, 0.90),
            rgba(49, 46, 129, 0.50)
        );
        margin-bottom: 30px;
    }

    .hero-icon {
        font-size: 48px;
        margin-bottom: 10px;
    }

    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(28px, 5vw, 46px);
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 12px;
    }

    .hero-subtitle {
        color: #cbd5e1;
        font-size: 16px;
        line-height: 1.8;
        max-width: 680px;
        margin: 0 auto;
    }

    .section-title {
        font-size: 25px;
        font-weight: 800;
        color: #f8fafc;
        margin: 20px 0 8px 0;
    }

    .section-description {
        color: #94a3b8;
        font-size: 14px;
        margin-bottom: 22px;
    }

    .app-card {
        min-height: 255px;
        padding: 24px;
        border-radius: 20px;
        background: rgba(15, 23, 42, 0.85);
        border: 1px solid rgba(148, 163, 184, 0.20);
        margin-bottom: 12px;
    }

    .drawing-card {
        border-top: 3px solid #8b5cf6;
    }

    .mood-card {
        border-top: 3px solid #06b6d4;
    }

    .card-icon {
        font-size: 38px;
        margin-bottom: 12px;
    }

    .card-title {
        font-size: 22px;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 12px;
    }

    .card-description {
        font-size: 14px;
        line-height: 1.8;
        color: #cbd5e1;
        min-height: 80px;
    }

    .feature-tag {
        display: inline-block;
        padding: 5px 10px;
        margin: 5px 4px 0 0;
        border-radius: 20px;
        font-size: 11px;
        color: #e2e8f0;
        background: rgba(99, 102, 241, 0.18);
        border: 1px solid rgba(129, 140, 248, 0.25);
    }

    .info-box {
        padding: 16px;
        border-radius: 12px;
        background: rgba(30, 41, 59, 0.80);
        border: 1px solid rgba(148, 163, 184, 0.15);
        color: #cbd5e1;
        font-size: 14px;
        line-height: 1.8;
        margin-bottom: 20px;
    }

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        padding: 25px 10px 10px 10px;
        margin-top: 30px;
        border-top: 1px solid rgba(148, 163, 184, 0.15);
    }

    div.stButton > button,
    div.stLinkButton > a {
        border-radius: 10px;
        font-weight: 600;
        min-height: 42px;
        transition: 0.2s ease;
    }

    div.stButton > button:hover,
    div.stLinkButton > a:hover {
        border-color: #818cf8;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ==================================================
# SIDEBAR NAVIGATION
# ==================================================

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding:18px 5px;">
            <div style="font-size:42px;">🌌</div>

            <div style="
                font-family:Orbitron,sans-serif;
                font-size:20px;
                font-weight:800;
                color:white;
            ">
                CREATIVE
            </div>

            <div style="
                font-size:12px;
                color:#94a3b8;
                letter-spacing:3px;
            ">
                UNIVERSE
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.caption("NAVIGATION")

    if st.button(
        "🏠 Home",
        use_container_width=True,
        key="nav_home"
    ):
        navigate_to("Home")
        st.rerun()

    if st.button(
        "🎨 AI Drawing Studio",
        use_container_width=True,
        key="nav_drawing"
    ):
        navigate_to("AI Drawing Studio")
        st.rerun()

    if st.button(
        "✨ MoodSpark",
        use_container_width=True,
        key="nav_moodspark"
    ):
        navigate_to("MoodSpark")
        st.rerun()

    st.markdown("---")

    st.markdown("### 💡 Explore")

    st.caption(
        "Discover creativity, express yourself, "
        "and explore new ideas."
    )

    st.markdown("---")

    st.caption("Built with Python and Streamlit")


# ==================================================
# HOME PAGE
# ==================================================

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-icon">🌌</div>

            <div class="hero-title">
                Creative Universe
            </div>

            <div class="hero-subtitle">
                Your personal space to create, explore, and express.
                Discover creative tools designed to turn your
                imagination into something meaningful.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">'
        'Explore Your Creative Space'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-description">'
        'Choose a tool and start exploring.'
        '</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    # ---------------- DRAWING STUDIO CARD ----------------

    with col1:

        st.markdown(
            """
            <div class="app-card drawing-card">

                <div class="card-icon">🎨</div>

                <div class="card-title">
                    AI Drawing Studio
                </div>

                <div class="card-description">
                    Bring your imagination to life. Explore
                    AI-powered drawing and transform your ideas
                    into visual concepts.
                </div>

                <span class="feature-tag">AI Creativity</span>
                <span class="feature-tag">Digital Art</span>
                <span class="feature-tag">Visual Ideas</span>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "🎨 Explore Drawing Studio",
            key="home_drawing",
            use_container_width=True
        ):
            navigate_to("AI Drawing Studio")
            st.rerun()

        st.link_button(
            "↗ Launch Drawing Studio",
            DRAWING_URL,
            use_container_width=True
        )

    # ---------------- MOODSPARK CARD ----------------

    with col2:

        st.markdown(
            """
            <div class="app-card mood-card">

                <div class="card-icon">✨</div>

                <div class="card-title">
                    MoodSpark
                </div>

                <div class="card-description">
                    Discover a space for moods, inspiration,
                    and positive moments. Take a break and
                    explore something uplifting.
                </div>

                <span class="feature-tag">Mood & Inspiration</span>
                <span class="feature-tag">Self-Expression</span>
                <span class="feature-tag">Positive Vibes</span>

            </div>
            """,
            unsafe_allow_html=True
        )

        if st.button(
            "✨ Explore MoodSpark",
            key="home_moodspark",
            use_container_width=True
        ):
            navigate_to("MoodSpark")
            st.rerun()

        st.link_button(
            "↗ Launch MoodSpark",
            MOODSPARK_URL,
            use_container_width=True
        )

    # ---------------- FOOTER ----------------

    st.markdown(
        """
        <div class="footer">
            🌌 Creative Universe · Built with Python and Streamlit
            <br><br>
            Create something wonderful today.
        </div>
        """,
        unsafe_allow_html=True
    )


# ==================================================
# AI DRAWING STUDIO PAGE
# ==================================================

elif st.session_state.page == "AI Drawing Studio":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-icon">🎨</div>

            <div class="hero-title">
                AI Drawing Studio
            </div>

            <div class="hero-subtitle">
                Bring your imagination to life with
                AI-powered creativity.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
            <strong>Your creative workspace is ready!</strong>
            <br>
            Launch AI Drawing Studio directly to avoid
            embedded-browser redirect and session issues.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "🚀 Launch AI Drawing Studio",
        DRAWING_URL,
        use_container_width=True
    )

    st.caption(
        "The Drawing Studio opens directly in a new browser tab."
    )

    if st.button(
        "🏠 Back to Home",
        use_container_width=True,
        key="drawing_back"
    ):
        navigate_to("Home")
        st.rerun()


# ==================================================
# MOODSPARK PAGE
# ==================================================

elif st.session_state.page == "MoodSpark":

    st.markdown(
        """
        <div class="hero">
            <div class="hero-icon">✨</div>

            <div class="hero-title">
                MoodSpark
            </div>

            <div class="hero-subtitle">
                Explore inspiration, discover your mood,
                and enjoy a creative space designed for you.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="info-box">
            <strong>Welcome to MoodSpark!</strong>
            <br>
            Open the application directly to explore its features.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "✨ Launch MoodSpark",
        MOODSPARK_URL,
        use_container_width=True
    )

    st.caption(
        "MoodSpark opens directly in a new browser tab."
    )

    if st.button(
        "🏠 Back to Home",
        use_container_width=True,
        key="moodspark_back"
    ):
        navigate_to("Home")
        st.rerun()
