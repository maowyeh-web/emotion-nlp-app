import streamlit as st

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

# ================== STYLE ==================
st.markdown("""
<style>

/* ===== BACKGROUND (BLACK + EMOJI PATTERN) ===== */
.stApp {
    background-color: #000000;
    background-image:
        radial-gradient(circle at 20% 20%, rgba(255,255,255,0.04) 2%, transparent 3%),
        radial-gradient(circle at 80% 30%, rgba(255,255,255,0.04) 2%, transparent 3%),
        radial-gradient(circle at 40% 70%, rgba(255,255,255,0.04) 2%, transparent 3%);
    background-size: 120px 120px;
}

/* ===== GLASS CARD ===== */
.glass-box {
    background: rgba(255, 255, 255, 0.88);
    backdrop-filter: blur(6px);
    border-radius: 26px;
    padding: 26px;
    margin-bottom: 26px;
    text-align: center;
}

/* ===== TITLE ===== */
.app-title {
    font-size: 42px;
    font-weight: 800;
    color: #000000;
}

/* ===== SUBTITLE ===== */
.app-subtitle {
    font-size: 18px;
    color: #111827;
}

/* ===== LABEL ===== */
.label {
    color: #ffffff;
    font-weight: 700;
    margin-bottom: 8px;
}

/* ===== TEXT AREA ===== */
textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
    border-radius: 16px !important;
    border: 3px solid #2563eb !important;
    font-size: 16px !important;
}

/* ===== BUTTON ===== */
button[kind="primary"] {
    background: linear-gradient(135deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    border-radius: 18px !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    padding: 14px 32px !important;
    box-shadow: 0 0 25px rgba(59,130,246,0.8);
}

button[kind="primary"]:hover {
    background: linear-gradient(135deg, #1e40af, #2563eb) !important;
}

/* ===== SUCCESS (STRONG GREEN) ===== */
div[data-testid="stAlert"][role="alert"] {
    background: linear-gradient(135deg, #16a34a, #22c55e) !important;
    color: white !important;
    font-weight: 800 !important;
    border-radius: 18px !important;
    box-shadow: 0 0 25px rgba(34,197,94,0.8);
}

/* ===== INFO (STRONG BLUE) ===== */
div[data-testid="stAlert"] svg {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ================== TITLE ==================
st.markdown("""
<div class="glass-box">
    <div class="app-title">🧠 Emotion Detection App</div>
</div>
""", unsafe_allow_html=True)

# ================== SUBTITLE ==================
st.markdown("""
<div class="glass-box">
    <div class="app-subtitle">
        AI-powered text emotion analysis using NLP
    </div>
</div>
""", unsafe_allow_html=True)

# ================== INPUT ==================
st.markdown('<div class="label">✍️ اكتب الجملة هنا:</div>', unsafe_allow_html=True)
text = st.text_area("", placeholder="اكتب شعورك أو جملة تعبّر عن إحساسك...")

# ================== BUTTON ==================
if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال جملة")
    else:
        st.success("✅ تم استلام الجملة بنجاح")
        st.info(f"🔍 سيتم تحليل المشاعر للنص:\n\n{text}")
