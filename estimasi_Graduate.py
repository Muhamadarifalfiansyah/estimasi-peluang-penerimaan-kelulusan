import pickle
import streamlit as st

model = pickle.load(open('estimasi_graduate.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Peluang Penerimaan')


GREScore = st.number_input('Input GRE Score')
TOEFLScore = st.number_input('Input TOEFL Score')
UniversityRating = st.number_input('Input University Rating')
SOP = st.number_input('Input SOP')
LOR = st.number_input('Input LOR')
CGPA = st.number_input('Input CGPA')
Research = st.number_input('Input Research')


predict = ''

if st.button('Cek Peluang'):
    predict = model.predict(
        [[GREScore,TOEFLScore,UniversityRating,SOP,LOR,CGPA,Research]]
    )
    st.write ('Estimasi jumlah Peluang Penerimaan : ', predict)