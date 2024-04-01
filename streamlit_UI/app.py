import streamlit as st
import requests

st.set_page_config(page_title="RAG Chatbot", page_icon=":robot_face:")
st.title('RAG Chatbot Interface')

# Function to send the prompt to the RAG API
def send_prompt_to_rag_api(prompt):
    url = "http://127.0.0.1:8001/question"  # Replace with your actual API endpoint
    payload = {"prompt": prompt}  # The body of your POST request
    headers = {"Content-Type": "application/json"}

    # Send the request to the API
    response = requests.post(url, json=payload, headers=headers)

    # Check if the request was successful
    if response.ok:
        # Return the response content directly
        return response.text  # No need to parse as JSON
    else:
        # If the response was not successful, show an error
        st.error(f"API request failed with status code {response.status_code}")
        return ""
# Session state to store chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Text input for the user prompt
with st.form(key='user_prompt_form'):
    user_input = st.text_input(label="Enter your message:", value="")
    submit_button = st.form_submit_button(label='Send')

# If the user sends a message, append it to the chat history and make an API call
if submit_button and user_input:
    # Update the chat history with the user's message
    st.session_state.chat_history.append({"sender": "User", "message": user_input})

    # Send the user's message to the RAG API and store the response
    bot_response = send_prompt_to_rag_api(user_input)
    if bot_response:
        st.session_state.chat_history.append({"sender": "Bot", "message": bot_response})

# Display the chat history
for chat in st.session_state.chat_history:
    if chat["sender"] == "User":
        st.text_area("", value=chat["message"], height=50, key=str(chat), disabled=True)
    else:  # For bot messages
        st.markdown(f"**Bot**: {chat['message']}")