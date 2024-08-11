import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        
        for k,v in kwargs.items():
            self.contents += [k] * v

    def draw(self,nballs):
        if nballs >= len(self.contents):
            drawn_balls = self.contents.copy()  # Copy all balls
            self.contents = []  # Empty the hat
            return drawn_balls
        else:
            random_balls = random.sample(self.contents, nballs)
            for ball in random_balls:
                self.contents.remove(ball)
            return random_balls



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    M = 0

    for _ in range(num_experiments):

        hat_copy = copy.deepcopy(hat)
        draws = hat_copy.draw(num_balls_drawn)
        draw_count = {}
        for color in draws:
            if color in draw_count:
                draw_count[color] += 1
            else:
                draw_count[color] = 1
        success = True
        for color, count in expected_balls.items():
            if draw_count.get(color, 0) < count:
                success = False
                break
        
        if success:
            M += 1
    probability = M / num_experiments
    return probability
   

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)