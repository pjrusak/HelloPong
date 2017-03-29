import gameobject

__author__ = 'pjr'


class Brick(gameobject.GameObject):
    """
        Brick object for Pong game
    """
    COLORS = {1: '#999999', 2: '#555555', 3: '#222222'}

    def __init__(self, canvas, x, y, hits):
        """
            Brick constructor
        :param canvas: reference to Cavnas
        :param x:  center position in width dimension
        :param y:  center position in height dimension
        :param hits:
        """
        self.width = 75
        self.height = 20
        self.hits = hits
        color = Brick.COLORS[hits]
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill=color, tags='brick')
        super(Brick, self).__init__(canvas, item)

    def hit(self):
        """
            Update brick on hit
        """
        self.hits -= 1
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])


def test_run():
    """
        Module test function:
        - create Frame
        - create Ball and interacts with it's methods
    """
    import tkinter as tk
    root = tk.Tk()
    root.title('Hello, Pong!')
    frame = tk.Frame(root)
    canvas = tk.Canvas(frame, width=600, height=400, bg='#aaaaff')
    brick1 = Brick(canvas, 50, 50, 1)
    print("I'm on: ", brick1.get_position())
    brick1.move(50, 50)
    print("After move I'm on: ", brick1.get_position())
    brick2 = Brick(canvas, 200, 200, 2)
    print("I'm on: ", brick2.get_position())
    brick3 = Brick(canvas, 300, 300, 3)
    print("I'm on: ", brick3.get_position())

    # pack widgets
    frame.pack()
    canvas.pack()
    # run widget
    root.mainloop()

if __name__ == '__main__':
    test_run()
