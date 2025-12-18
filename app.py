import streamlit as st
import urllib.parse

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

# ================== EMOJI SVG BACKGROUND ==================
emoji_svg = """
<svg xmlns='http://www.w3.org/2000/svg' width='400' height='400'>
  <rect width='100%' height='100%' fill='#000000'/>
  <text x='20' y='60' font-size='42'>😀 😢 😡 😱 ❤️</text>
  <text x='20' y='140' font-size='42'>😃 😞 😠 😨 💙</text>
  <text x='20' y='220' font-size='42'>🙂 😭 🤬 😰 💛</text>
  <text x='20' y='300' font-size='42'>😊 😔 😤 😳 💚</text>
</svg>
"""
emoji_bg = urllib.parse.quote(emoji_svg)

# ================== STYLE ==================
st.markdown(
    f"""
    <style>
    /* خلفية الإيموجي */
    .stApp {{
        background-image: url("data:image/svg+xml,{emoji_bg}");
        background-repeat: repeat;
        background-size: 380px 380px;
    }}

    /* ضبابية خفيفة */
    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(6px);
        -webkit-backdrop-filter: blur(6px);
        z-index: -1;
    }}

    /* الصناديق البيضاء */
    div[data-testid="stVerticalBlock"] > div {{
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 22px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.2);
        margin-bottom: 1.5rem;
    }}

    /* العنوان */
    h1 {{
        color: #000000;
        font-weight: 800;
        text-align: center;
        margin-bottom: 0.3rem;
    }}

    /* النصوص */
    p, label {{
        color: #000000 !important;
        font-size: 16px;
    }}

    /* مربع الإدخال */
    textarea {{
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 14px !important;
        border: 2px solid #2563eb !important;
        font-size: 16px !important;
        padding: 14px !important;
    }}

    textarea:focus {{
        outline: none !important;
        border-color: #1d4ed8 !important;
        box-shadow: 0 0 10px rgba(37,99,235,0.4) !important;
    }}

    /* زر التحليل */
    button[kind="primary"] {{
        background: linear-gradient(135deg, #2563eb, #1e40af) !important;
        color: white !important;
        border-radius: 14px !important;
        font-size: 16px !important;
        padding: 0.7rem 1.8rem !important;
        font-weight: 600 !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ================== APP ==================
st.title("🧠 Emotion Detection App")
st.write("AI-powered text emotion analysis using NLP")

text = st.text_area("✍️ اكتب الجملة هنا:")

if st.button("Analyze Emotion", type="primary"):
    if text.strip() == "":
        st.warning("الرجاء إدخال جملة")
    else:
        st.success("تم استلام الجملة بنجاح ✅")
        st.write("**النص المدخل:**")
        st.write(text)
        st.info("🔍 سيتم تحليل المشاعر بعد ربط المودل")
