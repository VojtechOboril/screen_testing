class Screen:
    def __init__(self):
        self.items = []

    def set_as_screen(self, window):
        for item in window.items:
            item.undraw()

        for item in self.items:
            item.draw(window)
    
    def update(self, window):
        self.set_as_screen(window)

    def add_item(self, item, update = False):
        self.items.append(item)
        if update:
            self.update()

    