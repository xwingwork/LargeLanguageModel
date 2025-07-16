from datetime import datetime, timezone
from sqlmodel import SQLModel, Field, DateTime

def get_utc_now():
    return datetime.now().replace(tzinfo=timezone.utc)
# 輸入資料的物件
class ChatMessagePayload(SQLModel):
    message: str
# 無存的物件
class ChatMessage(SQLModel,table=True):
    id: int | None = Field(default=None, primary_key=True) 
    message: str
    created_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=DateTime(timezone=True),
        primary_key=False,
        nullable=False
    )

# 回傳結果的物件
class ChatMessageListItem(SQLModel):
    message: str
    created_at: datetime = Field(default=None)