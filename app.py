import streamlit as st
import streamlit.components.v1 as components

# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Creative Universe | Project Portal",
    page_icon="◈",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# PROJECT DATA
# =========================================================

PROJECTS = {
    "AI Drawing Studio": {
        "url": "https://ai-drawing-studio.streamlit.app/",
        "creator": "Purnima Kushwaha",
        "category": "ARTIFICIAL INTELLIGENCE",
        "description": (
            "An interactive creative environment for exploring "
            "digital drawing and AI-assisted artwork."
        ),
        "icon": "🎨",
        "number": "01"
    },
    "MoodSpark": {
        "url": "https://moodspark-pe81.onrender.com/",
        "creator": "Kritika",
        "category": "MOOD & WELLBEING",
        "description": (
            "An interactive experience focused on moods, emotions, "
            "and engaging digital experiences."
        ),
        "icon": "✦",
        "number": "02"
    }
}

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Overview"

if "preview" not in st.session_state:
    st.session_state.preview = None

# =========================================================
# PROFESSIONAL STYLING
# =========================================================

st.markdown(
    """
    <style>
    /* ---------- Global layout ---------- */

    .stApp {
        background: #F4F6FA;
        color: #172033;
    }

    .block-container {
        max-width: 1320px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* ---------- Sidebar ---------- */

    section[data-testid="stSidebar"] {
        background: #111C32;
        border-right: 1px solid #25334B;
    }

    section[data-testid="stSidebar"] * {
        color: #E8EDF7;
    }

    section[data-testid="stSidebar"] .stButton button {
        text-align: left;
        background: transparent;
        color: #E8EDF7;
        border: 1px solid #34415A;
        border-radius: 8px;
        min-height: 42px;
    }

    section[data-testid="stSidebar"] .stButton button:hover {
        background: #25334B;
        border-color: #8AA9E8;
        color: white;
    }

    /* ---------- Typography ---------- */

    h1 {
        color: #14213A !important;
        font-weight: 750 !important;
        letter-spacing: -1.2px !important;
    }

    h2, h3 {
        color: #1C2D49 !important;
        font-weight: 650 !important;
        letter-spacing: -0.3px;
    }

    p, li {
        color: #4C5B72;
        line-height: 1.7;
    }

    /* ---------- Buttons ---------- */

    .stButton button,
    .stLinkButton a {
        border-radius: 8px !important;
        font-weight: 600 !important;
        min-height: 43px;
        transition: all 0.18s ease;
    }

    .stButton button {
        border: 1px solid #D5DDEA;
    }

    .stButton button:hover {
        border-color: #345EA8;
        color: #244D91;
    }

    .stLinkButton a {
        border: 1px solid #254D8B;
        background: #254D8B;
        color: white !important;
    }

    .stLinkButton a:hover {
        background: #193A6B;
        border-color: #193A6B;
    }

    /* ---------- Dividers ---------- */

    hr {
        border-color: #DDE3ED;
    }

    /* ---------- Small labels ---------- */

    .eyebrow {
        color: #526B91;
        font-size: 0.73rem;
        font-weight: 750;
        letter-spacing: 2px;
        margin-bottom: 0.65rem;
    }

    .subtitle {
        color: #65738A;
        font-size: 1rem;
        line-height: 1.8;
        max-width: 750px;
    }

    .section-label {
        color: #526B91;
        font-size: 0.75rem;
        font-weight: 750;
        letter-spacing: 1.7px;
        margin-bottom: 0.5rem;
    }

    .footer {
        text-align: center;
        color: #78859A;
        font-size: 0.83rem;
        padding-top: 1rem;
        line-height: 1.8;
    }

    /* ---------- Metrics ---------- */

    [data-testid="stMetric"] {
        background: #FFFFFF;
        border: 1px solid #E0E6EF;
        border-radius: 10px;
        padding: 18px 20px;
    }

    [data-testid="stMetricLabel"] {
        color: #68768B;
    }

    [data-testid="stMetricValue"] {
        color: #1D355D;
    }

    /* ---------- Containers ---------- */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #FFFFFF;
        border-color: #E0E6EF !important;
        border-radius: 12px;
    }

    /* ---------- Alerts ---------- */

    [data-testid="stAlert"] {
        border-radius: 8px;
    }

    /* ---------- Mobile adjustments ---------- */

    @media (max-width: 768px) {
        .block-container {
            padding-top: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        h1 {
            font-size: 2rem !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("## ◈ CREATIVE UNIVERSE")
    st.caption("DIGITAL PROJECT PORTAL")

    st.divider()

    st.markdown("##### WORKSPACE")

    if st.button(
        "▦   Overview",
        key="overview_nav",
        use_container_width=True
    ):
        st.session_state.page = "Overview"
        st.session_state.preview = None
        st.rerun()

    if st.button(
        "🎨   AI Drawing Studio",
        key="drawing_nav",
        use_container_width=True
    ):
        st.session_state.page = "AI Drawing Studio"
        st.session_state.preview = None
        st.rerun()

    if st.button(
        "✦   MoodSpark",
        key="moodspark_nav",
        use_container_width=True
    ):
        st.session_state.page = "MoodSpark"
        st.session_state.preview = None
        st.rerun()

    st.divider()

    st.markdown("##### ABOUT THIS PORTAL")

    st.caption(
        "A centralized workspace for discovering and accessing "
        "creative digital projects."
    )

    st.write("")

    st.caption("PLATFORM")
    st.caption("Creative Universe · v1.0")

# =========================================================
# MAIN HEADER
# =========================================================

header_left, header_right = st.columns([4, 1])

with header_left:
    st.markdown(
        '<div class="eyebrow">DIGITAL EXPERIENCE PLATFORM</div>',
        unsafe_allow_html=True
    )

    st.title("Creative Universe")

    st.markdown(
        """
        <div class="subtitle">
            A unified platform for exploring creative applications,
            interactive experiences, and technology-driven ideas.
        </div>
        """,
        unsafe_allow_html=True
    )

with header_right:
    st.write("")
    st.caption("PROJECT PORTAL")
    st.markdown("**● Operational**")

st.divider()

# =========================================================
# OVERVIEW PAGE
# =========================================================

if st.session_state.page == "Overview":

    st.markdown(
        '<div class="section-label">WORKSPACE OVERVIEW</div>',
        unsafe_allow_html=True
    )

    st.subheader("Projects at a glance")

    st.write(
        "Access the available applications, review project ownership, "
        "and launch an experience directly from this workspace."
    )

    st.write("")

    # Summary metrics
    metric1, metric2, metric3 = st.columns(3)

    with metric1:
        st.metric(
            label="Total Projects",
            value="02",
            help="Number of projects listed in this portal."
        )

    with metric2:
        st.metric(
            label="Project Categories",
            value="02",
            help="AI and creativity, and mood-focused experiences."
        )

    with metric3:
        st.metric(
            label="Access",
            value="Centralized",
            help="Both projects are available through this portal."
        )

    st.write("")
    st.divider()

    # Project section
    project_header, project_count = st.columns([4, 1])

    with project_header:
        st.markdown(
            '<div class="section-label">PORTFOLIO</div>',
            unsafe_allow_html=True
        )
        st.subheader("Featured projects")

    with project_count:
        st.write("")
        st.caption("02 APPLICATIONS")

    st.write("")

    left, right = st.columns(2, gap="large")

    # -----------------------------------------------------
    # PROJECT 01
    # -----------------------------------------------------

    with left:

        with st.container(border=True):

            top_left, top_right = st.columns([3, 1])

            with top_left:
                st.caption("PROJECT 01")
                st.markdown("## 🎨 AI Drawing Studio")

            with top_right:
                st.write("")
                st.caption("AI / CREATIVE")

            st.divider()

            st.write(PROJECTS["AI Drawing Studio"]["description"])

            st.write("")
            st.caption("PROJECT OWNER")
            st.markdown("**Purnima Kushwaha**")

            st.write("")

            st.link_button(
                "Launch application ↗",
                PROJECTS["AI Drawing Studio"]["url"],
                use_container_width=True
            )

            if st.button(
                "Open embedded preview",
                key="drawing_preview",
                use_container_width=True
            ):
                st.session_state.preview = "AI Drawing Studio"
                st.rerun()

    # -----------------------------------------------------
    # PROJECT 02
    # -----------------------------------------------------

    with right:

        with st.container(border=True):

            top_left, top_right = st.columns([3, 1])

            with top_left:
                st.caption("PROJECT 02")
                st.markdown("## ✦ MoodSpark")

            with top_right:
                st.write("")
                st.caption("MOOD / WELLBEING")

            st.divider()

            st.write(PROJECTS["MoodSpark"]["description"])

            st.write("")
            st.caption("PROJECT OWNER")
            st.markdown("**Kritika**")

            st.write("")

            st.link_button(
                "Launch application ↗",
                PROJECTS["MoodSpark"]["url"],
                use_container_width=True
            )

            if st.button(
                "Open embedded preview",
                key="moodspark_preview",
                use_container_width=True
            ):
                st.session_state.preview = "MoodSpark"
                st.rerun()

    st.write("")
    st.divider()

    # Platform information
    st.markdown(
        '<div class="section-label">PLATFORM INFORMATION</div>',
        unsafe_allow_html=True
    )

    st.subheader("Designed for easy access")

    info1, info2, info3 = st.columns(3, gap="large")

    with info1:
        st.markdown("### 01 · Centralized")
        st.write(
            "Access multiple projects from a single, organized interface."
        )

    with info2:
        st.markdown("### 02 · Accessible")
        st.write(
            "Use direct launch buttons to open project applications."
        )

    with info3:
        st.markdown("### 03 · Organized")
        st.write(
            "Review project descriptions and creator credits in one place."
        )

# =========================================================
# INDIVIDUAL PROJECT PAGE
# =========================================================

elif st.session_state.page in PROJECTS:

    project_name = st.session_state.page
    project = PROJECTS[project_name]

    st.markdown(
        f'<div class="section-label">PROJECT {project["number"]}</div>',
        unsafe_allow_html=True
    )

    st.title(f'{project["icon"]} {project_name}')

    st.caption(project["category"])

    st.write(project["description"])

    st.divider()

    details1, details2 = st.columns(2)

    with details1:
        st.caption("PROJECT OWNER")
        st.markdown(f'### {project["creator"]}')

    with details2:
        st.caption("ACCESS TYPE")
        st.markdown("### Web application")

    st.write("")

    st.link_button(
        f"Launch {project_name} ↗",
        project["url"],
        use_container_width=True
    )

    st.write("")
    st.divider()

    st.subheader("Application preview")

    st.write(
        "You can try loading the application below. If the external "
        "website does not permit embedding, launch it in a new tab."
    )

    if st.button(
        "Load preview",
        key=f"load_preview_{project_name}"
    ):
        st.session_state.preview = project_name
        st.rerun()

# =========================================================
# EMBEDDED PREVIEW
# =========================================================

if st.session_state.preview:

    preview_name = st.session_state.preview
    preview_project = PROJECTS[preview_name]

    st.divider()

    st.subheader(f'Application preview · {preview_name}')

    st.link_button(
        "Open in a new browser tab ↗",
        preview_project["url"],
        use_container_width=True
    )

    components.iframe(
        preview_project["url"],
        height=750,
        scrolling=True
    )

    if st.button("Close preview", key="close_preview"):
        st.session_state.preview = None
        st.rerun()

# =========================================================
# FOOTER
# =========================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        <strong>CREATIVE UNIVERSE</strong><br>
        A centralized portal for creative digital experiences.<br>
        Built with Streamlit.
    </div>
    """,
    unsafe_allow_html=True
)
