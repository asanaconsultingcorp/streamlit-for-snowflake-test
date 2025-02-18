import streamlit as st

st.title("About session...")

st.write(st.session_state)

message = ""
if st.button("Button", key="my-button"):
    message = "You clicked!"
    
if st.toggle("Toggle", key="my-toggle"):
    message = "You toggled!"
    
st.write(message)   
st.write(st.session_state)