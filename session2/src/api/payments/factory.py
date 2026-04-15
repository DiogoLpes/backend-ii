from payments.providers import MBWayPayment, PaypalPayment
from payments.adapter import PaymentBaseAdapter


class PaymentProviderFactory:
    REGISTRY:dict[str, type[PaymentBaseAdapter]] = {
        "mbway": "MBWayPayment",
        "paypal": "PaypalPayment"
    }
    
    def get_provider(self, name: str) -> PaymentBaseAdapter:
        
        provider = self.REGISTRY.get(name,None)
        
        if not provider:
            raise ValueError(f"Método de pagamento '{name}' não suportado.")
        
        return provider()