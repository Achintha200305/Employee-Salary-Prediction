import joblib
import streamlit as st
import numpy as np


st.title("Salary Prediction")
st.image("kw001-0155.jpg",width=500)
regressor=joblib.load("employee_salary_150.pkl")

col1,col2=st.columns(2)
with col1:
    years=st.number_input("Years",min_value=0,max_value=20,value=0)
with col2:
    months=st.number_input("Months",min_value=0,max_value=11,value=0)
Experience=(years*12)+months
Education=st.selectbox("Education Level",
                       options=[1,2,3,4],
                       format_func=lambda x:{
        1: "1 - High School / Diploma",
        2: "2 - Bachelor's Degree",
        3: "3 - Master's Degree",
        4: "4 - PhD"

                       }[x])
skill=st.slider("Skill Score (0 - 100)", min_value=0, max_value=100, value=0)
age=st.number_input("Age",min_value=18,max_value=65,value=18)

if st.button("Predict"):
    input_data=np.array([[Experience,Education,skill,age]])
    prediction=regressor.predict(input_data)
    st.success(f"Estimated Monthly Salary: LKR {prediction[0]:,.2f}")