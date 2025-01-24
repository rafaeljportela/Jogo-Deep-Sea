from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.sprite import *
from PPlay.mouse import *
from game import iniciar_jogo

janela = Window(1300,800)
keyboard = Keyboard()
mouse = Mouse()
cenario = GameImage("background.png")
fundo = GameImage("fundoins.png")
instrucoes = Sprite("instrucoes.png")
jogar = Sprite("jogar.png")
#ranking = Sprite("ranking.png")
sair = Sprite("sair.png")
facil = Sprite("facil.png")
medio = Sprite("medio.png")
dificil = Sprite("dificil.png")
facil.set_position(janela.width / 2 - facil.width / 2, 150)
medio.set_position(janela.width / 2 - medio.width / 2, 300)
dificil.set_position(janela.width / 2 - dificil.width / 2, 450)
instrucoes.set_position(janela.width / 2 - instrucoes.width / 2, 700)
jogar.set_position(janela.width / 2 - jogar.width / 2, 510)
#ranking.set_position(janela.width / 2 - ranking.width / 2, 360)
sair.set_position(janela.width / 2 - sair.width / 2, 600)


def mostrar_instrucoes():
    while True:
        fundo.draw()
        janela.update()

        if keyboard.key_pressed("ESC"):
            break
def mostrar_ranking(janela):
    try:
        with open("ranking.txt", "r") as arquivo:
            linhas = arquivo.readlines()
    except FileNotFoundError:
        linhas = []

    jogadores = []
    for linha in linhas:
        try:
            nome, pontuacao, data = linha.strip().split(", ")
            jogadores.append((nome, int(pontuacao), data))
        except ValueError:
            continue

    jogadores = sorted(jogadores, key=lambda x: x[1], reverse=True)

    janela.set_background_color((0, 0, 0))
    janela.draw_text("Ranking", janela.width // 2 - 50, 50, size=30, color=(255, 255, 255))
    for i, (nome, pontuacao, data) in enumerate(jogadores[:5]):
        texto = f"{i + 1}. {nome} - {pontuacao} pontos ({data})"
        janela.draw_text(texto, 100, 150 + i * 50, size=20, color=(255, 255, 255))

    janela.update()
    while not keyboard.key_pressed("ESC"):
        janela.update()


def game_loop():
    while True:
        janela.update()
        janela.set_background_color([0, 0, 0])
        if keyboard.key_pressed("ESC"):
            break

def escolher_dificuldade():
    while True:
        janela.update()
        cenario.draw()
        facil.draw()
        medio.draw()
        dificil.draw()
        if keyboard.key_pressed("ESC"):
            break
while True:
    cenario.draw()
    instrucoes.draw()
    jogar.draw()
    #ranking.draw()
    sair.draw()
    if mouse.is_over_object(jogar):
        if mouse.is_button_pressed(1):
            iniciar_jogo()

    if mouse.is_over_object(instrucoes):
        if mouse.is_button_pressed(1):
            mostrar_instrucoes()

    #if mouse.is_over_object(ranking):
        if mouse.is_button_pressed(1):
            mostrar_ranking(janela)

    if mouse.is_over_object(sair):
        if mouse.is_button_pressed(1):
            sys.exit()

    janela.update()