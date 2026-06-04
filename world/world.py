import pygame

from singletons.keyBus import key_bus

from src.gameProcess import GameProcess

from world.map.mapHandler import MapHandler


class World(GameProcess):
    def __init__(self, main: object) -> None:
        super().__init__(main)
        
        self.map_handler: MapHandler = MapHandler()
        
        self.pan: bool = False
        self.offset: pygame.Vector2 = pygame.Vector2()
        
    def setup_bus_calls(self) -> None:
        super().setup_bus_calls()
        
        key_bus.register('mouse_right_down', self.on_alt_click)
        key_bus.register('mouse_right_up', self.on_alt_release)
        
    def deregister(self) -> None:
        super().deregister()
        
        key_bus.deregister('mouse_right_down', self.on_alt_click)
        key_bus.deregister('mouse_right_up', self.on_alt_release)
    
    def on_alt_click(self) -> None:
        self.pan = True
        
    def on_alt_release(self) -> None:
        self.pan = False
        
    def update(self) -> None:
        super().update()
        
        if self.pan and (event := self.is_event(pygame.MOUSEMOTION)):
            rel: tuple[int, int] = self.mouse_handler.mouse_rel
            self.offset.xy = (
                max(min(self.offset.x + (rel[0] / 2), 0), self.temp_screen.get_width() - self.map_handler.current_map.map_image.get_width()), 
                max(min(self.offset.y + (rel[1] / 2), 0) , self.temp_screen.get_height() - self.map_handler.current_map.map_image.get_height())
            )
            
        
        self.draw()
        
    def draw(self) -> None:
        screen: pygame.Surface = self.temp_screen
        
        screen.fill('#313031')
        
        self.map_handler.draw(screen, self.offset.x, self.offset.y)
        
        super().draw()
        