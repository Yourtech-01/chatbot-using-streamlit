import streamlit as st
import json
import random
import joblib

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

with open("/content/intents (1).json") as f:
    intents = json.load(f)

def chatbot_response(text):
    text_vec = vectorizer.transform([text])
    tag = model.predict(text_vec)[0]

    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])

    return "Sorry, I didn't understand that."

st.set_page_config(page_title="Customer Support Chatbot")
st.title("🤖 Customer Support Chatbot")

user_input = st.text_input("You:")

if user_input:
    st.success(chatbot_response(user_input))
