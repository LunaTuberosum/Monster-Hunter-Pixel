import math

import pygame

from singletons import resourceHandler

from world.character.player import Player
from world.map.tileData import TileData


TILE_SIZE: int = 32

class MapData():
    def __init__(self, map_name: str) -> None:
        self.map_name: str = map_name
        
        self.tileset: list[pygame.Surface] = []
        self.__make_tileset()
        
        self.tileset_data: dict[dict[str, str]] = resourceHandler.load_json(f'.\\maps\\{self.map_name}\\TilesetData.json')
        
        self.map_image: pygame.Surface = None
        
        self.layers: list[list[list[list[int]]]] = []
        self.__make_layer_data()
        
        self.tiles: list[TileData] = []
        self.__make_map()
        
        self.players: list[Player] = [
            Player(
                (7, 8),
                'P1'
            ),
            Player(
                (8, 7),
                'P1'
            )
        ]
        
    def get_tile(self, grid_cords: tuple[int, int]) -> TileData:
        tiles: list[TileData] = []
        for _tile in self.tiles:
            if _tile.grid_cords == grid_cords:
                tiles.append(_tile)
                
        tile: TileData = None
        
        for _tile in tiles:
            if not tile:
                tile = _tile
                continue
            
            if tile.layer < _tile.layer:
                tile = _tile
                
        return tile

    def draw_map(self) -> None:
        self.map_image.fill('#000000')
        
        y_sort: list[TileData | Player] = self.tiles + self.players
        
        def ysort(e: TileData | Player) -> int:
            if isinstance(e, TileData):
                return e.grid_cords[1] + e.layer
            
            return e.grid_cords[1] + int(self.get_tile(e.grid_cords).layer)
        
        y_sort.sort(key=ysort)
        
        for _item in y_sort:
            if isinstance(_item, TileData):
                _item.draw(self.map_image)
                
            elif isinstance(_item, Player):
                _y_offset: int = 19 - int(self.get_tile(_item.grid_cords).tile_info['YOff'])
                if _y_offset == 17:
                    _y_offset = 1
            
                _item.draw(self.map_image, _y_offset)
        
    def __make_tileset(self) -> None:
        _image: pygame.Surface = resourceHandler.load_image(f'.\\maps\\{self.map_name}\\Tileset.png')
        
        for _y in range(_image.get_height() // TILE_SIZE):
            for _x in range(_image.get_width() // TILE_SIZE):
                _tile: pygame.Surface = pygame.surface.Surface((TILE_SIZE, TILE_SIZE))
                _tile.set_colorkey('#000000')
                _tile.blit(_image, (0, 0), pygame.rect.Rect(
                    _x * TILE_SIZE,
                    _y * TILE_SIZE,
                    TILE_SIZE,
                    TILE_SIZE,
                ))

                self.tileset.append(_tile)
                
    def __make_layer_data(self) -> None:
        _layers: list[str] = resourceHandler.load_dir(f'.\\maps\\{self.map_name}\\Map Data')
        for _layer in _layers:
            _layer_arr = []
            for _section in resourceHandler.load_dir(f'.\\maps\\{self.map_name}\\Map Data\\{_layer}'):
                _section_arr = []
                with open(f'.\\maps\\{self.map_name}\\Map Data\\{_layer}\\{_section}') as _data:
                    _data = resourceHandler.load_csv(_data)

                    for _row in _data:
                        _section_arr.append(list(_row))

                _layer_arr.append(_section_arr)

            self.layers.append(_layer_arr)
        
    def __make_map(self) -> None:
        _max_row: int = 0
        _max_col: int = 0
        
        for _layer in self.layers:
            for _section in _layer:
                _x: int = 0
                _y: int = 0
                
                _max_row = max(len(_section), _max_row)
                for _row in _section:
                    _max_col = max(len(_row), _max_col)

                    for _col in _row:
                        if _col != '-1':
                            self.tiles.append(TileData(
                                grid_cords=[_x // 16, _y // 16], 
                                map_image_cords=[_x + 160, _y - 160], 
                                layer=self.layers.index(_layer) + _layer.index(_section),
                                image=self.tileset[int(_col)],
                                image_path=_col, 
                                tile_info=self.tileset_data[_col]
                            ))
                        _x += TILE_SIZE // 2
                    _y += TILE_SIZE // 2
                    _x: int = 0
                    
        self.map_image = pygame.Surface((_max_row * TILE_SIZE, (_max_col / 2) * TILE_SIZE))
                    
                    