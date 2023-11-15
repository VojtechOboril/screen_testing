from .screen import Screen

class ScreenManager(Screen):
    def __init__(self, window):
        Screen.__init__(self)
        self.window = window

    def handle_click(self, mouse_pos):
        for item in self.items:
            if item.is_point_inside(mouse_pos):
                item.on_clicked()
    
    def update(self):
        Screen.update(self, self.window)
    