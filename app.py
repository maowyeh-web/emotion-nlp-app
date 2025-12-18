import streamlit as st

st.set_page_config(page_title="Emotion Detection App", layout="centered")

# ===================== BACKGROUND + GLOBAL STYLE =====================
st.markdown("""
<style>
/* الخلفية */
.stApp {
    background-color: black;
    background-image: 
        radial-gradient(circle at 10% 20%, rgba(255,255,255,0.05) 0%, transparent 20%),
        radial-gradient(circle at 80% 30%, rgba(255,255,255,0.05) 0%, transparent 20%);
    background-size: cover;
}

/* صندوق عام */
.box {
    background: rgba(255, 255, 255, 0.92);
    padding: 25px;
    border-radius: 22px;
    margin: 25px auto;
    max-width: 750px;
    text-align: center;
}

/* عنوان */
.title {
    font-size: 36px;
    font-weight: 800;
    color: black;
}

/* وصف */
.subtitle {
    font-size: 18px;
    color: #222;
}

/* عنوان الإدخال */
.input-title {
    font-size: 18px;
    font-weight: 700;
    text-align: right;
    color: black;
    margin-bottom: 10px;
}

/* زر */
.stButton>button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    font-size: 16px;
    padding: 10px 30px;
    border-radius: 12px;
    border: none;
}

/* مربع النص */
textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 12px !important;
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

# ===================== INPUT BOX (WITH TITLE INSIDE) =====================
st.markdown("""
<div class="box">
    <div class="input-title">✍️ اكتب الجملة هنا:</div>
</div>
""", unsafe_allow_html=True)

text = st.text_area("", height=120)

# ===================== BUTTON =====================
if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال نص")
    else:
        st.success("✅ تم استلام الجملة بنجاح")
        st.info("🔍 سيتم تحليل المشاعر بعد ربط المودل")

