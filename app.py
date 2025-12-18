import streamlit as st

st.set_page_config(
    page_title="Emotion Detection App",
    layout="centered"
)

# ================= BACKGROUND + STYLE =================
st.markdown("""
<style>
/* خلفية الإيموجي */
.stApp {
    background-color: black;
    background-image: url("https://i.imgur.com/2Jg9YQp.png");
    background-size: 220px;
    background-repeat: repeat;
}

/* صندوق موحّد */
.box {
    background: rgba(255, 255, 255, 0.92);
    padding: 25px;
    border-radius: 22px;
    margin: 25px auto;
    max-width: 750px;
}

/* العنوان الرئيسي */
.title {
    font-size: 36px;
    font-weight: 800;
    color: black;
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
    color: black;
    text-align: right;
    margin-bottom: 10px;
}

/* textarea */
textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 14px !important;
}

/* زر */
.stButton>button {
    background: linear-gradient(135deg, #2563eb, #1d4ed8);
    color: white;
    font-size: 16px;
    padding: 10px 35px;
    border-radius: 14px;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# ================= TITLE BOX =================
st.markdown("""
<div class="box">
    <div class="title">🧠 Emotion Detection App</div>
</div>
""", unsafe_allow_html=True)

# ================= SUBTITLE BOX =================
st.markdown("""
<div class="box">
    <div class="subtitle">
        AI-powered text emotion analysis using NLP
    </div>
</div>
""", unsafe_allow_html=True)

# ================= INPUT BOX (WITH TITLE INSIDE) =================
st.markdown("""
<div class="box">
    <div class="input-title">✍️ اكتب الجملة هنا:</div>
</div>
""", unsafe_allow_html=True)

text = st.text_area("", height=130)

# ================= BUTTON =================
if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال نص")
    else:
        st.success("✅ تم استلام الجملة بنجاح")
        st.info("🔍 سيتم تحليل المشاعر بعد ربط النموذج")
