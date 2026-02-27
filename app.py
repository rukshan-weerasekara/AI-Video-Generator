import streamlit as st
import requests

# Page Config
st.set_page_config(page_title="AI Video Generator", page_icon="🎥")

st.title("AI Video Generator")
st.write("Convert your text descriptions into short AI videos.")


with st.sidebar:
    st.title("How to use")
    st.write("1. Enter a detailed prompt.")
    st.write("2. Click 'Generate' button.")
    st.write("3. Wait for the AI to process.")

# User Input
prompt = st.text_input("Enter your prompt:", placeholder="Example: A futuristic city at night with flying cars...")

if st.button("Generate Video"):
    if prompt:
        with st.spinner("Processing your video... This might take a minute."):
            # Hugging Face Inference API
            API_URL = "https://api-inference.huggingface.co/models/damo-vilab/text-to-video-ms-1.7b"
            headers = {"Authorization": f"Bearer {st.secrets['HF_TOKEN']}"}
            
            try:
                response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
                
                if response.status_code == 200:
                    video_content = response.content
                    st.video(video_content)
                    st.success("Video generated successfully!")
                    st.download_button(label="Download Video", data=video_content, file_name="ai_video.mp4", mime="video/mp4")
                else:
                    st.error(f"Error: {response.status_code}. The API might be busy, please try again.")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt first.")

st.markdown("---")
st.caption("Powered by Hugging Face Models")
