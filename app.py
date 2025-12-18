import streamlit as st

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="Emotion Detection App",
    page_icon="🧠",
    layout="centered"
)

# ================== BACKGROUND & STYLE ==================
st.markdown(
    """
    <style>
    /* الخلفية */
    .stApp {
        background-image: 
        linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.85)),
        url("https://images.unsplash.com/photo-1581091012184-7c54ab6b6f2f");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* صندوق المحتوى */
    div[data-testid="stVerticalBlock"] > div {
        background-color: #f8fafc;
        padding: 2rem;
        border-radius: 18px;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 25px rgba(0,0,0,0.25);
    }

    /* العنوان */
    h1 {
        color: #0f172a;
        font-weight: 800;
        text-align: center;
        font-size: 3rem;
    }

    /* الوصف */
    .subtitle {
        text-align: center;
        font-size: 1.1rem;
        color: #334155;
        margin-top: -10px;
        margin-bottom: 30px;
    }

    /* textarea */
    textarea {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border-radius: 12px !important;
        border: 1px solid #cbd5e1 !important;
    }

    /* زر التحليل */
    div.stButton > button {
        background-color: #2563eb;
        color: white;
        border-radius: 10px;
        padding: 0.6rem 1.6rem;
        font-size: 1rem;
        font-weight: 600;
        border: none;
    }

    div.stButton > button:hover {
        background-color: #1d4ed8;
        color: white;
    }

    /* رسائل Streamlit */
    .stAlert-success {
        background-color: #dcfce7;
        color: #14532d;
        border-radius: 10px;
    }

    .stAlert-warning {
        background-color: #fef3c7;
        color: #78350f;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================== TITLE ==================
st.title("🧠 Emotion Detection App")

st.markdown(
    '<div class="subtitle">AI-powered text emotion analysis using NLP</div>',
    unsafe_allow_html=True
)

# ================== INPUT ==================
text = st.text_area("✍️ اكتب الجملة هنا:")

# ================== BUTTON ==================
if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("⚠️ الرجاء إدخال جملة")
    else:
        st.success("✅ تم استلام الجملة بنجاح")
        st.write("**النص المُدخل:**")
        st.write(text)

        # لاحقًا:
        # prediction = model.predict(tfidf.transform([text]))
        # st.write("**Emotion:**", prediction[0])
