import streamlit as st

# ---------------- PAGE CONFIGURATION ----------------
st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
/* Main background */
.stApp {
    background:
        radial-gradient(ellipse at top left, #30205e 0%, transparent 45%),
        radial-gradient(ellipse at bottom right, #123c66 0%, transparent 45%),
        linear-gradient(135deg, #090b1a, #14112b, #071827);
    color: #ffffff;
}

/* Hide Streamlit header and footer */
header[data-testid="stHeader"] {
    background: transparent;
}

footer {
    visibility: hidden;
}

/* Main content width */
.block-container {
    max-width: 1150px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Hero section */
.hero {
    text-align: center;
    padding: 45px 20px 35px 20px;
}

.hero-badge {
    display: inline-block;
    padding: 8px 18px;
    border: 1px solid rgba(255,255,255,0.22);
    border-radius: 30px;
    background: rgba(255,255,255,0.07);
    color: #d9c8ff;
    font-size: 14px;
    letter-spacing: 1px;
    margin-bottom: 20px;
}

.hero h1 {
    font-size: clamp(38px, 6vw, 68px);
    font-weight: 800;
    line-height: 1.15;
    margin: 10px 0;
    color: #ffffff;
}

.gradient-text {
    background: linear-gradient(90deg, #b8a0ff, #74e4ff, #ffb4df);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.hero p {
    color: #d0cce5;
    font-size: 18px;
    max-width: 700px;
    margin: 18px auto;
    line-height: 1.8;
}

/* Section headings */
.section-title {
    text-align: center;
    font-size: 32px;
    font-weight: 750;
    color: #ffffff;
    margin-top: 30px;
    margin-bottom: 8px;
}

.section-subtitle {
    text-align: center;
    color: #b9b6d0;
    font-size: 16px;
    margin-bottom: 30px;
}

/* App cards */
.app-card {
    min-height: 350px;
    padding: 30px 25px;
    border-radius: 24px;
    background: rgba(255,255,255,0.065);
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 12px 35px rgba(0,0,0,0.20);
    transition: all 0.3s ease;
    text-align: center;
    margin-bottom: 15px;
}

.app-card:hover {
    transform: translateY(-6px);
    border-color: rgba(190,160,255,0.65);
    background: rgba(255,255,255,0.10);
    box-shadow: 0 18px 40px rgba(0,0,0,0.30);
}

.app-icon {
    font-size: 55px;
    margin-bottom: 15px;
}

.app-card h3 {
    color: #ffffff;
    font-size: 25px;
    margin: 10px 0;
}

.app-card p {
    color: #d0cce5;
    font-size: 15px;
    line-height: 1.8;
    min-height: 80px;
}

.card-tag {
    display: inline-block;
    padding: 6px 12px;
    border-radius: 20px;
    background: rgba(175,145,255,0.15);
    color: #d8c8ff;
    font-size: 12px;
    margin: 8px 0 15px 0;
}

/* Streamlit buttons */
.stLinkButton > a {
    border-radius: 12px !important;
    border: 1px solid #a994ff !important;
    background: linear-gradient(90deg, #7957e8, #527ce8) !important;
    color: white !important;
    font-weight: 650 !important;
    padding: 12px 20px !important;
    transition: all 0.2s ease !important;
}

.stLinkButton > a:hover {
    border-color: #ffffff !important;
    filter: brightness(1.12);
}

/* Information panel */
.info-panel {
    padding: 25px;
    border-radius: 20px;
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.12);
    margin-top: 15px;
    margin-bottom: 15px;
}

.info-panel h3 {
    color: #c9b9ff;
    margin-top: 0;
}

.info-panel p {
    color: #d0cce5;
    line-height: 1.8;
}

/* Step cards */
.step-card {
    text-align: center;
    padding: 22px 15px;
    border-radius: 18px;
    background: rgba(255,255,255,0.055);
    border: 1px solid rgba(255,255,255,0.10);
    min-height: 155px;
    margin-bottom: 12px;
}

.step-number {
    font-size: 28px;
    margin-bottom: 8px;
}

.step-card h4 {
    color: #ffffff;
    margin: 8px 0;
}

.step-card p {
    color: #c7c3dd;
    font-size: 14px;
    line-height: 1.6;
}

/* Footer */
.custom-footer {
    text-align: center;
    padding: 30px 10px 10px 10px;
    margin-top: 35px;
    border-top: 1px solid rgba(255,255,255,0.12);
    color: #aaa6c4;
    font-size: 14px;
    line-height: 1.9;
}

/* Mobile layout */
@media (max-width: 768px) {
    .hero {
        padding-top: 25px;
    }

    .hero p {
        font-size: 16px;
    }

    .section-title {
        font-size: 27px;
    }

    .app-card {
        min-height: auto;
    }
}
</style>
""", unsafe_allow_html=True)


# ---------------- HERO SECTION ----------------
st.markdown("""
<div class="hero">
    <div class="hero-badge">✦ YOUR SPACE TO CREATE & EXPLORE ✦</div>

    <h1>
        Welcome to<br>
        <span class="gradient-text">Creative Universe 🌌</span>
    </h1>

    <p>
        A little universe of imagination, creativity, and self-discovery.
        Explore your artistic side, discover your emotions, and turn your
        ideas into something meaningful.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- APPLICATIONS SECTION ----------------
st.markdown("""
<div class="section-title">✨ Explore Our Universe</div>
<div class="section-subtitle">
    Choose an experience and begin your journey.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2, gap="large")

# Drawing app card
with col1:
    st.markdown("""
    <div class="app-card">
        <div class="app-icon">🎨</div>
        <h3>AI Drawing Studio</h3>
        <div class="card-tag">ART • IMAGINATION • CREATIVITY</div>
        <p>
            Bring your imagination to life. Explore your creative side
            and turn your ideas into artistic experiences.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "🎨 Open AI Drawing Studio",
        "https://ai-drawing-studio.streamlit.app/",
        use_container_width=True
    )

# MoodSpark app card
with col2:
    st.markdown("""
    <div class="app-card">
        <div class="app-icon">🌈</div>
        <h3>MoodSpark</h3>
        <div class="card-tag">MOOD • EMOTIONS • WELL-BEING</div>
        <p>
            Take a moment for yourself. Explore your mood, reflect on
            your feelings, and make space for a little positivity.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.link_button(
        "🌈 Explore MoodSpark",
        "https://moodspark-pe81.onrender.com/",
        use_container_width=True
    )


# ---------------- ABOUT SECTION ----------------
st.markdown("""
<div class="section-title">💫 About Creative Universe</div>
<div class="section-subtitle">
    Two different experiences, one creative destination.
</div>

<div class="info-panel">
    <h3>🌠 A universe of possibilities</h3>
    <p>
        Creative Universe brings together two experiences designed to
        encourage creativity and self-expression. Whether you want to
        explore art or take a moment to understand your mood, there is
        something here for you.
    </p>
    <p>
        <b>Our idea:</b> Make creativity accessible, encourage exploration,
        and give imagination room to grow.
    </p>
</div>
""", unsafe_allow_html=True)


# ---------------- HOW TO GET STARTED ----------------
st.markdown("""
<div class="section-title">🚀 Your Journey Starts Here</div>
<div class="section-subtitle">
    Three simple steps to explore.
</div>
""", unsafe_allow_html=True)

step1, step2, step3 = st.columns(3, gap="medium")

with step1:
    st.markdown("""
    <div class="step-card">
        <div class="step-number">🌌</div>
        <h4>01. Explore</h4>
        <p>Discover the experiences available in our universe.</p>
    </div>
    """, unsafe_allow_html=True)

with step2:
    st.markdown("""
    <div class="step-card">
        <div class="step-number">✨</div>
        <h4>02. Create</h4>
        <p>Express your ideas, imagination, and individuality.</p>
    </div>
    """, unsafe_allow_html=True)

with step3:
    st.markdown("""
    <div class="step-card">
        <div class="step-number">💜</div>
        <h4>03. Discover</h4>
        <p>Try something new and enjoy your own creative journey.</p>
    </div>
    """, unsafe_allow_html=True)


# ---------------- FOOTER ----------------
st.markdown("""
<div class="custom-footer">
    <div style="font-size: 24px;">🌌 ✨ 🎨 🌈</div>

    <b>Creative Universe</b><br>
    Made with creativity and a little bit of magic.

    <br><br>

    <span style="color:#c9b9ff;">Dashboard</span><br>
    Purnima Kushwaha &amp; Kritika

    <br><br>

    <span style="color:#c9b9ff;">AI Drawing Studio</span><br>
    Purnima Kushwaha

    <br><br>

    <span style="color:#c9b9ff;">MoodSpark</span><br>
    Kritika

    <br><br>

    © 2026 Creative Universe • Keep imagining. Keep creating.
</div>
""", unsafe_allow_html=True)
