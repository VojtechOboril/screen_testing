import graphics
from frontend.screens import ScreenManager
from frontend.items import Button

def main():
    window = graphics.GraphWin("Some ripoff", 512, 768)
    screen = ScreenManager(window)
    screen.update()

    while True:
        mouse_pos = window.getMouse()
        screen.handle_click(mouse_pos)


if __name__ == "__main__":
    main()