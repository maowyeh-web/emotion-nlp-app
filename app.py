import streamlit as st

st.set_page_config(
    page_title="Emotion Detection App",
    layout="centered"
)

# ===================== STYLE & BACKGROUND =====================
st.markdown("""
<style>

/* خلفية الإيموجي (نفس الشكل بالصورة) */
.stApp {
    background-color: black;
    background-image: url("https://i.imgur.com/0Z8FQYB.png");
    background-repeat: repeat;
    background-size: 180px;
}

/* صندوق موحد */
.box {
    background: rgba(255, 255, 255, 0.92);
    padding: 26px;
    border-radius: 24px;
    margin: 28px auto;
    max-width: 780px;
}

/* العنوان */
.title {
    font-size: 38px;
    font-weight: 800;
    color: #000;
    text-align: center;
}

/* الوصف */
.subtitle {
    font-size: 18px;
    color: #222;
    text-align: center;
}

/* عنوان الإدخال */
.input-title {
    font-size: 18px;
    font-weight: 700;
    color: #000;
    text-align: right;
    margin-bottom: 10px;
}

/* مربع الإدخال */
textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 16px !important;
    font-size: 16px !important;
}

/* زر التحليل */
.stButton>button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    font-size: 16px;
    padding: 10px 36px;
    border-radius: 16px;
    border: none;
}

</style>
""", unsafe_allow_html=True)

# ===================== TITLE BOX =====================
st.markdown("""
<div class="box">
    <div class="title">🧠 Emotion Detection App</div>
</div>
""", unsafe_allow_html=True)

# ===================== SUBTITLE BOX =====================
st.markdown("""
<div class="box">
    <div class="subtitle">
        AI-powered text emotion analysis using NLP
    </div>
</div>
""", unsafe_allow_html=True)

# ===================== INPUT BOX (NO EXTRA BOX) =====================
st.markdown("""
<div class="box">
    <div class="input-title">✍️ اكتب الجملة هنا:</div>
</div>
""", unsafe_allow_html=True)

text = st.text_area("", height=140)

# ===================== BUTTON & RESULT =====================
if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال نص")
    else:
        st.success("✅ تم استلام الجملة بنجاح")
        st.info("🔍 سيتم تحليل المشاعر بعد ربط النموذج")
