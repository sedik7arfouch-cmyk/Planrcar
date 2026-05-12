import streamlit as st
import google.generativeai as genai

api_key = "AIzaSyALY6w6dGvfYL7kWPTzcE4zx8VqyrbQUzk"
genai.configure(api_key=api_key)

st.set_page_config(page_title="Planrcar AI", page_icon="🌿")
st.title("🌿 خبير النباتات الذكي (Planrcar)")

query = st.text_input("اسألني أي شيء عن نباتاتك:")

if query:
    try:
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content(query)
        st.success("إليك الإجابة:")
        st.info(response.text)
    except Exception as e:
        st.error(f"حدث خطأ: {e}")
