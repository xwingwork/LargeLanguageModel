from langgraph.graph import StateGraph, END

from api.weather.openAI.agent import call_model
from api.weather.models import AllState
from api.weather.tools import weather_tool


# Defining condition function
def query_classify(state: AllState):
  messages = state["messages"]
  ctx = messages[0]
  if ctx == "no_response":
    return "end"
  else:
    return "continue"

def get_weather():    
    graph_builder = StateGraph(AllState)
    graph_builder.add_node("agent", call_model)
    graph_builder.add_node("weather", weather_tool)

    graph_builder.set_entry_point("agent")

    # Create an conditional edge
    graph_builder.add_conditional_edges('agent',query_classify,{
    "end": END,
    "continue": "weather"
    })


    app = graph_builder.compile()
    return app