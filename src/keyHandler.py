import pygame

from singletons.keyBus import key_bus
from singletons.eventBus import event_bus

class KeyHandler():
    def __init__(self) -> None:
        pass
    
    def handle_keys(self) -> None:
        self.__key_down()
        self.__key_up()
        
    def __key_down(self) -> None:
        keys = pygame.key.get_just_pressed()
    
    def __key_up(self) -> None:
        keys = pygame.key.get_just_released()