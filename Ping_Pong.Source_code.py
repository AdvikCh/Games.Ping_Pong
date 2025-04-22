import pygame
import pygame.freetype
import random
import os

pygame.init()
pygame.freetype.init()

window_info = pygame.display.Info()
window_width = window_info.current_w
window_height = window_info.current_h
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN)
pygame.display.set_caption("Ping Pong", "Ping Pong")
Ping_Pong_Logo = pygame.image.load("Ping_Pong.Image.png")
pygame.display.set_icon(Ping_Pong_Logo)

screen_ratio = window_width / window_height
margin = window_width / 100

white = (255, 255, 255)
gray = (178, 178, 178)
dark = (31, 31, 31)
black = (0, 0, 0)

font_size_1 = window_width / 8
font_ping_pong_1 = pygame.freetype.Font("Ping_Pong.Font.otf", font_size_1)
font_size_2 = window_width / 5
font_ping_pong_2 = pygame.freetype.Font("Ping_Pong.Font.otf", font_size_2)
font_size_3 = window_width / 3
font_ping_pong_3 = pygame.freetype.Font("Ping_Pong.Font.otf", font_size_3)

text_cont_width = window_width / 4
text_cont_height = window_height / 4
text_cont_x = (window_width - text_cont_width) / 2
text_cont_y = (window_height - text_cont_height) / 2

close_width = window_width / 20
close_height = close_width
close_x = (window_width - margin) - close_width
close_y = margin

dark_width = window_width / 20
dark_height = dark_width
dark_x = margin
dark_y = margin

help_width = dark_width
help_height = dark_height
help_x = dark_x
help_y = (dark_y + dark_height) + (margin * 2)

play_width = (window_width / 3) + (margin * 3)
play_height = (window_height / 3)
play_x = (window_width / 2) - (play_width / 2)
play_y = (window_height / 2) - (play_height / 2)

player_width = window_width / 30
player_height = window_height / 4
player_1_x = margin
player_1_y = window_height / 2 - player_height / 2
player_2_x = window_width - player_width - margin
player_2_y = window_height / 2 - player_height / 2
player_3_x = window_width / 2 - (player_height * screen_ratio) / 2
player_3_y = margin
player_4_x = window_width / 2 - (player_height * screen_ratio) / 2
player_4_y = window_height - player_width - margin

ball_width = player_width / 2
ball_height = ball_width
ball_x = window_width / 2
ball_y = window_height / 2

settings_width = window_width / 1.25
settings_height = window_height - (margin * 4)
settings_x = window_width / 2 - settings_width / 2
settings_y = margin * 2

continue_width = (settings_height / 3) / 2
continue_height = continue_width * (screen_ratio / 1.5)
continue_x = settings_x + settings_width + margin
continue_y = (settings_y + (settings_height / 2)) - (continue_height / 2)
continue_button = [(continue_x, continue_y), (continue_x, continue_y + continue_height), (continue_x + continue_width, continue_y + continue_height / 2)]

vertical_width = (settings_height / 3) / 2
vertical_height = vertical_width
vertical_x = settings_x + settings_width - vertical_width - margin
vertical_y = (settings_y + settings_height - vertical_height - margin) - (vertical_height * 3) - ((vertical_height / 15) * 6)

player_speed = 2
ball_speed = 3
directions = ["NE", "SE", "SW", "NW"]
direction = random.choice(directions)
solo_score = 0
local_score_1 = 0
local_score_2 = 0

def settings():
    if dark_mode:
        dark_button = pygame.image.load("Dark_mode.On.png")
        help_button = pygame.image.load("Help.Dark_mode.png")
    else:
        dark_button = pygame.image.load("Dark_mode.Off.png")
        help_button = pygame.image.load("Help.png")
    dark_button = pygame.transform.scale(dark_button, (dark_width, dark_height))
    window.blit(dark_button, (dark_x, dark_y))
    help_button = pygame.transform.scale(help_button, (help_width, help_height))
    window.blit(help_button, (help_x, help_y))
        
def close_button():
    if dark_mode:
        pygame.draw.rect(window, white, (close_x - (close_width / 10), close_y - (close_height / 10), close_width + (close_width / 5), close_height + (close_height / 5)))
        pygame.draw.rect(window, dark, (close_x, close_y, close_width, close_height))
        pygame.draw.line(window, white, (close_x + (close_width / 10), close_y + (close_width / 10)), (close_x + close_width - ((close_width / 10) * 1.5), close_y + close_height - (close_width / 10)), int(close_width / 10))
        pygame.draw.line(window, white, (close_x + (close_width / 10), close_y + close_height - (close_width / 10)), (close_x + close_width - ((close_width / 10) * 1.5), close_y + (close_width / 10)), int(close_width / 10))
    else:
        pygame.draw.rect(window, black, (close_x - (close_width / 10), close_y - (close_height / 10), close_width + (close_width / 5), close_height + (close_height / 5)))
        pygame.draw.rect(window, white, (close_x, close_y, close_width, close_height))
        pygame.draw.line(window, black, (close_x + (close_width / 10), close_y + (close_width / 10)), (close_x + close_width - ((close_width / 10) * 1.5), close_y + close_height - (close_width / 10)), int(close_width / 10))
        pygame.draw.line(window, black, (close_x + (close_width / 10), close_y + close_height - (close_width / 10)), (close_x + close_width - ((close_width / 10) * 1.5), close_y + (close_width / 10)), int(close_width / 10))

def main_menu():
    if dark_mode:
        window.fill(dark)
        play_button = pygame.image.load("Play.Dark_mode.png")
    else:
        window.fill(white)
        play_button = pygame.image.load("Play.png")
    play_button = pygame.transform.scale(play_button, (play_width, play_height))
    window.blit(play_button, (play_x, play_y))
    close_button()
    settings()
    pygame.display.update()
        
