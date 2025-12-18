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
        background: rgba(255,255,255,0.85);
        backdrop-filter: blur(7px);
        z-index: -1;
    }}

    /* الصندوق الرئيسي */
    .main-card {{
        background: rgba(255,255,255,0.95);
        padding: 2.5rem;
        border-radius: 26px;
        box-shadow: 0 20px 45px rgba(0,0,0,0.25);
        max-width: 720px;
        margin: auto;
    }}

    /* العنوان */
    h1 {{
        color: #000;
        font-weight: 900;
        text-align: center;
        margin-bottom: 0.3rem;
    }}

    /* الوصف */
    .subtitle {{
        text-align: center;
        color: #333;
        font-size: 16px;
        margin-bottom: 2rem;
    }}

    /* مربع الإدخال */
    textarea {{
        background: #fff !important;
        color: #000 !important;
        border-radius: 14px !important;
        border: 2px solid #2563eb !important;
        font-size: 16px !important;
        padding: 14px !important;
    }}

    textarea:focus {{
        border-color: #1e40af !important;
        box-shadow: 0 0 12px rgba(37,99,235,0.35) !important;
        outline: none !important;
    }}

    /* الزر */
    button[kind="primary"] {{
        background: linear-gradient(135deg, #2563eb, #1e40af) !important;
        border-radius: 14px !important;
        font-size: 16px !important;
        padding: 0.8rem 2.2rem !important;
        font-weight: 600 !important;
        margin-top: 1rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ================= APP CONTENT =================
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.title("🧠 Emotion Detection App")
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
