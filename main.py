import pygame
pygame.init()
x = 1280
y = 720
screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Monitores vs Gepeto")
#background
bg = pygame.image.load("C:\\Users\\gusrq\\PycharmProjects\\Monitores_vs_Gepeto\\imagens\\bg.jpg").convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

#monitor
monitor = pygame.image.load("C:\\Users\\gusrq\\PycharmProjects\\Monitores_vs_Gepeto\\imagens\\Monitor_Cin.png").convert_alpha()
monitor = pygame.transform.scale(monitor, (80, 80))
pos_monitor_x = 200
pos_monitor_y = 300

#inimigos ( erro, chatgpt, cola, aluno chato com duvida com duvida no discord)
erro = pygame.image.load("C:\\Users\\gusrq\\PycharmProjects\\Monitores_vs_Gepeto\\imagens\\erro.png").convert_alpha()
erro = pygame.transform.scale(erro, (70, 70))
pos_erro_x = 500
pos_erro_y = 360

chatgpt = pygame.image.load("C:\\Users\\gusrq\\PycharmProjects\\Monitores_vs_Gepeto\\imagens\\gpt.png").convert_alpha()
chatgpt = pygame.transform.scale(chatgpt, (70, 70))
pos_chatpgt_x = 500
pos_chatpgt_y = 300

#teste


rodando = True

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
    if tecla[pygame.K_UP] and pos_monitor_y >1:
        pos_monitor_y -= 1
    if tecla[pygame.K_DOWN] and pos_monitor_y < 665:
        pos_monitor_y += 1

    #movimento
    x -= 0.4
    pos_erro_x -= 1
    screen.blit(monitor,(pos_monitor_x, pos_monitor_y))
    screen.blit(erro, (pos_erro_x, pos_erro_y))
    screen.blit(chatgpt, (pos_chatpgt_y, pos_chatpgt_y))


    pygame.display.update()