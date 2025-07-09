import streamlit as st
import requests
from PIL import Image
import io

API_URL = "http://localhost:8000/compare_faces/"

st.title("🧠 Face Verification App")
st.write("Upload a **registered** and **current** image to verify identity.")

reg_img = st.file_uploader("Upload Registered Image", type=["jpg", "jpeg", "png", "webp"])
cur_img = st.file_uploader("Upload Current Image", type=["jpg", "jpeg", "png", "webp"])

if reg_img and cur_img:
    col1, col2 = st.columns(2)
    with col1:
        st.image(reg_img, caption="📷 Registered Image", width=250)
    with col2:
        st.image(cur_img, caption="📷 Current Image", width=250)

    if st.button("🔍 Compare Faces"):
        with st.spinner("Analyzing..."):
            files = {
                "registered": (reg_img.name, reg_img, reg_img.type),
                "current": (cur_img.name, cur_img, cur_img.type)
            }

            try:
                response = requests.post(API_URL, files=files)
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"✅ {data['result']}")
                    st.metric("Similarity Score", f"{data['similarity_score']:.4f}")
                else:
                    st.error(f"❌ Error: {response.json().get('error', 'Unknown')}")
            except Exception as e:
                st.error(f"🚫 Failed to connect to backend: {e}") 