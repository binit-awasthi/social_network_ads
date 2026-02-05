import streamlit as st
import joblib

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

st.title("ads classifier")
gender = int(st.number_input("gender (male->0;  female->1)"))
age = st.number_input("age")
salary = st.number_input("salary")


if st.button("will purchase ?"):
    x = [[gender, age, salary]]
    x_scaled = scaler.transform(x)
    pred = model.predict(X=x_scaled)
    st.success(f"{'yes' if pred else 'no'}")
