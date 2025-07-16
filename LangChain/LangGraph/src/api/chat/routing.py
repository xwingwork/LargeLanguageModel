from typing import List
from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from api.db import get_session
from api.ai.schemas import EmailMessageSchema
from api.ai.services import generate_email_message
from .models import ChatMessagePayload, ChatMessage, ChatMessageListItem

router = APIRouter()

@router.get("/")
def chat_health():
    return {"message":"is!!","status":"Ok..."}

@router.get("/recent", response_model=List[ChatMessageListItem])
def chat_list_message(session: Session = Depends(get_session)):
    query = select(ChatMessage)
    results = session.exec(query).fetchall()[:10] # 最多 10 筆
    return results

@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(
    payload:ChatMessagePayload,
    session: Session = Depends(get_session)
    ):
    data = payload.model_dump()
    print(data)
    obj = ChatMessage.model_validate(data)
    session.add(obj)
    session.commit()
    # session.refresh(obj) # 確保取得資料庫中的 ID
    # return obj
    response = generate_email_message(payload.message)
    return response