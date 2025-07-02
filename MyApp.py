import pandas as pd
import streamlit as st
from joblib import load
from streamlit import number_input
import warnings

st.title('Bank account Prediction  in east africa')
st.text("Kenya : 0,Rwanda : 1, Tanzania : 2 , Uganda : 3")
country=st.number_input("Choose the country")
year=st.number_input("Choose the year")
st.text("Rural : 0,Urban : 1")
locationType=number_input("Choose the location type")
st.text("No : 0,Yes : 1")
cellphone_access=number_input("Choose the cellphone number")
age_of_respondent=number_input("Choose the age of respondent")
st.text("Female : 0,Male : 1")
gender_of_respondent=number_input("Choose the gender of respondent")
st.text("Self employed : 9 ,Government Dependent: 4 ,Formally employed Private :3 ,Informally employed :5 ")
st.text("Formally employed Government : 2 ,Farming and Fishing : 1 ,Remittance Dependent : 8 , Other Income : 7 ")
st.text("Dont Know/Refuse to answer :0 ,No Income : 6 ")
job_type=number_input("Choose the job type")
st.text("Secondary education :3 ,No formal education : 0,Vocational/Specialised training:5,Primary education: 2,Tertiary education: 4,Other/Dont know/RTA:1 ")
education_level=number_input("Choose the education level")

xnewraw=pd.DataFrame({
    "country":[country],
    "year":[year],
    "location_type":[locationType],
    "cellphone_access":[cellphone_access],
    "age_of_respondent":[age_of_respondent],
    "gender_of_respondent":[gender_of_respondent],
    "education_level": [education_level],
    "job_type":[job_type],

})




model = load('model.joblib')

if st.button('Predict'):
    prediction = model.predict(xnewraw)
    st.write(prediction[0])
