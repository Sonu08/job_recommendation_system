import pickle
import streamlit as st
import requests

jobs = pickle.load(open('job.pkl','rb'))
indus_list = jobs['Industry_Interest'].values
job_list = jobs['Job_Type_Interest'].values
new_job_list = []
for v in job_list:
    if v not in new_job_list:
        new_job_list.append(v)
    
lo_list = jobs['Location_Interest'].values

def recommend(indus, job, lo):
    indus_index = jobs[jobs['Industry_Interest']== indus].index[0]
    job_index = jobs[jobs['Job_Type_Interest']== job].index[0]
    lo_index = jobs[jobs['Location_Interest']== lo].index[0]
    distances1 = similarity[indus_index]
    distances2 = similarity[job_index]
    distances3 = similarity[lo_index]
    tags_list = sorted(list(enumerate(distances1)), reverse=True, key=lambda x:x[1])[1:6] + sorted(list(enumerate(distances2)), reverse=True, key=lambda x:x[1])[1:6] + sorted(list(enumerate(distances3)), reverse=True, key=lambda x:x[1])[1:6]
    recommended_job = []
    
    unique_list = []
    for x in tags_list:
        if x not in unique_list:
            unique_list.append(x)
    
    for i in unique_list:
        # fetch the movie poster
        #job_id = new_job.iloc[i[0]].desired_company
        recommended_job.append(jobs.iloc[i[0]].desired_company)

    return recommended_job


st.header('Job Recommender System')
#industry = pickle.load(open('job/indus_list.pkl','rb'))
#job = pickle.load(open('job/job_list.pkl','rb'))
#lo = pickle.load(open('job/location_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

#indus_list = new_job['Industry_Interest'].values
selected_indus = st.selectbox(
    "Type or select an Industry Interest from the dropdown",
    indus_list
)

#job_list = new_job['Job_Type_Interest'].values
selected_job = st.selectbox(
    "Type or select a Job Type Interest from the dropdown",
    new_job_list
)

#lo_list = new_job['Location_Interest'].values
selected_location = st.selectbox(
    "Type or select a Location Interest from thr dropdown",
    lo_list
)


if st.button('Show Recommendation'):
    recommended_job = recommend(selected_indus, selected_job, selected_location)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_job[0])
    with col2:
        st.text(recommended_job[1])
    with col3:
        st.text(recommended_job[2])
    with col4:
        st.text(recommended_job[3])
    with col5:
        st.text(recommended_job[4])

