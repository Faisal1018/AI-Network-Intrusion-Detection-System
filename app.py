import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("rf_dashboard.pkl")

# Page Config
st.set_page_config(
    page_title="Network Intrusion Detection System",
    page_icon="🛡️",
    layout="wide"
)

# Title
st.title("🛡️ AI-Based Network Intrusion Detection System")

st.markdown("""
This application uses a **Random Forest Machine Learning Model**
to classify network traffic as:

✅ **BENIGN Traffic**

🚨 **DDoS Attack**
""")

# Performance Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Accuracy", "100%")

with col2:
    st.metric("Recall", "100%")

with col3:
    st.metric("F1 Score", "100%")

st.markdown("---")

# Input Section
st.subheader("📊 Traffic Features")

col1, col2 = st.columns(2)

with col1:
    fwd_packet_length_max = st.number_input(
        "Fwd Packet Length Max",
        min_value=0.0,
        value=0.0
    )

    total_length_fwd_packets = st.number_input(
        "Total Length of Fwd Packets",
        min_value=0.0,
        value=0.0
    )

    init_win_bytes_forward = st.number_input(
        "Init_Win_bytes_forward",
        min_value=0.0,
        value=0.0
    )

with col2:
    destination_port = st.number_input(
        "Destination Port",
        min_value=0.0,
        value=0.0
    )

    bwd_packet_length_mean = st.number_input(
        "Bwd Packet Length Mean",
        min_value=0.0,
        value=0.0
    )

st.markdown("---")

# Prediction Button
if st.button("🔍 Predict Traffic Type"):

    input_data = pd.DataFrame({
        ' Fwd Packet Length Max': [fwd_packet_length_max],
        'Total Length of Fwd Packets': [total_length_fwd_packets],
        'Init_Win_bytes_forward': [init_win_bytes_forward],
        ' Destination Port': [destination_port],
        ' Bwd Packet Length Mean': [bwd_packet_length_mean]
    })

    prediction = model.predict(input_data)

    st.subheader("Prediction Result")

    if prediction[0] == 1:
        st.error("🚨 DDoS ATTACK DETECTED")
        st.warning(
            "Suspicious network traffic detected. Immediate investigation is recommended."
        )
    else:
        st.success("✅ BENIGN TRAFFIC")
        st.info(
            "Traffic appears normal and safe."
        )
        

# Sidebar
st.sidebar.title("ℹ️ About Project")

st.sidebar.markdown("""
### Dataset
CIC-IDS2017

### Model
Random Forest Classifier

### Prediction Classes
✅ BENIGN

🚨 DDoS

### Author
MD. FAISAL HAMID
""")