def draw_court():
    if dark_mode:
        window.fill(dark)
        if players == 1:
            if vertical: pygame.draw.rect(window, white, (player_4_x, player_4_y, player_height * screen_ratio, player_width))
            else: pygame.draw.rect(window, white, (player_2_x, player_2_y, player_width, player_height))
            text_width, text_height = font_ping_pong_3.get_rect(f"{solo_score}")[2:]
            text_x = text_cont_x + (text_cont_width - text_width) / 2
            text_y = text_cont_y + (text_cont_height - text_height) / 2
            text_surface, _ = font_ping_pong_3.render(f"{solo_score}", white) 
            window.blit(text_surface, (text_x, text_y))
        elif players == 2:
            if vertical:
                pygame.draw.rect(window, white, (player_3_x, player_3_y, player_height * screen_ratio, player_width))
                pygame.draw.rect(window, white, (player_4_x, player_4_y, player_height * screen_ratio, player_width))
            else:
                pygame.draw.rect(window, white, (player_1_x, player_1_y, player_width, player_height))
                pygame.draw.rect(window, white, (player_2_x, player_2_y, player_width, player_height))
            text_width, text_height = font_ping_pong_3.get_rect(f"{local_score_1}-{local_score_2}")[2:]
            text_y = text_cont_y + (text_cont_height - text_height) / 2
            text_surface, _ = font_ping_pong_3.render(f"{local_score_1}-{local_score_2}", white)
            text_x = (window_width / 2) - (text_surface.get_width() / 2)
            window.blit(text_surface, (text_x, text_y))
        elif players == 3:
            if vertical:
                pygame.draw.rect(window, white, (player_1_x, player_1_y, player_width, player_height))
                pygame.draw.rect(window, white, (player_2_x, player_2_y, player_width, player_height))
                pygame.draw.rect(window, white, (player_3_x, player_3_y, player_height * screen_ratio, player_width))
            else:
                pygame.draw.rect(window, white, (player_1_x, player_1_y, player_width, player_height))
                pygame.draw.rect(window, white, (player_2_x, player_2_y, player_width, player_height))
                pygame.draw.rect(window, white, (player_4_x, player_4_y, player_height * screen_ratio, player_width))
        elif players == 4:
            pygame.draw.rect(window, white, (player_1_x, player_1_y, player_width, player_height))
            pygame.draw.rect(window, white, (player_2_x, player_2_y, player_width, player_height))
            pygame.draw.rect(window, white, (player_3_x, player_3_y, player_height * screen_ratio, player_width))
            pygame.draw.rect(window, white, (player_4_x, player_4_y, player_height * screen_ratio, player_width))
        pygame.draw.ellipse(window, white, (ball_x, ball_y, ball_width, ball_height))
    else:
        window.fill(white)
        if players == 1:
            if vertical: pygame.draw.rect(window, black, (player_4_x, player_4_y, player_height * screen_ratio, player_width))
            else: pygame.draw.rect(window, black, (player_2_x, player_2_y, player_width, player_height))
            text_width, text_height = font_ping_pong_3.get_rect(f"{solo_score}")[2:]
            text_x = text_cont_x + (text_cont_width - text_width) / 2
            text_y = text_cont_y + (text_cont_height - text_height) / 2
            text_surface, _ = font_ping_pong_3.render(f"{solo_score}", black) 
            window.blit(text_surface, (text_x, text_y))
        elif players == 2:
            if vertical:
                pygame.draw.rect(window, black, (player_3_x, player_3_y, player_height * screen_ratio, player_width))
                pygame.draw.rect(window, black, (player_4_x, player_4_y, player_height * screen_ratio, player_width))
            else:
                pygame.draw.rect(window, black, (player_1_x, player_1_y, player_width, player_height))
                pygame.draw.rect(window, black, (player_2_x, player_2_y, player_width, player_height))
            text_width, text_height = font_ping_pong_3.get_rect(f"{local_score_1}-{local_score_2}")[2:]
            text_y = text_cont_y + (text_cont_height - text_height) / 2
            text_surface, _ = font_ping_pong_3.render(f"{local_score_1}-{local_score_2}", black)
            text_x = (window_width / 2) - (text_surface.get_width() / 2)
            window.blit(text_surface, (text_x, text_y))
        if players == 3:
            if vertical:
                pygame.draw.rect(window, black, (player_1_x, player_1_y, player_width, player_height))
                pygame.draw.rect(window, black, (player_2_x, player_2_y, player_width, player_height))
                pygame.draw.rect(window, black, (player_3_x, player_3_y, player_height * screen_ratio, player_width))
            else:
                pygame.draw.rect(window, black, (player_1_x, player_1_y, player_width, player_height))
                pygame.draw.rect(window, black, (player_2_x, player_2_y, player_width, player_height))
                pygame.draw.rect(window, black, (player_4_x, player_4_y, player_height * screen_ratio, player_width))
        if players == 4:
            pygame.draw.rect(window, black, (player_1_x, player_1_y, player_width, player_height))
            pygame.draw.rect(window, black, (player_2_x, player_2_y, player_width, player_height))
            pygame.draw.rect(window, black, (player_3_x, player_3_y, player_height * screen_ratio, player_width))
            pygame.draw.rect(window, black, (player_4_x, player_4_y, player_height * screen_ratio, player_width))
        pygame.draw.ellipse(window, black, (ball_x, ball_y, ball_width, ball_height))
    pygame.display.update()
    
