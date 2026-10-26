import streamlit as st
import streamlit.components.v1 as components

# =====================================================
# PAGE CONFIGURATION
# =====================================================

st.set_page_config(
    page_title="Creative Universe | Explore Beyond",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# PROJECT DATA
# =====================================================

PROJECTS = {
    "AI Drawing Studio": {
        "url": "https://ai-drawing-studio.streamlit.app/",
        "creator": "Purnima Kushwaha",
        "category": "ARTIFICIAL INTELLIGENCE",
        "description": (
            "Transform imagination into visual art. "
            "Discover a creative environment that brings "
            "ideas to life through AI-powered drawing."
        ),
        "icon": "🎨",
        "number": "01",
        "accent": "#9B8AFB"
    },
    "MoodSpark": {
        "url": "https://moodspark-pe81.onrender.com/",
        "creator": "Kritika",
        "category": "MOOD & WELLBEING",
        "description": (
            "Discover an interactive digital experience "
            "centred around moods, emotions, and creativity."
        ),
        "icon": "✦",
        "number": "02",
        "accent": "#56D6C9"
    }
}

# =====================================================
# SESSION STATE
# =====================================================

if "page" not in st.session_state:
    st.session_state.page = "Home"

if "preview" not in st.session_state:
    st.session_state.preview = None

# =====================================================
# CUSTOM DESIGN
# =====================================================

st.markdown(
    """
    <style>
    /* =========================================
       GLOBAL THEME
    ========================================= */

    .stApp {
        background: #0B1020;
        color: #F1F5FF;
    }

    .block-container {
        max-width: 1380px;
        padding-top: 2.2rem;
        padding-bottom: 3rem;
    }

    /* Main text */
    h1, h2, h3, h4 {
        color: #F4F6FF !important;
        letter-spacing: -0.7px;
    }

    p, li {
        color: #B3BED3;
        line-height: 1.8;
    }

    /* =========================================
       SIDEBAR
    ========================================= */

    section[data-testid="stSidebar"] {
        background: #10172A;
        border-right: 1px solid #252E47;
    }

    section[data-testid="stSidebar"] * {
        color: #E8ECFA;
    }

    section[data-testid="stSidebar"] .stButton button {
        background: #141E34;
        color: #E8ECFA;
        border: 1px solid #2A3550;
        border-radius: 10px;
        text-align: left;
        min-height: 44px;
        transition: 0.2s ease;
    }

    section[data-testid="stSidebar"] .stButton button:hover {
        background: #253052;
        border-color: #8C7BFA;
        color: #FFFFFF;
    }

    /* =========================================
       BUTTONS
    ========================================= */

    .stButton button {
        background: #171F35;
        color: #F3F5FF;
        border: 1px solid #34405D;
        border-radius: 10px;
        min-height: 45px;
        font-weight: 600;
        transition: all 0.2s ease;
    }

    .stButton button:hover {
        background: #253252;
        border-color: #9B8AFB;
        color: #FFFFFF;
    }

    .stLinkButton a {
        background: #8B78F6;
        color: #FFFFFF !important;
        border: 1px solid #8B78F6;
        border-radius: 10px;
        min-height: 45px;
        font-weight: 650;
        justify-content: center;
        transition: all 0.2s ease;
    }

    .stLinkButton a:hover {
        background: #7561E6;
        border-color: #7561E6;
        color: #FFFFFF !important;
    }

    /* =========================================
       METRICS
    ========================================= */

    [data-testid="stMetric"] {
        background: #121B30;
        border: 1px solid #293550;
        border-radius: 14px;
        padding: 20px;
    }

    [data-testid="stMetricLabel"] {
        color: #9AA8C3 !important;
    }

    [data-testid="stMetricValue"] {
        color: #FFFFFF !important;
    }

    /* =========================================
       CONTAINERS
    ========================================= */

    [data-testid="stVerticalBlockBorderWrapper"] {
        background: #111A2D;
        border: 1px solid #293550 !important;
        border-radius: 16px;
    }

    /* =========================================
       DIVIDERS
    ========================================= */

    hr {
        border-color: #29334C;
    }

    /* =========================================
       DESIGN LABELS
    ========================================= */

    .eyebrow {
        color: #A89BFF;
        font-size: 0.75rem;
        font-weight: 750;
        letter-spacing: 3px;
        margin-bottom: 0.8rem;
    }

    .hero-title {
        color: #FFFFFF;
        font-size: clamp(2.7rem, 5vw, 4.7rem);
        line-height: 1.1;
        font-weight: 800;
        letter-spacing: -2.5px;
        margin-bottom: 1rem;
    }

    .gradient-word {
        background: linear-gradient(
            90deg,
            #B6A8FF 0%,
            #8BBAFF 50%,
            #70E3D4 100%
        );
        -webkit-background-clip: text;
        background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-description {
        color: #AAB6CF;
        font-size: 1.05rem;
        line-height: 1.9;
        max-width: 760px;
    }

    .section-label {
        color: #9C8CFF;
        font-size: 0.73rem;
        font-weight: 750;
        letter-spacing: 2.5px;
        margin-bottom: 0.5rem;
    }

    .small-muted {
        color: #8492AE;
        font-size: 0.88rem;
    }

    .footer {
        text-align: center;
        color: #7785A2;
        font-size: 0.85rem;
        line-height: 2;
        padding-top: 1.2rem;
    }

    /* =========================================
       RESPONSIVE
    ========================================= */

    @media (max-width: 768px) {
        .block-container {
            padding-top: 1rem;
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero-title {
            letter-spacing: -1.3px;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.markdown("## ✦ Creative")
    st.markdown("### Universe")

    st.markdown(
        '<p style="color:#8795B2;font-size:0.85rem;">'
        "YOUR CREATIVE SPACE"
        "</p>",
        unsafe_allow_html=True
    )

    st.divider()

    st.markdown("##### WORKSPACE")

    if st.button("⌂   Home", use_container_width=True):
        st.session_state.page = "Home"
        st.session_state.preview = None
        st.rerun()

    if st.button("🎨   AI Drawing Studio", use_container_width=True):
        st.session_state.page = "AI Drawing Studio"
        st.session_state.preview = None
        st.rerun()

    if st.button("✦   MoodSpark", use_container_width=True):
        st.session_state.page = "MoodSpark"
        st.session_state.preview = None
        st.rerun()

    st.divider()

    st.markdown("##### THE PLATFORM")

    st.caption(
        "A curated space for creative applications, "
        "digital experiences, and innovative ideas."
    )

    st.write("")

    st.markdown(
        """
        <div style="
            background:#171F35;
            border:1px solid #2D3956;
            border-radius:12px;
            padding:14px;
        ">
            <div style="color:#9B8AFB;font-size:0.72rem;
                        letter-spacing:1.5px;">
                PLATFORM STATUS
            </div>
            <div style="color:#E8ECFA;font-weight:600;
                        margin-top:6px;">
                ● Project portal
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# HOME PAGE
# =====================================================

if st.session_state.page == "Home":

    # Hero section
    st.markdown(
        """
        <div class="eyebrow">
            WELCOME TO YOUR CREATIVE SPACE
        </div>

        <div class="hero-title">
            Ideas become<br>
            <span class="gradient-word">
                experiences.
            </span>
        </div>

        <div class="hero-description">
            Welcome to Creative Universe — a central destination
            for exploring creative applications, discovering ideas,
            and experiencing technology in new ways.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")
    st.write("")

    # Quick summary
    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("PROJECTS", "02", "Creative applications")

    with c2:
        st.metric("CATEGORIES", "02", "Different experiences")

    with c3:
        st.metric("ACCESS", "One hub", "Centralized workspace")

    st.write("")
    st.divider()

    # Projects heading
    st.markdown(
        '<div class="section-label">DISCOVER</div>',
        unsafe_allow_html=True
    )

    st.markdown("## Explore our projects")

    st.markdown(
        '<p class="small-muted">'
        "A selection of digital experiences, ready to explore."
        "</p>",
        unsafe_allow_html=True
    )

    st.write("")

    left, right = st.columns(2, gap="large")

    # -------------------------------------------------
    # AI DRAWING STUDIO CARD
    # -------------------------------------------------

    with left:

        with st.container(border=True):

            st.markdown(
                """
                <div style="
                    color:#A99AFF;
                    font-size:0.75rem;
                    font-weight:700;
                    letter-spacing:2px;
                ">
                    PROJECT 01 &nbsp; / &nbsp; AI & CREATIVITY
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            st.markdown("## 🎨 AI Drawing Studio")

            st.markdown(
                """
                <p style="color:#AAB6CF;min-height:85px;">
                    Bring imagination to life through an interactive
                    digital drawing experience focused on creativity
                    and AI-assisted artwork.
                </p>
                """,
                unsafe_allow_html=True
            )

            st.divider()

            st.caption("CREATED BY")
            st.markdown("**Purnima Kushwaha**")

            st.write("")

            st.link_button(
                "Explore project ↗",
                PROJECTS["AI Drawing Studio"]["url"],
                use_container_width=True
            )

            if st.button(
                "View inside portal",
                key="preview_drawing",
                use_container_width=True
            ):
                st.session_state.preview = "AI Drawing Studio"
                st.rerun()

    # -------------------------------------------------
    # MOODSPARK CARD
    # -------------------------------------------------

    with right:

        with st.container(border=True):

            st.markdown(
                """
                <div style="
                    color:#67DCD0;
                    font-size:0.75rem;
                    font-weight:700;
                    letter-spacing:2px;
                ">
                    PROJECT 02 &nbsp; / &nbsp; MOOD & WELLBEING
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            st.markdown("## ✦ MoodSpark")

            st.markdown(
                """
                <p style="color:#AAB6CF;min-height:85px;">
                    Explore an interactive digital experience centred
                    around moods, emotions, and creative engagement.
                </p>
                """,
                unsafe_allow_html=True
            )

            st.divider()

            st.caption("CREATED BY")
            st.markdown("**Kritika**")

            st.write("")

            st.link_button(
                "Explore project ↗",
                PROJECTS["MoodSpark"]["url"],
                use_container_width=True
            )

            if st.button(
                "View inside portal",
                key="preview_moodspark",
                use_container_width=True
            ):
                st.session_state.preview = "MoodSpark"
                st.rerun()

    st.write("")
    st.divider()

    # About section
    st.markdown(
        '<div class="section-label">OUR APPROACH</div>',
        unsafe_allow_html=True
    )

    st.markdown("## One space. Multiple possibilities.")

    a, b, c = st.columns(3, gap="large")

    with a:
        st.markdown("### ◈ &nbsp; Discover")
        st.write(
            "Find creative digital projects in one organized space."
        )

    with b:
        st.markdown("### ↗ &nbsp; Explore")
        st.write(
            "Launch an application directly from its project card."
        )

    with c:
        st.markdown("### ✧ &nbsp; Create")
        st.write(
            "Explore different ways technology can support creativity."
        )

# =====================================================
# INDIVIDUAL PROJECT PAGE
# =====================================================

elif st.session_state.page in PROJECTS:

    project_name = st.session_state.page
    project = PROJECTS[project_name]

    st.markdown(
        f'<div class="section-label">'
        f'PROJECT {project["number"]} &nbsp; / &nbsp; PORTFOLIO'
        f'</div>',
        unsafe_allow_html=True
    )

    st.title(f'{project["icon"]} {project_name}')

    st.caption(project["category"])

    st.write(project["description"])

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.caption("PROJECT CREATOR")
        st.markdown(f'### {project["creator"]}')

    with col2:
        st.caption("APPLICATION TYPE")
        st.markdown("### Web application")

    st.write("")

    st.link_button(
        "Launch application ↗",
        project["url"],
        use_container_width=True
    )

    st.write("")
    st.divider()

    st.markdown("## Application preview")

    st.write(
        "Load the project within the portal, or open it in a separate tab."
    )

    if st.button("Load application preview", use_container_width=True):
        st.session_state.preview = project_name
        st.rerun()

# =====================================================
# APPLICATION PREVIEW
# =====================================================

if st.session_state.preview:

    preview_name = st.session_state.preview
    preview_project = PROJECTS[preview_name]

    st.divider()

    st.markdown(f"## {preview_project['icon']} {preview_name}")

    st.link_button(
        "Open in a new tab ↗",
        preview_project["url"],
        use_container_width=True
    )

    components.iframe(
        preview_project["url"],
        height=750,
        scrolling=True
    )

    if st.button("Close preview"):
        st.session_state.preview = None
        st.rerun()

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.markdown(
    """
    <div class="footer">
        <strong style="color:#DDE5F8;">
            ✦ CREATIVE UNIVERSE
        </strong>
        <br>
        A home for creativity, ideas, and digital experiences.
        <br>
        <span style="color:#63718D;">
            Designed with Streamlit
        </span>
    </div>
    """,
    unsafe_allow_html=True
)
