import pygame
import random
import time
pygame.init()
x = 1280
y = 720

tempo_restante = 40
start_time = time.time()
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Monitores vs Dikastis")
#background
bg = pygame.image.load("fotos/bg2.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

#monitor
monitor = pygame.image.load("fotos/Monitor_Cin.png").convert_alpha()
monitor = pygame.transform.scale(monitor, (80, 80))
pos_monitor_x = 100
pos_monitor_y = 300

#inimigos ( erro, chatgpt, cola, aluno chato com duvida com duvida no discord)
erro = pygame.image.load("fotos/erro.png").convert_alpha()
erro = pygame.transform.scale(erro, (70, 70))
pos_erro_x = 500
pos_erro_y = 360

chatgpt = pygame.image.load("fotos/gpt.png").convert_alpha()
chatgpt = pygame.transform.scale(chatgpt, (70, 70))
pos_chatgpt_x = 500
pos_chatgpt_y = 300

# municao do acerto
municao = pygame.image.load("fotos/pngwing.com.png").convert_alpha()
municao = pygame.transform.scale(municao, (35, 35 ))
pos_x_municao = 110
pos_y_municao = 300
vel_x_municao = 0

pontos = 1

triggered = False

#definido os rects
monitor_rect = monitor.get_rect()
erro_rect = erro.get_rect()
chatgpt_rect = chatgpt.get_rect()
municao_rect = municao.get_rect()



rodando = True


# definindo as colisoes
def colisoes():
    global pontos
    if monitor_rect.colliderect(erro_rect) or erro_rect.x == 60:
        pontos -= 1
        return True
    elif municao_rect.colliderect(erro_rect):
        pontos += 1

        return True
    else:
        return False

# respawnar os inimigos
def respawnar():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def respawnar_municao():
    triggered = False
    respawnar_municao_x = pos_monitor_x
    respawnar_municao_y = pos_monitor_y
    vel_x_municao = 0
    return [respawnar_municao_x, respawnar_municao_y, triggered, vel_x_municao]
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

    #movimentacao do monitor
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_monitor_y > 1:
        pos_monitor_y -= 1
        if not triggered:
            pos_y_municao -= 1

    if tecla[pygame.K_DOWN] and pos_monitor_y < 665:
        pos_monitor_y += 1
        if not triggered:
            pos_y_municao += 1
    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_x_municao = 1

    #movimento
    x -= 0.4
    pos_erro_x -= 0.6
    pos_chatgpt_x -= 0.5
    pos_x_municao += vel_x_municao
    screen.blit(monitor,(pos_monitor_x, pos_monitor_y))
    screen.blit(erro, (pos_erro_x, pos_erro_y))
    screen.blit(chatgpt, (pos_chatgpt_x, pos_chatgpt_y))
    screen.blit(municao, (pos_x_municao, pos_y_municao))

    #respawnar
    if pos_erro_x == 50:
        pos_erro_x = respawnar()[0]
        pos_erro_y = respawnar()[1]

    if pos_erro_x == 50 or colisoes():
        pos_erro_x = respawnar()[0]
        pos_erro_y = respawnar()[1]

    if pos_x_municao == 1300:
        pos_x_municao, pos_y_municao, triggered, vel_x_municao = respawnar_municao()

    if pos_chatgpt_x:
        pos_chatgpt_x = respawnar()[0]
        pos_chatgpt_y = respawnar()[1]

    if pos_chatgpt_x or colisoes():
        pos_chatgpt_x = respawnar()[0]
        pos_chatgpt_y = respawnar()[1]

    # criando as fontes de pontuação
    fonte = pygame.font.Font("fonte/ARCADECLASSIC.TTF", 30)
    placar = fonte.render(f"Score {int(pontos)}", False, (0, 0, 0))
    screen.blit(placar, (50,50))

    tempo_restante = 40 - int(time.time() - start_time)
    fonte_tempo = pygame.font.Font("fonte/ARCADECLASSIC.TTF", 30)
    texto_tempo = fonte_tempo.render(f"Tempo restante {tempo_restante}", False, (255, 255, 255))
    screen.blit(texto_tempo, (50, 100))





    #criar as imagens do jogo
    screen.blit(erro, (pos_erro_x, pos_erro_y))
    screen.blit(municao, (pos_x_municao, pos_y_municao))
    screen.blit(chatgpt, (pos_chatgpt_x, pos_chatgpt_y))
    screen.blit(monitor, (pos_monitor_x, pos_monitor_y))

    # criar o desenho
    pygame.draw.rect(screen, (255, 0, 0), erro_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), municao_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), chatgpt_rect, 4)
    pygame.draw.rect(screen, (255, 0, 0), monitor_rect, 4)

    monitor_rect.y = pos_monitor_y
    monitor_rect.x = pos_monitor_x

    chatgpt_rect.y = pos_chatgpt_y
    chatgpt_rect.x = pos_chatgpt_x

    erro_rect.y = pos_erro_y
    erro_rect.x = pos_erro_x

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

if game_over == True:
    print("Game Over")