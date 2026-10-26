import streamlit as st

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- DESIGN ----------------

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #100c28, #211746, #102b43);
    color: white;
}

[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: white !important;
}

p {
    color: #d8d5ed;
}

.hero {
    text-align: center;
    padding: 55px 15px 40px 15px;
}

.hero-title {
    font-size: 52px;
    font-weight: 800;
    line-height: 1.2;
    color: white;
}

.hero-subtitle {
    font-size: 18px;
    color: #d8d5ed;
    max-width: 700px;
    margin: 20px auto;
    line-height: 1.8;
}

.badge {
    display: inline-block;
    padding: 8px 18px;
    border-radius: 30px;
    border: 1px solid #7264a8;
    background: #2b2050;
    color: #d9c8ff;
    font-size: 13px;
    letter-spacing: 1px;
}

.gradient-text {
    color: #bdaaff;
}

.section-heading {
    text-align: center;
    font-size: 32px;
    font-weight: 750;
    margin-top: 25px;
    margin-bottom: 8px;
}

.section-description {
    text-align: center;
    color: #c6c1df;
    margin-bottom: 30px;
}

.app-card {
    background: rgba(255, 255, 255, 0.07);
    border: 1px solid rgba(210, 195, 255, 0.25);
    border-radius: 22px;
    padding: 30px 25px;
    text-align: center;
    min-height: 300px;
    margin-bottom: 12px;
}

.app-icon {
    font-size: 55px;
    margin-bottom: 12px;
}

.app-title {
    font-size: 25px;
    font-weight: 750;
    color: white;
    margin-bottom: 12px;
}

.app-description {
    color: #d8d5ed;
    font-size: 15px;
    line-height: 1.8;
}

.app-label {
    color: #c5b5ff;
    font-size: 12px;
    letter-spacing: 1px;
    margin-bottom: 15px;
}

.stLinkButton > a {
    display: flex;
    justify-content: center;
    align-items: center;
    border-radius: 12px;
    border: 1px solid #a994ff;
    background: linear-gradient(90deg, #7957e8, #527ce8);
    color: white !important;
    font-weight: 700;
    padding: 12px 15px;
    transition: 0.2s ease;
}

.stLinkButton > a:hover {
    border-color: white;
    filter: brightness(1.12);
}

.info-card {
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(210, 195, 255, 0.20);
    border-radius: 18px;
    padding: 24px;
    margin: 12px 0;
}

.info-title {
    font-size: 21px;
    font-weight: 700;
    color: #cbbaff;
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
    min-height: 175px;
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

@media (max-width: 768px) {
    .hero-title {
        font-size: 36px;
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


# ---------------- HERO SECTION ----------------

st.markdown(
    """
    <div class="hero">
        <div class="badge">✦ CREATE · EXPLORE · DISCOVER ✦</div>
        <div class="hero-title">
            Welcome to<br>
            <span class="gradient-text">Creative Universe 🌌</span>
        </div>
        <div class="hero-subtitle">
            A universe where imagination meets creativity.
            Explore art, discover your emotions, and give your
            ideas a place to grow.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------- APPLICATIONS ----------------

st.markdown(
    '<div class="section-heading">✨ Explore Our Universe</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">Choose your experience and begin your journey.</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2, gap="large")


# Drawing application

with col1:
    st.markdown(
        """
        <div class="app-card">
            <div class="app-icon">🎨</div>
            <div class="app-title">AI Drawing Studio</div>
            <div class="app-label">ART · IMAGINATION · CREATIVITY</div>
            <div class="app-description">
                Explore your artistic side and turn your
                imagination into a creative experience.
                Let your ideas inspire something new.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "🎨 Open AI Drawing Studio",
        "https://ai-drawing-studio.streamlit.app/",
        use_container_width=True
    )


# Mood application

with col2:
    st.markdown(
        """
        <div class="app-card">
            <div class="app-icon">🌈</div>
            <div class="app-title">MoodSpark</div>
            <div class="app-label">MOOD · REFLECTION · WELL-BEING</div>
            <div class="app-description">
                Take a moment for yourself. Explore your mood,
                reflect on your feelings, and make space
                for positivity in your day.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "🌈 Explore MoodSpark",
        "https://moodspark-pe81.onrender.com/",
        use_container_width=True
    )


# ---------------- ABOUT SECTION ----------------

st.markdown("---")

st.markdown(
    '<div class="section-heading">💫 About Creative Universe</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">Two experiences, one creative destination.</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="info-card">
        <div class="info-title">🌠 A Space for Creativity</div>
        <div class="info-description">
            Creative Universe brings together two different experiences.
            AI Drawing Studio encourages artistic exploration, while
            MoodSpark offers a space for mood reflection.
            <br><br>
            Our goal is to make exploring creativity and self-expression
            simple, welcoming, and enjoyable.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ---------------- HOW IT WORKS ----------------

st.markdown(
    '<div class="section-heading">🚀 Start Your Journey</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-description">Three simple steps to get started.</div>',
    unsafe_allow_html=True
)

step1, step2, step3 = st.columns(3, gap="medium")


with step1:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-icon">🌌</div>
            <div class="step-title">Explore</div>
            <div class="step-description">
                Discover the experiences available in our universe.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with step2:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-icon">🎨</div>
            <div class="step-title">Create</div>
            <div class="step-description">
                Express your ideas and explore your creativity.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


with step3:
    st.markdown(
        """
        <div class="step-card">
            <div class="step-icon">💜</div>
            <div class="step-title">Discover</div>
            <div class="step-description">
                Try something new and enjoy your creative journey.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- TEAM ----------------

st.markdown(
    '<div class="section-heading">👩‍💻 Meet the Creators</div>',
    unsafe_allow_html=True
)

team1, team2 = st.columns(2, gap="large")

with team1:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-title">🎨 AI Drawing Studio</div>
            <div class="info-description">
                Created by <b>Purnima Kushwaha</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

with team2:
    st.markdown(
        """
        <div class="info-card">
            <div class="info-title">🌈 MoodSpark</div>
            <div class="info-description">
                Created by <b>Kritika</b>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------- FOOTER ----------------

st.markdown(
    """
    <div class="footer">
        <div style="font-size: 25px;">🌌 ✨ 🎨 🌈</div>
        <b>Creative Universe</b><br>
        Dashboard collaboration: Purnima Kushwaha &amp; Kritika
        <br><br>
        Keep imagining. Keep creating. ✨
        <br>
        © 2026 Creative Universe
    </div>
    """,
    unsafe_allow_html=True
)
