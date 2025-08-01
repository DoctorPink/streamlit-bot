import streamlit as st
import numpy as np

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

# with st.chat_message("user"):  # should be from the person or user side
#    st.write("Hello 👋") 
 
# with st.chat_message("assistant"): # should be from the computer side
#   st.write("Hello human")
#   st.bar_chart(np.random.randn(30, 3))  # display a bar chart with random data

# String is returned
# prompt = st.chat_input("Say something")
# if prompt:
#    st.write(f"User has sent the following prompt: {prompt}")

st.title("Simple Bot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])         # response typed into chat message
 
# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)     

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Add response to display, the assistant echo users into chat message
    response = f"Echo: {prompt}"              
    # Display assistant response in chat message container
    
    with st.chat_message("assistant"):
        st.markdown(response)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})



