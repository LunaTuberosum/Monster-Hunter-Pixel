from enum import Enum

import pygame


class KeyButton(Enum):
    CONFIRM: int = 0
    CANCEL: int = 1
    
    MENU: int = 2
    DEBUG: int = 3
    
term_key_lookup: dict[KeyButton, str] = {
    KeyButton.CONFIRM: 'confirm',
    KeyButton.CANCEL: 'cancel',
    
    KeyButton.MENU: 'menu',
    KeyButton.DEBUG: 'debug',
}
    
pygame_key_lookup: dict[str, int] = {
    'a': pygame.K_a,
    'b': pygame.K_b,
    'c': pygame.K_c,
    'd': pygame.K_d,
    'e': pygame.K_e,
    'f': pygame.K_f,
    'g': pygame.K_g,
    'h': pygame.K_h,
    'i': pygame.K_i,
    'j': pygame.K_j,
    'k': pygame.K_k,
    'l': pygame.K_l,
    'm': pygame.K_m,
    'n': pygame.K_n,
    'o': pygame.K_o,
    'p': pygame.K_p,
    'q': pygame.K_q,
    'r': pygame.K_r,
    's': pygame.K_s,
    't': pygame.K_t,
    'u': pygame.K_u,
    'v': pygame.K_v,
    'w': pygame.K_w,
    'x': pygame.K_x,
    'y': pygame.K_y,
    'z': pygame.K_z,
    
    'escape': pygame.K_ESCAPE,
    
    'left shift': pygame.K_LSHIFT,
    'right shift': pygame.K_RSHIFT,
    'space': pygame.K_SPACE,
    
    'f1': pygame.K_F1,
    'f2': pygame.K_F2,
    'f3': pygame.K_F3,
    'f4': pygame.K_F4,
    'f5': pygame.K_F5,
    'f6': pygame.K_F6,
    'f7': pygame.K_F7,
    'f8': pygame.K_F8,
    'f9': pygame.K_F9,
    'f10': pygame.K_F10,
    'f11': pygame.K_F11,
    'f12': pygame.K_F12,
}