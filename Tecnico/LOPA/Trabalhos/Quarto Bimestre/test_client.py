import socket
import time

# Endereço do seu servidor (127.0.0.1 significa "este mesmo computador")
IP_SERVIDOR = "127.0.0.1"
PORTA_SERVIDOR = 5555

cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente.settimeout(2.0) # Espera no máximo 2 segundos por resposta

def enviar(mensagem):
    print(f"\n[ENVIANDO] -> {mensagem}")
    cliente.sendto(mensagem.encode("utf-8"), (IP_SERVIDOR, PORTA_SERVIDOR))
    
    try:
        resposta, _ = cliente.recvfrom(1024)
        print(f"[SERVIDOR RESPONDEU] <- {resposta.decode('utf-8')}")
    except socket.timeout:
        print("[ERRO] O servidor não respondeu! Ele está rodando?")

# --- SIMULAÇÃO DE JOGADA ---

# 1. Entra na partida
enviar("ENTRAR;JogadorTeste")
time.sleep(1)

# 2. Anda para X=150, Y=200, mira no ângulo 0 e deixa o escudo DESLIGADO (0)
enviar("POS;150;2000;0;")
time.sleep(1)

# 3. Dá um tiro
enviar("TIRO")
time.sleep(1)

# 4. Liga o escudo (1)
enviar("POS;150;200;0;1")
print("\nTeste finalizado!")
