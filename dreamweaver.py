import streamlit as st
import requests

# Set page configuration
st.set_page_config(page_title="DreamWeaver", layout="centered")

# Custom CSS for styling and background music
st.markdown("""
    <style>
        .main {
            background-color: #fffdf6;
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            color: #a0522d;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextArea textarea {
            border: 2px solid #ffa07a;
            border-radius: 8px;
            background-color: #fffaf0;
        }
        .stButton>button {
            background-color: #ffa07a;
            color: white;
            font-weight: bold;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
        }
        .stMarkdown a {
            color: #d2691e;
            font-weight: bold;
        }
    </style>

    <!-- Background music autoplay and loop -->
    <audio autoplay loop>
        <source src="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3" type="audio/mpeg">
        Your browser does not support the audio element.
    </audio>
""", unsafe_allow_html=True)

# Title and instructions
st.markdown("<h1>🌙 DreamWeaver - Visualize Your Dream</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter your dream and we'll turn it into art and sound!</p>", unsafe_allow_html=True)

# Function to fetch image from Unsplash API
def fetch_image(prompt):
    api_key = 'TnqkOGNvfEqFAO7LfSY1cIz3WbTywVWMq7kbQ1svVnU'  # Your Unsplash API key
    api_url = f'https://api.unsplash.com/photos/random?query={prompt}&client_id={api_key}'

    try:
        response = requests.get(api_url, timeout=10)
        data = response.json()
        if 'urls' in data:
            return data['urls']['regular']
        else:
            st.error("No images found for your query.")
            return None
    except Exception as e:
        st.error(f"Error fetching image: {str(e)}")
        return None

# Input area
dream_input = st.text_area("Describe your dream...", height=200, placeholder="e.g. A flock of birds flying over the sea")

# Button to generate dream visualization
if st.button("Generate Visualization"):
    with st.spinner("Weaving your dream..."):
        img_url = fetch_image(dream_input)

        if img_url:
            st.image(img_url, caption="Here's your dream!", use_container_width=True)

            # Optional sharing
            share_text = f"Check out my dream visualized by DreamWeaver! {img_url}"
            st.markdown(f"[Share this dream on Twitter](https://twitter.com/intent/tweet?text={share_text})")
        else:
            st.error("Failed to generate dream visualization.")
