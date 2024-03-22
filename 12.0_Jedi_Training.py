'''
# 12.0 Jedi Training (10 pts)  Name:________________
 
Update the code in this chapter to do the following:
Open a 500px by 500px window.
Change the Ball class to a Box class.
Instantiate two 30px by 30px boxes. One red and one blue.
Make the blue box have a speed of 240 pixels/second
Make the red box have a speed of 180 pixels/second
Control the blue box with the arrow keys.
Control the red box with the WASD keys.
Do not let the boxes go off of the screen.
Incorporate different sounds when either box hits the edge of the screen.
Have two people play this TAG game at the same time.
The red box is always "it" and needs to try to catch the blue box.
When you're done demonstrate to your instructor!


Starter Testing Code:
'''
import arcade
SW = 500
SH = 500
SPEED_RED = 3
SPEED_BLUE = 4

class Box_Blue:
    def __init__(self, pos_x, pos_y, dx, dy, width, height, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height
        self.col = col
        self.laser_sound = arcade.load_sound('laser.wav')
        self.explosion_sound = arcade.load_sound('explosion.wav')

    def draw_Box_Blue(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.col)

    def update_Box_Blue(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        #stop at edge of screen
        if self.pos_x < self.width / 2:
            self.pos_x = self.width / 2
            arcade.play_sound(self.laser_sound, .5)
            self.dx = 0
        if self.pos_x > SW - self.width / 2:
            self.pos_x = SW - self.width / 2
            arcade.play_sound(self.laser_sound, .5)
            self.dx = 0

        if self.pos_y < self.height / 2:
            self.pos_y = self.height / 2
            arcade.play_sound(self.laser_sound, .5)
            self.dy = 0
        if self.pos_y > SH - self.height / 2:
            self.pos_y = SH - self.height / 2
            arcade.play_sound(self.laser_sound, .5)
            self.dy = 0

class Box_Red:
    def __init__(self, pos_x, pos_y, dx, dy, width, height, col):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height
        self.col = col
        self.laser_sound = arcade.load_sound('laser.wav')
        self.explosion_sound = arcade.load_sound('explosion.wav')

    def draw_Box_Red(self):
        arcade.draw_rectangle_filled(self.pos_x, self.pos_y, self.width, self.height, self.col)

    def update_Box_Red(self):
        self.pos_y += self.dy
        self.pos_x += self.dx

        #stop at edge of screen
        if self.pos_x < self.width / 2:
            self.pos_x = self.width / 2
            arcade.play_sound(self.explosion_sound, .5)
            self.dx = 0
        if self.pos_x > SW - self.width / 2:
            self.pos_x = SW - self.width / 2
            arcade.play_sound(self.explosion_sound, .5)
            self.dx = 0

        if self.pos_y < self.height / 2:
            self.pos_y = self.height / 2
            arcade.play_sound(self.explosion_sound, .5)
            self.dy = 0
        if self.pos_y > SH - self.height / 2:
            self.pos_y = SH - self.height / 2
            arcade.play_sound(self.explosion_sound, .5)
            self.dy = 0

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.ASH_GREY)
        self.set_mouse_visible(False)
        self.Box_Red = Box_Red(250, 250, 0, 0, 30, 30, arcade.color.AUBURN)
        self.Box_Blue = Box_Blue(250, 250, 0, 0, 30, 30, arcade.color.BLUE)
        #self.Box = Box(250, 250, 30, 30, arcade.color.AUBURN)

    def on_draw(self):
        arcade.start_render()
        self.Box_Red.draw_Box_Red()
        self.Box_Blue.draw_Box_Blue()

    #def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        #self.Box.pos_x = x
        #self.Box.pos_y = y

    #def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        #if button==arcade.MOUSE_BUTTON_LEFT:
            #print("Left Mouse Button Pressed At ", x, y)
        #elif button==arcade.MOUSE_BUTTON_RIGHT:
            #print("Right Mouse Button Presses At ", x, y)

    def on_update(self, dt):
        self.Box_Red.update_Box_Red()
        self.Box_Blue.update_Box_Blue()
        if self.Box_Red.pos_x >= self.Box_Blue.pos_x - 30 and self.Box_Red.pos_x <= self.Box_Blue.pos_x + 30 and self.Box_Red.pos_y >= self.Box_Blue.pos_y -30 and self.Box_Red.pos_y <= self.Box_Blue.pos_y + 30:
            arcade.set_background_color(arcade.color.RED)
        else:
            arcade.set_background_color(arcade.color.ASH_GREY)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.A:
            self.Box_Red.dx = -SPEED_RED
        elif key == arcade.key.W:
            self.Box_Red.dy = SPEED_RED
        elif key == arcade.key.S:
            self.Box_Red.dy = -SPEED_RED
        elif key == arcade.key.D:
            self.Box_Red.dx = SPEED_RED
        elif key == arcade.key.LEFT:
            self.Box_Blue.dx = -SPEED_BLUE
        elif key == arcade.key.UP:
            self.Box_Blue.dy = SPEED_BLUE
        elif key == arcade.key.DOWN:
            self.Box_Blue.dy = -SPEED_BLUE
        elif key == arcade.key.RIGHT:
            self.Box_Blue.dx = SPEED_BLUE


    def on_key_release(self, key, modifiers):
        if key == arcade.key.S or key == arcade.key.W:
            self.Box_Red.dy = 0
        elif key == arcade.key.A or key == arcade.key.D:
            self.Box_Red.dx = 0
        elif key == arcade.key.DOWN or key == arcade.key.UP:
            self.Box_Blue.dy = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.Box_Blue.dx = 0
def main():
    window = MyGame(SW, SH, "User Control Practice")
    arcade.run()

if __name__=="__main__":
    main()
