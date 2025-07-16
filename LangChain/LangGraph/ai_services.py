import os

from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI

class EmailMessage(BaseModel):
    subject: str
    contents: str
    invalid_request: bool | None = Field(default=False)

OPENAI_BASE_URL = os.environ.get('OPENAI_BASE_URL') or None
OPENAI_MODEL_NAME = os.environ.get('OPENAI_MODEL_NAME') or 'gpt-4o-mini'
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    raise NotImplementedError("`OPENAI_API_KEY` is required")

openai_params={    
    "model": OPENAI_MODEL_NAME,
    "api_key": OPENAI_API_KEY,
}
if OPENAI_BASE_URL:
    openai_params['base_url'] = OPENAI_BASE_URL

llm_base = ChatOpenAI(**openai_params) # ** 等同於指定 key 方式傳遞值(model_name="gpt-3.5-turbo",)
llm = llm_base.with_structured_output(EmailMessage)

messages = [
    ("system",""),()
]

response = llm.invoke(llm)

print(response)