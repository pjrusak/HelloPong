import gameobject

__author__ = 'pjr'


class Ball(gameobject.GameObject):
    """
        Ball object for Pong game
    """
    def __init__(self, canvas, x, y):
        """
            Ball constructor
        :param canvas: reference to Cavnas
        :param x:  center position in width dimension
        :param y:  center position in height dimension
        """
        self.radius = 10
        self.direction = [1, -1]  # initial direction is upper-right
        self.speed = 10  # initial speed
        item = canvas.create_oval(x - self.radius, y - self.radius,
                                  x + self.radius, y + self.radius,
                                  fill='white')
        super(Ball, self).__init__(canvas, item)


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
    ball = Ball(canvas, 50, 50)
    print("I'm on: ", ball.get_position())
    ball.move(50, 50)
    print("After move I'm on: ", ball.get_position())
    # game_object.delete()

    # pack widgets
    frame.pack()
    canvas.pack()
    # run widget
    root.mainloop()

if __name__ == '__main__':
    test_run()
