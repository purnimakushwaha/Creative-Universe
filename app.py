```python
import streamlit as st

st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# APP URLS
# ==========================================

DRAWING_URL = "https://ai-drawing-studio.streamlit.app/?embed=true"
DRAWING_DIRECT_URL = "https://ai-drawing-studio.streamlit.app/"
MOODSPARK_URL = "https://moodspark-pe81.onrender.com/"

# ==========================================
# SESSION STATE
# ==========================================

if "page" not in st.session_state:
    st.session_state.page = "Home"


def navigate_to(page):
    st.session_state.page = page


# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(ellipse at top left,
            rgba(110, 75, 210, 0.20), transparent 42%),
        radial-gradient(ellipse at bottom right,
            rgba(36, 145, 190, 0.14), transparent 40%),
        linear-gradient(135deg, #0b1020, #14142d, #101c32);
    color: #f5f3ff;
}

[data-testid="stHeader"] {
    background: transparent;
}

[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #111329, #171630);
    border-right: 1px solid rgba(190, 175, 255, 0.12);
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3, h4 {
    color: #ffffff !important;
    letter-spacing: -0.5px;
}

p {
    color: #cbd0e5;
    line-height: 1.75;
}

[data-testid="stCaptionContainer"] {
    color: #aaa8ce;
}

.stButton > button,
.stLinkButton > a {
    min-height: 46px;
    border-radius: 12px;
    border: 1px solid rgba(174, 153, 255, 0.55);
    background: linear-gradient(110deg, #7757e8, #536ee7);
    color: white !important;
    font-weight: 650;
    transition: 0.2s ease;
}

.stButton > button:hover,
.stLinkButton > a:hover {
    border-color: #d8ceff;
    box-shadow: 0 6px 22px rgba(111, 85, 231, 0.24);
    transform: translateY(-2px);
}

.hero {
    padding: 46px 38px;
    margin: 8px 0 30px;
    border-radius: 26px;
    background:
        radial-gradient(circle at 85% 15%,
            rgba(143, 111, 255, 0.30), transparent 35%),
        linear-gradient(120deg,
            rgba(65, 52, 133, 0.70),
            rgba(29, 50, 91, 0.80));
    border: 1px solid rgba(190, 175, 255, 0.25);
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.18);
}

.hero-label {
    display: inline-block;
    padding: 7px 12px;
    margin-bottom: 18px;
    border-radius: 30px;
    background: rgba(255, 255, 255, 0.09);
    border: 1px solid rgba(255, 255, 255, 0.15);
    color: #ded5ff;
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 1.5px;
}

.hero-title {
    font-size: clamp(2.1rem, 5vw, 3.5rem);
    font-weight: 850;
    line-height: 1.15;
    color: white;
    margin-bottom: 16px;
}

.hero-description {
    max-width: 680px;
    font-size: 1.05rem;
    line-height: 1.8;
    color: #dedff4;
}

.section-label {
    color: #b4a4ff;
    font-size: 0.78rem;
    font-weight: 750;
    letter-spacing: 2px;
    margin-bottom: 8px;
}

.app-card {
    min-height: 270px;
    padding: 27px;
    border-radius: 21px;
    background: linear-gradient(
        145deg,
        rgba(255, 255, 255, 0.075),
        rgba(255, 255, 255, 0.025)
    );
    border: 1px solid rgba(205, 195, 255, 0.17);
    transition: 0.2s ease;
}

.app-card:hover {
    transform: translateY(-4px);
    border-color: rgba(176, 156, 255, 0.55);
    background: rgba(130, 104, 224, 0.10);
}

.app-icon {
    width: 66px;
    height: 66px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    border-radius: 19px;
    font-size: 2.1rem;
    background: rgba(141, 117, 255, 0.13);
    border: 1px solid rgba(190, 175, 255, 0.19);
}

.app-name {
    color: white;
    font-size: 1.35rem;
    font-weight: 750;
    margin-bottom: 10px;
}

.app-description {
    color: #c4c8e0;
    font-size: 0.96rem;
    line-height: 1.8;
    min-height: 75px;
}

.app-tag {
    display: inline-block;
    padding: 5px 10px;
    margin-top: 12px;
    border-radius: 20px;
    background: rgba(121, 93, 231, 0.15);
    color: #d6caff;
    font-size: 0.76rem;
    font-weight: 600;
}

.info-panel {
    padding: 23px;
    border-radius: 17px;
    background: rgba(255, 255, 255, 0.045);
    border: 1px solid rgba(200, 190, 255, 0.12);
    min-height: 150px;
}

.info-title {
    color: white;
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 8px;
}

.info-description {
    color: #bfc4dd;
    font-size: 0.92rem;
    line-height: 1.75;
}

.footer {
    margin-top: 48px;
    padding: 24px 10px 5px;
    text-align: center;
    border-top: 1px solid rgba(255, 255, 255, 0.12);
    color: #a7aac5;
    font-size: 0.87rem;
}

hr {
    border-color: rgba(255, 255, 255, 0.11);
}

[data-testid="stIFrame"] {
    border-radius: 16px;
    overflow: hidden;
    border: 1px solid rgba(190, 175, 255, 0.18);
}

@media (max-width: 768px) {
    .block-container {
        padding: 1rem;
    }

    .hero {
        padding: 30px 23px;
    }

    .app-card {
        padding: 21px;
    }
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# REUSABLE FUNCTIONS
# ==========================================

def render_footer():
    st.markdown("""
    <div class="footer">
        <div style="font-size: 1.1rem; margin-bottom: 8px;">
            🌌 <strong>Creative Universe</strong>
        </div>
        Create something meaningful. Explore something new.
        <br><br>
        © Creative Universe · Keep imagining. Keep creating.
    </div>
    """, unsafe_allow_html=True)


def render_app_card(icon, title, description, tag):
    st.markdown(f"""
    <div class="app-card">
        <div class="app-icon">{icon}</div>
        <div class="app-name">{title}</div>
        <div class="app-description">{description}</div>
        <div class="app-tag">{tag}</div>
    </div>
    """, unsafe_allow_html=True)


def render_external_app(title, description, url, embed_url=None):
    st.write(description)

    st.link_button(
        f"Open {title} in a New Tab ↗",
        url,
        use_container_width=True
    )

    st.caption(
        "If the embedded application does not load, "
        "use the button above to open it directly."
    )

    if embed_url:
        st.markdown("---")
        st.subheader("Application Preview")
        st.components.v1.iframe(
            embed_url,
            height=780,
            scrolling=True
        )


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:
    st.markdown("""
    <div style="padding: 8px 0 18px;">
        <div style="font-size: 2.4rem;">🌌</div>
        <div style="
            font-size: 1.25rem;
            font-weight: 800;
            color: white;
            margin-top: 5px;
        ">Creative Universe</div>
        <div style="
            font-size: 0.82rem;
            color: #aaa8ce;
            margin-top: 6px;
        ">Create · Explore · Discover</div>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
    st.caption("NAVIGATION")

    pages = {
        "🏠 Home": "Home",
        "🎨 AI Drawing Studio": "Drawing",
        "🌈 MoodSpark": "MoodSpark"
    }

    for label, page_name in pages.items():
        if st.session_state.page == page_name:
            button_label = f"● {label}"
        else:
            button_label = label

        if st.button(
            button_label,
            key=f"nav_{page_name}",
            use_container_width=True
        ):
            navigate_to(page_name)
            st.rerun()

    st.divider()
    st.markdown("### ✨ Your Creative Space")

    st.caption(
        "One dashboard. Two experiences. "
        "A universe of possibilities."
    )

    st.markdown("---")
    st.caption("PROJECTS")
    st.markdown("🎨 **AI Drawing Studio**")
    st.caption("Creative exploration")
    st.markdown("🌈 **MoodSpark**")
    st.caption("Mood and reflection")


# ==========================================
# HOME PAGE
# ==========================================

if st.session_state.page == "Home":

    st.markdown("""
    <div class="hero">
        <div class="hero-label">
            ✦ YOUR SPACE TO CREATE AND EXPLORE
        </div>
        <div class="hero-title">
            Welcome to Your<br>
            Creative Universe.
        </div>
        <div class="hero-description">
            A place where imagination meets expression.
            Explore creative tools, discover new perspectives,
            and turn your ideas into experiences.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section-label">EXPLORE</div>
    <h2 style="margin-top: 0;">
        Discover Your Next Experience
    </h2>
    <p style="margin-bottom: 25px;">
        Choose an application and begin your journey.
    </p>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="large")

    with col1:
        render_app_card(
            "🎨",
            "AI Drawing Studio",
            "Bring your imagination to life. Explore artistic "
            "ideas and enjoy a creative space for visual expression.",
            "ART · CREATIVITY"
        )

        if st.button(
            "Explore Drawing Studio →",
            key="home_drawing",
            use_container_width=True
        ):
            navigate_to("Drawing")
            st.rerun()

    with col2:
        render_app_card(
            "🌈",
            "MoodSpark",
            "Take a moment to explore your mood, reflect on "
            "your feelings, and create a mindful experience.",
            "MOOD · REFLECTION"
        )

        if st.button(
            "Explore MoodSpark →",
            key="home_moodspark",
            use_container_width=True
        ):
            navigate_to("MoodSpark")
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

    st.markdown("""
    <div class="section-label">ABOUT THE PROJECT</div>
    <h2>More Than a Dashboard</h2>
    <p>
        Creative Universe brings two independent applications
        together in one convenient space. Each project has its
        own purpose, experience, and creative possibilities.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    step1, step2, step3 = st.columns(3, gap="medium")

    with step1:
        st.markdown("""
        <div class="info-panel">
            <div style="font-size: 1.8rem;">🌌</div>
            <div class="info-title">01 · Explore</div>
            <div class="info-description">
                Discover the tools and experiences available.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with step2:
        st.markdown("""
        <div class="info-panel">
            <div style="font-size: 1.8rem;">🎨</div>
            <div class="info-title">02 · Create</div>
            <div class="info-description">
                Express your ideas and experiment creatively.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with step3:
        st.markdown("""
        <div class="info-panel">
            <div style="font-size: 1.8rem;">💜</div>
            <div class="info-title">03 · Discover</div>
            <div class="info-description">
                Explore new perspectives at your own pace.
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-label">THE PEOPLE BEHIND THE PROJECT</div>
    <h2>Project Credits</h2>
    """, unsafe_allow_html=True)

    credit1, credit2 = st.columns(2, gap="large")

    with credit1:
        st.markdown("""
        <div class="info-panel">
            <div style="font-size: 1.8rem;">🎨</div>
            <div class="info-title">AI Drawing Studio</div>
            <div class="info-description">
                Created by Purnima Kushwaha
            </div>
        </div>
        """, unsafe_allow_html=True)

    with credit2:
        st.markdown("""
        <div class="info-panel">
            <div style="font-size: 1.8rem;">🌈</div>
            <div class="info-title">MoodSpark</div>
            <div class="info-description">
                Created by Kritika
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        "Dashboard collaboration: "
        "Purnima Kushwaha & Kritika"
    )

    render_footer()


# ==========================================
# AI DRAWING STUDIO
# ==========================================

elif st.session_state.page == "Drawing":

    st.button(
        "← Back to Home",
        key="drawing_back",
        on_click=navigate_to,
        args=("Home",)
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-label">CREATIVE EXPERIENCE</div>
    <h1>🎨 AI Drawing Studio</h1>
    <p>
        Give your imagination a canvas.
        Explore your creative ideas in AI Drawing Studio.
    </p>
    """, unsafe_allow_html=True)

    st.link_button(
        "Launch Drawing Studio in New Tab ↗",
        DRAWING_DIRECT_URL,
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        "If the preview stays blank or shows a redirect error, "
        "open the application in a new tab. Some deployed "
        "applications restrict iframe embedding."
    )

    st.markdown("### Application Preview")

    st.components.v1.iframe(
        DRAWING_URL,
        height=780,
        scrolling=True
    )

    render_footer()


# ==========================================
# MOODSPARK
# ==========================================

elif st.session_state.page == "MoodSpark":

    st.button(
        "← Back to Home",
        key="moodspark_back",
        on_click=navigate_to,
        args=("Home",)
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div class="section-label">MOOD AND REFLECTION</div>
    <h1>🌈 MoodSpark</h1>
    <p>
        Make space for your feelings.
        Explore MoodSpark and discover its mood-related experiences.
    </p>
    """, unsafe_allow_html=True)

    st.link_button(
        "Launch MoodSpark in New Tab ↗",
        MOODSPARK_URL,
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.info(
        "If MoodSpark takes time to start, the service may be "
        "waking up. If the preview does not work, use the button "
        "above to open it directly."
    )

    st.markdown("### Application Preview")

    st.components.v1.iframe(
        MOODSPARK_URL,
        height=780,
        scrolling=True
    )

    render_footer()
```
