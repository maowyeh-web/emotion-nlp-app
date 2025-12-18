import streamlit as st

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

# ================= STYLE =================
st.markdown("""
<style>

/* ===== BASE ===== */
.stApp {
    background: black;
    color: white;
}

/* ===== EMOJI BACKGROUND ===== */
.stApp::before {
    content: "😀 😢 😡 😍 😱 💙 😊 😔 😤 😲 💛 😭 😠 😌 😕 💚 😄 😞 😠 😮 💙";
    position: fixed;
    inset: 0;
    font-size: 40px;
    opacity: 0.12;
    filter: blur(2px);
    z-index: -1;
    line-height: 1.6;
    white-space: pre-wrap;
}

/* ===== CARD ===== */
.card {
    background: rgba(255,255,255,0.95);
    color: black;
    border-radius: 24px;
    padding: 28px;
    margin: 24px 0;
}

/* ===== TITLE ===== */
.title {
    font-size: 38px;
    font-weight: 800;
    text-align: center;
}

/* ===== SUBTITLE ===== */
.subtitle {
    text-align: center;
    font-size: 17px;
    color: #1f2937;
}

/* ===== TEXT AREA ===== */
textarea {
    background: white !important;
    color: black !important;
    border-radius: 16px !important;
    border: 2px solid #2563eb !important;
    font-size: 16px !important;
}

/* ===== BUTTON ===== */
button[kind="primary"] {
    background: #2563eb !important;
    color: white !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    border-radius: 18px !important;
    padding: 12px 30px !important;
}

/* ===== SUCCESS ===== */
div[data-testid="stAlert"] {
    border-radius: 16px !important;
    font-weight: 700;
}

</style>
""", unsafe_allow_html=True)

# ================= CONTENT =================

# TITLE
st.markdown("""
<div class="card">
    <div class="title">🧠 Emotion Detection App</div>
</div>
""", unsafe_allow_html=True)

# SUBTITLE
st.markdown("""
<div class="card">
    <div class="subtitle">
        AI-powered text emotion analysis using NLP
    </div>
</div>
""", unsafe_allow_html=True)

# INPUT
st.markdown("""
<div class="card">
    <b>✍️ اكتب الجملة هنا:</b>
</div>
""", unsafe_allow_html=True)

text = st.text_area(
    "",
    placeholder="اكتب شعورك أو جملة تعبّر عن إحساسك..."
)

# BUTTON
if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال جملة")
    else:
        st.success("✅ تم استلام الجملة بنجاح")
        st.info(f"🔍 النص المدخل:\n{text}")
