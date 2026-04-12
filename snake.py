# this class represent the snake it has different methods .


class Snake:
    def __init__(self):
        self.reset() # reset the snake to its initial state, basically it is reusing the logics.

    def reset(self):
        self.body = [(5, 5)] # initial position of the snake head, the body will grow as snake eat.
        self.direction = (1, 0) # initial direction .
        self.grow_flag = False  # tells about whether snake should grown or not.

    def move(self): 
        head_x, head_y = self.body[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy) 

        self.body.insert(0, new_head) # adding the new head to the body list 

        if not self.grow_flag:
            self.body.pop()
        else:
            self.grow_flag = False

    def grow(self): # when it eats food.
        self.grow_flag = True

    def change_direction(self, new_direction):
        dx, dy = self.direction
        ndx, ndy = new_direction

        if (dx + ndx, dy + ndy) != (0, 0):
            self.direction = new_direction

    def check_self_collision(self): 
        return self.body[0] in self.body[1:] # if that list contains means there is collision .