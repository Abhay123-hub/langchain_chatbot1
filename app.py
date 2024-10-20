from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
os.environ["OPENAI_API_KEY"] = 

app = FastAPI(
       title = "langchain server",
       version = "1.0",
       description = "A simple API server"


               )
add_routes(
    app,
    ChatOpenAI(),
    path = "/openai"
)


model = ChatOpenAI()
llm = ChatOpenAI()

# creating prompt template for openai
prompt1 = ChatPromptTemplate.from_template("write an paragraph on the {topic} within 100 words")
# creating prompt for ollama
prompt2 = ChatPromptTemplate.from_template("write a poem on the {topic} within 100 words for five year old children")


add_routes(
    app,
    prompt1|model,
    path = "/essay"
)
add_routes(
    app,
    prompt2|llm,
    path = "/poem"
)


if __name__ == "__main__":
    uvicorn.run(app,host = "localhost",port = 8002)