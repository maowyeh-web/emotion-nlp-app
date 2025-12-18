import streamlit as st

# ================== Page Config ==================
st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

# ================== Background + Style ==================
st.markdown(
    """
    <style>
    /* الخلفية العامة */
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1520975916090-3105956dac38");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* الكروت البيضاء */
    .card {
        background-color: rgba(255, 255, 255, 0.92);
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }

    /* العنوان */
    .title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        color: #000000;
    }

    /* الوصف */
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #000000;
        margin-top: 10px;
    }

    /* النصوص */
    label, textarea, p, div {
        color: #000000 !important;
        font-size: 16px;
    }

    /* زر التحليل */
    .stButton > button {
        background-color: #2563eb;
        color: white;
        font-size: 18px;
        padding: 10px 30px;
        border-radius: 12px;
        border: none;
    }

    .stButton > button:hover {
        background-color: #1e40af;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================== Header ==================
st.markdown(
    """
    <div class="card">
        <div class="title">🧠 Emotion Detection App</div>
        <div class="subtitle">
            AI-powered text emotion analysis using Natural Language Processing
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ================== Input Section ==================
st.markdown('<div class="card">', unsafe_allow_html=True)

text = st.text_area("✍️ اكتب الجملة هنا:", height=120)

if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال نص")
    else:
        st.success("✅ تم استلام الجملة بنجاح")
        st.markdown("**النص المُدخل:**")
        st.write(text)

st.markdown('</div>', unsafe_allow_html=True)

# ================== Result Placeholder ==================
st.markdown(
    """
    <div class="card">
        <p><strong>🔍 النتيجة ستظهر هنا بعد ربط المودل</strong></p>
    </div>
    """,
    unsafe_allow_html=True
)
