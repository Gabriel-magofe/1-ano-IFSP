import socket
import threading

# Configurações do servidor
HOST = '0.0.0.0'
PORTA = 61234

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen()
print(f"[SERVIDOR] Rodando na porta {PORTA}. Aguardando conexões...")

# Guarda as posições iniciais dos jogadores: "ID: 'X,Y'"
posicoes_jogadores = {
    0: "50,50",
    1: "400,50"
}
clientes = {}
id_atual = 0

def gerenciar_cliente(conexao, jogador_id):
    # Envia o ID do próprio jogador e as posições atuais logo ao conectar
    conexao.send(str(jogador_id).encode())
    
    while True:
        try:
            # Recebe a nova posição deste jogador (ex: "120,250")
            dados = conexao.recv(64).decode()
            if not dados:
                break
                
            posicoes_jogadores[jogador_id] = dados
            
            # Envia a posição de AMBOS os jogadores para este cliente específico
            # Formato enviado: "50,50|400,50"
            resposta = f"{posicoes_jogadores[0]}|{posicoes_jogadores[1]}"
            conexao.send(resposta.encode())
        except:
            break

    print(f"[DESCONECTADO] Jogador {jogador_id} saiu.")
    clientes.pop(jogador_id, None)
    conexao.close()

while True:
    conexao, endereco = servidor.accept()
    print(f"[CONEXÃO] {endereco} conectado como Jogador {id_atual}")
    
    clientes[id_atual] = conexao
    threading.Thread(target=gerenciar_cliente, args=(conexao, id_atual)).start()
    id_atual += 1