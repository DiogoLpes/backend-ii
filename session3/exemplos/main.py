import threading
import time

def tarefa_demorada(nome, segundos):
    print(f"Linha {nome}: Iniciando...")
    time.sleep(segundos) # Simula uma espera (I/O)
    print(f"Linha {nome}: Finalizada após {segundos}s")

# Criamos as threads
t1 = threading.Thread(target=tarefa_demorada, args=("A", 3))
t2 = threading.Thread(target=tarefa_demorada, args=("B", 2))

# Iniciamos
t1.start()
t2.start()

# O 'join' faz o programa principal esperar por elas antes de continuar
t1.join()
t2.join()

print("Todas as tarefas concluídas!")