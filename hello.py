import streamlit as st
import pickle

job_list = pickle.load(open('job.pkl''rb'))
job_list = job_list['Academic_Background'].values

st.title('Job Recommendation System')

option = st.selectbox(
       "Enter",
        job_list)

 