def game_settings():
    global ball_speed_plus_x, ball_speed_plus_y, ball_speed_plus_width, ball_speed_plus_height, ball_speed_minus_x, ball_speed_minus_y, ball_speed_minus_width, ball_speed_minus_height, move_speed_plus_x, move_speed_plus_y, move_speed_plus_width, move_speed_plus_height, move_speed_minus_x, move_speed_minus_y, move_speed_minus_width, move_speed_minus_height, players_plus_x, players_plus_y, players_plus_width, players_plus_height, players_minus_x, players_minus_y, players_minus_width, players_minus_height
    if dark_mode: game_settings_background = pygame.image.load("Game_settings.Background.Dark_mode.png")
    else: game_settings_background = pygame.image.load("Game_settings.Background.png")
    game_settings_background = pygame.transform.scale(game_settings_background, (window_width, window_height))
    window.blit(game_settings_background, (0, 0))
    if dark_mode:
        pygame.draw.rect(window, white, (settings_x - (margin / 2), settings_y - (margin / 2), settings_width + margin, settings_height + margin))
        pygame.draw.rect(window, dark, (settings_x, settings_y, settings_width, settings_height))
        text_surface, _ = font_ping_pong_2.render("settings", white)
    else:
        pygame.draw.rect(window, black, (settings_x - (margin / 2), settings_y - (margin / 2), settings_width + margin, settings_height + margin))
        pygame.draw.rect(window, white, (settings_x, settings_y, settings_width, settings_height))
        text_surface, _ = font_ping_pong_2.render("settings", black)
    text_x = settings_x + margin
    text_y = settings_y + margin
    window.blit(text_surface, (text_x, text_y))
    if players == 4: 
        pygame.draw.rect(window, gray, (vertical_x - (margin / 2), vertical_y - (margin / 2), vertical_width + margin, vertical_height + margin))
        text_surface, _ = font_ping_pong_1.render("vertical", gray)
        if dark_mode: pygame.draw.rect(window, dark, (vertical_x, vertical_y, vertical_width, vertical_height))
        else: pygame.draw.rect(window, white, (vertical_x, vertical_y, vertical_width, vertical_height))
    else:
        if dark_mode:
            pygame.draw.rect(window, white, (vertical_x - (margin / 2), vertical_y - (margin / 2), vertical_width + margin, vertical_height + margin))
            pygame.draw.rect(window, dark, (vertical_x, vertical_y, vertical_width, vertical_height))
            text_surface, _ = font_ping_pong_1.render("vertical", white)
        else:
            pygame.draw.rect(window, black, (vertical_x - (margin / 2), vertical_y - (margin / 2), vertical_width + margin, vertical_height + margin))
            pygame.draw.rect(window, white, (vertical_x, vertical_y, vertical_width, vertical_height))
            text_surface, _ = font_ping_pong_1.render("vertical", black)
    text_x = settings_x + margin
    text_y = vertical_y + (vertical_height / 5)
    window.blit(text_surface, (text_x, text_y))
    if vertical:
        if players < 4:
            if dark_mode: 
                pygame.draw.line(window, white, (vertical_x + margin, vertical_y + (vertical_height / 2)), (vertical_x + (vertical_width / 3), (vertical_y + vertical_height) - margin), int(margin))
                pygame.draw.line(window, white, (vertical_x + (vertical_width / 3), (vertical_y + vertical_height) - margin), ((vertical_x + vertical_width) - margin, vertical_y + margin), int(margin))
            else:
                pygame.draw.line(window, black, (vertical_x + margin, vertical_y + (vertical_height / 2)), (vertical_x + (vertical_width / 3), (vertical_y + vertical_height) - margin), int(margin))
                pygame.draw.line(window, black, (vertical_x + (vertical_width / 3), (vertical_y + vertical_height) - margin), ((vertical_x + vertical_width) - margin, vertical_y + margin), int(margin))
        else:
            pygame.draw.line(window, gray, (vertical_x + margin, vertical_y + (vertical_height / 2)), (vertical_x + (vertical_width / 3), (vertical_y + vertical_height) - margin), int(margin))
            pygame.draw.line(window, gray, (vertical_x + (vertical_width / 3), (vertical_y + vertical_height) - margin), ((vertical_x + vertical_width) - margin, vertical_y + margin), int(margin))
    ball_speed_plus_width = vertical_width / 2
    ball_speed_plus_height = ball_speed_plus_width
    ball_speed_plus_x = (vertical_x + vertical_width) - ball_speed_plus_width
    ball_speed_plus_y = (vertical_y + vertical_height) + ball_speed_plus_height
    if dark_mode: text_surface, _ = font_ping_pong_2.render(f"{ball_speed}", white)
    else: text_surface, _ = font_ping_pong_2.render(f"{ball_speed}", black)
    text_x = ball_speed_plus_x - text_surface.get_width() - margin
    text_y = vertical_y + vertical_height + margin
    window.blit(text_surface, (text_x, text_y))
    ball_speed_minus_width = ball_speed_plus_width
    ball_speed_minus_height = ball_speed_plus_height
    ball_speed_minus_x = text_x - ball_speed_minus_width - margin
    ball_speed_minus_y = ball_speed_plus_y
    if dark_mode: text_surface, _ = font_ping_pong_1.render("ball speed", white)
    else: text_surface, _ = font_ping_pong_1.render("ball speed",black)
    text_x = settings_x + margin
    text_y = (vertical_y + vertical_height) + margin + (vertical_height / 5)
    window.blit(text_surface, (text_x, text_y))
    if ball_speed > 98: 
        pygame.draw.line(window, gray, (ball_speed_plus_x, ball_speed_plus_y + (ball_speed_plus_height / 2)), (ball_speed_plus_x + ball_speed_plus_width, ball_speed_plus_y + (ball_speed_plus_width / 2)), 10)
        pygame.draw.line(window, gray, (ball_speed_plus_x + (ball_speed_plus_width / 2), ball_speed_plus_y), (ball_speed_plus_x + (ball_speed_plus_width / 2), ball_speed_plus_y + ball_speed_plus_height), 10)
    else:
        if dark_mode:
            pygame.draw.line(window, white, (ball_speed_plus_x, ball_speed_plus_y + (ball_speed_plus_height / 2)), (ball_speed_plus_x + ball_speed_plus_width, ball_speed_plus_y + (ball_speed_plus_width / 2)), 10)
            pygame.draw.line(window, white, (ball_speed_plus_x + (ball_speed_plus_width / 2), ball_speed_plus_y), (ball_speed_plus_x + (ball_speed_plus_width / 2), ball_speed_plus_y + ball_speed_plus_height), 10)
        else:
            pygame.draw.line(window, black, (ball_speed_plus_x, ball_speed_plus_y + (ball_speed_plus_height / 2)), (ball_speed_plus_x + ball_speed_plus_width, ball_speed_plus_y + (ball_speed_plus_width / 2)), 10)
            pygame.draw.line(window, black, (ball_speed_plus_x + (ball_speed_plus_width / 2), ball_speed_plus_y), (ball_speed_plus_x + (ball_speed_plus_width / 2), ball_speed_plus_y + ball_speed_plus_height), 10)
    if ball_speed < 1: pygame.draw.line(window, gray, (ball_speed_minus_x, ball_speed_minus_y + (ball_speed_minus_height / 2)), (ball_speed_minus_x + ball_speed_minus_width, ball_speed_minus_y + (ball_speed_minus_height / 2)), 10)
    else:
        if dark_mode: pygame.draw.line(window, white, (ball_speed_minus_x, ball_speed_minus_y + (ball_speed_minus_height / 2)), (ball_speed_minus_x + ball_speed_minus_width, ball_speed_minus_y + (ball_speed_minus_height / 2)), 10)
        else: pygame.draw.line(window, black, (ball_speed_minus_x, ball_speed_minus_y + (ball_speed_minus_height / 2)), (ball_speed_minus_x + ball_speed_minus_width, ball_speed_minus_y + (ball_speed_minus_height / 2)), 10)
    if dark_mode: text_surface, _ = font_ping_pong_1.render("move speed", white)
    else: text_surface, _ = font_ping_pong_1.render("move speed", black)
    text_x = settings_x + margin
    text_y = (vertical_y + (vertical_height * 2)) + (margin * 2) + (vertical_height / 5)
    window.blit(text_surface, (text_x, text_y))
    move_speed_plus_width = vertical_width / 2
    move_speed_plus_height = move_speed_plus_width
    move_speed_plus_x = (vertical_x + vertical_width) - move_speed_plus_width
    move_speed_plus_y = (ball_speed_plus_y + ball_speed_plus_height) + move_speed_plus_height
    if dark_mode: text_surface, _ = font_ping_pong_2.render(f"{player_speed}", white)
    else: text_surface, _ = font_ping_pong_2.render(f"{player_speed}", black)
    text_x = move_speed_plus_x - text_surface.get_width() - margin
    text_y = vertical_y + (vertical_height * 2) + (margin * 2)
    window.blit(text_surface, (text_x, text_y))
    move_speed_minus_width = move_speed_plus_width
    move_speed_minus_height = move_speed_plus_height
    move_speed_minus_x = text_x - move_speed_minus_width - margin
    move_speed_minus_y = move_speed_plus_y
    if player_speed > 98: 
        pygame.draw.line(window, gray, (move_speed_plus_x, move_speed_plus_y + (move_speed_plus_height / 2)), (move_speed_plus_x + move_speed_plus_width, move_speed_plus_y + (move_speed_plus_width / 2)), 10)
        pygame.draw.line(window, gray, (move_speed_plus_x + (move_speed_plus_width / 2), move_speed_plus_y), (move_speed_plus_x + (move_speed_plus_width / 2), move_speed_plus_y + move_speed_plus_height), 10)
    else:
        if dark_mode:
            pygame.draw.line(window, white, (move_speed_plus_x, move_speed_plus_y + (move_speed_plus_height / 2)), (move_speed_plus_x + move_speed_plus_width, move_speed_plus_y + (move_speed_plus_width / 2)), 10)
            pygame.draw.line(window, white, (move_speed_plus_x + (move_speed_plus_width / 2), move_speed_plus_y), (move_speed_plus_x + (move_speed_plus_width / 2), move_speed_plus_y + move_speed_plus_height), 10)
        else:
            pygame.draw.line(window, black, (move_speed_plus_x, move_speed_plus_y + (move_speed_plus_height / 2)), (move_speed_plus_x + move_speed_plus_width, move_speed_plus_y + (move_speed_plus_width / 2)), 10)
            pygame.draw.line(window, black, (move_speed_plus_x + (move_speed_plus_width / 2), move_speed_plus_y), (move_speed_plus_x + (move_speed_plus_width / 2), move_speed_plus_y + move_speed_plus_height), 10)
    if player_speed < 1: pygame.draw.line(window, gray, (move_speed_minus_x, move_speed_minus_y + (move_speed_minus_height / 2)), (move_speed_minus_x + move_speed_minus_width, move_speed_minus_y + (move_speed_minus_height / 2)), 10)
    else:
        if dark_mode: pygame.draw.line(window, white, (move_speed_minus_x, move_speed_minus_y + (move_speed_minus_height / 2)), (move_speed_minus_x + move_speed_minus_width, move_speed_minus_y + (move_speed_minus_height / 2)), 10)
        else: pygame.draw.line(window, black, (move_speed_minus_x, move_speed_minus_y + (move_speed_minus_height / 2)), (move_speed_minus_x + move_speed_minus_width, move_speed_minus_y + (move_speed_minus_height / 2)), 10)
    if dark_mode: text_surface, _ = font_ping_pong_1.render("players", white)
    else: text_surface, _ = font_ping_pong_1.render("players", black)
    text_x = settings_x + margin
    text_y = text_y + vertical_height + (margin * 2)
    window.blit(text_surface, (text_x, text_y))
    players_plus_width = vertical_width / 2
    players_plus_height = players_plus_width
    players_plus_x = (vertical_x + vertical_width) - players_plus_width
    players_plus_y = (move_speed_plus_y + move_speed_plus_height) + players_plus_height
    if dark_mode: text_surface, _ = font_ping_pong_2.render(f"{players}", white)
    else: text_surface, _ = font_ping_pong_2.render(f"{players}", black)
    text_x = players_plus_x - text_surface.get_width() - margin
    text_y = vertical_y + (vertical_height * 3) + (margin * 3)
    window.blit(text_surface, (text_x, text_y))
    players_minus_width = players_plus_width
    players_minus_height = players_plus_height
    players_minus_x = text_x - players_minus_width - margin
    players_minus_y = players_plus_y
    if players > 3: 
        pygame.draw.line(window, gray, (players_plus_x, players_plus_y + (players_plus_height / 2)), (players_plus_x + players_plus_width, players_plus_y + (players_plus_width / 2)), 10)
        pygame.draw.line(window, gray, (players_plus_x + (players_plus_width / 2), players_plus_y), (players_plus_x + (players_plus_width / 2), players_plus_y + players_plus_height), 10)
    else:
        if dark_mode:
            pygame.draw.line(window, white, (players_plus_x, players_plus_y + (players_plus_height / 2)), (players_plus_x + players_plus_width, players_plus_y + (players_plus_width / 2)), 10)
            pygame.draw.line(window, white, (players_plus_x + (players_plus_width / 2), players_plus_y), (players_plus_x + (players_plus_width / 2), players_plus_y + players_plus_height), 10)
        else: 
            pygame.draw.line(window, black, (players_plus_x, players_plus_y + (players_plus_height / 2)), (players_plus_x + players_plus_width, players_plus_y + (players_plus_width / 2)), 10)
            pygame.draw.line(window, black, (players_plus_x + (players_plus_width / 2), players_plus_y), (players_plus_x + (players_plus_width / 2), players_plus_y + players_plus_height), 10)
    if players < 2: pygame.draw.line(window, gray, (players_minus_x, players_minus_y + (players_minus_height / 2)), (players_minus_x + players_minus_width, players_minus_y + (players_minus_height / 2)), 10)
    else: 
        if dark_mode: pygame.draw.line(window, white, (players_minus_x, players_minus_y + (players_minus_height / 2)), (players_minus_x + players_minus_width, players_minus_y + (players_minus_height / 2)), 10)
        else: pygame.draw.line(window, black, (players_minus_x, players_minus_y + (players_minus_height / 2)), (players_minus_x + players_minus_width, players_minus_y + (players_minus_height / 2)), 10)
    if players == 0: pygame.draw.polygon(window, gray, continue_button)
    else: 
        if dark_mode: pygame.draw.polygon(window, white, continue_button)
        else: pygame.draw.polygon(window, black, continue_button)
    close_button()
    pygame.display.update()
    
