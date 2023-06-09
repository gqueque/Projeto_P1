
#importa os itens necessários para o jogo rodar
import pygame
import time
from functions import colisoes_erro
from functions import colisoes_gpt
from functions import colisoes_runtimeerror
from functions import respawnar
from functions import respawnar_municao

# Criando janela
pygame.init()
x = 1280
y = 720

# Startando tempo
tempo_restante = 40
start_time = time.time()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Vida de Monitor")
# background
bg = pygame.image.load("fotos/bg2.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

# monitor
monitor = pygame.image.load("fotos/Monitor_Cin.png").convert_alpha()
monitor = pygame.transform.scale(monitor, (80, 80))
pos_monitor_x = 100
pos_monitor_y = 300

# inimigos ( erro, chatgpt, e runtime)
erro = pygame.image.load("fotos/erro.png").convert_alpha()
erro = pygame.transform.scale(erro, (70, 70))
pos_erro_x = 500
pos_erro_y = 360

chatgpt = pygame.image.load("fotos/gpt.png").convert_alpha()
chatgpt = pygame.transform.scale(chatgpt, (70, 70))
pos_chatgpt_x = 500
pos_chatgpt_y = 300

runtimeerror = pygame.image.load("fotos/runtimeerror.png").convert_alpha()
runtimeerror = pygame.transform.scale(runtimeerror, (70, 70))
pos_runtimeerror_x = 500
pos_runtimeerror_y = 360

# municao do acerto
municao = pygame.image.load("fotos/acerto.png").convert_alpha()
municao = pygame.transform.scale(municao, (35, 35))
pos_x_municao = 110
pos_y_municao = 300
vel_x_municao = 0

# pontuação, startando como 16 por causa de um bug que não conseguimos solucionar
pontos = 16

triggered = False

# definido os rects
monitor_rect = monitor.get_rect()
erro_rect = erro.get_rect()
chatgpt_rect = chatgpt.get_rect()
runtimeerror_rect = runtimeerror.get_rect()
municao_rect = municao.get_rect()

rodando = True

game_over = False
while rodando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    screen.blit(bg, (0, 0))

    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))

    # movimentacao do monitor
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_monitor_y > 1:
        pos_monitor_y -= 5
        if not triggered:
            pos_y_municao -= 5

    if tecla[pygame.K_DOWN] and pos_monitor_y < 665:
        pos_monitor_y += 5
        if not triggered:
            pos_y_municao += 5
    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_municao = 5

    # movimento
    x -= 0.8
    pos_erro_x -= 1.5
    pos_chatgpt_x -= 2.0
    pos_runtimeerror_x -= 2.5
    pos_x_municao += vel_x_municao
    screen.blit(monitor, (pos_monitor_x, pos_monitor_y))
    screen.blit(erro, (pos_erro_x, pos_erro_y))
    screen.blit(chatgpt, (pos_chatgpt_x, pos_chatgpt_y))
    screen.blit(runtimeerror, (pos_runtimeerror_x, pos_runtimeerror_y))
    screen.blit(municao, (pos_x_municao, pos_y_municao))

    # respawnar
    if pos_erro_x == 50:
        pos_erro_x = respawnar()[0]
        pos_erro_y = respawnar()[1]

    if colisoes_erro(monitor_rect, erro_rect, municao_rect) == 2:
        pontos += 1
        pos_erro_x = respawnar()[0]
        pos_erro_y = respawnar()[1]
        pos_x_municao, pos_y_municao, triggered, vel_x_municao = respawnar_municao(pos_monitor_x, pos_monitor_y)
    if colisoes_erro(monitor_rect, erro_rect, municao_rect) == 1:
        pontos -= 1
        pos_erro_x = respawnar()[0]
        pos_erro_y = respawnar()[1]

    if pos_x_municao == 1300:
        pos_x_municao, pos_y_municao, triggered, vel_x_municao = respawnar_municao(pos_monitor_x, pos_monitor_y)

    if pos_chatgpt_x == 50:
        pos_chatgpt_x = respawnar()[0]
        pos_chatgpt_y = respawnar()[1]

    if colisoes_gpt(monitor_rect, chatgpt_rect, municao_rect) == 2:
        pontos += 5
        pos_chatgpt_x = respawnar()[0]
        pos_chatgpt_y = respawnar()[1]
        pos_x_municao, pos_y_municao, triggered, vel_x_municao = respawnar_municao(pos_monitor_x, pos_monitor_y)
    if colisoes_gpt(monitor_rect, chatgpt_rect, municao_rect) == 1:
        pontos -= 5
        pos_chatgpt_x = respawnar()[0]
        pos_chatgpt_y = respawnar()[1]

    if pos_runtimeerror_x == 50:
        pos_runtimeerror_x = respawnar()[0]
        pos_runtimeerror_y = respawnar()[1]

    if colisoes_runtimeerror(monitor_rect, runtimeerror_rect, municao_rect) == 2:
        pontos += 10
        pos_runtimeerror_x = respawnar()[0]
        pos_runtimeerror_y = respawnar()[1]
        pos_x_municao, pos_y_municao, triggered, vel_x_municao = respawnar_municao(pos_monitor_x, pos_monitor_y)
    if colisoes_runtimeerror(monitor_rect, runtimeerror_rect, municao_rect) == 1:
        pontos -= 10
        pos_runtimeerror_x = respawnar()[0]
        pos_runtimeerror_y = respawnar()[1]

    # criando as fontes de pontuação
    estrela = pygame.image.load("fotos/estrela.png").convert_alpha()
    estrela = pygame.transform.scale(estrela, (40, 40))
    pos_estrela_x = 20
    pos_estrela_y = 45
    estrela_rect = estrela.get_rect()
    screen.blit(estrela, (pos_estrela_x, pos_estrela_y))
    estrela_rect.y = pos_estrela_y
    estrela_rect.x = pos_estrela_x

    relogio = pygame.image.load("fotos/relogio.png").convert_alpha()
    relogio = pygame.transform.scale(relogio, (40, 40))
    pos_relogio_x = 20
    pos_relogio_y = 90
    relogio_rect = relogio.get_rect()
    screen.blit(relogio, (pos_relogio_x, pos_relogio_y))
    relogio_rect.y = pos_relogio_y
    relogio_rect.x = pos_relogio_x

    fonte = pygame.font.Font("fonte/Arcades.ttf", 40)
    placar = fonte.render(f"{pontos}", False, (0, 0, 0))
    screen.blit(placar, (80, 50))

    tempo_restante = 40 - int(time.time() - start_time)
    fonte_tempo = pygame.font.Font("fonte/Arcades.ttf", 40)
    texto_tempo = fonte_tempo.render(f"{tempo_restante}s", False, (0, 0, 0))
    screen.blit(texto_tempo, (80, 100))

    # criar as imagens do jogo
    screen.blit(erro, (pos_erro_x, pos_erro_y))
    screen.blit(municao, (pos_x_municao, pos_y_municao))
    screen.blit(chatgpt, (pos_chatgpt_x, pos_chatgpt_y))
    screen.blit(runtimeerror, (pos_runtimeerror_x, pos_runtimeerror_y))
    screen.blit(monitor, (pos_monitor_x, pos_monitor_y))

    # criar o desenho
    # pygame.draw.rect(screen, (255, 0, 0), erro_rect, 4)
    # pygame.draw.rect(screen, (255, 0, 0), municao_rect, 4)
    # pygame.draw.rect(screen, (255, 0, 0), chatgpt_rect, 4)
    # pygame.draw.rect(screen, (255, 0, 0), runtimeerror_rect, 4)
    # pygame.draw.rect(screen, (255, 0, 0), monitor_rect, 4)

    monitor_rect.y = pos_monitor_y
    monitor_rect.x = pos_monitor_x

    erro_rect.y = pos_erro_y
    erro_rect.x = pos_erro_x

    chatgpt_rect.y = pos_chatgpt_y
    chatgpt_rect.x = pos_chatgpt_x

    runtimeerror_rect.y = pos_runtimeerror_y
    runtimeerror_rect.x = pos_runtimeerror_x

    municao_rect.y = pos_y_municao
    municao_rect.x = pos_x_municao

    # Calcule o tempo decorrido desde o início do jogo
    elapsed_time = time.time() - start_time
    if tempo_restante <= 0:
        rodando = False
        game_over = True

    # Se o tempo decorrido for maior ou igual ao tempo de jogo, encerre o jogo

    # Fecha o jogo

    pygame.display.update()
