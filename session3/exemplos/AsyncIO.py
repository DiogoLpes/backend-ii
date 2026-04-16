import asyncio

async def saudacao(nome, tempo):
    print(f"A preparar saudação para {nome}...")
    await asyncio.sleep(tempo) # Simula uma espera de rede/disco
    print(f"Olá, {nome}! (após {tempo}s)")

async def main():
    # Criamos várias tarefas ao mesmo tempo
    tarefa1 = asyncio.create_task(saudacao("Alice", 3))
    tarefa2 = asyncio.create_task(saudacao("Bruno", 1))
    tarefa3 = asyncio.create_task(saudacao("Carlos", 2))
    
    print("Iniciei as saudações...")
    
    # Esperamos que ambas terminem
    await tarefa1
    await tarefa2
    await tarefa3

# Para correr o programa assíncrono
asyncio.run(main())