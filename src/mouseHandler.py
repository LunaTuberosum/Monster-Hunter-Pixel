import pygame

from singletons.dataBus import data_bus
from singletons.keyBus import key_bus


LEFT: int = 1
MIDDLE: int = 2
RIGHT: int = 3
SCROLL_UP: int = 4
SCROLL_DOWN: int = 5

DEFUALT_SCREEN_SIZE: tuple[int, int] = (1280, 720)

class MouseHandler():
    def __init__(self) -> None:
        self.mouse_pos: tuple[int, int] = ()
        self.mouse_rel: tuple[int, int] = ()
        self.scroll_wheel: tuple[int, int] = ()
        
        data_bus.register('get_mouse_pos', self.get_pos)
        
    def get_pos(self) -> tuple[int, int]:
        res: tuple[int, int] = data_bus.sign('get_resolution')
        scale: tuple[int, int] = (
            res[0] / DEFUALT_SCREEN_SIZE[0], 
            res[1] / DEFUALT_SCREEN_SIZE[1]
        )
        
        return (self.mouse_pos[0] / scale[0], self.mouse_pos[1] / scale[1])
        
    def handle_mouse(self, events: list[pygame.Event]) -> None:
        self.mouse_pos = pygame.mouse.get_pos()
        
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == LEFT:
                    key_bus.sign('mouse_left_down')
                    
                if event.button == MIDDLE:
                    key_bus.sign('mouse_middle_down')
                    
                if event.button == RIGHT:
                    key_bus.sign('mouse_right_down')
                    
                if event.button == SCROLL_UP:
                    key_bus.sign('mouse_scroll_up')
                    
                if event.button == SCROLL_DOWN:
                    key_bus.sign('mouse_scroll_down')
                    
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == LEFT:
                    key_bus.sign('mouse_left_up')
                    
                if event.button == MIDDLE:
                    key_bus.sign('mouse_middle_up')
                    
                if event.button == RIGHT:
                    key_bus.sign('mouse_right_up')
                    
            if event.type == pygame.MOUSEMOTION:
                self.mouse_rel = event.rel
                
            if event.type == pygame.MOUSEWHEEL:
                self.scroll_wheel = (event.x, event.y)