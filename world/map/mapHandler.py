import pygame

from singletons import resourceHandler

from world.map.mapData import MapData


class MapHandler():
    def __init__(self, start_map: str = 'None') -> None:
        self.maps: list[str] = resourceHandler.load_dir('.\\maps')
        self.current_map_name: str = start_map if start_map != 'None' else self.maps[0] ## TEMP
        self.current_map: MapData = self.create_map()
        
    def create_map(self) -> MapData:
        return MapData(self.current_map_name)
    
    def draw(self, screen: pygame.Surface, x_offset: int, y_offset: int) -> None:
        self.current_map.draw_map()
        
        screen.blit(self.current_map.map_image, (x_offset, y_offset))