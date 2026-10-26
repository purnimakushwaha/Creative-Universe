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
# APP LINKS
# --------------------------------------------------

DRAWING_URL = "https://ai-drawing-studio.streamlit.app/"
MOODSPARK_URL = "https://moodspark-pe81.onrender.com/"

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "Home"


# --------------------------------------------------
# MAIN BACKGROUND AND GLOBAL CSS
# --------------------------------------------------

st.markdown(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Poppins:wght@300;400;500;600;700&display=swap'
    );

    /* Main application background */

    .stApp {
        background:
            radial-gradient(
                circle at 10% 10%,
                rgba(151, 71, 255, 0.32),
                transparent 35%
            ),
            radial-gradient(
                circle at 90% 20%,
                rgba(0, 217, 255, 0.20),
                transparent 35%
            ),
            radial-gradient(
                circle at 50% 90%,
                rgba(255, 48, 173, 0.22),
                transparent 40%
            ),
            linear-gradient(
                135deg,
                #08051c,
                #100b32,
                #08051c
            );

        color: white;
        font-family: 'Poppins', sans-serif;
    }

    /* Hide Streamlit header */

    header[data-testid="stHeader"] {
        background: transparent;
    }

    /* Main content */

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1250px;
    }

    /* Sidebar */

    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #100b32,
            #1b1045,
            #09071d
        );

        border-right: 1px solid rgba(255,255,255,0.12);
    }

    /* Headings */

    h1, h2, h3 {
        font-family: 'Orbitron', sans-serif !important;
        color: white !important;
    }

    /* Main title */

    .main-title {
        text-align: center;
        font-family: 'Orbitron', sans-serif;

        font-size: clamp(2.2rem, 5vw, 4.2rem);
        font-weight: 900;
        letter-spacing: 3px;

        background: linear-gradient(
            90deg,
            #ff5cf4,
            #9b8cff,
            #37e8ff,
            #ff5cf4
        );

        background-size: 300% 300%;

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        animation: gradientMove 6s ease infinite;

        margin-bottom: 0.5rem;
    }

    @keyframes gradientMove {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .subtitle {
        text-align: center;
        color: #d4d1ff;
        font-size: 1.05rem;
        margin-bottom: 2rem;
    }

    /* Glass cards */

    .glass-card {
        background: rgba(255,255,255,0.065);

        border: 1px solid rgba(255,255,255,0.16);
        border-radius: 22px;

        padding: 22px;

        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);

        box-shadow: 0 10px 35px rgba(0,0,0,0.25);

        transition: transform 0.3s ease,
                    border-color 0.3s ease,
                    box-shadow 0.3s ease;

        min-height: 190px;
    }

    .glass-card:hover {
        transform: translateY(-6px);

        border-color: rgba(133, 116, 255, 0.8);

        box-shadow:
            0 0 25px rgba(132, 88, 255, 0.22),
            0 12px 35px rgba(0,0,0,0.3);
    }

    .card-icon {
        font-size: 2.7rem;
        margin-bottom: 10px;
    }

    .card-title {
        color: white;
        font-family: 'Orbitron', sans-serif;
        font-size: 1.25rem;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .card-description {
        color: #d6d2f5;
        font-size: 0.94rem;
        line-height: 1.7;
    }

    /* Section headings */

    .section-title {
        text-align: center;
        color: #ffffff;
        font-size: 1.65rem;
        font-family: 'Orbitron', sans-serif;
        margin-top: 2.5rem;
        margin-bottom: 1.5rem;
    }

    /* Buttons */

    div.stButton > button,
    div.stLinkButton > a {
        width: 100%;
        min-height: 45px;

        border-radius: 12px !important;
        border: 1px solid rgba(180,150,255,0.65) !important;

        background: linear-gradient(
            100deg,
            #7b35ff,
            #b62cff,
            #493dff
        ) !important;

        color: white !important;
        font-weight: 600 !important;

        transition: all 0.25s ease !important;

        text-decoration: none !important;
    }

    div.stButton > button:hover,
    div.stLinkButton > a:hover {
        transform: translateY(-2px);

        box-shadow:
            0 0 18px rgba(174, 82, 255, 0.55);

        border-color: #ffffff !important;
    }

    /* Team credits */

    .credit-card {
        text-align: center;

        padding: 22px 15px;

        border-radius: 18px;

        background: rgba(255,255,255,0.06);

        border: 1px solid rgba(255,255,255,0.13);
    }

    .credit-name {
        font-size: 1.1rem;
        font-weight: 700;
        color: #ffffff;
    }

    .credit-role {
        color: #c9c2f4;
        font-size: 0.9rem;
        margin-top: 6px;
    }

    /* Divider */

    hr {
        border-color: rgba(255,255,255,0.15) !important;
        margin-top: 2rem;
        margin-bottom: 2rem;
    }

    /* Footer */

    .footer {
        text-align: center;
        color: #a9a2d6;
        padding-top: 2rem;
        font-size: 0.85rem;
    }

    /* Streamlit form elements */

    [data-testid="stAlert"] {
        border-radius: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# --------------------------------------------------
# ANIMATED LOADING SCREEN WITH WAVES
# --------------------------------------------------

def show_app_with_loader(app_name, app_url):

    components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>

        <meta charset="UTF-8">

        <style>

        * {{
            box-sizing: border-box;
        }}

        body {{
            margin: 0;
            padding: 0;

            font-family: Arial, sans-serif;

            background: #08051c;
            color: white;
        }}

        .app-container {{
            position: relative;

            width: 100%;
            height: 780px;

            overflow: hidden;

            background:
                radial-gradient(
                    circle at 20% 20%,
                    rgba(151, 71, 255, 0.3),
                    transparent 40%
                ),
                linear-gradient(
                    135deg,
                    #08051c,
                    #110b32,
                    #08051c
                );

            border-radius: 18px;

            border: 1px solid rgba(255,255,255,0.15);
        }}

        /* Loading overlay */

        .loader {{
            position: absolute;
            inset: 0;

            z-index: 10;

            display: flex;
            flex-direction: column;

            justify-content: center;
            align-items: center;

            overflow: hidden;

            background:
                radial-gradient(
                    circle at 50% 45%,
                    rgba(94, 45, 170, 0.45),
                    transparent 55%
                ),
                #08051c;

            transition: opacity 0.8s ease;
        }}

        .loader.hidden {{
            opacity: 0;
            pointer-events: none;
        }}

        .loader-title {{
            position: relative;
            z-index: 5;

            font-size: clamp(23px, 4vw, 36px);

            font-weight: 800;
            letter-spacing: 2px;

            text-align: center;

            background: linear-gradient(
                90deg,
                #ff62ef,
                #9c8cff,
                #37e8ff
            );

            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .loader-subtitle {{
            position: relative;
            z-index: 5;

            color: #ded9ff;

            font-size: 14px;

            margin-top: 16px;

            text-align: center;
        }}

        /* Wave layers */

        .wave {{
            position: absolute;

            width: 180%;
            height: 260px;

            left: -40%;

            border-radius: 43%;

            opacity: 0.48;

            filter: blur(2px);

            animation: waveMove 7s linear infinite;
        }}

        .wave-one {{
            bottom: -90px;

            background: linear-gradient(
                90deg,
                #7b2cff,
                #ed3ca8,
                #584cff
            );
        }}

        .wave-two {{
            bottom: -125px;

            background: linear-gradient(
                90deg,
                #00d9ff,
                #824cff,
                #ff4fc8
            );

            opacity: 0.4;

            animation-duration: 10s;
            animation-direction: reverse;
        }}

        .wave-three {{
            bottom: -160px;

            background: linear-gradient(
                90deg,
                #ff3dcb,
                #4d8dff,
                #a34dff
            );

            opacity: 0.4;

            animation-duration: 13s;
        }}

        @keyframes waveMove {{
            0% {{
                transform: rotate(0deg) translateX(0);
            }}

            50% {{
                transform: rotate(180deg) translateX(3%);
            }}

            100% {{
                transform: rotate(360deg) translateX(0);
            }}
        }}

        /* Floating particles */

        .particle {{
            position: absolute;

            width: 5px;
            height: 5px;

            border-radius: 50%;

            background: #ffffff;

            box-shadow:
                0 0 10px #8e72ff,
                0 0 20px #42eaff;

            animation: floatUp linear infinite;
        }}

        @keyframes floatUp {{
            from {{
                transform: translateY(800px);
                opacity: 0;
            }}

            20% {{
                opacity: 1;
            }}

            80% {{
                opacity: 0.8;
            }}

            to {{
                transform: translateY(-100px);
                opacity: 0;
            }}
        }}

        /* Spinner */

        .spinner {{
            position: relative;
            z-index: 5;

            width: 48px;
            height: 48px;

            margin-top: 25px;

            border: 4px solid rgba(255,255,255,0.15);

            border-top: 4px solid #ff63ed;
            border-right: 4px solid #47e5ff;

            border-radius: 50%;

            animation: spin 1s linear infinite;
        }}

        @keyframes spin {{
            to {{
                transform: rotate(360deg);
            }}
        }}

        /* App iframe */

        .app-frame {{
            width: 100%;
            height: 100%;

            border: none;

            background: #08051c;
        }}

        .fallback {{
            position: relative;
            z-index: 20;

            margin-top: 8px;

            text-align: center;

            font-size: 13px;
            color: #d5ceff;
        }}

        .fallback a {{
            color: #68eaff;
            font-weight: bold;
            text-decoration: none;
        }}

        </style>
        </head>

        <body>

        <div class="app-container">

            <!-- Animated loading screen -->

            <div class="loader" id="loader">

                <div class="loader-title">
                    ✨ Entering {app_name} ✨
                </div>

                <div class="loader-subtitle" id="status">
                    Creating your creative space...
                </div>

                <div class="spinner"></div>

                <div class="wave wave-one"></div>
                <div class="wave wave-two"></div>
                <div class="wave wave-three"></div>

                <div class="particle"
                     style="left:10%;animation-duration:8s;"></div>

                <div class="particle"
                     style="left:25%;animation-duration:11s;animation-delay:2s;"></div>

                <div class="particle"
                     style="left:45%;animation-duration:9s;animation-delay:1s;"></div>

                <div class="particle"
                     style="left:65%;animation-duration:12s;animation-delay:3s;"></div>

                <div class="particle"
                     style="left:85%;animation-duration:10s;animation-delay:1s;"></div>

            </div>

            <!-- Actual application -->

            <iframe
                class="app-frame"
                id="appFrame"
                src="{app_url}"
                title="{app_name}"
                allow="clipboard-read; clipboard-write"
                onload="hideLoader()">
            </iframe>

        </div>

        <div class="fallback">
            App not appearing?
            <a href="{app_url}" target="_blank" rel="noopener">
                Open {app_name} in a new tab ↗
            </a>
        </div>

        <script>

        function hideLoader() {{

            const loader = document.getElementById("loader");

            if (loader) {{

                setTimeout(function() {{

                    loader.classList.add("hidden");

                }}, 700);

            }}

        }}

        // Update loading messages

        const messages = [
            "Creating your creative space...",
            "Painting the digital universe...",
            "Connecting the stars...",
            "Almost ready..."
        ];

        let messageIndex = 0;

        setInterval(function() {{

            const status = document.getElementById("status");

            if (status) {{

                messageIndex =
                    (messageIndex + 1) % messages.length;

                status.textContent = messages[messageIndex];

            }}

        }}, 1800);

        </script>

        </body>
        </html>
        """,
        height=810,
        scrolling=False
    )


# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:

    st.markdown(
        """
        <div style="text-align:center; padding:15px 0 25px 0;">

            <div style="font-size:3.5rem;">🌌</div>

            <div style="
                font-family:Orbitron,sans-serif;
                font-size:1.4rem;
                font-weight:800;
                color:white;
            ">
                CREATIVE
            </div>

            <div style="
                font-family:Orbitron,sans-serif;
                font-size:1.4rem;
                font-weight:800;
                color:#b99aff;
            ">
                UNIVERSE
            </div>

            <p style="color:#c9c2f4;font-size:0.85rem;">
                Your imagination, your universe.
            </p>

        </div>
        """,
        unsafe_allow_html=True
    )

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

    st.markdown(
        """
        <div style="
            background:rgba(255,255,255,0.06);
            border:1px solid rgba(255,255,255,0.12);
            padding:14px;
            border-radius:14px;
            margin-bottom:12px;
        ">
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
            border-radius:14px;
        ">
            <div style="color:#e5d8ff;font-weight:700;">
                Kritika
            </div>
            <div style="color:#bcb4e7;font-size:0.82rem;">
                Creator — MoodSpark
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#a9a2d6;
            font-size:0.8rem;
        ">
            Made with 💜 and imagination
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# HOME PAGE
# --------------------------------------------------

if st.session_state.page == "Home":

    st.markdown(
        """
        <div class="main-title">
            CREATIVE UNIVERSE
        </div>

        <div class="subtitle">
            ✨ Explore your imagination. Discover your creativity. ✨
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="
            text-align:center;
            padding:22px;
            margin-bottom:30px;
            border-radius:20px;

            background:rgba(255,255,255,0.045);
            border:1px solid rgba(255,255,255,0.12);
        ">
            <div style="font-size:1.2rem;color:#e8e2ff;">
                Welcome to your creative universe!
            </div>

            <p style="
                color:#c5bee8;
                line-height:1.8;
                max-width:750px;
                margin:12px auto 0 auto;
            ">
                A place where imagination meets technology.
                Create beautiful AI-generated artwork and explore
                a world of moods, ideas and inspiration.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">🚀 EXPLORE OUR UNIVERSE</div>',
        unsafe_allow_html=True
    )

    # Application cards

    col1, col2 = st.columns(2, gap="large")

    with col1:

        st.markdown(
            """
            <div class="glass-card">

                <div class="card-icon">🎨</div>

                <div class="card-title">
                    AI Drawing Studio
                </div>

                <div class="card-description">
                    Turn your ideas into visual creations.
                    Explore your imagination and create artwork
                    with the power of artificial intelligence.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "🎨 Enter Drawing Studio",
            key="enter_drawing",
            use_container_width=True
        ):
            st.session_state.page = "AI Drawing Studio"
            st.rerun()

    with col2:

        st.markdown(
            """
            <div class="glass-card">

                <div class="card-icon">✨</div>

                <div class="card-title">
                    MoodSpark
                </div>

                <div class="card-description">
                    Explore moods, discover inspiration and
                    find creative sparks for your day.
                    Give your ideas a little extra magic.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        if st.button(
            "✨ Enter MoodSpark",
            key="enter_moodspark",
            use_container_width=True
        ):
            st.session_state.page = "MoodSpark"
            st.rerun()

    # Team section

    st.markdown("---")

    st.markdown(
        '<div class="section-title">💜 THE CREATORS</div>',
        unsafe_allow_html=True
    )

    team1, team2 = st.columns(2, gap="large")

    with team1:

        st.markdown(
            """
            <div class="credit-card">

                <div style="font-size:2.5rem;">👩‍🎨</div>

                <div class="credit-name">
                    Purnima Kushwaha
                </div>

                <div class="credit-role">
                    Creator of AI Drawing Studio
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with team2:

        st.markdown(
            """
            <div class="credit-card">

                <div style="font-size:2.5rem;">👩‍💻</div>

                <div class="credit-name">
                    Kritika
                </div>

                <div class="credit-role">
                    Creator of MoodSpark
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown(
        """
        <div class="footer">
            🌌 Creative Universe · Where imagination comes alive ✨
        </div>
        """,
        unsafe_allow_html=True
    )


# --------------------------------------------------
# AI DRAWING STUDIO PAGE
# --------------------------------------------------

elif st.session_state.page == "AI Drawing Studio":

    st.markdown(
        """
        <div class="main-title">
            🎨 AI DRAWING STUDIO
        </div>

        <div class="subtitle">
            Turn your imagination into art.
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("← Back to Home", key="back_drawing"):
        st.session_state.page = "Home"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    show_app_with_loader(
        "AI Drawing Studio",
        DRAWING_URL
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.link_button(
        "↗ Open AI Drawing Studio Directly",
        DRAWING_URL,
        use_container_width=True
    )


# --------------------------------------------------
# MOODSPARK PAGE
# --------------------------------------------------

elif st.session_state.page == "MoodSpark":

    st.markdown(
        """
        <div class="main-title">
            ✨ MOODSPARK
        </div>

        <div class="subtitle">
            Find your spark. Explore your mood.
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("← Back to Home", key="back_moodspark"):
        st.session_state.page = "Home"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    show_app_with_loader(
        "MoodSpark",
        MOODSPARK_URL
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.link_button(
        "↗ Open MoodSpark Directly",
        MOODSPARK_URL,
        use_container_width=True
    )
