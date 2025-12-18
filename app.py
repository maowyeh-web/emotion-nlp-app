import streamlit as st

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

# ================== GLOBAL STYLE ==================
st.markdown("""
<style>

/* ===== BACKGROUND ===== */
.stApp {
    background-color: #000000;
    background-image: url("https://i.imgur.com/6Z8F7Qm.png");
    background-repeat: repeat;
    background-size: 120px;
}

/* ===== GLASS CARD ===== */
.glass-box {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(6px);
    border-radius: 24px;
    padding: 24px;
    margin-bottom: 24px;
    text-align: center;
}

/* ===== TITLE ===== */
.app-title {
    font-size: 40px;
    font-weight: 800;
    color: #000000;
}

/* ===== SUBTITLE ===== */
.app-subtitle {
    font-size: 18px;
    color: #111827;
}

/* ===== TEXT AREA ===== */
textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 14px !important;
    border: 2px solid #2563eb !important;
    font-size: 16px !important;
}

/* ===== BUTTON ===== */
button[kind="primary"] {
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    border-radius: 16px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    padding: 12px 28px !important;
    box-shadow: 0 12px 30px rgba(37,99,235,0.7);
}

button[kind="primary"]:hover {
    background: linear-gradient(135deg, #1e40af, #2563eb) !important;
    box-shadow: 0 0 25px rgba(59,130,246,0.9);
}

/* ===== SUCCESS (GREEN STRONG) ===== */
div[data-testid="stAlert"] {
    border-radius: 18px !important;
    font-weight: 700 !important;
}

div[data-testid="stAlert"][role="alert"] {
    background: linear-gradient(135deg, #16a34a, #22c55e) !important;
    color: #ffffff !important;
    box-shadow: 0 0 18px rgba(34,197,94,0.7);
}

/* ===== INFO (BLUE STRONG) ===== */
div[data-testid="stAlert"] svg {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ================== TITLE CARD ==================
st.markdown("""
<div class="glass-box">
    <div class="app-title">🧠 Emotion Detection App</div>
</div>
""", unsafe_allow_html=True)

# ================== SUBTITLE CARD ==================
st.markdown("""
<div class="glass-box">
    <div class="app-subtitle">
        AI-powered text emotion analysis using NLP
    </div>
</div>
""", unsafe_allow_html=True)

# ================== INPUT ==================
st.markdown("✍️ **اكتب الجملة هنا:**")
text = st.text_area("", placeholder="اكتب شعورك أو جملة تعبّر عن إحساسك...")

# ================== BUTTON ==================
if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال جملة")
    else:
        st.success("✅ تم استلام الجملة بنجاح")
        st.info(f"🔍 سيتم تحليل المشاعر للنص:\n\n{text}")
