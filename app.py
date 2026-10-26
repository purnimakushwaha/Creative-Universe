```python
import streamlit as st

st.set_page_config(
    page_title="Creative Universe | Explore Your Imagination",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# --------------------------------------------------
# APP URLS
# --------------------------------------------------

DRAWING_APP_URL = "https://ai-drawing-studio.streamlit.app/"
MOOD_APP_URL = (
    "https://moodspark-pe81.onrender.com/"
    "?fbclid=PAT01DUAUu2FZleHRuA2FlbQIxMABwZG9mAnNydGMGYXBwX2lkDzU2NzA2NzM0MzM1MjQyNwABp0GciMyRnMyqd0FNDq_F1T2vakUAlXoLo0YTw8PYdg5zyZtXjQEY39qjDVI__aem_8r1z0GkBF224THvCT87eXQ"
)

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(
    """
    <style>
    @import url(
        'https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap'
    );

    :root {
        --bg: #080b1a;
        --text: #f8f7ff;
        --muted: #b8bbd6;
        --purple: #a78bfa;
        --blue: #60a5fa;
        --pink: #f0abfc;
    }

    /* Main background */

    .stApp {
        background:
            radial-gradient(
                ellipse at 12% 5%,
                rgba(124, 58, 237, 0.23),
                transparent 35%
            ),
            radial-gradient(
                ellipse at 90% 25%,
                rgba(59, 130, 246, 0.16),
                transparent 35%
            ),
            linear-gradient(
                145deg,
                #080b1a 0%,
                #11132b 48%,
                #17112e 100%
            );

        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    /* Page spacing */

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 1rem;
    }

    /* Hide Streamlit chrome */

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Top badge */

    .top-badge {
        display: inline-block;
        padding: 9px 17px;
        border: 1px solid rgba(196, 181, 253, 0.3);
        border-radius: 50px;
        background: rgba(139, 92, 246, 0.10);
        color: #ddd6fe;
        font-size: 0.8rem;
        font-weight: 600;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        margin-bottom: 24px;
    }

    /* Hero section */

    .hero {
        text-align: center;
        padding: 55px 15px 50px;
    }

    .hero h1 {
        font-size: clamp(2.8rem, 6vw, 5rem);
        font-weight: 800;
        letter-spacing: -3px;
        line-height: 1.1;
        margin: 0 0 22px 0;

        background: linear-gradient(
            100deg,
            #ffffff 5%,
            #c4b5fd 45%,
            #93c5fd 75%,
            #f0abfc 100%
        );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-subtitle {
        color: #e0def5;
        font-size: clamp(1rem, 2vw, 1.25rem);
        line-height: 1.8;
        max-width: 700px;
        margin: 0 auto;
    }

    .hero-caption {
        color: #9298bd;
        font-size: 0.92rem;
        margin-top: 12px;
    }

    /* Section heading */

    .section-heading {
        text-align: center;
        margin: 18px 0 35px;
    }

    .section-heading h2 {
        color: #ffffff;
        font-size: 1.9rem;
        font-weight: 700;
        letter-spacing: -0.8px;
        margin-bottom: 8px;
    }

    .section-heading p {
        color: var(--muted);
        font-size: 0.98rem;
    }

    /* App cards */

    .app-card {
        position: relative;
        overflow: hidden;

        min-height: 285px;
        padding: 32px 27px;

        border: 1px solid rgba(255, 255, 255, 0.13);
        border-radius: 24px;

        background: linear-gradient(
            145deg,
            rgba(255, 255, 255, 0.09),
            rgba(255, 255, 255, 0.025)
        );

        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);

        transition:
            transform 0.3s ease,
            border-color 0.3s ease,
            box-shadow 0.3s ease;
    }

    .app-card::before {
        content: "";
        position: absolute;
        top: 0;
        left: 10%;
        width: 80%;
        height: 2px;

        background: linear-gradient(
            90deg,
            transparent,
            var(--card-accent),
            transparent
        );

        opacity: 0.9;
    }

    .app-card:hover {
        transform: translateY(-8px);
        border-color: var(--card-accent);

        box-shadow:
            0 18px 55px rgba(0, 0, 0, 0.25),
            0 0 25px var(--card-glow);
    }

    .drawing-card {
        --card-accent: #a78bfa;
        --card-glow: rgba(139, 92, 246, 0.15);
    }

    .mood-card {
        --card-accent: #f0abfc;
        --card-glow: rgba(217, 70, 239, 0.13);
    }

    .card-top {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 28px;
    }

    .app-icon {
        width: 72px;
        height: 72px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 21px;
        font-size: 2.5rem;
    }

    .drawing-icon {
        background: linear-gradient(
            135deg,
            rgba(139, 92, 246, 0.24),
            rgba(96, 165, 250, 0.14)
        );

        border: 1px solid rgba(167, 139, 250, 0.3);
    }

    .mood-icon {
        background: linear-gradient(
            135deg,
            rgba(217, 70, 239, 0.20),
            rgba(244, 114, 182, 0.12)
        );

        border: 1px solid rgba(240, 171, 252, 0.3);
    }

    .app-number {
        color: #8589aa;
        font-size: 0.8rem;
        font-weight: 700;
        letter-spacing: 2px;
    }

    .app-card h3 {
        color: #ffffff;
        font-size: 1.55rem;
        font-weight: 700;
        margin: 0 0 13px;
        letter-spacing: -0.5px;
    }

    .app-description {
        color: #c0c3dc;
        font-size: 0.96rem;
        line-height: 1.85;
        margin: 0;
    }

    .app-tag {
        display: inline-block;
        margin-top: 23px;
        padding: 7px 12px;

        border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.12);

        background: rgba(255, 255, 255, 0.05);
        color: #d9d5f2;

        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.4px;
    }

    /* Buttons */

    div.stLinkButton {
        margin-top: 13px;
    }

    div.stLinkButton > a {
        min-height: 52px;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 14px;
        border: 1px solid rgba(255, 255, 255, 0.15);

        background: linear-gradient(
            100deg,
            #7c3aed,
            #6366f1
        );

        color: #ffffff !important;

        font-size: 0.95rem;
        font-weight: 700;

        transition:
            transform 0.25s ease,
            box-shadow 0.25s ease,
            filter 0.25s ease;
    }

    div.stLinkButton > a:hover {
        transform: translateY(-2px);
        filter: brightness(1.12);

        box-shadow:
            0 8px 25px rgba(124, 58, 237, 0.3);

        border-color: rgba(196, 181, 253, 0.7);
    }

    /* Mood button override */

    div[data-testid="stVerticalBlock"] .mood-launch div.stLinkButton > a {
        background: linear-gradient(
            100deg,
            #9333ea,
            #db2777
        );
    }

    /* Divider */

    .soft-divider {
        height: 1px;
        border: 0;
        margin: 55px 0 35px;

        background: linear-gradient(
            90deg,
            transparent,
            rgba(196, 181, 253, 0.35),
            transparent
        );
    }

    /* About section */

    .about-box {
        padding: 28px;
        border-radius: 20px;

        background: rgba(255, 255, 255, 0.035);
        border: 1px solid rgba(255, 255, 255, 0.09);

        text-align: center;
    }

    .about-box h3 {
        color: #e9ddff;
        font-size: 1.15rem;
        margin-bottom: 12px;
    }

    .about-box p {
        color: #b8bbd6;
        line-height: 1.9;
        font-size: 0.93rem;
        margin: 0;
    }

    /* Footer */

    .footer {
        text-align: center;
        padding: 35px 10px 18px;
    }

    .footer-title {
        color: #e5dcff;
        font-size: 1rem;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .footer-text {
        color: #8f94b5;
        font-size: 0.82rem;
        line-height: 1.9;
    }

    .footer-highlight {
        color: #c4b5fd;
        font-weight: 600;
    }

    /* Mobile */

    @media (max-width: 768px) {
        .block-container {
            padding-left: 1rem;
            padding-right: 1rem;
        }

        .hero {
            padding: 35px 5px;
        }

        .hero h1 {
            letter-spacing: -1.5px;
        }

        .app-card {
            min-height: auto;
            padding: 26px 22px;
        }

        .section-heading h2 {
            font-size: 1.6rem;
        }

        .soft-divider {
            margin: 35px 0 25px;
        }
    }

    /* Accessibility: reduced motion */

    @media (prefers-reduced-motion: reduce) {
        *,
        *::before,
        *::after {
            animation-duration: 0.01ms !important;
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

        <div class="top-badge">
            ✦ Your Creative Space ✦
        </div>

        <h1>Creative Universe</h1>

        <p class="hero-subtitle">
            A little space for your imagination,
            a little magic for your mood.
        </p>

        <p class="hero-caption">
            Explore ideas. Express yourself. Discover something new.
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# APP SECTION
# --------------------------------------------------

st.markdown(
    """
    <div class="section-heading">
        <h2>Explore Your Universe</h2>
        <p>Choose your experience and let your creativity flow.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns(2, gap="large")

# Drawing Studio

with left:
    st.markdown(
        """
        <div class="app-card drawing-card">

            <div class="card-top">
                <div class="app-icon drawing-icon">🎨</div>
                <span class="app-number">EXPERIENCE 01</span>
            </div>

            <h3>AI Drawing Studio</h3>

            <p class="app-description">
                Turn your imagination into an experience.
                Explore drawing, take on creative challenges,
                and give your ideas a visual form.
            </p>

            <span class="app-tag">
                ✦ ART · IMAGINATION · CREATIVITY
            </span>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    if DRAWING_APP_URL.startswith("https://"):
        st.link_button(
            "Explore Drawing Studio ↗",
            DRAWING_APP_URL,
            use_container_width=True,
        )
    else:
        st.warning("Please configure the Drawing Studio URL.")

# MoodSpark

with right:
    st.markdown(
        """
        <div class="app-card mood-card">

            <div class="card-top">
                <div class="app-icon mood-icon">💜</div>
                <span class="app-number">EXPERIENCE 02</span>
            </div>

            <h3>MoodSpark</h3>

            <p class="app-description">
                Take a moment to explore your mood.
                Discover a mood-focused experience
                designed to bring a little colour to your day.
            </p>

            <span class="app-tag">
                ✦ MOOD · DISCOVERY · EXPRESSION
            </span>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    if MOOD_APP_URL.startswith("https://"):
        st.link_button(
            "Discover MoodSpark ↗",
            MOOD_APP_URL,
            use_container_width=True,
        )
    else:
        st.warning("Please configure the MoodSpark URL.")

# --------------------------------------------------
# ABOUT
# --------------------------------------------------

st.markdown(
    '<hr class="soft-divider">',
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="section-heading">
        <h2>Two Ideas. One Universe.</h2>
        <p>Different experiences, connected by creativity.</p>
    </div>

    <div class="about-box">

        <h3>Built with creativity and collaboration ✨</h3>

        <p>
            Creative Universe brings two independent applications
            together in one place.<br>
            Explore each experience, follow your curiosity,
            and find your own way to create.
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
                Purnima Kushwaha & Kritika
            </span>
            <br>
            AI Drawing Studio · Purnima Kushwaha
            &nbsp; | &nbsp;
            MoodSpark · Kritika
            <br><br>
            Made with creativity, curiosity & Streamlit ✦
            <br>
            © 2026 Creative Universe
        </p>

    </div>
    """,
    unsafe_allow_html=True,
)
```
