from fastapi import FastAPI
from payments.adapter import PaymentBaseAdapter
from payments.factory import PaymentProviderFactory
from models import PaymentRequest

app = FastAPI()

@app.post("/pay")
async def pay(payload:PaymentRequest):
    
    provider:PaymentBaseAdapter = PaymentProviderFactory().get_provider(name=payload.payment_method)
    await provider.pay(payload.payment_payload)
    return 1