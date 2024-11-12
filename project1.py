import random,turtle,time
colors=["blue","red","green","yellow","black","pink"]
t1=time.time()
class Fractal:
    def __init__(self,sides,lenght,repetition):
        self.sides=sides
        self.lenght=lenght
        self.repetition=repetition
    def shape(self):
        t=turtle.Pen()
        for i in range (self.repetition):
            color=random.choice(colors)
            t.left(25)
            t.speed(0)
            for a in range (self.sides):
                t.pencolor(color)
                t.fd(self.lenght)
                t.left(360/self.sides)


s=Fractal(8,120,40)
s.shape()                
t2=time.time()
print("performance time is : ",t2-t1)

