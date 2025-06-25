from pydantic import BaseModel


class ChatRequest(BaseModel):
    """채팅 요청 모델"""
    message: str
    
    class Config:
        schema_extra = {
            "example": {
                "message": "iPhone 15 Pro 가격 알려줘"
            }
        }


class ChatResponse(BaseModel):
    """채팅 응답 모델"""
    response: str
    
    class Config:
        schema_extra = {
            "example": {
                "response": "iPhone 15 Pro 최저가 정보를 찾았습니다. 다나와에서 1,200,000원에 판매 중입니다."
            }
        }