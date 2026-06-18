import streamlit as st
from chatbot import ChatBot

bot = ChatBot()

st.title("🤖 Sentiment-Aware Customer Support Chatbot")

user_input = st.text_input("Ask something:")

if user_input:
    response = bot.get_response(user_input)
    st.write("Bot:", response)
