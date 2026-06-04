import pygame

from singletons.dataBus import data_bus
from singletons.keyBus import key_bus
from singletons.keyConsts import KeyButton, pygame_key_lookup, term_key_lookup
from singletons.eventBus import event_bus
from singletons import resourceHandler

class KeyHandler():
    def __init__(self) -> None:
        self.keyboard_config: dict[str, str] = resourceHandler.load_json('.\\data\\keyboardConfig.json')
        
        data_bus.register('get_key', self.get_key)
        
    def get_key(self, key: KeyButton) -> str:
        return self.keyboard_config.get(term_key_lookup.get(key))
    
    def handle_keys(self) -> None:
        self.__key_down()
        self.__key_up()
        
    def __key_down(self) -> None:
        keys = pygame.key.get_just_pressed()
    
        for term, key in self.keyboard_config.items():
            if keys[pygame_key_lookup.get(key)]:
                key_bus.sign(f'{term}_down')
    
    def __key_up(self) -> None:
        keys = pygame.key.get_just_released()
        
        for term, key in self.keyboard_config.items():
            if keys[pygame_key_lookup.get(key)]:
                key_bus.sign(f'{term}_up')