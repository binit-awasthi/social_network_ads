import streamlit as st
import joblib

model = joblib.load("model.joblib")

st.title("lab1: iris flower classifier")
sepal_length = st.number_input("enter sepal length")
sepal_width = st.number_input("enter sepal width")
petal_length = st.number_input("enter petal length")
petal_width = st.number_input("enter petal width")

if st.button("Predict"):
    pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
    st.success(f"species:{pred} ")
