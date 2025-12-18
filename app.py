import streamlit as st

st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

st.markdown(
    """
    <style>
    /* ===== Base App ===== */
    html, body, [class*="css"] {
        background-color: #000000 !important;
    }

    .stApp {
        background-color: #000000;
    }

    /* ===== Emoji Background ===== */
    .emoji-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        z-index: 0;
        pointer-events: none;
        opacity: 0.18;
        font-size: 42px;
        line-height: 1.6;
        color: white;
        white-space: pre-wrap;
        padding: 20px;
    }

    /* ===== Content Layer ===== */
    .content {
        position: relative;
        z-index: 10;
    }

    .box {
        background-color: #f2f2f2;
        padding: 25px;
        border-radius: 25px;
        margin-bottom: 25px;
        text-align: center;
    }

    .title {
        font-size: 36px;
        font-weight: bold;
        color: #000;
    }

    .subtitle {
        font-size: 18px;
        color: #111;
    }

    .label {
        color: #ffffff;
        font-size: 18px;
        margin-bottom: 8px;
    }

    textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 15px !important;
        font-size: 16px !important;
    }

    .stButton>button {
        background-color: #1d4ed8;
        color: white;
        border-radius: 15px;
        padding: 10px 30px;
        font-size: 16px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #2563eb;
    }

    .success {
        background-color: #14532d;
        color: #bbf7d0;
        padding: 16px;
        border-radius: 15px;
        margin-top: 20px;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== Emoji Background =====
st.markdown(
    """
    <div class="emoji-bg">
    😀 😢 😡 😱 😍 😐 🙂 😭 😠 💙 💚 💛 🧠
    😀 😢 😡 😱 😍 😐 🙂 😭 😠 💙 💚 💛 🧠
    😀 😢 😡 😱 😍 😐 🙂 😭 😠 💙 💚 💛 🧠
    😀 😢 😡 😱 😍 😐 🙂 😭 😠 💙 💚 💛 🧠
    </div>
    """,
    unsafe_allow_html=True
)

# ===== Content =====
st.markdown('<div class="content">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="box">
        <div class="title">🧠 Emotion Detection App</div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="box">
        <div class="subtitle">
            AI-powered text emotion analysis using NLP
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="label">✍️ اكتب الجملة هنا:</div>', unsafe_allow_html=True)

text = st.text_area(
    "",
    height=120,
    placeholder="اكتب الجملة التي تريد تحليل مشاعرها..."
)

if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال جملة أولاً")
    else:
        st.markdown(
            """
            <div class="success">
                ✅ تم استلام الجملة بنجاح<br>
                🔍 سيتم تحليل المشاعر بعد ربط النموذج
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown('</div>', unsafe_allow_html=True)

