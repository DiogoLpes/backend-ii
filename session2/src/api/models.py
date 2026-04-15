from pydantic import BaseModel

class PaymentRequest(BaseModel):
    email: str
    cart: list[dict]
    payment_method: str
    payment_payload: dict