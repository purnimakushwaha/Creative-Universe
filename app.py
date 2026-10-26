import streamlit as st

# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================
# APP URLS
# =====================================

DRAWING_URL = "https://ai-drawing-studio.streamlit.app/?embed=true"
DRAWING_DIRECT_URL = "https://ai-drawing-studio.streamlit.app/"

MOODSPARK_URL = "https://moodspark-pe81.onrender.com/"

# =====================================
# NAVIGATION STATE
# =====================================

if "page" not in st.session_state:
    st.session_state.page = "Home"


def go_to(page):
    st.session_state.page = page


# =====================================
# CUSTOM CSS
# No HTML content is used for page sections.
# =====================================

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

.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: white !important;
}

p, .stMarkdown {
    color: #e0dcf3;
}

div.stButton > button {
    width: 100%;
    min-height: 45px;
    border-radius: 12px;
    border: 1px solid #a994ff;
    background: linear-gradient(90deg, #7957e8, #527ce8);
    color: white;
    font-weight: 650;
}

div.stButton > button:hover {
    border-color: white;
    color: white;
}

div.stLinkButton > a {
    border-radius: 12px;
    border: 1px solid #a994ff;
    background: linear-gradient(90deg, #7957e8, #527ce8);
    color: white !important;
    font-weight: 650;
}

.hero-box {
    padding: 35px 10px;
    text-align: center;
}

.app-box {
    padding: 25px;
    border: 1px solid rgba(210, 195, 255, 0.30);
    border-radius: 20px;
    background: rgba(255, 255, 255, 0.07);
    text-align: center;
    min-height: 245px;
}

.footer-box {
    padding: 25px 10px;
    margin-top: 35px;
    text-align: center;
    border-top: 1px solid rgba(255,255,255,0.15);
    color: #c5bfdf;
}

</style>
""", unsafe_allow_html=True)


# =====================================
# SIDEBAR
# =====================================

with st.sidebar:
    st.title("🌌 Creative Universe")
    st.caption("Create • Explore • Discover")

    st.divider()

    if st.button("🏠 Home", key="nav_home"):
        go_to("Home")
        st.rerun()

    if st.button("🎨 AI Drawing Studio", key="nav_drawing"):
        go_to("Drawing")
        st.rerun()

    if st.button("🌈 MoodSpark", key="nav_moodspark"):
        go_to("MoodSpark")
        st.rerun()


# =====================================
# HOME PAGE
# =====================================

if st.session_state.page == "Home":

    st.markdown(
        "<div class='hero-box'></div>",
        unsafe_allow_html=True
    )

    st.caption("✦ YOUR SPACE TO CREATE AND EXPLORE ✦")

    st.title("🌌 Creative Universe")

    st.markdown(
        "Welcome to a universe where imagination meets creativity. "
        "Explore art, discover your emotions, and give your ideas "
        "a place to grow."
    )

    st.divider()

    st.subheader("✨ Explore Our Universe")

    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            st.markdown("<h2>🎨</h2>", unsafe_allow_html=True)
            st.subheader("AI Drawing Studio")
            st.write(
                "Explore your imagination and artistic side. "
                "Turn your ideas into creative experiences."
            )

            if st.button(
                "Open AI Drawing Studio →",
                key="home_open_drawing"
            ):
                go_to("Drawing")
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("<h2>🌈</h2>", unsafe_allow_html=True)
            st.subheader("MoodSpark")
            st.write(
                "Explore your mood, reflect on your feelings, "
                "and make space for positivity."
            )

            if st.button(
                "Open MoodSpark →",
                key="home_open_moodspark"
            ):
                go_to("MoodSpark")
                st.rerun()

    st.divider()

    st.subheader("💫 About Creative Universe")

    st.write(
        "Creative Universe brings together two independent projects "
        "in one dashboard. AI Drawing Studio focuses on creativity, "
        "while MoodSpark offers a mood-related experience."
    )

    st.subheader("🚀 How to Get Started")

    step1, step2, step3 = st.columns(3)

    with step1:
        st.markdown("### 🌌 Explore")
        st.write("Choose an application.")

    with step2:
        st.markdown("### 🎨 Create")
        st.write("Explore your creative side.")

    with step3:
        st.markdown("### 💜 Discover")
        st.write("Enjoy your own journey.")

    st.markdown("---")

    st.markdown("### 👩‍💻 Project Credits")

    credit1, credit2 = st.columns(2)

    with credit1:
        st.info("🎨 AI Drawing Studio\n\nPurnima Kushwaha")

    with credit2:
        st.info("🌈 MoodSpark\n\nKritika")

    st.markdown(
        "Dashboard collaboration: Purnima Kushwaha & Kritika"
    )

    st.markdown("---")
    st.caption("🌌 Creative Universe | Keep imagining. Keep creating.")


# =====================================
# DRAWING STUDIO PAGE
# =====================================

elif st.session_state.page == "Drawing":

    if st.button("← Back to Home", key="drawing_back"):
        go_to("Home")
        st.rerun()

    st.title("🎨 AI Drawing Studio")

    st.write(
        "Welcome to AI Drawing Studio. "
        "The application is displayed below if embedding is supported."
    )

    st.link_button(
        "Open Drawing Studio Directly ↗",
        DRAWING_DIRECT_URL,
        use_container_width=True
    )

    st.divider()

    try:
        st.components.v1.iframe(
            DRAWING_URL,
            height=800,
            scrolling=True
        )

    except Exception:
        st.warning(
            "The embedded Drawing Studio could not be loaded. "
            "Please open it using the button above."
        )

    st.info(
        "If you see a redirect error or a blank area here, "
        "the deployed Drawing Studio may need a separate fix."
    )


# =====================================
# MOODSPARK PAGE
# =====================================

elif st.session_state.page == "MoodSpark":

    if st.button("← Back to Home", key="moodspark_back"):
        go_to("Home")
        st.rerun()

    st.title("🌈 MoodSpark")

    st.write(
        "Welcome to MoodSpark. You can try opening the application "
        "inside this page."
    )

    st.link_button(
        "Open MoodSpark Directly ↗",
        MOODSPARK_URL,
        use_container_width=True
    )

    st.divider()

    try:
        st.components.v1.iframe(
            MOODSPARK_URL,
            height=800,
            scrolling=True
        )

    except Exception:
        st.warning(
            "MoodSpark could not be embedded. "
            "Please use the direct-open button."
        )
