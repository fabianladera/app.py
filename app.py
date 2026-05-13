import streamlit as st
st.title("Mi primera aplicación en python")

st.sidebar.title("Parámetros")

st.write("Elaborado por: Carlos Carrillo")

sesion = st.selectbox("Selecciones una sesion",["Sesion 1 ","Sesion 2","Sesion 3","Sesion 4"])
