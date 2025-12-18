import streamlit as st

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

# ================== STYLE ==================
st.markdown(
    """
    <style>
    /* الخلفية مع صورة + ضبابية */
    .stApp {
        background-image: url("emotions_bg.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(255, 255, 255, 0.6);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        z-index: -1;
    }

    /* الصناديق */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        margin-bottom: 1.5rem;
    }

    /* العنوان */
    h1 {
        color: #000000;
        font-weight: 800;
        text-align: center;
    }

    /* النص */
    p, label {
        color: #000000 !important;
        font-size: 16px;
    }

    /* مربع الإدخال */
    textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 14px !important;
        border: 2px solid #2563eb !important;
        font-size: 16px !important;
        padding: 14px !important;
    }

    textarea:focus {
        outline: none !important;
        border-color: #1e40af !important;
        box-shadow: 0 0 10px rgba(37,99,235,0.4) !important;
    }

    /* الزر */
    button[kind="primary"] {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 14px !important;
        font-size: 16px !important;
        padding: 0.7rem 1.8rem !important;
        font-weight: 600 !important;
    }
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
