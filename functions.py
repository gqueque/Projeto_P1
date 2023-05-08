import random

# definindo as colisoes


def colisoes_erro(monitor_rect, erro_rect, municao_rect):
    if monitor_rect.colliderect(erro_rect) or erro_rect.x == 60:
        return 1
    elif municao_rect.colliderect(erro_rect):
        return 2


def colisoes_gpt(monitor_rect, chatgpt_rect, municao_rect):
    if monitor_rect.colliderect(chatgpt_rect) or chatgpt_rect.x == 60:
        return 1
    elif municao_rect.colliderect(chatgpt_rect):
        return 2


def colisoes_runtimeerror(monitor_rect, runtimeerror_rect, municao_rect):
    if monitor_rect.colliderect(runtimeerror_rect) or runtimeerror_rect.x == 60:
        return 1
    elif municao_rect.colliderect(runtimeerror_rect):
        return 2


# respawnar
def respawnar():
    x = 1350
    y = random.randint(80, 560)
    return [x, y]


def respawnar_municao(x, y):
    triggered = False
    respawnar_municao_x = x
    respawnar_municao_y = y
    vel_x_municao = 0
    return [respawnar_municao_x, respawnar_municao_y, triggered, vel_x_municao]
