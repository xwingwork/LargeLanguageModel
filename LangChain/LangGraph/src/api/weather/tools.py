from api.weather.models import AllState


def get_taiwan_weather(city: str) -> str:
    """查詢台灣特定城市的天氣狀況。"""
    weather_data = {
        "台北": "晴天，溫度28°C",
        "台中": "多雲，溫度26°C",
        "高雄": "陰天，溫度30°C"
    }
    print(f"{city}*******")
    return f"{city}的天氣：{weather_data.get(city, '暫無資料')}"

def weather_tool(state):
  context = state["messages"]
  print(context)
  city_name = context[1].content
  data = get_taiwan_weather(city_name)
  return {"messages": [data]}
