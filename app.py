import streamlit as st

# ===== Background Style =====
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f5f7fa;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===== App Title =====
st.title("Emotion Detection App")

# ===== Text Input =====
text = st.text_area("اكتب الجملة هنا:")

# ===== Button =====
if st.button("Analyze Emotion"):
    if text.strip() == "":
        st.warning("الرجاء إدخال جملة")
    else:
        st.success("الجملة تم استلامها بنجاح ✅")
        st.write("النص المدخل:")
        st.write(text)
