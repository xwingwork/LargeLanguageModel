
from api.weather.openAI.model import get_openai_llm
from api.weather.models import AllState
from langchain.prompts import ChatPromptTemplate


def call_model(state: AllState):
    llm = get_openai_llm()
    messages = state["messages"]
    prompt_str = """
You are given one question and you have to extract city name from it
Don't respond anything except the city name and don't reply anything if you can't find city name
Only reply the city name if it exists or reply 'no_response' if there is no city name in question

  Here is the question:
  {messages}
"""
    prompt = ChatPromptTemplate.from_template(prompt_str)
    chain = prompt | llm    
    response = chain.invoke(messages)
    return  {"messages": [response]}
