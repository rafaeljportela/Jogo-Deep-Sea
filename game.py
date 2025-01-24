from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.sprite import *
import time
import random

def iniciar_jogo():
    janela = Window(1300, 800)
    keyboard = Keyboard()

    fundo_estatico = GameImage("fundo1.png")
    fundo_dinamico1 = GameImage("fundo2.png")
    fundo_dinamico2 = GameImage("fundo2.png")
    fundo_dinamico1.set_position(0, 0)
    fundo_dinamico2.set_position(fundo_dinamico1.width, 0)
    fundo_dinamico_velocidade = 100

    submarino = Sprite("submarino.png")
    submarino.set_position(100, janela.height // 2 - submarino.height // 2)
    velsub = 2

    coracao_sprite = Sprite("coracao.png")
    moeda_sprite = Sprite("moeda.png")

    coracao_ativo = False
    moeda_ativa = False
    tempo_coracao = 5  # Tempo entre coracoes
    tempo_moeda = 7  # Tempo entre moedas
    ultimo_coracao = time.time()
    ultima_moeda = time.time()


    obstaculos_data = {
        "tubarao": {"sprite": "tubarao.png", "velocidade": 250, "intervalo": 3, "pontos": 10, "quantidade": 3},
        "baleia": {"sprite": "baleia.png", "velocidade": 200, "intervalo": 5, "pontos": 20, "quantidade": 2}
    }

    obstaculos_ativos = []
    for key, data in obstaculos_data.items():
        for _ in range(data["quantidade"]):
            obstaculo = Sprite(data["sprite"])
            obstaculo.set_position(janela.width + random.randint(0, 300), random.randint(0, janela.height - obstaculo.height))
            data.setdefault("sprites", []).append(obstaculo)
            obstaculos_ativos.append((key, obstaculo))
        data["ultimo_tempo"] = time.time()

    tiros = []
    tiro_sprite = "tiro.png"
    velocidade_tiro = 300
    cooldown_tiro = 0.5
    ultimo_tiro = 0

    jogo_ativo = True
    fase = 1
    vidas = 1
    pontuacao = 0
    moedas = 0

    barra_vida = 100
    barra_diminui = 3  # Velocidade de diminuição da barra por segundo

    inicio_fase = time.time()
    duracao_fase1 = 60  # 1 minuto e 30 segundos

    super_tiro = False
    super_tiro_usado = False

    mensagem_fase = False
    fase2_concluida = False

    bin = 3

    while jogo_ativo:
        tempo_restante = duracao_fase1 - (time.time() - inicio_fase)

        if fase == 1:
            barra_vida -= barra_diminui * janela.delta_time()

            if barra_vida <= 0:
                jogo_ativo = False
                print("Game Over! O submarino ficou sem vida.")

            if time.time() - ultimo_coracao >= tempo_coracao and not coracao_ativo:
                coracao_ativo = True
                coracao_sprite.set_position(janela.width, random.randint(0, janela.height - coracao_sprite.height))
                ultimo_coracao = time.time()

            if time.time() - ultima_moeda >= tempo_moeda and not moeda_ativa:
                moeda_ativa = True
                moeda_sprite.set_position(janela.width, random.randint(0, janela.height - moeda_sprite.height))
                ultima_moeda = time.time()

            if tempo_restante <= 0:
                if moedas > 6:
                    super_tiro = True

                mensagem_fase = True




        elif fase == 2:

            if mensagem_fase:
                # Função para reiniciar o cenário ao entrar na fase 2

                def reiniciar_fase_2():
                    nonlocal fundo_dinamico1, fundo_dinamico2, obstaculos_ativos, submarino

                    # Resetar o fundo dinâmico

                    fundo_dinamico1.set_position(0, 0)

                    fundo_dinamico2.set_position(fundo_dinamico1.width, 0)

                    # Limpar todos os obstáculos da fase anterior

                    obstaculos_ativos = []

                    # Reposicionar o submarino na posição inicial

                    submarino.set_position(100, janela.height // 2 - submarino.height // 2)

                reiniciar_fase_2()

                mensagem_fase = False

            tempo_restante = duracao_fase1 - (time.time() - inicio_fase)

            if tempo_restante <= 0:

                if all(obstaculo.x + obstaculo.width < 0 for _, obstaculo in obstaculos_ativos):

                    # O jogador venceu a fase 2

                    fundo_estatico.draw()

                    fundo_dinamico1.draw()

                    fundo_dinamico2.draw()

                    janela.draw_text("Parabéns! Você venceu a Fase 2!", janela.width // 2 - 200,
                                     janela.height // 2 - 50, size=32, color=(255, 255, 255))

                    janela.update()

                    time.sleep(3)

                    jogo_ativo = False

                else:

                    # O jogador perdeu a fase 2

                    fundo_estatico.draw()

                    fundo_dinamico1.draw()

                    fundo_dinamico2.draw()

                    janela.draw_text("Você perdeu! Não eliminou todos os obstáculos a tempo.", janela.width // 2 - 300,
                                     janela.height // 2 - 50, size=32, color=(255, 255, 255))

                    janela.update()

                    time.sleep(3)

                    jogo_ativo = False

            tempo_restante = duracao_fase1 - (time.time() - inicio_fase)

            if tempo_restante <= 0:

                if all(obstaculo.x + obstaculo.width < 0 for _, obstaculo in obstaculos_ativos):

                    # O jogador venceu a fase 2

                    fundo_estatico.draw()

                    fundo_dinamico1.draw()

                    fundo_dinamico2.draw()

                    janela.draw_text("Parabéns! Você venceu a Fase 2!", janela.width // 2 - 200,
                                     janela.height // 2 - 50, size=32, color=(255, 255, 255))

                    janela.update()

                    time.sleep(3)

                    jogo_ativo = False

                else:

                    # O jogador perdeu a fase 2

                    fundo_estatico.draw()

                    fundo_dinamico1.draw()

                    fundo_dinamico2.draw()

                    janela.draw_text("Você perdeu! Não eliminou todos os obstáculos a tempo.", janela.width // 2 - 300,
                                     janela.height // 2 - 50, size=32, color=(255, 255, 255))

                    janela.update()

                    time.sleep(3)

                    jogo_ativo = False

        if mensagem_fase:
            fundo_estatico.draw()
            fundo_dinamico1.draw()
            fundo_dinamico2.draw()
            janela.draw_text(f"Fim da Fase 1! Moedas coletadas: {moedas}", janela.width // 2 - 200, janela.height // 2 - 50, size=32, color=(255, 255, 255))
            janela.draw_text("Pressione 'P' para avançar para a Fase 2", janela.width // 2 - 200, janela.height // 2, size=24, color=(255, 255, 255))
            janela.update()

            if keyboard.key_pressed("P"):
                fase = 2
                mensagem_fase = False
                inicio_fase = time.time()
                moedas = 0

            continue

        if keyboard.key_pressed("UP") and submarino.y > 0:
            submarino.y -= velsub
        if keyboard.key_pressed("DOWN") and submarino.y + submarino.height < janela.height:
            submarino.y += velsub
        if keyboard.key_pressed("LEFT") and submarino.x > 0:
            submarino.x -= velsub
        if keyboard.key_pressed("RIGHT") and submarino.x + submarino.width < janela.width:
            submarino.x += velsub

        if keyboard.key_pressed("SPACE") and time.time() - ultimo_tiro >= cooldown_tiro:
            novo_tiro = Sprite(tiro_sprite)
            novo_tiro.set_position(submarino.x + submarino.width, submarino.y + submarino.height // 2 - novo_tiro.height // 2)
            novo_tiro.y_speed = 0
            tiros.append(novo_tiro)
            ultimo_tiro = time.time()


        if super_tiro and keyboard.key_pressed("F") and bin > 0:
            # Tiro reto
            novo_tiro_reto = Sprite(tiro_sprite)
            novo_tiro_reto.set_position(submarino.x + submarino.width, submarino.y + submarino.height // 2 - novo_tiro_reto.height // 2)
            novo_tiro_reto.y_speed = 0
            tiros.append(novo_tiro_reto)

            # Tiro diagonal superior
            novo_tiro_superior = Sprite(tiro_sprite)
            novo_tiro_superior.set_position(submarino.x + submarino.width, submarino.y + submarino.height // 2 - novo_tiro_superior.height // 2)
            novo_tiro_superior.y_speed = -100
            tiros.append(novo_tiro_superior)

            # Tiro diagonal inferior
            novo_tiro_inferior = Sprite(tiro_sprite)
            novo_tiro_inferior.set_position(submarino.x + submarino.width, submarino.y + submarino.height // 2 - novo_tiro_inferior.height // 2)
            novo_tiro_inferior.y_speed = 100
            tiros.append(novo_tiro_inferior)

            bin = bin - 1

        fundo_dinamico1.x -= fundo_dinamico_velocidade * janela.delta_time()
        fundo_dinamico2.x -= fundo_dinamico_velocidade * janela.delta_time()

        if fundo_dinamico1.x + fundo_dinamico1.width <= 0:
            fundo_dinamico1.x = fundo_dinamico2.x + fundo_dinamico2.width
        if fundo_dinamico2.x + fundo_dinamico2.width <= 0:
            fundo_dinamico2.x = fundo_dinamico1.x + fundo_dinamico1.width

        fundo_estatico.draw()
        fundo_dinamico1.draw()
        fundo_dinamico2.draw()

        submarino.draw()

        for tiro in tiros[:]:
            tiro.x += velocidade_tiro * janela.delta_time()
            if hasattr(tiro, 'y_speed'):
                tiro.y += tiro.y_speed * janela.delta_time()
            tiro.draw()
            if tiro.x > janela.width or tiro.y < 0 or tiro.y > janela.height:
                tiros.remove(tiro)

        if coracao_ativo:
            coracao_sprite.x -= fundo_dinamico_velocidade * janela.delta_time()
            coracao_sprite.draw()
            if coracao_sprite.collided(submarino):
                barra_vida = min(100, barra_vida + 20)
                coracao_ativo = False

        if moeda_ativa:
            moeda_sprite.x -= fundo_dinamico_velocidade * janela.delta_time()
            moeda_sprite.draw()
            if moeda_sprite.collided(submarino):
                moedas += 1
                moeda_ativa = False

        for key, obstaculo in obstaculos_ativos:
            obstaculo.x -= obstaculos_data[key]["velocidade"] * janela.delta_time()
            obstaculo.draw()

            # Colisão com o submarino
            if obstaculo.collided(submarino):
                jogo_ativo = False
                print("Game Over! O submarino colidiu com um obstáculo.")

            # Colisão com os tiros
            for tiro in tiros[:]:
                if tiro.collided(obstaculo):
                    tiros.remove(tiro)
                    obstaculo.set_position(janela.width + random.randint(0, 300), random.randint(0, janela.height - obstaculo.height))

            if obstaculo.x + obstaculo.width < 0:
                obstaculo.set_position(janela.width + random.randint(0, 300), random.randint(0, janela.height - obstaculo.height))

        janela.draw_text(f"Vida: {int(barra_vida)}", 10, 10, size=24, color=(255, 255, 255))
        janela.draw_text(f"Moedas: {moedas}", 10, 40, size=24, color=(255, 255, 255))
        janela.draw_text(f"Tempo restante: {int(tempo_restante)}", janela.width // 2 - 100, 10, size=24, color=(255, 255, 255))

        janela.update()
