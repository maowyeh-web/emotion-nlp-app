import streamlit as st

st.markdown(
    """
    <style>
    /* الخلفية بالصورة */
    .stApp {
        background-image: url("emotions_bg.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* طبقة ضبابية فوق الخلفية */
    .stApp::before {
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(255, 255, 255, 0.55);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        z-index: -1;
    }

    /* الكروت (الصناديق البيضاء) */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        margin-bottom: 1.5rem;
    }

    /* العنوان */
    h1 {
        color: #000000;
        font-weight: 800;
        text-align: center;
    }

    /* النصوص */
    p, label {
        color: #000000 !important;
        font-size: 16px;
    }

    /* صندوق الإدخال */
    textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
        border-radius: 12px !important;
        border: 2px solid #2563eb !important;
        font-size: 16px !important;
        padding: 12px !important;
    }

    textarea:focus {
        outline: none !important;
        border-color: #1e40af !important;
        box-shadow: 0 0 8px rgba(37,99,235,0.4) !important;
    }

    /* الزر */
    button[kind="primary"] {
        background-color: #2563eb !important;
        color: white !important;
        border-radius: 12px !important;
        font-size: 16px !important;
        padding: 0.6rem 1.5rem !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
