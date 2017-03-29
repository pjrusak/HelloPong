import tkinter as tk
import brick as bricks
import paddle
import ball

__author__ = 'pjr'


class Game(tk.Frame):
    """
        Pong game
    """
    def __init__(self, master):
        """
            Game constructor
            :param master: reference to Tk widget
        """
        super(Game, self).__init__(master)
        self.lives = 3
        self.width = 610
        self.height = 400
        self.canvas = tk.Canvas(self, bg='#aaaaff',
                                width=self.width,
                                height=self.height)
        self.canvas.pack()
        self.pack()

        # setup game objects
        self.ball = None

        # add to item dictionary things
        # that can collide with ball
        self.items = {}
        self.paddle = paddle.Paddle(self.canvas, self.width / 2, 326)
        self.items[self.paddle.item] = self.paddle

        # create and add bricks
        for x in range(5, self.width - 5, 75):
            self.add_brick(x + 37.5, 50, 2)
            self.add_brick(x + 37.5, 70, 1)
            self.add_brick(x + 37.5, 90, 1)

        # initialize game
        self.hud = None
        self.setup_game()
        # bind event handlers
        self.canvas.focus_set()
        self.canvas.bind('<Left>', lambda _: self.paddle.move(-10))
        self.canvas.bind('<Right>', lambda _: self.paddle.move(10))

    def setup_game(self):
        """
            Game initialization
        """
        self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 200, 'Press Space to start')
        self.canvas.bind('<space>', lambda _: self.start_game())

    def add_ball(self):
        """
            Add ball on top of the paddle
        """
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) * 0.5
        self.ball = ball.Ball(self.canvas, x, 310)
        self.paddle.set_ball(self.ball)

    def add_brick(self, x, y, hits):
        """
            Add bricks to game
            :param x: center position in width dimension
            :param y: center position in height dimension
            :param hits: number of hits left
        """
        brick = bricks.Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def draw_text(self, x, y, text, size='40'):
        font = ('Helvetica', size)
        return self.canvas.create_text(x, y, text=text, font=font)

    def update_lives_text(self):
        text = 'Lives: %s' % self.lives
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, str(15))
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def start_game(self):
        pass


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Hello, Pong!')
    game = Game(root)
    game.mainloop()
