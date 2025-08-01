import streamlit as st
import numpy as np

# with st.chat_message("user"):  # should be from the person or user side
#    st.write("Hello 👋") 
 
# with st.chat_message("assistant"): # should be from the computer side
#   st.write("Hello human")
#   st.bar_chart(np.random.randn(30, 3))  # display a bar chart with random data

# String is returned
# prompt = st.chat_input("Say something")
# if prompt:
#    st.write(f"User has sent the following prompt: {prompt}")

st.title("Echo Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])





