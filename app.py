import streamlit as st

st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide"
)

DRAWING_URL = "https://ai-drawing-studio.streamlit.app/"
MOODSPARK_URL = "https://moodspark-pe81.onrender.com/"

# Initialize navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Styling
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #100c28, #211746, #102b43);
    color: white;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

h1, h2, h3, p {
    color: white;
}

.hero {
    text-align: center;
    padding: 35px 10px;
}

.hero-title {
    font-size: 48px;
    font-weight: bold;
}

.hero-text {
    color: #d8d5ed;
    font-size: 18px;
    line-height: 1.7;
}

.app-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.2);
    border-radius: 20px;
    padding: 25px;
    text-align: center;
    min-height: 220px;
}

.app-icon {
    font-size: 48px;
}

.app-description {
    color: #d8d5ed;
    line-height: 1.7;
}

iframe {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# Navigation
st.sidebar.title("🌌 Creative Universe")
st.sidebar.caption("Explore your creative space")

if st.sidebar.button("🏠 Home", use_container_width=True):
    st.session_state.page = "Home"

if st.sidebar.button("🎨 AI Drawing Studio", use_container_width=True):
    st.session_state.page = "Drawing"

if st.sidebar.button("🌈 MoodSpark", use_container_width=True):
    st.session_state.page = "MoodSpark"


# Home page
if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="hero-title">🌌 Creative Universe</div>
        <div class="hero-text">
            A place where creativity meets imagination.<br>
            Choose an application to begin your journey.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.markdown("""
        <div class="app-card">
            <div class="app-icon">🎨</div>
            <h2>AI Drawing Studio</h2>
            <div class="app-description">
                Explore your imagination and create
                artistic experiences.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🎨 Open AI Drawing Studio",
            use_container_width=True,
            key="open_drawing"
        ):
            st.session_state.page = "Drawing"
            st.rerun()

    with col2:
        st.markdown("""
        <div class="app-card">
            <div class="app-icon">🌈</div>
            <h2>MoodSpark</h2>
            <div class="app-description">
                Explore your mood and take a moment
                for reflection and self-discovery.
            </div>
        </div>
        """, unsafe_allow_html=True)

        if st.button(
            "🌈 Open MoodSpark",
            use_container_width=True,
            key="open_moodspark"
        ):
            st.session_state.page = "MoodSpark"
            st.rerun()


# AI Drawing Studio page
elif st.session_state.page == "Drawing":

    if st.button("← Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🎨 AI Drawing Studio")
    st.caption("Your creative space")

    st.info(
        "If the application appears below, you can use it here. "
        "If it does not load, the website may block iframe embedding."
    )

    st.components.v1.iframe(
        DRAWING_URL,
        height=800,
        scrolling=True
    )


# MoodSpark page
elif st.session_state.page == "MoodSpark":

    if st.button("← Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    st.title("🌈 MoodSpark")
    st.caption("Your space for mood exploration")

    st.info(
        "If the application appears below, you can use it here. "
        "If it does not load, the website may block iframe embedding."
    )

    st.components.v1.iframe(
        MOODSPARK_URL,
        height=800,
        scrolling=True
    )
