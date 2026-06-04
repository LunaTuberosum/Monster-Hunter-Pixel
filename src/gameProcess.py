import pygame

from singletons.eventBus import event_bus

from src.display import Display, ScreenOptions


class GameProcess():
    def __init__(self, main: object) -> None:
        from src.gameLoop import GameLoop
        self.main: GameLoop = main
        
        self.events: list[pygame.Event] = []
        
        self.setup_bus_calls()
        
    def setup_bus_calls(self) -> None:
        pass
    
    def deregister(self) -> None:
        pass
    
    def is_event(self, event_id: int) -> pygame.Event:
        for event in self.events:
            if event.type == event_id:
                return event
            
    def update(self) -> None:
        self.main.clock.tick(self.main.display.get_framerate())
        self.events = pygame.event.get()
        
        if self.is_event(pygame.QUIT):
            self.quit()
            
    def draw(self) -> None:
        self.main.display.draw()
            
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
        