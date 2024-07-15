import streamlit as st
import requests
import json

# AWS API Gateway endpoint
api_url = 'https://t8ldpkt0yl.execute-api.us-east-1.amazonaws.com/Dev'

def get_response_from_api(prompt):
    headers = {
        'Content-Type': 'application/json'
    }
    payload = {
        'prompt': prompt
    }
    try:
        response = requests.post(api_url, headers=headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json().get('body')
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Streamlit app layout
st.title('Your Child Labour Law Assistant')

user_input = st.text_input("You: ", "")

if st.button("Send"):
    if user_input:
        # Add the user input to the chat history
        st.session_state.chat_history.append(('user', user_input))
        response = get_response_from_api(user_input)
        # Add the response to the chat history
        st.session_state.chat_history.append(('bot', response))
    else:
        st.warning("Please enter a prompt.")

# Display chat history
for role, message in st.session_state.chat_history:
    if role == 'user':
        st.markdown(f"<div style='color: orange;'><strong>You:</strong> {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='color: blue;'><strong>Bedrock KB:</strong> {message}</div>", unsafe_allow_html=True)
