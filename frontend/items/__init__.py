from graphics import Rectangle

class Button(Rectangle): 
    def __init__(self, p1, p2, function_list, argument_list):
        Rectangle.__init__(self, p1, p2)
        self.p1 = p1
        self.p2 = p2
        self.function_list = function_list
        self.argument_list = argument_list
    
    def on_clicked(self):
        for index, function in enumerate(self.function_list):
            function(*self.argument_list[index])

    def is_point_inside(self, point):
        if ((point.x < self.p1.x and self.p2.x < point.x) or \
            (point.x > self.p1.x and self.p2.x > point.x)) and \
            ((point.y < self.p1.y and self.p2.y < point.y) or \
            (point.y > self.p1.y and self.p2.y > point.y)):
            return True
        return False


class TextButton(Button):
    def __init__(self):
        pass

class ImageButton(Button):
    def __init__(self):
        pass