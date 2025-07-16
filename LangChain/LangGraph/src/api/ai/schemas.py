from pydantic import BaseModel, Field

class EmailMessageSchema(BaseModel):
    subject: str
    contents: str
    invalid_request: bool | None = Field(default=False)