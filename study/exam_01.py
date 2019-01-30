class Circle:
    pi = 3.14
    def __init__(self, r, x=0, y=0):
        self.r = r
        self.x = x
        self.y = y

    def area(self):
        return self.r **2 *  Circle.pi
    def circumference(self):
        return 2* self.r * Circle.pi
    def center(self):
        return self.x, self.y
    def move(self, x, y):
        self.x = x
        self.y = y
        print(f'{x}, {y}로 이동되었습니다.')
        return self.center()    

