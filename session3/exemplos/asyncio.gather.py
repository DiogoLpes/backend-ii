import asyncio
import time

async def simular_api(id_chamada):
    print(f"Chamada {id_chamada}: Enviando pedido...")
    await asyncio.sleep(2)  # Simula latência da internet
    return f"Resultado da API {id_chamada}"

async def main():
    inicio = time.time()
    
    print("Fazendo 5 chamadas de uma vez...")
    
    # O gather junta várias corrotinas e executa-as em simultâneo
    resultados = await asyncio.gather(
        simular_api(1),
        simular_api(2),
        simular_api(3),
        simular_api(4),
        simular_api(5)
    )
    
    for r in resultados:
        print(r)
        
    fim = time.time()
    print(f"\nTempo total: {fim - inicio:.2f} segundos")
    print("Nota: Cada chamada demora 2s, mas o total foi ~2s e não 10s!")

asyncio.run(main())