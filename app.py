import streamlit as st

st.set_page_config(
    page_title="Creative Universe | Create. Explore. Express.",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# APP CONFIGURATION
# --------------------------------------------------

DRAWING_APP_URL = "https://ai-drawing-studio.streamlit.app/"
MOOD_APP_URL = "https://moodspark-pe81.onrender.com/"

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
    );

    :root {
        --background: #0b0d1e;
        --surface: rgba(255, 255, 255, 0.055);
        --border: rgba(255, 255, 255, 0.12);
        --text: #f8f7ff;
        --muted: #b8bdd6;
        --purple: #a78bfa;
        --blue: #7dd3fc;
        --pink: #f0abfc;
    }

    /* PAGE BACKGROUND */

    .stApp {
        background:
            radial-gradient(
                circle at 8% 8%,
                rgba(124, 58, 237, 0.20),
                transparent 32%
            ),
            radial-gradient(
                circle at 92% 25%,
                rgba(59, 130, 246, 0.15),
                transparent 30%
            ),
            linear-gradient(
                145deg,
                #090b19 0%,
                #11142b 52%,
                #171129 100%
            );

        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 2rem;
        padding-bottom: 1rem;
    }

    #MainMenu,
    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* HERO SECTION */

    .hero {
        position: relative;
        text-align: center;
        padding: 65px 16px 55px;
    }

    .hero-badge {
        display: inline-block;
        padding: 9px 17px;
        border: 1px solid rgba(196, 181, 253, 0.25);
        border-radius: 50px;
        background: rgba(139, 92, 246, 0.10);
        color: #ddd6fe;
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 1.4px;
        margin-bottom: 25px;
    }

    .hero h1 {
        font-size: clamp(2.7rem, 7vw, 5rem);
        line-height: 1.12;
        letter-spacing: -2.5px;
        font-weight: 800;
        margin: 0 0 22px;

        background: linear-gradient(
            100deg,
            #ffffff 5%,
            #c4b5fd 42%,
            #93c5fd 72%,
            #f0abfc 100%
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-description {
        max-width: 660px;
        margin: 0 auto;
        color: #d0d2e9;
        font-size: clamp(1rem, 2vw, 1.16rem);
        line-height: 1.9;
    }

    .hero-note {
        color: #969bbb;
        font-size: 0.88rem;
        margin-top: 17px;
    }

    /* SECTION HEADINGS */

    .section-heading {
        text-align: center;
        margin: 15px 0 30px;
    }

    .section-heading h2 {
        color: #ffffff;
        font-size: clamp(1.6rem, 4vw, 2.1rem);
        font-weight: 700;
        letter-spacing: -0.7px;
        margin-bottom: 10px;
    }

    .section-heading p {
        color: var(--muted);
        font-size: 0.96rem;
        line-height: 1.8;
    }

    /* APP CARDS */

    .app-card {
        position: relative;
        overflow: hidden;
        min-height: 335px;
        padding: 29px 26px;

        border: 1px solid var(--border);
        border-radius: 24px;

        background: linear-gradient(
            145deg,
            rgba(255, 255, 255, 0.085),
            rgba(255, 255, 255, 0.025)
        );

        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);

        transition:
            transform 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }

    .app-card:hover {
        transform: translateY(-5px);
        border-color: var(--accent);

        box-shadow:
            0 15px 40px var(--glow);
    }

    .drawing-card {
        --accent: rgba(167, 139, 250, 0.8);
        --glow: rgba(139, 92, 246, 0.12);
    }

    .mood-card {
        --accent: rgba(240, 171, 252, 0.8);
        --glow: rgba(217, 70, 239, 0.12);
    }

    .card-top {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 25px;
    }

    .app-icon {
        width: 68px;
        height: 68px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 20px;
        font-size: 2.25rem;
    }

    .drawing-icon {
        background: rgba(139, 92, 246, 0.17);
        border: 1px solid rgba(167, 139, 250, 0.3);
    }

    .mood-icon {
        background: rgba(217, 70, 239, 0.13);
        border: 1px solid rgba(240, 171, 252, 0.3);
    }

    .card-number {
        color: #9599b8;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 1.3px;
    }

    .app-card h3 {
        color: #ffffff;
        font-size: 1.48rem;
        font-weight: 700;
        letter-spacing: -0.5px;
        margin-bottom: 12px;
    }

    .app-description {
        color: #c5c8df;
        font-size: 0.93rem;
        line-height: 1.85;
        min-height: 82px;
        margin-bottom: 20px;
    }

    .feature-chip {
        display: inline-block;
        padding: 7px 11px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        border-radius: 30px;
        background: rgba(255, 255, 255, 0.045);
        color: #d9d5f2;
        font-size: 0.73rem;
        font-weight: 500;
    }

    /* BUTTONS */

    div.stLinkButton {
        margin-top: 14px;
        margin-bottom: 8px;
    }

    div.stLinkButton > a {
        display: flex;
        min-height: 51px;
        align-items: center;
        justify-content: center;

        border-radius: 13px;
        border: 1px solid rgba(196, 181, 253, 0.25);

        background: linear-gradient(
            100deg,
            #7c3aed,
            #6366f1
        );

        color: #ffffff !important;
        font-size: 0.94rem;
        font-weight: 700;

        transition:
            transform 0.2s ease,
            filter 0.2s ease,
            box-shadow 0.2s ease;
    }

    div.stLinkButton > a:hover {
        transform: translateY(-2px);
        filter: brightness(1.12);
        box-shadow: 0 8px 25px rgba(124, 58, 237, 0.28);
    }

    /* HOW IT WORKS */

    .steps-grid {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 17px;
        margin-top: 25px;
    }

    .step-card {
        padding: 24px 19px;
        text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.09);
        border-radius: 19px;
        background: rgba(255, 255, 255, 0.035);
    }

    .step-icon {
        font-size: 1.9rem;
        margin-bottom: 13px;
    }

    .step-card h3 {
        color: #eeeaff;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 9px;
    }

    .step-card p {
        color: #aeb3d0;
        font-size: 0.84rem;
        line-height: 1.8;
        margin-bottom: 0;
    }

    /* ABOUT */

    .about-box {
        padding: 29px 25px;
        border: 1px solid rgba(196, 181, 253, 0.14);
        border-radius: 21px;

        background: linear-gradient(
            120deg,
            rgba(124, 58, 237, 0.09),
            rgba(96, 165, 250, 0.055)
        );

        text-align: center;
    }

    .about-box h3 {
        color: #e9ddff;
        font-size: 1.12rem;
        margin-bottom: 12px;
    }

    .about-box p {
        color: #bfc3dc;
        font-size: 0.91rem;
        line-height: 1.9;
        margin-bottom: 0;
    }

    /* FOOTER */

    .footer {
        text-align: center;
        padding: 34px 10px 15px;
    }

    .footer-title {
        color: #e5dcff;
        font-size: 0.98rem;
        font-weight: 800;
        letter-spacing: 1.4px;
    }

    .footer-text {
        color: #9298b6;
        font-size: 0.81rem;
        line-height: 2;
        margin-top: 12px;
    }

    .footer-highlight {
        color: #c4b5fd;
        font-weight: 600;
    }

    .divider {
        height: 1px;
        border: 0;
        margin: 45px 0 35px;

        background: linear-gradient(
            90deg,
            transparent,
            rgba(196, 181, 253, 0.3),
            transparent
        );
    }

    /* MOBILE RESPONSIVENESS */

    @media (max-width: 768px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero {
            padding: 35px 4px 40px;
        }

        .hero h1 {
            letter-spacing: -1.3px;
        }

        .app-card {
            min-height: auto;
            padding: 24px 20px;
        }

        .app-description {
            min-height: auto;
        }

        .steps-grid {
            grid-template-columns: 1fr;
        }

        .divider {
            margin: 32px 0 25px;
        }
    }

    @media (prefers-reduced-motion: reduce) {
        *,
        *::before,
        *::after {
            transition-duration: 0.01ms !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# HERO
# --------------------------------------------------

st.markdown(
    """
    <div class="hero">
        <div class="hero-badge">
            ✦ YOUR LITTLE CORNER OF CREATIVITY ✦
        </div>

        <h1>Creative Universe 🌌</h1>

        <p class="hero-description">
            Your imagination deserves a space of its own.
            Explore creative experiences, express yourself,
            and discover something new along the way.
        </p>

        <p class="hero-note">
            Two experiences. One place. Endless possibilities.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# APP SELECTION
# --------------------------------------------------

st.markdown(
    """
    <div class="section-heading">
        <h2>Where would you like to begin?</h2>
        <p>
            Pick what interests you today. You can always
            explore the other experience later.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns(2, gap="large")

# DRAWING APP

with left:
    st.markdown(
        """
        <div class="app-card drawing-card">
            <div class="card-top">
                <div class="app-icon drawing-icon">🎨</div>
                <span class="card-number">EXPERIENCE 01</span>
            </div>

            <h3>AI Drawing Studio</h3>

            <p class="app-description">
                Ready to get creative? Explore drawing,
                experiment with ideas, and take on creative
                challenges in your own artistic space.
            </p>

            <span class="feature-chip">
                🎨 Drawing &nbsp; · &nbsp; 💡 Creativity
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.link_button(
        "Let's Create  ↗",
        DRAWING_APP_URL,
        use_container_width=True,
    )

    st.caption("For when you feel like creating something.")

# MOOD APP

with right:
    st.markdown(
        """
        <div class="app-card mood-card">
            <div class="card-top">
                <div class="app-icon mood-icon">💜</div>
                <span class="card-number">EXPERIENCE 02</span>
            </div>

            <h3>MoodSpark</h3>

            <p class="app-description">
                Take a little moment for yourself.
                Explore a mood-focused experience and
                discover a different way to engage with your day.
            </p>

            <span class="feature-chip">
                💜 Mood &nbsp; · &nbsp; ✨ Discovery
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.link_button(
        "Explore MoodSpark  ↗",
        MOOD_APP_URL,
        use_container_width=True,
    )

    st.caption("For when you want to explore something different.")

# --------------------------------------------------
# HOW IT WORKS
# --------------------------------------------------

st.markdown(
    '<hr class="divider">',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-heading">
        <h2>Getting started is easy ✨</h2>
        <p>No complicated navigation. Just choose and explore.</p>
    </div>

    <div class="steps-grid">

        <div class="step-card">
            <div class="step-icon">🧭</div>
            <h3>01. Choose</h3>
            <p>
                Pick the experience that matches
                your curiosity.
            </p>
        </div>

        <div class="step-card">
            <div class="step-icon">🚀</div>
            <h3>02. Explore</h3>
            <p>
                Open the app and discover
                what you can do.
            </p>
        </div>

        <div class="step-card">
            <div class="step-icon">✨</div>
            <h3>03. Enjoy</h3>
            <p>
                Try something new and
                make the experience your own.
            </p>
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# ABOUT THE PROJECT
# --------------------------------------------------

st.markdown(
    '<hr class="divider">',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="about-box">
        <h3>Made with creativity & collaboration 💫</h3>

        <p>
            Creative Universe brings two independent
            applications together in one convenient place.
            Each has its own purpose, personality, and experience.
            <br>
            <br>
            <span style="color:#d8c8ff;">
                One shared space to discover what inspires you.
            </span>
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <div class="footer">
        <div class="footer-title">
            🌌 CREATIVE UNIVERSE
        </div>

        <p class="footer-text">
            A collaborative project by
            <span class="footer-highlight">
                Purnima Kushwaha &amp; Kritika
            </span>
            <br>

            AI Drawing Studio · Purnima Kushwaha
            &nbsp; | &nbsp;
            MoodSpark · Kritika

            <br><br>
            Made with curiosity, creativity &amp; Streamlit ✦
            <br>
            © 2026 Creative Universe
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
