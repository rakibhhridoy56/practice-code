from random import choice

class RandomWalk:
    def __init__(self,num_points =5000):
        self.num_points = num_points

        self.x = [0]
        self.y = [0]
    
    def fill_walk(self):
        while len(self.x) < self.num_points:
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance
            
            y_direction= choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance
            
            if x_step == 0 and y_step == 0:
                continue
                
#xf is for x final value

            xf = self.x[-1] + x_step
            yf = self.y [-1] + y_step
            
            self.x.append(xf)
            self.y.append(yf)
     
    
    

class Dice:
    '''A Class Representing A Individual Dice
    '''
    def __init__(self, num_sides_are = 6):
        self.num_sides_are = num_sides_are
        
    def num_having_in_the_dice():
        return randint(1,num_sides_are)

    
    