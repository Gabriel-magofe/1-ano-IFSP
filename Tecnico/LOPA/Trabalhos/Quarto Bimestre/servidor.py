import socket
import math

# Configurações de Rede
IP = "0.0.0.0" # Aceita conexões de qualquer lugar (sua rede ou internet)
PORTA = 5555
MAX_JOGADORES = 30

# Cria o socket UDP (rápido para jogos em tempo real)
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind((IP, PORTA))

# Guarda os jogadores conectados: { endereco_ip_porta: {dados} }
jogadores = {}
proximo_id = 1

print(f"Servidor rodando na porta {PORTA}... Aguardando até {MAX_JOGADORES} jogadores!")

def verificar_acerto(atirador_addr, atirador):
    # Calcula a linha do tiro baseada no ângulo da arma (em graus)
    rad = math.radians(atirador["angulo"])
    dir_x = math.cos(rad)
    dir_y = math.sin(rad)

    # Verifica todos os outros jogadores na arena
    for addr, alvo in jogadores.items():
        if addr == atirador_addr or alvo["vida"] <= 0:
            continue

        # Distância entre o atirador e o possível alvo
        dx = alvo["x"] - atirador["x"]
        dy = alvo["y"] - atirador["y"]
        distancia = math.hypot(dx, dy)

        if distancia > 500: # Alcance máximo da arma
            continue

        # Checa se o alvo está na linha da mira (produto escalar simples)
        alinhamento = (dx * dir_x + dy * dir_y) / (distancia + 0.0001)
        if alinhamento > 0.98: # Margem de acerto do cubo
            # CHECAGEM DO ESCUDO
            if alvo["escudo"] == 1:
                print(f"{alvo['nome']} bloqueou o tiro de {atirador['nome']} com o escudo!")
                return

            # Aplica dano
            alvo["vida"] -= 25
            print(f"{atirador['nome']} acertou {alvo['nome']}! Vida restante: {alvo['vida']}")

            if alvo["vida"] <= 0:
                print(f"{alvo['nome']} foi eliminado por {atirador['nome']}!")
                # AQUI VOCÊ VAI CHAMAR O ARQUIVO DA PESSOA 3 NO FUTURO:
                # banco.registrar_abate(atirador['nome'], alvo['nome'])

while True:
    try:
        # Recebe mensagem de até 1024 bytes de algum jogador
        dados, addr = servidor.recvfrom(1024)
        mensagem = dados.decode("utf-8")
        partes = mensagem.split(";")
        comando = partes[0]

        # 1. JOGADOR ENTRANDO NA SALA
        if comando == "ENTRAR":
            if len(jogadores) >= MAX_JOGADORES:
                servidor.sendto("CHEIO".encode("utf-8"), addr)
                continue

            nome = partes[1]
            jogadores[addr] = {
                "id": proximo_id,
                "nome": nome,
                "x": 100.0,
                "y": 100.0,
                "angulo": 0.0,
                "vida": 100,
                "escudo": 0
            }
            servidor.sendto(f"BEMVINDO;{proximo_id}".encode("utf-8"), addr)
            print(f"Jogador {nome} (ID {proximo_id}) entrou! Total: {len(jogadores)}/30")
            proximo_id += 1

        # 2. ATUALIZAÇÃO DE MOVIMENTO E ESCUDO
        elif comando == "POS" and addr in jogadores:
            # Formato esperado: POS;x;y;angulo;escudo
            jogadores[addr]["x"] = float(partes[1])
            jogadores[addr]["y"] = float(partes[2])
            jogadores[addr]["angulo"] = float(partes[3])
            jogadores[addr]["escudo"] = int(partes[4])

        # 3. JOGADOR ATIROU
        elif comando == "TIRO" and addr in jogadores:
            if jogadores[addr]["vida"] > 0:
                verificar_acerto(addr, jogadores[addr])

        # 4. ENVIA O ESTADO DE TODOS OS CUBOS DE VOLTA PARA QUEM MANDOU MSG
        estado_mundo = []
        for j in jogadores.values():
            estado_mundo.append(f"{j['id']},{j['x']},{j['y']},{j['angulo']},{j['vida']},{j['escudo']}")
        
        pacote_resposta = "ESTADO;" + "|".join(estado_mundo)
        servidor.sendto(pacote_resposta.encode("utf-8"), addr)

    except Exception as e:
        print(f"Erro na rede: {e}")
