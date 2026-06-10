import pygame

from singletons import resourceHandler


TILE_SIZE: int = 32

class Player():
    def __init__(self, grid_cords: tuple[int, int], name: str) -> None:
        self.grid_cords: tuple[int, int] = grid_cords
        self.map_image_cords: tuple[int, int] = (
            (self.grid_cords[0] - 1) * (TILE_SIZE // 2) + 160, 
            (self.grid_cords[1] - 1) * (TILE_SIZE // 2) - 160
        )
        
        self.name: str = name
        self.image: pygame.Surface = resourceHandler.load_image('.\\assets\\Player test.png')
        self.outline_image_blue = pygame.image.load(".\\assets\\blue.png").convert_alpha()
        
        self.selected: bool = False
        
    def draw(self, screen: pygame.Surface, y_offset: int) -> None:
        _blit_cords: tuple[int, int] = (
            int(self.map_image_cords[0] - self.map_image_cords[1]), 
            int(self.map_image_cords[0] + self.map_image_cords[1]) // 2
        )
        _blit_cords = (_blit_cords[0], _blit_cords[1] - y_offset)
        
        
        if self.selected:
            screen.blit(self.outline_image_blue, (_blit_cords[0], _blit_cords[1]))
        
        screen.blit(self.image, _blit_cords)