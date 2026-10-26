import streamlit as st
import streamlit.components.v1 as components

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Creative Universe",
    page_icon="🌌",
    layout="wide"
)

DRAWING_URL = "https://ai-drawing-studio.streamlit.app/"
MOODSPARK_URL = "https://moodspark-pe81.onrender.com/"

if "page" not in st.session_state:
    st.session_state.page = "Home"


# ==========================================
# GLOBAL STYLING
# ==========================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Poppins:wght@300;400;500;600;700&display=swap');

.stApp {
    background:
        radial-gradient(circle at 10% 10%, #3b1760 0%, transparent 35%),
        radial-gradient(circle at 90% 20%, #123c64 0%, transparent 35%),
        linear-gradient(135deg, #08051c, #100b32, #08051c);
    color: white;
    font-family: 'Poppins', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #100b32, #1b1045, #09071d);
}

h1, h2, h3 {
    color: white !important;
    font-family: 'Orbitron', sans-serif !important;
}

.main-title {
    text-align: center;
    font-family: 'Orbitron', sans-serif;
    font-size: clamp(2rem, 5vw, 4rem);
    font-weight: 900;
    letter-spacing: 2px;
    background: linear-gradient(90deg, #ff5cf4, #9b8cff, #37e8ff);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle {
    text-align: center;
    color: #d4d1ff;
    margin: 15px 0 35px 0;
    font-size: 1.05rem;
}

.welcome-card {
    text-align: center;
    padding: 25px;
    border-radius: 20px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 30px;
}

.welcome-title {
    font-size: 1.3rem;
    font-weight: 600;
}

.welcome-text {
    color: #d0c9f4;
    line-height: 1.8;
    margin-top: 12px;
}

.section-title {
    text-align: center;
    font-family: 'Orbitron', sans-serif;
    font-size: 1.5rem;
    margin: 35px 0 25px 0;
}

.glass-card {
    background: rgba(255,255,255,0.07);
    border: 1px solid rgba(255,255,255,0.16);
    border-radius: 20px;
    padding: 25px;
    min-height: 215px;
    transition: 0.3s ease;
}

.glass-card:hover {
    transform: translateY(-5px);
    border-color: #a78bfa;
    box-shadow: 0 0 25px rgba(140,80,255,0.3);
}

.card-icon {
    font-size: 2.7rem;
}

.card-title {
    font-family: 'Orbitron', sans-serif;
    font-size: 1.2rem;
    font-weight: 700;
    margin: 12px 0;
}

.card-description {
    color: #d6d2f5;
    line-height: 1.7;
    font-size: 0.93rem;
}

.credit-card {
    text-align: center;
    padding: 25px 15px;
    border-radius: 18px;
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.15);
}

.credit-name {
    font-weight: 700;
    font-size: 1.1rem;
    margin-top: 10px;
}

.credit-role {
    color: #c9c2f4;
    font-size: 0.9rem;
    margin-top: 6px;
}

.footer {
    text-align: center;
    color: #aaa2d6;
    padding: 30px 0;
}

div.stButton > button,
div.stLinkButton > a {
    width: 100%;
    min-height: 45px;
    border-radius: 12px;
    background: linear-gradient(100deg, #7b35ff, #b62cff, #493dff);
    color: white;
    border: 1px solid #a78bfa;
    font-weight: 600;
}

div.stButton > button:hover,
div.stLinkButton > a:hover {
    border-color: white;
    box-shadow: 0 0 18px rgba(174,82,255,0.5);
}

hr {
    border-color: rgba(255,255,255,0.15);
}
</style>
""", unsafe_allow_html=True)


# ==========================================
# LOADING SCREEN + EMBEDDED APP
# ==========================================

def show_app_with_loader(app_name, app_url):

    # HTML is rendered inside a component iframe.
    # The colourful loader covers the app until its iframe loads.

    components.html(
        """
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">

        <style>
        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            background: #08051c;
            font-family: Arial, sans-serif;
        }

        .container {
            position: relative;
            width: 100%;
            height: 720px;
            overflow: hidden;
            background: #08051c;
            border-radius: 18px;
        }

        .app-frame {
            width: 100%;
            height: 100%;
            border: none;
            background: #08051c;
        }

        .loader {
            position: absolute;
            inset: 0;
            z-index: 5;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            overflow: hidden;
            background:
                radial-gradient(
                    circle at center,
                    rgba(103,58,183,0.45),
                    transparent 65%
                ),
                #08051c;
            transition: opacity 0.8s ease;
        }

        .loader.hidden {
            opacity: 0;
            pointer-events: none;
        }

        .loader-title {
            z-index: 6;
            text-align: center;
            font-size: clamp(22px, 4vw, 34px);
            font-weight: 900;
            letter-spacing: 2px;
            background: linear-gradient(
                90deg,
                #ff5cf4,
                #9b8cff,
                #37e8ff
            );
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }

        .loader-message {
            z-index: 6;
            color: #ded9ff;
            margin-top: 15px;
            text-align: center;
        }

        .spinner {
            z-index: 6;
            width: 45px;
            height: 45px;
            margin-top: 25px;
            border: 4px solid rgba(255,255,255,0.2);
            border-top-color: #ff63ed;
            border-right-color: #47e5ff;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        .wave {
            position: absolute;
            left: -40%;
            width: 180%;
            height: 260px;
            border-radius: 43%;
            animation: waveMove 8s linear infinite;
        }

        .wave-one {
            bottom: -100px;
            background: linear-gradient(
                90deg, #7b2cff, #ed3ca8, #584cff
            );
            opacity: 0.65;
        }

        .wave-two {
            bottom: -130px;
            background: linear-gradient(
                90deg, #00d9ff, #824cff, #ff4fc8
            );
            opacity: 0.5;
            animation-duration: 11s;
            animation-direction: reverse;
        }

        .wave-three {
            bottom: -165px;
            background: linear-gradient(
                90deg, #ff3dcb, #4d8dff, #a34dff
            );
            opacity: 0.45;
            animation-duration: 14s;
        }

        @keyframes waveMove {
            from { transform: rotate(0deg); }
            to { transform: rotate(360deg); }
        }

        .particle {
            position: absolute;
            width: 5px;
            height: 5px;
            border-radius: 50%;
            background: white;
            box-shadow: 0 0 12px #8e72ff, 0 0 20px #42eaff;
            animation: floatUp 8s linear infinite;
        }

        @keyframes floatUp {
            from {
                transform: translateY(760px);
                opacity: 0;
            }
            20% { opacity: 1; }
            to {
                transform: translateY(-100px);
                opacity: 0;
            }
        }
        </style>
        </head>

        <body>

        <div class="container">

            <div class="loader" id="loader">

                <div class="loader-title" id="title">
                    ✨ Entering Creative Universe ✨
                </div>

                <div class="loader-message" id="message">
                    Creating your creative space...
                </div>

                <div class="spinner"></div>

                <div class="wave wave-one"></div>
                <div class="wave wave-two"></div>
                <div class="wave wave-three"></div>

                <div class="particle" style="left:10%;"></div>
                <div class="particle" style="left:30%;animation-delay:2s;"></div>
                <div class="particle" style="left:50%;animation-delay:1s;"></div>
                <div class="particle" style="left:70%;animation-delay:3s;"></div>
                <div class="particle" style="left:90%;animation-delay:1.5s;"></div>

            </div>

            <iframe
                class="app-frame"
                id="appFrame"
                src="about:blank"
                title="Creative application">
            </iframe>

        </div>

        <script>
        const params = new URLSearchParams(window.location.search);
        const appUrl = params.get("app");

        if (appUrl) {
            document.getElementById("appFrame").src = appUrl;
        }

        const messages = [
            "Creating your creative space...",
            "Painting the digital universe...",
            "Connecting the stars...",
            "Almost ready..."
        ];

        let index = 0;

        setInterval(() => {
            index = (index + 1) % messages.length;
            document.getElementById("message").textContent = messages[index];
        }, 1800);

        document.getElementById("appFrame").addEventListener("load", () => {
            if (document.getElementById("appFrame").src !== "about:blank") {
                setTimeout(() => {
                    document.getElementById("loader").classList.add("hidden");
                }, 500);
            }
        });
        </script>

        </body>
        </html>
        """,
        height=730,
        scrolling=False
    )

    st.link_button(
        f"↗ Open {app_name} in a New Tab",
        app_url,
        use_container_width=True
    )


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.markdown("""
    <div style="text-align:center;padding:15px 0 25px 0;">
        <div style="font-size:3.5rem;">🌌</div>
        <div style="font-family:Orbitron,sans-serif;font-size:1.4rem;font-weight:800;color:white;">
            CREATIVE
        </div>
        <div style="font-family:Orbitron,sans-serif;font-size:1.4rem;font-weight:800;color:#b99aff;">
            UNIVERSE
        </div>
        <p style="color:#c9c2f4;font-size:0.85rem;">
            Your imagination, your universe.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🧭 Navigation")

    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "Home"
        st.rerun()

    if st.button("🎨 AI Drawing Studio", use_container_width=True):
        st.session_state.page = "AI Drawing Studio"
        st.rerun()

    if st.button("✨ MoodSpark", use_container_width=True):
        st.session_state.page = "MoodSpark"
        st.rerun()

    st.markdown("---")
    st.markdown("### 👩‍💻 Our Team")

    st.markdown("""
    <div style="
        background:rgba(255,255,255,0.06);
        border:1px solid rgba(255,255,255,0.12);
        padding:14px;
        border-radius:14px;
        margin-bottom:12px;">
        <div style="color:#e5d8ff;font-weight:700;">
            Purnima Kushwaha
        </div>
        <div style="color:#bcb4e7;font-size:0.82rem;">
            Creator — AI Drawing Studio
        </div>
    </div>

    <div style="
        background:rgba(255,255,255,0.06);
        border:1px solid rgba(255,255,255,0.12);
        padding:14px;
        border-radius:14px;">
        <div style="color:#e5d8ff;font-weight:700;">
            Kritika
        </div>
        <div style="color:#bcb4e7;font-size:0.82rem;">
            Creator — MoodSpark
        </div>
    </div>

    <p style="text-align:center;color:#a9a2d6;font-size:0.8rem;margin-top:20px;">
        Made with 💜 and imagination
    </p>
    """, unsafe_allow_html=True)


# ==========================================
# HOME PAGE
# ==========================================

if st.session_state.page == "Home":

    st.markdown("""
    <div class="main-title">CREATIVE UNIVERSE</div>
    <div class="subtitle">
        ✨ Explore your imagination. Discover your creativity. ✨
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="welcome-card">
        <div class="welcome-title">
            Welcome to your creative universe!
        </div>
        <div class="welcome-text">
            A place where imagination meets technology.
            Create beautiful AI-generated artwork and explore
            a world of moods, ideas and inspiration.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">🚀 EXPLORE OUR UNIVERSE</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown("""
        <div class="glass-card">
            <div class="card-icon">🎨</div>
            <div class="card-title">AI Drawing Studio</div>
            <div class="card-description">
                Turn your ideas into visual creations.
                Explore your imagination and create artwork
                with the power of artificial intelligence.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button("🎨 Enter Drawing Studio", key="drawing", use_container_width=True):
            st.session_state.page = "AI Drawing Studio"
            st.rerun()

    with col2:

        st.markdown("""
        <div class="glass-card">
            <div class="card-icon">✨</div>
            <div class="card-title">MoodSpark</div>
            <div class="card-description">
                Explore moods, discover inspiration and
                find creative sparks for your day.
                Give your ideas a little extra magic.
            </div>
        </div>
        """, unsafe_allow_html=True)

        st.write("")

        if st.button("✨ Enter MoodSpark", key="moodspark", use_container_width=True):
            st.session_state.page = "MoodSpark"
            st.rerun()

    st.markdown("---")

    st.markdown(
        '<div class="section-title">💜 THE CREATORS</div>',
        unsafe_allow_html=True
    )

    team1, team2 = st.columns(2, gap="large")

    with team1:
        st.markdown("""
        <div class="credit-card">
            <div class="credit-icon">👩‍🎨</div>
            <div class="credit-name">Purnima Kushwaha</div>
            <div class="credit-role">
                Creator of AI Drawing Studio
            </div>
        </div>
        """, unsafe_allow_html=True)

    with team2:
        st.markdown("""
        <div class="credit-card">
            <div class="credit-icon">👩‍💻</div>
            <div class="credit-name">Kritika</div>
            <div class="credit-role">
                Creator of MoodSpark
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        🌌 Creative Universe · Where imagination comes alive ✨
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# AI DRAWING STUDIO PAGE
# ==========================================

elif st.session_state.page == "AI Drawing Studio":

    st.markdown("""
    <div class="main-title">🎨 AI DRAWING STUDIO</div>
    <div class="subtitle">Turn your imagination into art.</div>
    """, unsafe_allow_html=True)

    if st.button("← Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    show_app_with_loader("AI Drawing Studio", DRAWING_URL)


# ==========================================
# MOODSPARK PAGE
# ==========================================

elif st.session_state.page == "MoodSpark":

    st.markdown("""
    <div class="main-title">✨ MOODSPARK</div>
    <div class="subtitle">Find your spark. Explore your mood.</div>
    """, unsafe_allow_html=True)

    if st.button("← Back to Home"):
        st.session_state.page = "Home"
        st.rerun()

    show_app_with_loader("MoodSpark", MOODSPARK_URL)
