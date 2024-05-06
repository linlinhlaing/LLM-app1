from dotenv import load_dotenv
import os
import langchain_openai
import langchain_community
from langchain_openai import OpenAI
load_dotenv()


myOpenAIKey = os.getenv("myOpenAIKey")
os.environ["OPENAI_API_KEY"] = myOpenAIKey

llm = OpenAI(temperature = 0.9)
response = llm("write a short song about Yangon,Myanmar")
print(response)