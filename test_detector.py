import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf

# 🔹 Load model
model = tf.keras.models.load_model("keras_model.h5")

# 🔹 Load labels
with open("labels.txt", "r") as f:
    labels = [line.strip().split(" ")[1] for line in f.readlines()]

# 🌈 VIBRANT COLORFUL CSS
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #ff9a9e, #fad0c4, #a18cd1, #fbc2eb);
    background-size: 400% 400%;
    animation: gradientBG 10s ease infinite;
    color: #222;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Title */
h1 {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #4a148c;
}

/* Glass Cards */
.card {
    background: rgba(255, 255, 255, 0.6);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    text-align: center;
    margin: 10px;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.05);
}

/* Upload */
.stFileUploader {
    background: rgba(255,255,255,0.7);
    border-radius: 15px;
    padding: 15px;
}

/* Result */
.result-box {
    background: rgba(255,255,255,0.8);
    padding: 15px;
    border-radius: 15px;
    margin-top: 10px;
    text-align: center;
}

/* Button */
button {
    background: linear-gradient(45deg, #ff6ec4, #7873f5) !important;
    color: white !important;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# 🎯 HERO
st.markdown("""
<h1>🧵 AI Textile Fabric Defect Detector</h1>
<p style='text-align:center; font-size:20px;'>Smart • Fast • Beautiful AI Inspection</p>
""", unsafe_allow_html=True)

# 🚀 FEATURES
st.markdown("### 🚀 Features")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>⚡ Instant Detection</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'>🧠 AI Powered</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='card'>🎯 4 Defect Classes</div>", unsafe_allow_html=True)

st.divider()

# ⭐ REVIEWS
st.markdown("## ⭐ Reviews")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='card'>⭐⭐⭐⭐⭐<br>Super fast and accurate!</div>", unsafe_allow_html=True)
with col2:
    st.markdown("<div class='card'>⭐⭐⭐⭐⭐<br>Looks like real product 😍</div>", unsafe_allow_html=True)
with col3:
    st.markdown("<div class='card'>⭐⭐⭐⭐⭐<br>Very impressive UI!</div>", unsafe_allow_html=True)

st.divider()

# 📷 INPUT MODE
st.markdown("## 📸 Choose Input Method")

mode = st.radio("", ["Upload Image", "Use Webcam"])

# 📸 WEBCAM
if mode == "Use Webcam":
    img_file = st.camera_input("Take a picture")

    if img_file is not None:
        image = Image.open(img_file).convert("RGB")
        st.image(image, use_container_width=True)

        image = image.resize((224, 224))
        img_array = np.array(image) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        prediction = model.predict(img_array)
        index = np.argmax(prediction)
        confidence = float(np.max(prediction)) * 100

        st.markdown(f"<div class='result-box'>✨ {labels[index]}<br>{confidence:.2f}%</div>", unsafe_allow_html=True)

# 📂 UPLOAD (AT LAST ✅)
if mode == "Upload Image":
    uploaded_files = st.file_uploader("", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file).convert("RGB")
            st.image(image, use_container_width=True)

            image = image.resize((224, 224))
            img_array = np.array(image) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            prediction = model.predict(img_array)
            index = np.argmax(prediction)
            confidence = float(np.max(prediction)) * 100

            st.markdown(f"<div class='result-box'>✨ {labels[index]}<br>{confidence:.2f}%</div>", unsafe_allow_html=True)

# 🎯 CTA
st.markdown("""
<div style='text-align:center; padding:30px'>
<h2>🚀 Try It Now</h2>
<p>Upload or capture fabric images and detect defects instantly!</p>
</div>
""", unsafe_allow_html=True)