import streamlit as st
import streamlit.components.v1 as components

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# PROJECT INFORMATION
# --------------------------------------------------

PROJECTS = {
    "AI Drawing Studio": {
        "description": (
            "Turn your creative ideas into artwork. "
            "Explore digital creativity through AI-powered drawing."
        ),
        "url": "https://ai-drawing-studio.streamlit.app/",
        "creator": "Purnima Kushwaha",
        "icon": "🎨",
        "category": "AI & Creativity"
    },
    "MoodSpark": {
        "description": (
            "Explore moods and discover a more engaging "
            "way to interact with emotions and ideas."
        ),
        "url": "https://moodspark-pe81.onrender.com/",
        "creator": "Kritika",
        "icon": "✨",
        "category": "Mood & Wellbeing"
    }
}

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    /* Main application background */
    .stApp {
        background-color: #F5F7FB;
        color: #1E293B;
    }

    /* Main content width and spacing */
    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #172554;
    }

    section[data-testid="stSidebar"] * {
        color: #FFFFFF;
    }

    /* Main headings */
    h1, h2, h3 {
        color: #172554;
    }

    /* Buttons */
    .stButton > button {
        width: 100%;
        min-height: 44px;
        border-radius: 9px;
        border: 1px solid #D5DDF0;
        background-color: #FFFFFF;
        color: #1D4ED8;
        font-weight: 600;
        transition: 0.2s ease;
    }

    .stButton > button:hover {
        background-color: #1D4ED8;
        color: #FFFFFF;
        border-color: #1D4ED8;
    }

    /* Link buttons */
    .stLinkButton > a {
        width: 100%;
        justify-content: center;
        border-radius: 9px;
        font-weight: 600;
    }

    /* Divider */
    hr {
        border-color: #E2E8F0;
    }

    /* Small informational text */
    .muted-text {
        color: #64748B;
        font-size: 0.95rem;
    }

    /* Footer */
    .footer-text {
        text-align: center;
        color: #64748B;
        font-size: 0.9rem;
        padding-top: 25px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

if "loading_project" not in st.session_state:
    st.session_state.loading_project = None

# --------------------------------------------------
# SIDEBAR NAVIGATION
# --------------------------------------------------

with st.sidebar:
    st.markdown("# 🌌 Creative")
    st.markdown("## Universe")
    st.caption("Your creative project hub")

    st.divider()

    st.markdown("### NAVIGATION")

    if st.button("🏠  Home", key="nav_home"):
        st.session_state.selected_page = "Home"
        st.session_state.loading_project = None
        st.rerun()

    if st.button("🎨  AI Drawing Studio", key="nav_drawing"):
        st.session_state.selected_page = "AI Drawing Studio"
        st.session_state.loading_project = None
        st.rerun()

    if st.button("✨  MoodSpark", key="nav_moodspark"):
        st.session_state.selected_page = "MoodSpark"
        st.session_state.loading_project = None
        st.rerun()

    st.divider()

    st.markdown("### ABOUT")
    st.caption(
        "Creative Universe brings creative projects "
        "together in one convenient place."
    )

    st.markdown("---")
    st.caption("Version 1.0")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown("# Creative Universe")
st.markdown(
    '<p class="muted-text">'
    "A central place to explore creativity, technology, and ideas."
    "</p>",
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if st.session_state.selected_page == "Home":

    st.subheader("Welcome to your creative space 👋")

    st.write(
        "Discover projects designed to make technology "
        "more interactive, creative, and accessible."
    )

    st.write("")

    # Dashboard metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Total Projects",
            value="2"
        )

    with col2:
        st.metric(
            label="Creative Categories",
            value="2"
        )

    with col3:
        st.metric(
            label="Project Hub",
            value="Active"
        )

    st.write("")
    st.divider()

    st.subheader("Explore Projects")

    st.write(
        "Select a project below to learn more or open the application."
    )

    st.write("")

    # Project cards
    col1, col2 = st.columns(2, gap="large")

    with col1:
        with st.container(border=True):
            st.markdown("## 🎨 AI Drawing Studio")
            st.caption("AI & Creativity")

            st.write(
                "Turn your imagination into artwork. "
                "Explore an interactive space built around "
                "digital drawing and AI-powered creativity."
            )

            st.markdown("**Created by:** Purnima Kushwaha")

            st.link_button(
                "Open AI Drawing Studio ↗",
                PROJECTS["AI Drawing Studio"]["url"],
                use_container_width=True
            )

            if st.button(
                "Preview inside dashboard",
                key="preview_drawing",
                use_container_width=True
            ):
                st.session_state.loading_project = "AI Drawing Studio"
                st.rerun()

    with col2:
        with st.container(border=True):
            st.markdown("## ✨ MoodSpark")
            st.caption("Mood & Wellbeing")

            st.write(
                "Explore a project designed around moods, "
                "emotions, and interactive experiences."
            )

            st.markdown("**Created by:** Kritika")

            st.link_button(
                "Open MoodSpark ↗",
                PROJECTS["MoodSpark"]["url"],
                use_container_width=True
            )

            if st.button(
                "Preview inside dashboard",
                key="preview_moodspark",
                use_container_width=True
            ):
                st.session_state.loading_project = "MoodSpark"
                st.rerun()

    st.write("")
    st.divider()

    st.subheader("Why Creative Universe?")

    feature1, feature2, feature3 = st.columns(3)

    with feature1:
        st.markdown("### 🧭 Easy Navigation")
        st.write(
            "Find your projects from one organized dashboard."
        )

    with feature2:
        st.markdown("### 🚀 Quick Access")
        st.write(
            "Launch project websites without searching for their URLs."
        )

    with feature3:
        st.markdown("### 💡 Creative Ideas")
        st.write(
            "Explore different applications and creative experiences."
        )

# --------------------------------------------------
# INDIVIDUAL PROJECT PAGES
# --------------------------------------------------

elif st.session_state.selected_page in PROJECTS:

    project_name = st.session_state.selected_page
    project = PROJECTS[project_name]

    st.subheader(f"{project['icon']} {project_name}")
    st.caption(project["category"])

    st.write(project["description"])

    st.info(f"Project creator: {project['creator']}")

    st.link_button(
        f"Open {project_name} in a new tab ↗",
        project["url"],
        use_container_width=True
    )

    st.write("")
    st.divider()

    st.markdown("### Project preview")

    st.write(
        "You can open the project here or use the button above "
        "to launch it in a new browser tab."
    )

    if st.button(
        "Load project inside dashboard",
        key=f"load_{project_name}"
    ):
        st.session_state.loading_project = project_name
        st.rerun()

# --------------------------------------------------
# EMBEDDED PROJECT VIEW
# --------------------------------------------------

if st.session_state.loading_project:

    project_name = st.session_state.loading_project
    project = PROJECTS[project_name]

    st.divider()
    st.subheader(f"{project['icon']} {project_name}")

    st.write(
        "If the project does not appear below, use the "
        "'Open project in a new tab' button."
    )

    st.link_button(
        "Open project in a new tab ↗",
        project["url"],
        use_container_width=True
    )

    # Put the URL directly into the iframe.
    # This avoids relying on missing URL query parameters.
    components.iframe(
        project["url"],
        height=750,
        scrolling=True
    )

    if st.button("Close preview", key="close_preview"):
        st.session_state.loading_project = None
        st.rerun()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <div class="footer-text">
        <strong>Creative Universe</strong><br>
        Bringing ideas and creativity together.<br>
        Built with Streamlit.
    </div>
    """,
    unsafe_allow_html=True
)
