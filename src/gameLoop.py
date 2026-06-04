import sys
from os import listdir
from typing import Callable

import pygame

from singletons.eventBus import event_bus
from singletons import resourceHandler

from src.display import Display
from src.gameProcess import GameProcess

from world.world import World


GAME_SCREEN_SIZE: tuple[int, int] = (640, 360)
DEFUALT_SCREEN_SIZE: tuple[int, int] = (1280, 720)

def error_handle(func: Callable) -> Callable:
    def inner(*args):
        try:
            return func(*args)
        
        except KeyboardInterrupt:
            if not args[0].run:
                pygame.quit()
                sys.exit(130)

        except Exception:
            if not args[0].run:
                pygame.quit()
                sys.exit(0)
                return
            
            import traceback
            traceback.print_exc(file=sys.stdout)
            
            with open(f'.\\logs\\error_log_{len(listdir('.\\logs'))}.txt', 'w') as error_log:
                error_log.write(traceback.format_exc())
                
            sys.exit(-1)
            
    return inner

class GameLoop():
    def __init__(self) -> None:
        pygame.init()
        
        self.clock = pygame.Clock()
        self.display: Display = None 
        self.load_setting_save()
        
        pygame.mixer.set_num_channels(3)
        
        pygame.display.set_caption('Monster Hunter Pixel')
        
        pygame.key.set_repeat(200, 100)
        
        self.current_process: GameProcess = World(self)
        self.run: bool = True
        
        self.set_up_bus_calls()
        
    def set_up_bus_calls(self) -> None:
        event_bus.register('quit', self.quit)
        
    def quit(self) -> None:
        pygame.quit()
        sys.exit(0)
        self.run = False
        
    def load_setting_save(self) -> None:
        setting_save: dict[str] = resourceHandler.load_pickle('.//settings.pkl')

        if not setting_save:
            setting_save = {
                'monitor': 1,
                
                'windowSize': DEFUALT_SCREEN_SIZE,
                'displayOption': 1,
                'framerate': 0,
                'vsync': False,
                
                'volume': 1
            }

            resourceHandler.save_pickle('.//settings.pkl', setting_save)

        self.display = Display(setting_save['windowSize'][0], setting_save['windowSize'][1])
        self.display.set_monitor(setting_save['monitor'])
        self.display.set_fullscreen(setting_save['displayOption'])
        self.display.set_framerate(setting_save['framerate'])
        self.display.set_vsync(setting_save['vsync'])
        
        self.display.set_volume(setting_save['volume'])
        
        self.display.create_screen()
        
    def get_screen(self) -> pygame.Surface:
        return self.display.screen
    
    @error_handle
    def update(self) -> None:
        while self.run:
            self.current_process.update()
