import streamlit as st
import google.generativeai as genai

# ضع مفتاحك الذي نسخته هنا بين القوسين
genai.configure(api_key=AIzaSyALY6w6dGvfYL7kWPTzcE4zx8VqyrbQUzk)

st.set_page_config(page_title="PlantCare AI", page_icon="🌿")
st.title("🌿 خبير النباتات الذكي")

query = st.text_input("كيف يمكنني مساعدتك في العناية بنباتاتك؟")

if query:
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(query)
    st.write(response.text)
