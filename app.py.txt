import streamlit as st
import pickle
model = pickle.load(open('model.pkl','rb'))
st.title("Placement Prediction App")
cgpa = st.number_input("Apna CGPA dalo", 0.0, 10.0, 7.5)
iq = st.number_input("Apna IQ dalo", 0, 200, 100)
if st.button("Predict Karo"):
    result = model.predict([[cgpa, iq]])
    if result[0] == 1:
        st.success("Congrats! Placement ho jayega")
    else:
        st.error("Thoda aur mehnat karni padegi")