import streamlit as st

# ===================== Page Config =====================
st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

# ===================== Custom CSS =====================
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000;
    }

    .box {
        background-color: #f2f2f2;
        padding: 25px;
        border-radius: 25px;
        margin-bottom: 25px;
        text-align: center;
    }

    .title-text {
        font-size: 36px;
        font-weight: bold;
        color: #000000;
    }

    .subtitle-text {
        font-size: 18px;
        color: #111827;
    }

    .label-text {
        color: #ffffff;
        font-size: 18px;
        margin-bottom: 8px;
    }

    .success-box {
        background-color: #14532d;
        color: #bbf7d0;
        padding: 18px;
        border-radius: 15px;
        margin-top: 20px;
        font-size: 16px;
    }

    textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 15px !important;
        font-size: 16px !important;
    }

    .stButton>button {
        background-color: #1d4ed8;
        color: white;
        border-radius: 15px;
        padding: 10px 30px;
        font-size: 16px;
        border: none;
    }

    .stButton>button:hover {
        background-color: #2563eb;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===================== Title Box =====================
st.markdown(
    """
    <div class="box">
        <span class="title-text">🧠 Emotion Detection App</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ===================== Subtitle Box =====================
st.markdown(
    """
    <div class="box">
        <span class="subtitle-text">
            AI-powered text emotion analysis using NLP
        </span>
    </div>
    """,
    unsafe_allow_html=True
)

# ===================== Text Input =====================
st.markdown('<div class="label-text">✍️ اكتب الجملة هنا:</div>', unsafe_allow_html=True)

text = st.text_area(
    "",
    height=120,
    placeholder="اكتب الجملة التي تريد تحليل مشاعرها..."
)

# ===================== Button =====================
if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال جملة أولاً")
    else:
        st.markdown(
            """
            <div class="success-box">
                ✅ تم استلام الجملة بنجاح<br>
                🔍 سيتم تحليل المشاعر بعد ربط النموذج
            </div>
            """,
            unsafe_allow_html=True
        )
