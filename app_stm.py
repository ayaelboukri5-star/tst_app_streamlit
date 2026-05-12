import streamlit as st
import time
st.title("Suite streamlit")
if st.button("Cliquer ici"):
    with st.spinner("chargement en cours..."):
        time.sleep(2)
    st.success("termine ! ")    
     