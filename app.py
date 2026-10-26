import streamlit as st
import streamlit.components.v1 as components

# -----------------------------------
# PAGE CONFIGURATION
# -----------------------------------
st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------------
# APP URLS
# -----------------------------------
DRAWING_URL = "https://ai-drawing-studio.streamlit.app/"
MOODSPARK_URL = "https://moodspark-pe81.onrender.com/"

# -----------------------------------
# SESSION STATE
# -----------------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"


def go_to(page):
    st.session_state.page = page


# -----------------------------------
# CUSTOM CSS
# -----------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap');

    .stApp {
        background:
            linear-gradient(
                rgba(7, 10, 30, 0.88),
                rgba(13, 10, 40, 0.91)
            ),
            url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=2000&q=85");

        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #ffffff;
        font-family: 'Poppins', sans-serif;
    }

    [data-testid="stSidebar"] {
        background: rgba(9, 12, 35, 0.96);
        border-right: 1px solid rgba(160, 130, 255, 0.35);
    }

    [data-testid="stSidebar"] * {
        color: #ffffff;
    }

    .hero-title {
        font-family: 'Orbitron', sans-serif;
        font-size: clamp(35px, 5vw, 65px);
        font-weight: 800;
        text-align: center;
        line-height: 1.25;
        margin-top: 15px;
        margin-bottom: 10px;
        color: #ffffff;
        text-shadow: 0 0 25px rgba(154, 105, 255, 0.8);
    }

    .hero-subtitle {
        text-align: center;
        color: #d5d8ff;
        font-size: 17px;
        margin-bottom: 35px;
    }

    .section-title {
        font-family: 'Orbitron', sans-serif;
        text-align: center;
        font-size: 26px;
        color: #e3d8ff;
        margin-top: 30px;
        margin-bottom: 20px;
    }

    .app-description {
        color: #e0e3ff;
        font-size: 15px;
        line-height: 1.7;
        min-height: 70px;
    }

    .credit-box {
        background: rgba(255, 255, 255, 0.06);
        border: 1px solid rgba(180, 155, 255, 0.3);
        border-radius: 16px;
        padding: 20px;
        text-align: center;
        margin-top: 25px;
    }

    .credit-box h3 {
        color: #d8c7ff;
        font-family: 'Orbitron', sans-serif;
    }

    .footer-text {
        text-align: center;
        color: #bfc5e8;
        font-size: 13px;
        padding-top: 35px;
        padding-bottom: 10px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        border: 1px solid rgba(193, 166, 255, 0.65);
        background: linear-gradient(135deg, #7455df, #4933a5);
        color: white;
        font-weight: 600;
        padding: 0.65rem 1rem;
        transition: 0.25s ease;
    }

    div.stButton > button:hover {
        border-color: #ffffff;
        background: linear-gradient(135deg, #9677ff, #6048d5);
        color: white;
        box-shadow: 0 0 18px rgba(145, 115, 255, 0.45);
    }

    .small-note {
        color: #c8cbed;
        font-size: 13px;
        line-height: 1.6;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# -----------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------
with st.sidebar:
    st.markdown(
        """
        <div style="text-align:center; padding:15px 0 20px;">
            <div style="font-size:48px;">🌌</div>
            <h2 style="
                font-family:Orbitron,sans-serif;
                color:#d9caff;
                margin-bottom:0;">
                CREATIVE
            </h2>
            <h2 style="
                font-family:Orbitron,sans-serif;
                color:#a99aff;
                margin-top:0;">
                UNIVERSE
            </h2>
            <p style="color:#c7c9ed; font-size:13px;">
                Explore your imagination
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")
    st.markdown("### 🧭 Navigation")

    if st.button("🏠 Home", key="nav_home"):
        go_to("Home")

    if st.button("🎨 AI Drawing Studio", key="nav_drawing"):
        go_to("AI Drawing Studio")

    if st.button("✨ MoodSpark", key="nav_moodspark"):
        go_to("MoodSpark")

    st.markdown("---")

    st.markdown("### 👩‍💻 Project Team")
    st.markdown("**Purnima Kushwaha**")
    st.caption("AI Drawing Studio")

    st.markdown("**Kritika**")
    st.caption("MoodSpark")

    st.markdown("---")
    st.markdown(
        """
        <p class="small-note">
        A shared space for creativity, imagination,
        and exploring new ideas.
        </p>
        """,
        unsafe_allow_html=True
    )


# -----------------------------------
# HOME PAGE
# -----------------------------------
if st.session_state.page == "Home":

    st.markdown(
        """
        <h1 class="hero-title">
            CREATIVE UNIVERSE
        </h1>

        <p class="hero-subtitle">
            ✦ Where imagination meets innovation ✦
            <br>
            Discover. Create. Express.
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<h2 class="section-title">🚀 Explore Our Universe</h2>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    # AI DRAWING STUDIO CARD
    with col1:
        st.image(
            "https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=1000&q=85",
            use_container_width=True
        )

        st.markdown("### 🎨 AI Drawing Studio")

        st.markdown(
            """
            <p class="app-description">
            Turn your imagination into art. Explore your creative
            side and bring your ideas to life with AI-powered drawing.
            </p>
            """,
            unsafe_allow_html=True
        )

        if st.button("🎨 Enter Drawing Studio", key="home_drawing"):
            go_to("AI Drawing Studio")
            st.rerun()

        st.link_button(
            "↗ Open Drawing Studio Directly",
            DRAWING_URL,
            use_container_width=True
        )

    # MOODSPARK CARD
    with col2:
        st.image(
            "https://images.unsplash.com/photo-1470252649378-9c29740c9fa8?auto=format&fit=crop&w=1000&q=85",
            use_container_width=True
        )

        st.markdown("### ✨ MoodSpark")

        st.markdown(
            """
            <p class="app-description">
            Explore a space designed around moods and self-expression.
            Take a moment, discover your feelings, and explore MoodSpark.
            </p>
            """,
            unsafe_allow_html=True
        )

        if st.button("✨ Enter MoodSpark", key="home_moodspark"):
            go_to("MoodSpark")
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

    st.markdown(
        """
        <div class="credit-box">
            <h3>Two Ideas. One Universe.</h3>
            <p>
            Creative Universe brings two independent applications
            together in one dashboard, making it easier to discover
            and explore both projects.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # CREDITS
    st.markdown(
        '<h2 class="section-title">💜 Meet the Creators</h2>',
        unsafe_allow_html=True
    )

    credit1, credit2 = st.columns(2, gap="large")

    with credit1:
        st.markdown(
            """
            <div class="credit-box">
                <div style="font-size:35px;">👩‍💻</div>
                <h3>Purnima Kushwaha</h3>
                <p>Creator of AI Drawing Studio</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with credit2:
        st.markdown(
            """
            <div class="credit-box">
                <div style="font-size:35px;">👩‍💻</div>
                <h3>Kritika</h3>
                <p>Creator of MoodSpark</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="footer-text">
            🌌 CREATIVE UNIVERSE
            <br>
            Made with creativity, curiosity, and code.
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------------
# AI DRAWING STUDIO PAGE
# -----------------------------------
elif st.session_state.page == "AI Drawing Studio":

    st.markdown(
        """
        <h1 class="hero-title">🎨 AI Drawing Studio</h1>
        <p class="hero-subtitle">
            Turn your imagination into art
        </p>
        """,
        unsafe_allow_html=True
    )

    if st.button("⬅️ Back to Home", key="drawing_home"):
        go_to("Home")
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

    st.markdown(
        """
        <div class="footer-text">
            AI Drawing Studio · Created by Purnima Kushwaha
        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------------
# MOODSPARK PAGE
# -----------------------------------
elif st.session_state.page == "MoodSpark":

    st.markdown(
        """
        <h1 class="hero-title">✨ MoodSpark</h1>
        <p class="hero-subtitle">
            Explore moods. Discover moments.
        </p>
        """,
        unsafe_allow_html=True
    )

    if st.button("⬅️ Back to Home", key="moodspark_home"):
        go_to("Home")
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

    st.markdown(
        """
        <div class="footer-text">
            MoodSpark · Created by Kritika
        </div>
        """,
        unsafe_allow_html=True
    )
