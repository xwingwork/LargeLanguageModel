from typing import AsyncGenerator
from api.weather.openAI.model import get_openai_llm
from api.ai.schemas import EmailMessageSchema
from api.chat.models import ChatMessage, ChatMessagePayload
from api.db import get_session
from api.weather.services import get_weather

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlmodel import Session, select
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

# from api.db import get_session
# from api.ai.schemas import EmailMessageSchema
# from api.ai.services import generate_email_message
# from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem

router = APIRouter()



# @router.get("/recent", response_model=List[ChatMessageListItem])
# def chat_list_message(session: Session = Depends(get_session)):
#     query = select(ChatMessage)
#     results = session.exec(query).fetchall()[:10] # 最多 10 筆
#     return results

# 使用其他案例際有的傳輸物件 ChatMessagePayload & EmailMessageSchema
@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(
    payload:ChatMessagePayload,
    session: Session = Depends(get_session)
    ):
    data = payload.model_dump()    
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    app = get_weather()

    response = app.invoke({"message":[payload.message]})    
    return response


@router.post("/q")
async def chat_create_message(
    payload:ChatMessagePayload,
    # session: Session = Depends(get_session)
    ):
    # data = payload.model_dump()    
    # obj = ChatMessage.model_validate(data)
    # session.add(obj)
    # session.commit()

    prompt = ChatPromptTemplate.from_template("請你告訴我 k8s 跟 docker 區別 {topic}")
    parser = StrOutputParser()
    app = prompt | get_openai_llm() | parser
    # chunks = []
    # async for chunk in app.astream("請你告訴我 k8s 跟 docker 區別"):
    #     chunks.append(chunk)
    #     print(chunk.content, end="|", flush=True)


    full_response_content = ""
    async def generate_response_chunks() -> AsyncGenerator[str, None]:
        nonlocal full_response_content # 允許修改外層變數
        try:
            # 使用 LangChain LLM 的 .stream() 方法進行串流
            # 假設您的 llm_model.stream() 方法接收一個列表或單個訊息
            # 如果您的 app.invoke() 預期的是字典，這裡也需要調整
            async for chunk in app.astream("請你告訴我 k8s 跟 docker 區別"):
                # 每個 chunk 通常是一個 BaseModel，包含 content 屬性
                if chunk:
                    full_response_content += chunk
                    yield chunk # 將每個片段傳送給客戶端
            # 在串流結束後，您可以選擇將完整的回答儲存到資料庫
            # 例如：new_chat_message.response = full_response_content
            # session.add(new_chat_message)
            # await session.commit() # 再次提交以儲存完整的 LLM 回應
            
        except Exception as e:
            # 處理 LLM 呼叫或串流中的錯誤
            print(f"LLM 串流錯誤: {e}")
            yield f"ERROR: LLM 串流發生錯誤 - {e}"
            # 這裡不應該拋出 HTTPException，因為 HTTP 狀態碼已經是 200，
            # 錯誤會作為串流的一部分傳送。
    # 4. 返回 StreamingResponse
    # media_type 通常是 "text/event-stream" 用於 SSE，或 "text/plain" 用於簡單的文字串流
    return StreamingResponse(generate_response_chunks(), media_type="text/plain") # 或 "text/event-stream"

