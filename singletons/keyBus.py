from singletons.bus import Bus


class KeyBus(Bus):
    def __init__(self) -> None:
        super().__init__(
            {
                'mouse_left_down': [],
                'mouse_left_up': [],
                
                'mouse_right_down': [],
                'mouse_right_up': [],
                
                'mouse_middle_down': [],
                'mouse_middle_up': [],
                
                'mouse_scroll_down': [],
                'mouse_scroll_up': [],
                
                'confirm_down': [], 
                'confirm_up': [], 
                
                'cancel_down': [], 
                'cancel_up': [], 
                
                'menu_down': [], 
                'menu_up': [], 
                
                'debug_down': [], 
                'debug_up': [], 
            }
        )
        
key_bus: KeyBus = KeyBus()