import streamlit as st
import urllib.parse

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

# ================= EMOJI BACKGROUND =================
emoji_svg = """
<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'>
  <rect width='100%' height='100%' fill='#000'/>
  <text x='20' y='60' font-size='42'>😀 😢 😡 😱 ❤️</text>
  <text x='20' y='140' font-size='42'>😃 😞 😠 😨 💙</text>
  <text x='20' y='220' font-size='42'>🙂 😭 🤬 😰 💛</text>
  <text x='20' y='300' font-size='42'>😊 😔 😤 😳 💚</text>
</svg>
"""
emoji_bg = urllib.parse.quote(emoji_svg)

# ================= STYLE =================
st.markdown(
    f"""
    <style>
    /* خلفية الصفحة */
    .stApp {{
        background-image: url("data:image/svg+xml,{emoji_bg}");
        background-repeat: repeat;
        background-size: 360px 360px;
    }}

    /* طبقة ضبابية */
    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.65);
        backdrop-filter: blur(6px);
        z-index: -1;
    }}

    /* الصندوق الرئيسي (واحد فقط) */
    .main-card {{
        background: rgba(255,255,255,0.93);
        padding: 2.8rem 2.5rem;
        border-radius: 28px;
        box-shadow: 0 25px 55px rgba(0,0,0,0.35);
        max-width: 720px;
        margin: 3rem auto;
    }}

    /* العنوان داخل الصندوق */
    .app-title {{
        font-size: 42px;
        font-weight: 900;
        text-align: center;
        color: #000;
        margin-bottom: 0.4rem;
    }}

    .subtitle {{
        text-align: center;
        color: #222;
        font-size: 16px;
        margin-bottom: 2rem;
    }}

    /* مربع الإدخال (نفس الشفافية) */
    textarea {{
        background: rgba(255,255,255,0.95) !important;
        color: #000 !important;
        border-radius: 16px !important;
        border: 2px solid #2563eb !important;
        font-size: 16px !important;
        padding: 16px !important;
    }}

    textarea:focus {{
        border-color: #1e40af !important;
        box-shadow: 0 0 14px rgba(37,99,235,0.45) !important;
        outline: none !important;
    }}

    /* الزر */
    button[kind="primary"] {{
        background: linear-gradient(135deg, #2563eb, #1e40af) !important;
        border-radius: 16px !important;
        font-size: 17px !important;
        padding: 0.9rem 2.6rem !important;
        font-weight: 700 !important;
        margin-top: 1.2rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ================= APP CONTENT =================
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<div class="app-title">🧠 Emotion Detection App</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">AI-powered text emotion analysis using NLP</div>',
    unsafe_allow_html=True
)

text = st.text_area("✍️ اكتب الجملة هنا:")

if st.button("Analyze Emotion", type="primary"):
    if text.strip() == "":
        st.warning("الرجاء إدخال جملة")
    else:
        st.success("تم استلام الجملة بنجاح ✅")
        st.write("**النص المدخل:**")
        st.write(text)
        st.info("🔍 سيتم تحليل المشاعر بعد ربط المودل")

st.markdown("</div>", unsafe_allow_html=True)
