
import streamlit as st

st.set_page_config(
    page_title="AI Spectrum Optimization",
    page_icon="📡",
    layout="wide"
)

st.title("📡 AI-Powered Intelligent Spectrum Optimization")

st.write(
    "An AI-based system for spectrum sensing, "
    "anomaly detection and adaptive channel selection."
)

st.divider()

st.header("Project Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("AI Algorithms", "4")
col2.metric("RF Channels", "5")
col3.metric("Dataset Samples", "1500")
col4.metric("System", "Simulation")

st.subheader("Implemented Algorithms")

st.write("1. Random Forest – Spectrum classification")
st.write("2. CNN – Spectrogram classification")
st.write("3. Autoencoder – Anomaly detection")
st.write("4. Q-Learning – Adaptive channel selection")

st.info("Welcome to the Intelligent Spectrum Optimization Dashboard.")

