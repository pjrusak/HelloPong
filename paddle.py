import gameobject

__author__ = 'pjr'


class Paddle(gameobject.GameObject):
    """
        Paddle object for Pong game
    """
    def __init__(self, canvas, x, y):
        """
            Paddle constructor
        :param canvas: reference to Cavnas
        :param x:  center position in width dimension
        :param y:  center position in height dimension
        """
        self.width = 80
        self.height = 10
        self.ball = None
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill='blue')
        super(Paddle, self).__init__(canvas, item)

    def set_ball(self, ball):
        """
            sets ball on the paddle
            :param ball: Ball reference
        """
        self.ball = ball

    def move(self, offset):
        """
            moves paddle
            :param offset: offset to move in width dimension
        """
        coords = self.get_position()
        width = self.canvas.winfo_width()  # get width for widget

        # move paddle by offset in x direction
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super(Paddle, self).move(offset, 0)
            # if ball is on the paddle, move also the ball
            if self.ball is not None:
                self.ball.move(offset, 0)
