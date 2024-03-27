
import arcade
import random
SW = 640
SH = 480
SPEED = 10

class Stars:
    def __init__(self, pos_x, pos_y, dx, dy, rad, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.rad = rad
        self.col = col

    def draw_Stars(self):
        arcade.draw_circle_filled(self.pos_x, self.pos_y, self.rad, self.col)

    def update_Stars(self):
        self.pos_x += self.dx
        self.pos_y += self.dy

        if self.pos_y < -3:
            self.pos_y = 490

class Ship:
    def __init__(self, pos_x, pos_y, dx, dy):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy



    def draw_Ship(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, 10, 40, arcade.color.YELLOW)
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, 30, 30, arcade.color.ORANGE)
        arcade.draw_arc_filled(self.pos_x, self.pos_y, 50, 50, arcade.color.GREEN, 0, 180, 180)

    def update_Ship(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        #loop at edge of screen
        if self.pos_x > 650 + 25:
            self.pos_x = -8
        if self.pos_x < -10 - 25:
            self.pos_x = SW + 8

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.set_mouse_visible(False)
        self.Ship = Ship(320, 50, 0, 0)
        self.star_list = []
        for i in range(300):
            star = Stars(random.randint(0, 640), random.randint(0, 490), 0, -1, random.randint(1, 3), arcade.color.WHITE)
            self.star_list.append(star)

    def on_draw(self):
        arcade.start_render()
        self.Ship.draw_Ship()
        for star in self.star_list:
            star.draw_Stars()

    def on_update(self, dt):
        self.Ship.update_Ship()
        for star in self.star_list:
            star.update_Stars()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.Ship.dx = -SPEED
        elif key == arcade.key.RIGHT:
            self.Ship.dx = SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.Ship.dx = 0
def main():
    window = MyGame(SW, SH, "CSP SPACE INVADERS!")
    arcade.run()

if __name__=="__main__":
    main()
