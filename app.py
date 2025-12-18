import streamlit as st

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

# ================== EMOJI BACKGROUND ==================
st.markdown(
    """
    <style>
    .stApp {
        background-color: black;
    }

    .emoji-bg {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        z-index: -1;
        font-size: 34px;
        line-height: 60px;
        opacity: 0.25;
        white-space: pre-wrap;
        color: white;
        padding: 20px;
    }

    .box {
        background: rgba(255,255,255,0.93);
        padding: 25px;
        border-radius: 20px;
        margin-bottom: 25px;
        text-align: center;
    }

    .title {
        font-size: 40px;
        font-weight: bold;
        color: black;
    }

    .subtitle {
        font-size: 18px;
        color: #333;
    }

    label {
        color: white !important;
        font-size: 18px !important;
        font-weight: bold;
    }

    textarea {
        background-color: white !important;
        color: black !important;
        border-radius: 15px !important;
        border: 3px solid #2563eb !important;
        font-size: 16px !important;
    }

    button[kind="primary"] {
        background: #2563eb !important;
        color: white !important;
        border-radius: 14px !important;
        font-size: 18px !important;
        padding: 10px 25px !important;
    }
    </style>

    <div class="emoji-bg">
    😀 😢 😡 😱 ❤️ 🙂 😭 😍 😠 😮 💙 😁 😞 😤 😨 💛
    😀 😢 😡 😱 ❤️ 🙂 😭 😍 😠 😮 💙 😁 😞 😤 😨 💛
    😀 😢 😡 😱 ❤️ 🙂 😭 😍 😠 😮 💙 😁 😞 😤 😨 💛
    😀 😢 😡 😱 ❤️ 🙂 😭 😍 😠 😮 💙 😁 😞 😤 😨 💛
    😀 😢 😡 😱 ❤️ 🙂 😭 😍 😠 😮 💙 😁 😞 😤 😨 💛
    </div>
    """,
    unsafe_allow_html=True
)

# ================== TITLE ==================
st.markdown(
    """
    <div class="box">
        <div class="title">🧠 Emotion Detection App</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ================== SUBTITLE ==================
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

# ================== INPUT ==================
text = st.text_area("✍️ اكتب الجملة هنا:")

# ================== BUTTON ==================
if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال نص أولًا")
    else:
        st.success("✅ تم استلام الجملة بنجاح")
        st.write("**النص المدخل:**")
        st.write(text)
