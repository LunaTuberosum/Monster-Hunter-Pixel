import pygame

from singletons.dataBus import data_bus
from singletons.keyBus import key_bus

from src.debug import Debug
from src.gameProcess import GameProcess

from world.map.mapHandler import MapHandler
from world.map.tileData import TileData


class World(GameProcess):
    def __init__(self, main: object) -> None:
        super().__init__(main)
        
        self.map_handler: MapHandler = MapHandler()
        
        self.pan: bool = False
        self.offset: pygame.Vector2 = pygame.Vector2()
        
        self.current_tile: TileData = None
        
        self.debug: Debug = Debug(self)
        
    def setup_bus_calls(self) -> None:
        super().setup_bus_calls()
        
        key_bus.register('mouse_left_down', self.on_click)
        
        key_bus.register('mouse_right_down', self.on_alt_click)
        key_bus.register('mouse_right_up', self.on_alt_release)
        
        key_bus.register('debug_down', self.on_debug)
        
    def deregister(self) -> None:
        super().deregister()
        
        key_bus.deregister('mouse_left_down', self.on_click)
        
        key_bus.deregister('mouse_right_down', self.on_alt_click)
        key_bus.deregister('mouse_right_up', self.on_alt_release)
        
        key_bus.deregister('debug_down', self.on_debug)
    
    def on_click(self) -> None:
        for _player in self.map_handler.current_map.players:
            if (_tile := self.map_handler.current_map.get_tile(_player.grid_cords)).hover:
                _player.selected = not _player.selected
    
    def on_alt_click(self) -> None:
        self.pan = True
        
    def on_alt_release(self) -> None:
        self.pan = False
        
    def on_debug(self) -> None:
        self.debug.toggle_active()
        
    def update(self) -> None:
        super().update()
        
        if self.pan and self.is_event(pygame.MOUSEMOTION):
            rel: tuple[int, int] = self.mouse_handler.mouse_rel
            self.offset.xy = (
                max(min(self.offset.x + (rel[0] / 2), 0), self.temp_screen.get_width() - self.map_handler.current_map.map_image.get_width()), 
                max(min(self.offset.y + (rel[1] / 2), 0) , self.temp_screen.get_height() - self.map_handler.current_map.map_image.get_height())
            )
            
        self.check_tiles()
        
        self.draw()
        
    def draw(self) -> None:
        screen: pygame.Surface = self.temp_screen
        
        screen.fill('#313031')
        
        self.map_handler.draw(screen, self.offset.x, self.offset.y)
        
        self.debug.draw()
        
        super().draw()
        
    def check_tiles(self):
        screen_size: tuple[int, int] = self.main.get_screen().size
        
        _mouse_pos: tuple[float, float] = data_bus.sign('get_mouse_pos')
        _mouse_scale: tuple[float, float] = (
            screen_size[0] / self.temp_screen.get_width(),
            screen_size[1] / self.temp_screen.get_height()
        )
        _mouse_pos = (
            (_mouse_pos[0] / _mouse_scale[0]) - self.offset.x,
            (_mouse_pos[1] / _mouse_scale[1]) - self.offset.y
        )
        
        _mouse_mask: pygame.Mask = pygame.mask.from_surface(pygame.Surface((1, 1)))
        
        _collided_tiles: list[TileData] = []
        for _tile in self.map_handler.current_map.tiles:
            _y_offset: int = (19 - int(_tile.tile_info['YOff']))
            _tile.hover = False
            
            if not _tile.mask.overlap(
                _mouse_mask,
                (
                    _mouse_pos[0] - (_tile.rect.x - int(_tile.tile_info['XOff'])), 
                    _mouse_pos[1] - (_tile.rect.y - int(_tile.tile_info['YOff'])) + _y_offset
                )
            ):
                continue
            
            _collided_tiles.append(_tile)
            
        for _tile in _collided_tiles:
            if 'OBS' in _tile.tile_info['Name']:
                _collided_tiles = [_tile]
                break
            
        def sort_key(e: TileData) -> int:
            return e.layer + e.grid_cords.y + int(e.tile_info['Elv'])
        
        _collided_tiles.sort(key=sort_key, reverse=True)
        
        if _collided_tiles:
            for _tile in _collided_tiles:
                if not ('WLL' in _tile.tile_info['Name']):
                    continue
                
                if _tile.layer > _collided_tiles[0].layer:
                    _collided_tiles = [_tile]
                    break
                
            _collided_tiles[0].hover = True
            self.current_tile = _collided_tiles[0]