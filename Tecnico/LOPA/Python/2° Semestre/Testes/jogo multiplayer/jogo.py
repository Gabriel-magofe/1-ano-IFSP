import pygame
import socket
import threading

# Configurações de Rede
IP_SERVIDOR = '10.125.230.207' 
PORTA = 61234

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((IP_SERVIDOR, PORTA))
meu_id = int(cliente.recv(64).decode())

# VARIÁVEIS GLOBAIS COMPARTILHADAS ENTRE AS THREADS
# Usamos dicionários ou listas para que as modificações dentro da thread reflitam no jogo
minha_pos = [50, 50] if meu_id == 0 else [400, 50]
pos_adversario = [400, 50] if meu_id == 0 else [50, 50]
jogo_rodando = True

# 1. FUNÇÃO QUE VAI RODAR NA THREAD DE REDE
def escutar_servidor(sock):
    global pos_adversario, jogo_rodando
    
    while jogo_rodando:
        try:
            # Envia nossa posição atual continuamente
            mensagem = f"{minha_pos[0]},{minha_pos[1]}"
            sock.send(mensagem.encode())
            
            # Fica bloqueado aqui esperando a resposta sem travar a tela do jogo!
            dados_recebidos = sock.recv(64).decode()
            if not dados_recebidos:
                break
                
            pos_j0, pos_j1 = dados_recebidos.split("|")
            
            # Atualiza a posição do adversário com base nos dados do servidor
            if meu_id == 0:
                coords = pos_j1.split(",")
                pos_adversario = [int(coords[0]), int(coords[1])]
            else:
                coords = pos_j0.split(",")
                pos_adversario = [int(coords[0]), int(coords[1])]
                
        except Exception as e:
            print("Erro na conexão:", e)
            break
            
    jogo_rodando = False

# 2. INICIANDO A THREAD ANTES DE ENTRAR NO PYGAME
# O argumento daemon=True faz com que a thread feche automaticamente se o programa principal fechar
thread_rede = threading.Thread(target=escutar_servidor, args=(cliente,), daemon=True)
thread_rede.start()

# 3. LOOP PRINCIPAL DO PYGAME (Roda de forma independente)
pygame.init()
tela = pygame.display.set_mode((600, 400))
pygame.display.set_caption(f"Multiplayer com Threads - J0gador {meu_id}")
relogio = pygame.time.Clock()

while jogo_rodando:
    relogio.tick(60) # A tela sempre vai atualizar cravada em 60 FPS
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jogo_rodando = False

    # Input local (atualiza 'minha_pos' imediatamente na tela)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:  minha_pos[0] -= 5
    if teclas[pygame.K_RIGHT]: minha_pos[0] += 5
    if teclas[pygame.K_UP]:    minha_pos[1] -= 5
    if teclas[pygame.K_DOWN]:  minha_pos[1] += 5

    # Desenho dos elementos usando as variáveis compartilhadas
    tela.fill((30, 30, 30))
    
    # Meu quadrado
    cor_meu = (0, 128, 255) if meu_id == 0 else (0, 255, 128)
    pygame.draw.rect(tela, cor_meu, (minha_pos[0], minha_pos[1], 40, 40))
    
    # Quadrado do inimigo (atualizado em background pela thread)
    pygame.draw.rect(tela, (255, 50, 50), (pos_adversario[0], pos_adversario[1], 40, 40))

    pygame.display.flip()

pygame.quit()
cliente.close()