import os

from langchain_openai import ChatOpenAI
OPENAI_BASE_URL = os.environ.get('OPENAI_BASE_URL') or None
OPENAI_MODEL_NAME = os.environ.get('OPENAI_MODEL_NAME') or 'gpt-4o-mini'
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')

# https://python.langchain.com/docs/integrations/chat/openai/#instantiation

def get_openai_llm():
    openai_params={    
        "model": OPENAI_MODEL_NAME,
        "api_key": OPENAI_API_KEY,
        "temperature":0.4 # 指定範圍，避免過多的臆測
    }
    return ChatOpenAI(**openai_params)
