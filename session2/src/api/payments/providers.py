from adapter import PaymentBaseAdapter


class MBWayPayment(PaymentBaseAdapter):
    
    async def pay(self, payload: dict) -> bool:
        print(f"Processando pagamento via MBWay com payload: {payload}")
        return True
    
class PaypalPayment(PaymentBaseAdapter):
    
    async def pay(self, payload: dict) -> bool:
        print(f"Processando pagamento via Paypal com payload: {payload}")
        return True