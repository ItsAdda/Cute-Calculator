import os

import pygame
import sys

pygame.init()
pygame.mixer.init()
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

sound_path = os.path.join(base_path, "calculator-button-click-sound-[AudioTrimmer.com].mp3")
buttonClick = pygame.mixer.Sound(sound_path)


WIDTH, HEIGHT = 800, 600
black = (0, 0, 0)
white = (255, 255, 255)
dark_red = (255, 0, 0)
gray = (128, 128, 128)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Cute lil Calculator for my AMAZING GIRLFRIEND")
clock = pygame.time.Clock()
font = pygame.font.SysFont("comicsans", 30)
current_input = ""

def draw_button(screen, w, h, x, y, text, text_color, color, hover_color, mouse_pos):
    is_hovered = x <= mouse_pos[0] <= x + w and y <= mouse_pos[1] <= y + h
    pygame.draw.rect(screen, hover_color if is_hovered else color, (x, y, w, h), border_radius=8)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + w / 2, y + h / 2))
    screen.blit(text_surface, text_rect)
    return is_hovered

def draw_text(text, text_color, x, y):
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)

heart_base_size = 300
heart_font_name = "segoeuiemoji"
heart_font = pygame.font.SysFont(heart_font_name, heart_base_size)

btn_w, btn_h = 60, 40
counter = 0
while True:
    mouse_pos = pygame.mouse.get_pos()
    if counter < 0:
        counter = 0
    screen.fill(black)
    text_surface = font.render(current_input, True, white)
    screen.blit(text_surface, (30, 100))
    draw_text("CALCULATOR", dark_red, 380, 30)
    hovered = draw_button(screen, btn_w, btn_h, 40, 300, "+", white, dark_red, gray, mouse_pos)
    hovered2 = draw_button(screen, btn_w, btn_h, 40, 350, "x", white, dark_red, gray, mouse_pos )
    hovered3 = draw_button(screen, btn_w, btn_h, 110, 300, "-", white, dark_red, gray, mouse_pos )
    hovered4 = draw_button(screen, btn_w, btn_h, 110, 350, "÷", white, dark_red, gray, mouse_pos )
    num1 = draw_button(screen, btn_w, btn_h, 200, 300, "1", white, dark_red, gray, mouse_pos)
    num2 = draw_button(screen, btn_w, btn_h, 270, 300, "2", white, dark_red, gray, mouse_pos)
    num3 = draw_button(screen, btn_w, btn_h, 200, 350, "3", white, dark_red, gray, mouse_pos)
    num4 = draw_button(screen, btn_w, btn_h, 270, 350, "4", white, dark_red, gray, mouse_pos)
    num5 = draw_button(screen, btn_w, btn_h, 200, 400, "5", white, dark_red, gray, mouse_pos)
    num6 = draw_button(screen, btn_w, btn_h, 270, 400, "6", white, dark_red, gray, mouse_pos)
    num7 = draw_button(screen, btn_w, btn_h, 200, 450, "7", white, dark_red, gray, mouse_pos)
    num8 = draw_button(screen, btn_w, btn_h, 270, 450, "8", white, dark_red, gray, mouse_pos)
    num9 = draw_button(screen, btn_w, btn_h, 200, 500, "9", white, dark_red, gray, mouse_pos)
    num0 = draw_button(screen, btn_w, btn_h, 270, 500, "0", white, dark_red, gray, mouse_pos)
    equal = draw_button(screen, btn_w, btn_h, 40, 500, "=", white, dark_red, gray, mouse_pos)
    clear = draw_button(screen, 70, btn_h, 350, 500, "Clear", white, dark_red, gray, mouse_pos)

    import pygame.transform
    import math

    time = pygame.time.get_ticks() / 1000
    scale = 1 + 0.05 * math.sin(time * 4)


    heart_surface = heart_font.render("❤️", True, (255, 0, 0))


    scaled_width = int(heart_surface.get_width() * scale)
    scaled_height = int(heart_surface.get_height() * scale)
    heart_surface_scaled = pygame.transform.smoothscale(heart_surface, (scaled_width, scaled_height))


    heart_rect = heart_surface_scaled.get_rect(center=(600, 420))
    screen.blit(heart_surface_scaled, heart_rect)



    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if current_input == "Error":
                current_input = ""
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and hovered:
            if counter % 2 == 0 and current_input != "":
                if len(current_input) < 30:
                    buttonClick.play()
                    current_input += "+"
                    counter += 1
        if event.type == pygame.MOUSEBUTTONDOWN and hovered2:
            if counter % 2 == 0 and current_input != "":
                if len(current_input) < 30:
                    buttonClick.play()
                    current_input += "x"
                    counter += 1
        if event.type == pygame.MOUSEBUTTONDOWN and hovered3:
            if counter % 2 == 0 and current_input != "":
                if len(current_input) < 30:
                    buttonClick.play()
                    current_input += "-"
                    counter += 1
        if event.type == pygame.MOUSEBUTTONDOWN and hovered4:
            if counter % 2 == 0 and current_input != "":
                if len(current_input) < 30:
                    buttonClick.play()
                    current_input += "÷"
                    counter += 1
        if event.type == pygame.MOUSEBUTTONDOWN and num1:
            if len(current_input) < 30:
                buttonClick.play()
                current_input += str(1)
                counter -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and num2:
            if len(current_input) < 30:
                buttonClick.play()
                current_input += str(2)
                counter -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and num3:
            if len(current_input) < 30:
                buttonClick.play()
                current_input += str(3)
                counter -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and num4:
            if len(current_input) < 30:
                buttonClick.play()
                current_input += str(4)
                counter -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and num5:
            if len(current_input) < 30:
                buttonClick.play()
                current_input += str(5)
                counter -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and num6:
            if len(current_input) < 30:
                buttonClick.play()
                current_input += str(6)
                counter -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and num7:
            if len(current_input) < 30:
                buttonClick.play()
                current_input += str(7)
                counter -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and num8:
            if len(current_input) < 30:
                buttonClick.play()
                current_input += str(8)
                counter -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and num9:
            if len(current_input) < 30:
                buttonClick.play()
                current_input += str(9)
                counter -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and num0 and current_input != "":
            if len(current_input) < 30:
                buttonClick.play()
                current_input += str(0)
                counter -= 1
        if event.type == pygame.MOUSEBUTTONDOWN and clear:
            buttonClick.play()
            current_input = ""
        if event.type == pygame.MOUSEBUTTONDOWN and equal:
            try:
                buttonClick.play()
                expression = current_input.replace("x", "*").replace("÷", "/")
                result = eval(expression)


                if isinstance(result, float) and result.is_integer():
                    result = int(result)

                current_input = str(result)
                counter = 0
            except Exception:
                if current_input == "":
                    current_input = ""
                else:
                    current_input = "Error"






    pygame.display.update()





