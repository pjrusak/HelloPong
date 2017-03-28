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
