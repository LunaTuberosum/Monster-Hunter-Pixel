import pygame


TILE_SIZE: int = 32

class TileData():
    def __init__(self, grid_cords: list[int], map_image_cords: list[int], layer: int, image: pygame.Surface, image_path: str, tile_info: dict[str, str]) -> None:
        self.grid_cords: pygame.Vector2 = pygame.Vector2(grid_cords)
        self.map_image_cords: pygame.Vector2 = pygame.Vector2(map_image_cords)
        self.layer: int = layer

        self.image: pygame.Surface = image
        self.imageID: str = image_path
        
        self.outline_image = pygame.image.load('.\\assets\\outline.png').convert_alpha()
        self.outline_image_red = pygame.image.load('.\\assets\\outline_red.png').convert_alpha()
        
        self.mask: pygame.Mask = pygame.mask.from_surface(self.outline_image, threshold=0)

        self.tile_info: dict[str, str] = tile_info
        self.hover: bool = False
        
        if int(self.tile_info['Elv']) >= 1:
            self.grid_cords.x += 1
            self.grid_cords.y += 1

        self.rect: pygame.Rect = pygame.rect.Rect(
            int(self.map_image_cords.x - self.map_image_cords.y) + int(self.tile_info['XOff']), 
            (int(self.map_image_cords.x + self.map_image_cords.y) // 2) + int(self.tile_info['YOff']), 
            TILE_SIZE - int(self.tile_info['WOff']), 
            (TILE_SIZE // 2) - int(self.tile_info['HOff'])
        )
        
    def __repr__(self) -> str:
        return f'{self.tile_info}, {self.layer}, {self.map_image_cords}'

    def draw(self, screen: pygame.Surface) -> None:
        _blit_cords: tuple[int, int] = (
            int(self.map_image_cords.x - self.map_image_cords.y), 
            int(self.map_image_cords.x + self.map_image_cords.y) // 2
        )
        _y_offset: int = (19 - int(self.tile_info['YOff']))

        if self.hover and "OBS" in self.tile_info["Name"]:
            if self.tile_info["NAS"]:
                screen.blit(self.outline_image_red, (_blit_cords[0], _blit_cords[1] - _y_offset))
            else:
                screen.blit(self.outline_image, (_blit_cords[0], _blit_cords[1] - _y_offset))

        screen.blit(self.image, _blit_cords)
        if "WLL" in self.tile_info["Name"]: return

        if self.hover and "OBS" not in self.tile_info["Name"]:
            if self.tile_info["NAS"]:
                screen.blit(self.outline_image_red, (_blit_cords[0], _blit_cords[1] - _y_offset))
            else:
                screen.blit(self.outline_image, (_blit_cords[0], _blit_cords[1] - _y_offset))
                
        