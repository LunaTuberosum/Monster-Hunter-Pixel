import pygame


class Debug():
    def __init__(self, main: object) -> None:
        from world.world import World
        self.main: World = main

        self.__active: bool = False

        self.font: pygame.Font = pygame.font.SysFont("Arial", 10)

        self.__sections: dict[str, bool] = {
            'Tile': False
        }

        self.tile_selector: int = '-1'

        self.components: list[str] = self.update_components()

    def update_components(self) -> None:
        return [
            f'FPS: {round(self.main.main.clock.get_fps())}',
            f'MAP: {self.main.map_handler.current_map_name}',
            f'[X, Y]: {self.main.current_tile.grid_cords if self.main.current_tile else "[-1, -1]"}',
            f'',
            f'Tiles: {self.__sections["Tile"]}',
            f'T ID: {self.tile_selector}'
        ]

    def toggle_active(self) -> None:
        self.__active = not self.__active

    def get_active(self) -> bool:
        return self.__active

    def toggle_section_active(self, section_name: str) -> None:
        self.__sections[section_name] = not self.__sections[section_name]

    def draw(self) -> None:
        ## Checking if not on
        if not self.__active: return

        ## Resting Components
        self.components = self.update_components()

        ## Drawing Components
        _x: int = 5
        _y: int = 2
        for _item in self.components:
            self.main.temp_screen.blit(self.font.render(_item, False, '#ffffff'), (_x, _y))
            _y += 10

        # ## Drawing Mouse Square
        # _mouse_pos: list[float] = pygame.mouse.get_pos()
        # _mouseScale: list[float] = [display_width / SCREEN_WIDTH, display_height / SCREEN_HEIGHT]
        # _mouse_pos: list[float] = [_mouse_pos[0] / _mouseScale[0], _mouse_pos[1] / _mouseScale[1]]
        # _rect: pygame.Rect = pygame.Rect(0, 0, 4, 4) 
        # _rect.center = [_mouse_pos[0], _mouse_pos[1]]

        # pygame.draw.rect(self.main.screen, '#ff00ff', _rect)

        # ## Drawing tile hit boxes
        # if self.__sections['Tile']:
        #     if self.main.eventHandler.currentTile: 
        #         _yOffset: int = (19 - int(self.main.eventHandler.currentTile.tileInfo['YOff']))
        #         self.main.screen.blit(self.main.eventHandler.currentTile.mask.to_surface(unsetcolor=(0, 255, 0, 0)), (self.main.eventHandler.currentTile.rect.x - int(self.main.eventHandler.currentTile.tileInfo['XOff']), self.main.eventHandler.currentTile.rect.y - int(self.main.eventHandler.currentTile.tileInfo['YOff']) - _yOffset))