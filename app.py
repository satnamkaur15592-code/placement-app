import streamlit as st
import pickle
import numpy as np

# Page setup
st.set_page_config(page_title="Placement Prediction", page_icon="🎓", layout="centered")

# Load model
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# UI
st.title("🎓 Campus Placement Predictor")
st.markdown("Check your placement chances in one click!")

st.divider()

col1, col2 = st.columns(2)
with col1:
    cgpa = st.number_input("Enter your CGPA (0-10)", min_value=0.0, max_value=10.0, value=7.5, step=0.1)
with col2:
    iq = st.number_input("Enter your IQ Score (50-200)", min_value=50, max_value=200, value=100)

st.write("")
if st.button("🚀 Predict My Placement", use_container_width=True):
    input_data = np.array([[cgpa, iq]])
    prediction = model.predict(input_data)
    
    st.divider()
    if prediction[0] == 1:
        st.balloons()
        st.success("### 🎉 Congratulations! You will be Placed!")
        st.metric("CGPA", cgpa, "Eligible")
    else:
        st.error("### 😔 Low Chances of Placement")
        st.warning("Try to improve your CGPA & Skills!")
    
    st.info(f"Your Profile: CGPA = {cgpa} | IQ = {iq}")

st.divider()
st.caption("Built with ❤️ by Satnam Kaur | Live Demo for Resume")
