import requests
import streamlit as st

# for openai response
def get_openai_response(input_text):
    response = requests.post("http://localhost:8001/essay/invoke",
      json = {'input':{'topic':input_text}}                       
                             )
    return response.json()['output']['content']


   
# for ollama response
def get_ollama_response(input_text):
    response = requests.post("http://localhost:8001/poem/invoke",
     json = {'input':{'topic':input_text}}                        
     )
    return response.json()['output']['content']
# creating streamlit application
st.title("Langchain Demo with OpenAI  🤖💡🐦🔗 🦙💻")
input_text1 = st.text_input("write an essay on ")
input_text2 = st.text_input("write a poem on ")

if input_text1:
    st.write(get_openai_response(input_text1))
if input_text2:
    st.write(get_ollama_response(input_text2))    
    