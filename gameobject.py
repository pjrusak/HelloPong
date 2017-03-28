__author__ = "pjr"

class GameObject(object):
    """
        Base class for Breakout game objects
    """
    def __init__(self, canvas, item):
        """
            Constructor
            :param canvas: reference to Tk Canvas
            :param item: reference to item draw on Canvas
        """
        self.canvas = canvas
        self.item = item

    def get_position(self):
        """
            GameObject position getter
        """
        return self.canvas.coords(self.item)

    def move(self, x, y):
        """
            Moves GamesObject to new position
            :param x: move offset in pixels in width dimension
            :param y: move offset in pixels in height dimension
        """
        self.canvas.move(self.item, x, y)

    def delete(self):
        """
            Delete GameObject from Canvas
        """
        self.canvas.delete(self.item)


def test_run():
    """
        Module test function:
        - create Frame
        - create GameObject and interacts with it's methods
    """
    import tkinter as tk
    root = tk.Tk()
    root.title('Hello, Pong!')
    frame = tk.Frame(root)
    canvas = tk.Canvas(frame, width=600, height=400, bg='#aaaaff')
    item = canvas.create_rectangle(10, 10, 100, 80, fill='green')
    game_object = GameObject(canvas, item)
    print("I'm on: ", game_object.get_position())
    game_object.move(50, 50)
    print("After move I'm on: ", game_object.get_position())
    # game_object.delete()

    # pack widgets
    frame.pack()
    canvas.pack()
    # run widget
    root.mainloop()

if __name__ == '__main__':
    test_run()
