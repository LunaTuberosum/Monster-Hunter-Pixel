import pygame

from src.gameProcess import GameProcess


class World(GameProcess):
    def __init__(self, main: object) -> None:
        super().__init__(main)
        
    def setup_bus_calls(self) -> None:
        super().setup_bus_calls()
        
    def deregister(self) -> None:
        super().deregister()
        
    def update(self) -> None:
        super().update()
        
        self.draw()
        
    def draw(self) -> None:
        screen: pygame.Surface = self.main.get_screen()
        
        screen.fill('#313031')
        
        super().draw()
        