def reset_game():
    global solo_score, local_score_1, local_score_2, player_1_x, player_1_y, player_2_x, player_2_y, player_3_x, player_3_y, player_4_x, player_4_y, ball_x, ball_y, direction
    solo_score = 0
    local_score_1 = 0
    local_score_2 = 0
    player_1_x = 10
    player_1_y = window_height / 2 - player_height / 2
    player_2_x = window_width - player_width - 10
    player_2_y = window_height / 2 - player_height / 2
    player_3_x = window_width / 2 - (player_height * screen_ratio) / 2
    player_3_y = 10
    player_4_x = window_width / 2 - (player_height * screen_ratio) / 2
    player_4_y = window_height - player_width - 10
    ball_x = window_width / 2
    ball_y = window_height / 2
    direction = random.choice(directions)

players = 0
game_running = True
dark_mode = True
in_settings = False
vertical = False
pressed = False
main_menu()
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: game_running = False
        elif event.type == pygame.KEYUP: 
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN or event.key == pygame.K_v: pressed = False
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if close_x <= mouse_x <= close_x + close_width and close_y <= mouse_y <= close_y + close_height:
                if players == 0:
                    if in_settings:
                        vertical = False
                        in_settings = False
                        main_menu()
                    else: game_running = False
                elif players == 1 or players == 2 or players == 3 or players == 4:
                    reset_game()
                    players = 0
                    vertical = False
                    if in_settings: in_settings = False
                    main_menu()
            if players == 0 or in_settings:
                if not in_settings:
                    if dark_x <= mouse_x <= dark_x + dark_width and dark_y <= mouse_y <= dark_y + dark_height:
                        if dark_mode: dark_mode = False
                        else: dark_mode = True
                        main_menu()
                    if help_x <= mouse_x <= help_x + help_width and help_y <= mouse_y <= help_y + help_height:
                        if hasattr(os, "startfile"): os.startfile("Help.txt")  
                        else: os.system("open Help.txt 2>/dev/null || xdg-open Help.txt 2>/dev/null")
                    if play_x <= mouse_x <= play_x + play_width and play_y <= mouse_y <= play_y + play_height:
                        if dark_mode: window.fill(dark)
                        else: window.fill(white)
                        in_settings = True
                        game_settings()
                else:
                    if vertical_x <= mouse_x <= vertical_x + vertical_width and vertical_y <= mouse_y <= vertical_y + vertical_height and players < 4:
                        if not vertical: vertical = True
                        else:
                            vertical = False
                            if dark_mode: window.fill(dark)
                            else: window.fill(white)
                        game_settings()
                    if ball_speed_plus_x <= mouse_x <= ball_speed_plus_x + ball_speed_plus_width and ball_speed_plus_y <= mouse_y <= ball_speed_plus_y + ball_speed_plus_height and ball_speed < 99:
                        ball_speed += 1
                        game_settings()
                    if ball_speed_minus_x <= mouse_x <= ball_speed_minus_x + ball_speed_minus_width and ball_speed_minus_y <= mouse_y <= ball_speed_minus_y + ball_speed_minus_height and ball_speed > 0:
                        ball_speed -= 1
                        game_settings()
                    if move_speed_plus_x <= mouse_x <= move_speed_plus_x + move_speed_plus_width and move_speed_plus_y <= mouse_y <= move_speed_plus_y + move_speed_plus_height and player_speed < 99:
                        player_speed += 1
                        game_settings()
                    if move_speed_minus_x <= mouse_x <= move_speed_minus_x + move_speed_minus_width and move_speed_minus_y <= mouse_y <= move_speed_minus_y + move_speed_minus_height and player_speed > 0:
                        player_speed -= 1
                        game_settings()
                    if players_plus_x <= mouse_x <= players_plus_x + players_plus_width and players_plus_y <= mouse_y <= players_plus_y + players_plus_height and players < 4:
                        players += 1
                        game_settings()
                    if players_minus_x <= mouse_x <= players_minus_x + players_minus_width and players_minus_y <= mouse_y <= players_minus_y + players_minus_height and players > 1:
                        players -= 1
                        game_settings()
                    if continue_x <= mouse_x <= continue_x + continue_width and continue_y <= mouse_y <= continue_y + continue_height and players != 0:
                        direction = random.choice(directions)
                        in_settings = False
                        draw_court()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE] and not pressed:
        pressed = True
        if players == 0:
            if in_settings:
                vertical = False
                in_settings = False
                main_menu()
            else: game_running = False
        elif players == 1 or players == 2 or players == 3 or players == 4:
            reset_game()
            players = 0
            vertical = False
            if in_settings: in_settings = False
            main_menu()
    if players == 0 or in_settings:
        if not in_settings:
            if keys[pygame.K_MINUS] and not dark_mode:
                dark_mode = True
                main_menu()
            if keys[pygame.K_EQUALS] and dark_mode:
                dark_mode = False
                main_menu()
            if keys[pygame.K_SLASH]:
                if hasattr(os, "startfile"): os.startfile("Help.txt")  
                else: os.system("open Help.txt 2>/dev/null || xdg-open Help.txt 2>/dev/null")
            if keys[pygame.K_RETURN] and not pressed:
                pressed = True
                in_settings = True
                game_settings()
        else:
            if keys[pygame.K_v] and not pressed and players < 4:
                pressed = True
                if not vertical:
                    vertical = True
                else:
                    vertical = False
                    if dark_mode: window.fill(dark)
                    else: window.fill(white)
                game_settings()
            if keys[pygame.K_RETURN] and not pressed and players != 0:
                pressed = True
                in_settings = False
                direction = random.choice(directions)
                draw_court()
    elif players == 1 and not in_settings:
        if vertical:
            if (keys[pygame.K_LEFT] or keys[pygame.K_a] or keys[pygame.K_b] or keys[pygame.K_KP_PLUS]) and player_4_x > 0: player_4_x -= player_speed
            if (keys[pygame.K_RIGHT] or keys[pygame.K_d] or keys[pygame.K_n] or keys[pygame.K_KP_MINUS]) and player_4_x + (player_height * (window_width / window_height)) < window_width: player_4_x += player_speed
            if keys[pygame.K_r]: reset_game()
            if direction == "NE":
                if ball_x + ball_width >= window_width: direction = "NW"
                elif ball_y <= 0: direction = "SE"
                else:
                    ball_x += ball_speed
                    ball_y -= ball_speed
                    draw_court()
            elif direction == "SE":
                if ball_x + ball_width >= window_width: direction = "SW"
                elif ball_y + ball_height >= window_height:
                    if dark_mode: window.fill(dark)
                    else: window.fill(white)
                    pygame.draw.rect(window, white, (player_4_x, player_4_y, player_height * screen_ratio, player_width))
                    pygame.draw.ellipse(window, white, (ball_x, ball_y, ball_width, ball_height))
                    text_width, text_height = font_ping_pong_1.get_rect(f"you lost")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2 - text_height - text_height / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render(f"you lost", white) 
                    else: text_surface, _ = font_ping_pong_1.render(f"you lost", black)
                    window.blit(text_surface, (text_x, text_y))
                    text_width, text_height = font_ping_pong_2.get_rect(f"score: {solo_score}")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_2.render(f"score: {solo_score}", white) 
                    else: text_surface, _ = font_ping_pong_2.render(f"score: {solo_score}", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif (player_4_x <= ball_x or ball_x + ball_width >= player_4_x) and ball_x <= player_4_x + player_height * screen_ratio and player_4_y <= ball_y + ball_height:
                    direction = "NE"
                    solo_score += 1
                else:
                    ball_x += ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "SW":
                if ball_x <= 0: direction = "SE"
                elif ball_y + ball_height >= window_height:
                    if dark_mode: window.fill(dark)
                    else: window.fill(white)
                    pygame.draw.rect(window, white, (player_4_x, player_4_y, player_height * screen_ratio, player_width))
                    pygame.draw.ellipse(window, white, (ball_x, ball_y, ball_width, ball_height))
                    text_width, text_height = font_ping_pong_1.get_rect(f"you lost")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2 - text_height - text_height / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render(f"you lost", white) 
                    else: text_surface, _ = font_ping_pong_1.render(f"you lost", black)
                    window.blit(text_surface, (text_x, text_y))
                    text_width, text_height = font_ping_pong_2.get_rect(f"score: {solo_score}")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_2.render(f"score: {solo_score}", white) 
                    else: text_surface, _ = font_ping_pong_2.render(f"score: {solo_score}", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif (player_4_x <= ball_x or ball_x + ball_width >= player_4_x) and ball_x <= player_4_x + player_height * screen_ratio and player_4_y <= ball_y + ball_height:
                    direction = "NW"
                    solo_score += 1
                else:
                    ball_x -= ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "NW":
                if ball_x <= 0: direction = "NE"
                elif ball_y <= 0: direction = "SW"
                else:
                    ball_x -= ball_speed
                    ball_y -= ball_speed
                    draw_court()
        else:
            if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_2_y > 0: player_2_y -= player_speed
            if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_2_y < window_height - player_height: player_2_y += player_speed
            if keys[pygame.K_r]: reset_game()
            if direction == "NE":
                if ball_x + ball_width >= window_width:
                    if dark_mode: window.fill(dark)
                    else: window.fill(white)
                    pygame.draw.rect(window, white, (player_2_x, player_2_y, player_width, player_height))
                    pygame.draw.ellipse(window, white, (ball_x, ball_y, ball_width, ball_height))
                    text_width, text_height = font_ping_pong_1.get_rect(f"you lost")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2 - text_height - text_height / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render(f"you lost", white) 
                    else: text_surface, _ = font_ping_pong_1.render(f"you lost", black)
                    window.blit(text_surface, (text_x, text_y))
                    text_width, text_height = font_ping_pong_2.get_rect(f"score: {solo_score}")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_2.render(f"score: {solo_score}", white) 
                    else: text_surface, _ = font_ping_pong_2.render(f"score: {solo_score}", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif ball_y <= 0: direction = "SE"
                elif player_2_x <= ball_x + ball_width and player_2_y <= ball_y <= player_2_y + player_height:
                    direction = "NW"
                    solo_score += 1
                else:
                    ball_x += ball_speed
                    ball_y -= ball_speed
                    draw_court()
            elif direction == "SE":
                if ball_x + ball_width >= window_width:
                    if dark_mode: window.fill(dark)
                    else: window.fill(white)
                    pygame.draw.rect(window, white, (player_2_x, player_2_y, player_width, player_height))
                    pygame.draw.ellipse(window, white, (ball_x, ball_y, ball_width, ball_height))
                    text_width, text_height = font_ping_pong_1.get_rect(f"you lost")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2 - text_height - text_height / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render(f"you lost", white) 
                    else: text_surface, _ = font_ping_pong_1.render(f"you lost", black)
                    window.blit(text_surface, (text_x, text_y))
                    text_width, text_height = font_ping_pong_2.get_rect(f"score: {solo_score}")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_2.render(f"score: {solo_score}", white) 
                    else: text_surface, _ = font_ping_pong_2.render(f"score: {solo_score}", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif ball_y + ball_height >= window_height: direction = "NE"
                elif player_2_x <= ball_x + ball_width and player_2_y <= ball_y <= player_2_y + player_height:
                    direction = "SW"
                    solo_score += 1
                else:
                    ball_x += ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "SW":
                if ball_x <= 0: direction = "SE"
                elif ball_y + ball_height >= window_height: direction = "NW"
                else:
                    ball_x -= ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "NW":
                if ball_x <= 0: direction = "NE"
                elif ball_y <= 0: direction = "SW"
                else:
                    ball_x -= ball_speed
                    ball_y -= ball_speed
                    draw_court()
    elif players == 2 and not in_settings:
        if vertical:
            if (keys[pygame.K_a] or keys[pygame.K_b]) and player_3_x > 0: player_3_x -= player_speed
            if (keys[pygame.K_d] or keys[pygame.K_n]) and player_3_x + (player_height * screen_ratio) < window_width: player_3_x += player_speed
            if (keys[pygame.K_LEFT] or keys[pygame.K_KP_PLUS]) and player_4_x > 0: player_4_x -= player_speed
            if (keys[pygame.K_RIGHT] or keys[pygame.K_KP_MINUS]) and player_4_x + (player_height * screen_ratio) < window_width: player_4_x += player_speed
            if keys[pygame.K_r]: reset_game()
            if direction == "NE":
                if ball_x + ball_width >= window_width: direction = "NW"
                elif ball_y <= 0: 
                    direction = "SE"
                    if local_score_2 > 5: local_score_2 -= 5
                    else: local_score_2 = 0
                elif (player_3_x <= ball_x or ball_x + ball_width >= player_3_x) and ball_x <= player_3_x + player_height * screen_ratio and ball_y <= player_3_y + player_width:
                    direction = "SE"
                    local_score_2 += 1
                    draw_court()
                else:
                    ball_x += ball_speed
                    ball_y -= ball_speed
                    draw_court()
            elif direction == "SE":
                if ball_x + ball_width >= window_width: direction = "SW"
                elif ball_y + ball_height >= window_height: 
                    direction = "NE"
                    if local_score_1 > 5: local_score_1 -= 5
                    else: local_score_1 = 0
                elif (player_4_x <= ball_x or ball_x + ball_width >= player_4_x) and ball_x <= player_4_x + player_height * screen_ratio and player_4_y <= ball_y + ball_height:
                    direction = "NE"
                    local_score_1 += 1
                    draw_court()
                else:
                    ball_x += ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "SW":
                if ball_x <= 0: direction = "SE"
                elif ball_y + ball_height >= window_height: 
                    direction = "NW"
                    if local_score_1 > 5: local_score_1 -= 5
                    else: local_score_1 = 0
                elif (player_4_x <= ball_x or ball_x + ball_width >= player_4_x) and ball_x <= player_4_x + player_height * screen_ratio and player_4_y <= ball_y + ball_height:
                    direction = "NW"
                    local_score_1 += 1
                    draw_court()
                else:
                    ball_x -= ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "NW":
                if ball_x <= 0: direction = "NE"
                elif ball_y <= 0: 
                    direction = "SW"
                    if local_score_2 > 5: local_score_2 -= 5
                    else: local_score_2 = 0
                elif (player_3_x <= ball_x or ball_x + ball_width >= player_3_x) and ball_x <= player_3_x + player_height * screen_ratio and ball_y <= player_3_y + player_width:
                    direction = "SW"
                    local_score_2 += 1
                    draw_court()
                else:
                    ball_x -= ball_speed
                    ball_y -= ball_speed
                    draw_court()
        else:
            if keys[pygame.K_w] and player_1_y > 0: player_1_y -= player_speed
            if keys[pygame.K_s] and player_1_y < window_height - player_height: player_1_y += player_speed
            if (keys[pygame.K_UP] or keys[pygame.K_KP_MINUS]) and player_2_y > 0: player_2_y -= player_speed
            if (keys[pygame.K_DOWN] or keys[pygame.K_KP_PLUS]) and player_2_y < window_height - player_height: player_2_y += player_speed
            if keys[pygame.K_r]: reset_game()
            if direction == "NE":
                if ball_x + ball_width >= window_width: 
                    direction = "NW"
                    if local_score_2 > 5: local_score_2 -= 5
                    else: local_score_2 = 0
                elif ball_y <= 0: direction = "SE"
                elif player_2_x <= ball_x + ball_width and player_2_y <= ball_y <= player_2_y + player_height:
                    direction = "NW"
                    local_score_2 += 1
                    draw_court()
                else:
                    ball_x += ball_speed
                    ball_y -= ball_speed
                    draw_court()
            elif direction == "SE":
                if ball_x + ball_width >= window_width: 
                    direction = "SW"
                    if local_score_2 > 5: local_score_2 -= 5
                    else: local_score_2 = 0
                elif ball_y + ball_height >= window_height: direction = "NE"
                elif player_2_x <= ball_x + ball_width and player_2_y <= ball_y <= player_2_y + player_height:
                    direction = "SW"
                    local_score_2 += 1
                    draw_court()
                else:
                    ball_x += ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "SW":
                if ball_x <= 0: 
                    direction = "SE"
                    if local_score_1 > 5: local_score_1 -= 5
                    else: local_score_1 = 0
                elif ball_y + ball_height >= window_height: direction = "NW"
                elif ball_x <= player_1_x + player_width and player_1_y <= ball_y <= player_1_y + player_height:
                    direction = "SE"
                    local_score_1 += 1
                    draw_court()
                else:
                    ball_x -= ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "NW":
                if ball_x <= 0:
                    direction = "NE"
                    if local_score_1 > 5: local_score_1 -= 5
                    else: local_score_1 = 0
                elif ball_y <= 0: direction = "SW"
                elif ball_x <= player_1_x + player_width and player_1_y <= ball_y <= player_1_y + player_height:
                    direction = "NE"
                    local_score_1 += 1
                    draw_court()
                else:
                    ball_x -= ball_speed
                    ball_y -= ball_speed
                    draw_court()
    elif players == 3 and not in_settings:
        if vertical:
            if keys[pygame.K_w] and player_1_y > 0: player_1_y -= player_speed
            if keys[pygame.K_s] and player_1_y < window_height - player_height: player_1_y += player_speed
            if keys[pygame.K_UP] and player_2_y > 0: player_2_y -= player_speed
            if keys[pygame.K_DOWN] and player_2_y < window_height - player_height: player_2_y += player_speed
            if (keys[pygame.K_b] or keys[pygame.K_KP_PLUS]) and player_3_x > 0: player_3_x -= player_speed
            if (keys[pygame.K_n] or keys[pygame.K_KP_MINUS]) and player_3_x < window_width - player_height * screen_ratio: player_3_x += player_speed
            if keys[pygame.K_r]: reset_game()
            if direction == "NE":
                if ball_y <= 0:
                    text_width, text_height = font_ping_pong_1.get_rect("top player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("top player loses", white) 
                    else: text_surface, _ = font_ping_pong_1.render("top player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif ball_x + ball_width >= window_width:
                    text_width, text_height = font_ping_pong_1.get_rect("right player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("right player loses", white)
                    else: text_surface, _ = font_ping_pong_1.render("right player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif player_2_x <= ball_x + ball_width and player_2_y <= ball_y <= player_2_y + player_height: direction = "NW"
                elif player_3_x <= ball_x <= player_3_x + player_height * screen_ratio and ball_y <= player_3_y + player_width: direction = "SE"
                else:
                    ball_x += ball_speed
                    ball_y -= ball_speed
                    draw_court()
            elif direction == "SE":
                if ball_y + ball_height >= window_height: direction = "NE"
                elif ball_x + ball_width >= window_width:
                    text_width, text_height = font_ping_pong_1.get_rect("right player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("right player loses", white)
                    else: text_surface, _ = font_ping_pong_1.render("right player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif player_2_x <= ball_x + ball_width and player_2_y <= ball_y <= player_2_y + player_height: direction = "SW"
                else:
                    ball_x += ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "SW":
                if ball_x <= 0:
                    text_width, text_height = font_ping_pong_1.get_rect("left player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("left player loses", white)
                    else: text_surface, _ = font_ping_pong_1.render("left player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif ball_y + ball_height >= window_height: direction = "NW"
                elif ball_x <= player_1_x + player_width and player_1_y <= ball_y <= player_1_y + player_height: direction = "SE"
                else:
                    ball_x -= ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "NW":
                if ball_x <= 0:
                    text_width, text_height = font_ping_pong_1.get_rect("left player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("left player loses", white)
                    else: text_surface, _ = font_ping_pong_1.render("left player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif ball_y <= 0:
                    text_width, text_height = font_ping_pong_1.get_rect("top player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("top player loses", white) 
                    else: text_surface, _ = font_ping_pong_1.render("top player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif ball_x <= player_1_x + player_width and player_1_y <= ball_y <= player_1_y + player_height: direction = "NE"
                elif player_3_x <= ball_x <= player_3_x + player_height * screen_ratio and ball_y <= player_3_y + player_width: direction = "SW"
                else:
                    ball_x -= ball_speed
                    ball_y -= ball_speed
                    draw_court()
        else:
            if keys[pygame.K_w] and player_1_y > 0: player_1_y -= player_speed
            if keys[pygame.K_s] and player_1_y < window_height - player_height: player_1_y += player_speed
            if keys[pygame.K_UP] and player_2_y > 0: player_2_y -= player_speed
            if keys[pygame.K_DOWN] and player_2_y < window_height - player_height: player_2_y += player_speed
            if (keys[pygame.K_KP_PLUS] or keys[pygame.K_b]) and player_4_x > 0: player_4_x -= player_speed
            if (keys[pygame.K_KP_MINUS] or keys[pygame.K_n]) and player_4_x < window_width - player_height * screen_ratio: player_4_x += player_speed
            if keys[pygame.K_r]: reset_game()
            if direction == "NE":
                if ball_y <= 0: direction = "SE"
                elif ball_x + ball_width >= window_width:
                    text_width, text_height = font_ping_pong_1.get_rect("right player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("right player loses", white)
                    else: text_surface, _ = font_ping_pong_1.render("right player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif player_2_x <= ball_x + ball_width and player_2_y <= ball_y <= player_2_y + player_height: direction = "NW"
                else:
                    ball_x += ball_speed
                    ball_y -= ball_speed
                    draw_court()
            elif direction == "SE":
                if ball_y + ball_height >= window_height:
                    text_width, text_height = font_ping_pong_1.get_rect("bottom player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("bottom player loses", white)
                    else: text_surface, _ = font_ping_pong_1.render("bottom player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif ball_x + ball_width >= window_width:
                    text_width, text_height = font_ping_pong_1.get_rect("right player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("right player loses", white)
                    else: text_surface, _ = font_ping_pong_1.render("right player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif player_2_x <= ball_x + ball_width and player_2_y <= ball_y <= player_2_y + player_height: direction = "SW"
                elif player_4_x <= ball_x <= player_4_x + player_height * screen_ratio and ball_y + ball_height >= player_4_y: direction = "NE"
                else:
                    ball_x += ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "SW":
                if ball_x <= 0:
                    text_width, text_height = font_ping_pong_1.get_rect("left player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("left player loses", white)
                    else: text_surface, _ = font_ping_pong_1.render("left player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif ball_y + ball_height >= window_height:
                    text_width, text_height = font_ping_pong_1.get_rect("bottom player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("bottom player loses", white)
                    else: text_surface, _ = font_ping_pong_1.render("bottom player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif ball_x <= player_1_x + player_width and player_1_y <= ball_y <= player_1_y + player_height: direction = "SE"
                elif player_4_x <= ball_x <= player_4_x + player_height * screen_ratio and ball_y + ball_height >= player_4_y: direction = "NW"
                else:
                    ball_x -= ball_speed
                    ball_y += ball_speed
                    draw_court()
            elif direction == "NW":
                if ball_x <= 0:
                    text_width, text_height = font_ping_pong_1.get_rect("left player loses")[2:]
                    text_x = text_cont_x + (text_cont_width - text_width) / 2
                    text_y = text_cont_y + (text_cont_height - text_height) / 2
                    if dark_mode: text_surface, _ = font_ping_pong_1.render("left player loses", white)
                    else: text_surface, _ = font_ping_pong_1.render("left player loses", black)
                    window.blit(text_surface, (text_x, text_y))
                    pygame.display.update()
                elif ball_y <= 0: direction = "SW"
                elif ball_x <= player_1_x + player_width and player_1_y <= ball_y <= player_1_y + player_height: direction = "NE"
                else:
                    ball_x -= ball_speed
                    ball_y -= ball_speed
                    draw_court()
    elif players == 4 and not in_settings:
        if keys[pygame.K_w] and player_1_y > 0: player_1_y -= player_speed
        if keys[pygame.K_s] and player_1_y < window_height - player_height: player_1_y += player_speed
        if keys[pygame.K_UP] and player_2_y > 0: player_2_y -= player_speed
        if keys[pygame.K_DOWN] and player_2_y < window_height - player_height: player_2_y += player_speed
        if keys[pygame.K_b] and player_3_x > 0: player_3_x -= player_speed
        if keys[pygame.K_n] and player_3_x < window_width - player_height * screen_ratio: player_3_x += player_speed
        if keys[pygame.K_KP_PLUS] and player_4_x > 0: player_4_x -= player_speed
        if keys[pygame.K_KP_MINUS] and player_4_x < window_width - player_height * screen_ratio: player_4_x += player_speed
        if keys[pygame.K_r]: reset_game()
        if direction == "NE":
            if ball_y <= 0:
                text_width, text_height = font_ping_pong_1.get_rect("top player loses")[2:]
                text_x = text_cont_x + (text_cont_width - text_width) / 2
                text_y = text_cont_y + (text_cont_height - text_height) / 2
                if dark_mode: text_surface, _ = font_ping_pong_1.render("top player loses", white) 
                else: text_surface, _ = font_ping_pong_1.render("top player loses", black)
                window.blit(text_surface, (text_x, text_y))
                pygame.display.update()
            elif ball_x + ball_width >= window_width:
                text_width, text_height = font_ping_pong_1.get_rect("right player loses")[2:]
                text_x = text_cont_x + (text_cont_width - text_width) / 2
                text_y = text_cont_y + (text_cont_height - text_height) / 2
                if dark_mode: text_surface, _ = font_ping_pong_1.render("right player loses", white)
                else: text_surface, _ = font_ping_pong_1.render("right player loses", black)
                window.blit(text_surface, (text_x, text_y))
                pygame.display.update()
            elif player_2_x <= ball_x + ball_width and player_2_y <= ball_y <= player_2_y + player_height: direction = "NW"
            elif player_3_x <= ball_x <= player_3_x + player_height * screen_ratio and ball_y <= player_3_y + player_width: direction = "SE"
            else:
                ball_x += ball_speed
                ball_y -= ball_speed
                draw_court()
        elif direction == "SE":
            if ball_y + ball_height >= window_height:
                text_width, text_height = font_ping_pong_1.get_rect("bottom player loses")[2:]
                text_x = text_cont_x + (text_cont_width - text_width) / 2
                text_y = text_cont_y + (text_cont_height - text_height) / 2
                if dark_mode: text_surface, _ = font_ping_pong_1.render("bottom player loses", white)
                else: text_surface, _ = font_ping_pong_1.render("bottom player loses", black)
                window.blit(text_surface, (text_x, text_y))
                pygame.display.update()
            elif ball_x + ball_width >= window_width:
                text_width, text_height = font_ping_pong_1.get_rect("right player loses")[2:]
                text_x = text_cont_x + (text_cont_width - text_width) / 2
                text_y = text_cont_y + (text_cont_height - text_height) / 2
                if dark_mode: text_surface, _ = font_ping_pong_1.render("right player loses", white)
                else: text_surface, _ = font_ping_pong_1.render("right player loses", black)
                window.blit(text_surface, (text_x, text_y))
                pygame.display.update()
            elif player_2_x <= ball_x + ball_width and player_2_y <= ball_y <= player_2_y + player_height: direction = "SW"
            elif player_4_x <= ball_x <= player_4_x + player_height * screen_ratio and ball_y + ball_height >= player_4_y: direction = "NE"
            else:
                ball_x += ball_speed
                ball_y += ball_speed
                draw_court()
        elif direction == "SW":
            if ball_x <= 0:
                text_width, text_height = font_ping_pong_1.get_rect("left player loses")[2:]
                text_x = text_cont_x + (text_cont_width - text_width) / 2
                text_y = text_cont_y + (text_cont_height - text_height) / 2
                if dark_mode: text_surface, _ = font_ping_pong_1.render("left player loses", white)
                else: text_surface, _ = font_ping_pong_1.render("left player loses", black)
                window.blit(text_surface, (text_x, text_y))
                pygame.display.update()
            elif ball_y + ball_height >= window_height:
                text_width, text_height = font_ping_pong_1.get_rect("bottom player loses")[2:]
                text_x = text_cont_x + (text_cont_width - text_width) / 2
                text_y = text_cont_y + (text_cont_height - text_height) / 2
                if dark_mode: text_surface, _ = font_ping_pong_1.render("bottom player loses", white)
                else: text_surface, _ = font_ping_pong_1.render("bottom player loses", black)
                window.blit(text_surface, (text_x, text_y))
                pygame.display.update()
            elif ball_x <= player_1_x + player_width and player_1_y <= ball_y <= player_1_y + player_height: direction = "SE"
            elif player_4_x <= ball_x <= player_4_x + player_height * screen_ratio and ball_y + ball_height >= player_4_y: direction = "NW"
            else:
                ball_x -= ball_speed
                ball_y += ball_speed
                draw_court()
        elif direction == "NW":
            if ball_x <= 0:
                text_width, text_height = font_ping_pong_1.get_rect("left player loses")[2:]
                text_x = text_cont_x + (text_cont_width - text_width) / 2
                text_y = text_cont_y + (text_cont_height - text_height) / 2
                if dark_mode: text_surface, _ = font_ping_pong_1.render("left player loses", white)
                else: text_surface, _ = font_ping_pong_1.render("left player loses", black)
                window.blit(text_surface, (text_x, text_y))
                pygame.display.update()
            elif ball_y <= 0:
                text_width, text_height = font_ping_pong_1.get_rect("top player loses")[2:]
                text_x = text_cont_x + (text_cont_width - text_width) / 2
                text_y = text_cont_y + (text_cont_height - text_height) / 2
                if dark_mode: text_surface, _ = font_ping_pong_1.render("top player loses", white) 
                else: text_surface, _ = font_ping_pong_1.render("top player loses", black)
                window.blit(text_surface, (text_x, text_y))
                pygame.display.update()
            elif ball_x <= player_1_x + player_width and player_1_y <= ball_y <= player_1_y + player_height: direction = "NE"
            elif player_3_x <= ball_x <= player_3_x + player_height * screen_ratio and ball_y <= player_3_y + player_width: direction = "SW"
            else:
                ball_x -= ball_speed
                ball_y -= ball_speed
                draw_court()
pygame.quit()