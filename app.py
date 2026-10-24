
import streamlit as st

st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide",
)

# Replace these with your actual deployed app URLs.
DRAWING_APP_URL = "https://ai-drawing-studio.streamlit.app/"
MOOD_APP_URL = "https://moodspark-pe81.onrender.com/?fbclid=PAT01DUAUu2FZleHRuA2FlbQIxMABwZG9mAnNydGMGYXBwX2lkDzU2NzA2NzM0MzM1MjQyNwABp0GciMyRnMyqd0FNDq_F1T2vakUAlXoLo0YTw8PYdg5zyZtXjQEY39qjDVI__aem_8r1z0GkBF224THvCT87eXQ"

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(circle at top left, #35245f, transparent 40%),
            linear-gradient(135deg, #100d25, #21163b, #101326);
        color: white;
    }

    h1, h2, h3, p, label {
        color: white;
    }

    .hero {
        text-align: center;
        padding: 45px 12px 30px 12px;
    }

    .hero h1 {
        font-size: clamp(2.2rem, 5vw, 3.7rem);
        margin-bottom: 10px;
    }

    .hero p {
        color: #d8cbed;
        font-size: 1.1rem;
    }

    .app-card {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 22px;
        padding: 28px 22px;
        min-height: 235px;
        text-align: center;
    }

    .app-icon {
        font-size: 3rem;
        margin-bottom: 12px;
    }

    .app-description {
        color: #e2dcef;
        min-height: 55px;
    }

    .credits {
        text-align: center;
        color: #c9bfdc;
        padding: 30px 0 15px 0;
    }

    div.stLinkButton > a {
        width: 100%;
        justify-content: center;
        border-radius: 12px;
        font-weight: 600;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero">
        <h1>🌌 Creative Universe</h1>
        <p>One universe. Two creative experiences.</p>
        <p>Explore your imagination and discover your mood.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

left, right = st.columns(2, gap="large")

with left:
    st.markdown(
        """
        <div class="app-card">
            <div class="app-icon">🎨</div>
            <h2>AI Drawing Studio</h2>
            <p class="app-description">
                Draw, experiment with creative challenges,
                and explore your artistic imagination.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    if DRAWING_APP_URL.startswith("https://"):
        st.link_button(
            "Open AI Drawing Studio ↗",
            DRAWING_APP_URL,
            use_container_width=True,
        )
    else:
        st.warning("Add your deployed AI Drawing Studio URL in app.py.")

with right:
    st.markdown(
        """
        <div class="app-card">
            <div class="app-icon">💜</div>
            <h2>MoodSpark</h2>
            <p class="app-description">
                Explore Kritika's mood-focused experience
                and discover what the app offers.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")
    if MOOD_APP_URL.startswith("https://"):
        st.link_button(
            "Open MoodSpark ↗",
            MOOD_APP_URL,
            use_container_width=True,
        )
    else:
        st.warning("Add the deployed MoodSpark URL in app.py.")

st.markdown("---")

st.markdown(
    """
    <div class="credits">
        <p><b>Creative Universe</b></p>
        <p>Dashboard collaboration: Purnima Kushwaha & Kritika</p>
        <p>AI Drawing Studio: Purnima Kushwaha · MoodSpark: Kritika</p>
        <p>Each original application remains in its own repository.</p>
    </div>
    """,
    unsafe_allow_html=True,
)
