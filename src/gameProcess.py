import pygame

from singletons.keyBus import key_bus
from singletons.eventBus import event_bus

from src.display import Display, ScreenOptions
from src.keyHandler import KeyHandler
from src.mouseHandler import MouseHandler


class GameProcess():
    def __init__(self, main: object) -> None:
        from src.gameLoop import GameLoop, DEFUALT_SCREEN_SIZE
        self.main: GameLoop = main
        
        self.temp_screen: pygame.Surface = pygame.Surface(DEFUALT_SCREEN_SIZE)
        
        self.key_handler: KeyHandler = KeyHandler()
        self.mouse_handler: MouseHandler = MouseHandler()
        
        self.events: list[pygame.Event] = []
        
        self.setup_bus_calls()
        
    def setup_bus_calls(self) -> None:
        key_bus.register('menu_down', self.quit)
    
    def deregister(self) -> None:
        key_bus.deregister('menu_down', self.quit)
    
    def is_event(self, event_id: int) -> pygame.Event:
        for event in self.events:
            if event.type == event_id:
                return event
            
    def update(self) -> None:
        self.main.clock.tick(self.main.display.get_framerate())
        self.events = pygame.event.get()
        
        self.key_handler.handle_keys()
        self.mouse_handler.handle_mouse(self.events)
        
        if self.is_event(pygame.QUIT):
            self.quit()
            
    def draw(self) -> None:
        self.main.display.draw(self.temp_screen)
            
    def quit(self) -> None:
        event_bus.sign('quit')
        
    def set_resolution(self, resolution: tuple[int, int]) -> None:
        self.main.display.set_resolution(resolution[0], resolution[1])
        
    def get_display(self) -> Display:
        return self.main.display
        
    def get_resolution(self) -> tuple[int, int]:
        return self.main.display.get_resolution()
    
    def get_fullscreen(self) -> ScreenOptions:
        return self.main.display.get_fullscreen()
        
    def get_fps(self) -> int:
        return round(self.main.clock.get_fps())
    
    def get_monitor(self) -> int:
        return self.main.display.get_monitor()
        