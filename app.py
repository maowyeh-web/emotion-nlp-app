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
  <rect width='100%' height='100%' fill='black'/>
  <text x='20' y='60' font-size='42'>😀 😢 😡 😱 ❤️</text>
  <text x='20' y='140' font-size='42'>😃 😞 😠 😨 💙</text>
  <text x='20' y='220' font-size='42'>🙂 😭 🤬 😰 💛</text>
  <text x='20' y='300' font-size='42'>😊 😔 😤 😳 💚</text>
</svg>
"""
bg = urllib.parse.quote(emoji_svg)

# ================= STYLE =================
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/svg+xml,{bg}");
        background-repeat: repeat;
        background-size: 360px 360px;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,0.75);
        backdrop-filter: blur(6px);
        z-index: -1;
    }}

    .card {{
        background: rgba(255,255,255,0.92);
        padding: 2rem;
        border-radius: 28px;
        box-shadow: 0 25px 60px rgba(0,0,0,0.45);
        max-width: 720px;
        margin: 1.8rem auto;
    }}

    .title {{
        font-size: 40px;
        font-weight: 900;
        text-align: center;
        color: #000;
    }}

    .subtitle {{
        text-align: center;
        font-size: 16px;
        color: #111;
    }}

    textarea {{
        background: white !important;
        color: black !important;
        border-radius: 16px !important;
        border: 2px solid #2563eb !important;
        font-size: 16px !important;
        padding: 16px !important;
    }}

    button[kind="primary"] {{
        background: linear-gradient(135deg,#2563eb,#1e40af) !important;
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

# ================= TITLE CARD =================
st.markdown("""
<div class="card">
    <div class="title">🧠 Emotion Detection App</div>
</div>
""", unsafe_allow_html=True)

# ================= SUBTITLE CARD =================
st.markdown("""
<div class="card">
    <div class="subtitle">
        AI-powered text emotion analysis using NLP
    </div>
</div>
""", unsafe_allow_html=True)

# ================= INPUT CARD (المربع الوحيد المتبقي تحت) =================
st.markdown('<div class="card">', unsafe_allow_html=True)

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
