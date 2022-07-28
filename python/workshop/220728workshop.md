1. 도형 만들기 

   아래의 명세를 읽고 Python 클래스를 활용하여 점(Point)과 사각형(Rectangle)을 표현하시오.

   예를 들어, 좌표 (4, 3)의 점은 아래와 같이 표현할 수 있다

   ```python
   p1 = Point(4, 3)

​		코드를 실행했을때 아래와 같이 출력되어야 한다.

```python
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area()) #4
print(r1.get_perimeter())#8
print(r1.is_square())#True
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())#9
print(r2.get_perimeter())#12
print(r2.is_square())#True


class Point:
	
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:

    def __init__(self,p1,p2):
        self.garo = p2.x-p1.x
        self.sero = p1.y-p2.y
    def get_area(self):
        return int(self.garo*self.sero)

    def get_perimeter(self):
        return int(self.garo*2+self.sero*2)

    def is_square(self):
        return self.garo == self.sero

p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectangle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())
p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectangle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())
```