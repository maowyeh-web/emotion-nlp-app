import streamlit as st

# ====== BACKGROUND STYLE ======
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1559757175-5700dde675bc");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    /* صندوق المحتوى */
    div[data-testid="stVerticalBlock"] > div {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 2rem;
        border-radius: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ====== APP CONTENT ======
st.title("Emotion Detection App")

text = st.text_area("اكتب الجملة هنا:")

if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("الرجاء إدخال جملة")
    else:
        st.success("الجملة تم استلامها بنجاح ✅")
        st.write(text)
