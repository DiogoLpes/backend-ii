import threading
import time

def baixar_ficheiro(nome):
    print(f"A descarregar {nome}...")
    time.sleep(2) # Simula o tempo de rede
    print(f"Ficheiro {nome} concluído.")

urls = ["Imagem1.jpg", "Video.mp4", "Relatorio.pdf"]

# --- MODO SEQUENCIAL ---
print("--- TESTE SEQUENCIAL ---")
inicio = time.time()
for u in urls:
    baixar_ficheiro(u)
print(f"Tempo total sequencial: {time.time() - inicio:.2f} segundos\n")

# --- MODO COM THREADS ---
print("--- TESTE COM THREADS ---")
inicio_threads = time.time()
threads = []

for u in urls:
    t = threading.Thread(target=baixar_ficheiro, args=(u,))
    threads.append(t)
    t.start()

# Esperar todas as threads terminarem
for t in threads:
    t.join()

print(f"Tempo total com threads: {time.time() - inicio_threads:.2f} segundos")