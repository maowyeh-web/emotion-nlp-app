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
    .stApp {
        background-image: 
        linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
        url("https://images.unsplash.com/photo-1581091012184-7c54ab6b6f2f");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* صندوق المحتوى */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.93);
        padding: 2rem;
        border-radius: 18px;
        margin-bottom: 1.5rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
    }

    /* العنوان */
    h1 {
        color: #0f172a;
        font-weight: 800;
        text-align: center;
        font-size: 3rem;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.2);
    }

    /* الوصف */
    .subtitle {
        text-align: center;
        font-size: 1.2rem;
        color: #334155;
        margin-top: -10px;
        margin-bottom: 30px;
    }

    /* زر التحليل */
    div.stButton > button {
        background-color: #0f172a;
        color: white;
        border-radius: 10px;
        padding: 0.6rem 1.5rem;
        font-size: 1rem;
        font-weight: 600;
    }

    div.stButton > button:hover {
        background-color: #1e293b;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ================== TITLE ==================
st.title("🧠 Emotion Detection App")

st.markdown(
    '<div class="subtitle">AI-powered text emotion analysis using Natural Language Processing</div>',
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

        # لاحقًا هنا تربط المودل:
        # prediction = model.predict(tfidf.transform([text]))
        # st.write("**Emotion:**", prediction[0])
