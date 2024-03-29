# diapasons
simple library for working with data that can be represented as a set of points on a straight line.
# Installing
```commandline
pip install diapasons
```
# Usage
Here is some examples, how you can use this module
### Create some diapason objects
```python
from diapasons import Diapason

first_diapason = Diapason([1, 2, 3])
second_diapason = Diapason([3, 4, 5])
print(first_diapason.points) # [1, 2, 3]
print(second_diapason.points) # [3, 4, 5]
```
Now you can imagine them as segments on a straight line
### You can easily see length each of objects
```python
from diapasons import Diapason

first_diapason = Diapason([1, 2, 3])

first_diapason.length # 2
len(first_diapason) # 2
```
### diapason can have only one point

```python
from diapasons import Diapason

point_diapason = Diapason([1])
point_diapason.is_point  # True
line_diapason = Diapason([5, 16, 9.6])
line_diapason.is_point # False
```
### You can add points to diapason
```python
from diapasons import Diapason

my_diapason = Diapason([1, 4])
my_diapason.points # [1, 4]
my_diapason.add_point(9)
my_diapason.points # [1, 4, 9]
my_diapason.add_points([3, 5])
my_diapason.points # [1, 3, 4, 5, 9]
```
Point can be only integer or float!
### Each Diapason have start_point, end_point
```python
from diapasons import Diapason

my_diapason = Diapason([1, 4, 8])
my_diapason.start_point # 1
my_diapason.end_point # 8
```
### Operations with diapasons
add diapasons to each other
```python
from diapasons import Diapason

my_diapason = Diapason([1, 2.6]) + Diapason([5, 6])
print(my_diapason.points) # [1, 2.6, 5, 6]
```
move diapason on straight line
```python
from diapasons import Diapason

my_diapason = Diapason([1, 2.6])
my_diapason.move(2)
print(my_diapason.points) # [2, 3.6]
my_diapason.move(-3)
print(my_diapason.points) # [-1, 0.6]
```
split by point
```python
from diapasons import Diapason

my_diapason = Diapason([1, 2.6])
left_d, right_d = my_diapason.split_by_point(2)
left_d.points # [1, 2]
right_d.points # [2, 2.6]
```
split by another diapason
```python
from diapasons import Diapason

my_diapason = Diapason([1, 10])
spliter = Diapason([3, 6])
left_diapason, right_diapason = my_diapason.split_by_diapason(spliter)
left_diapason.points # [1, 3]
right_diapason.points # [6, 10]
```
find common diapason
```python
from diapasons import Diapason

my_diapason = Diapason([1, 10])
another_diapason = Diapason([3, 15])
common = my_diapason.common(another_diapason)
print(common.points) # [3, 10]
```
find different
```python
from diapasons import Diapason

my_diapason = Diapason([1, 10])
another_diapason = Diapason([3, 15])
left_d, right_d = my_diapason.different(another_diapason)
print(left_d.points) # [1, 3]
print(right_d.points) # [10, 15]
```
find distance between diapasons
```python
from diapasons import Diapason

my_diapason = Diapason([1, 10])
another_diapason = Diapason([20, 25, 30])
distance = my_diapason.distance(another_diapason)
print(distance) # 10
```
### Diapason comparisons
diapason touch another, when they have at least one common point
```python
from diapasons import Diapason

my_diapason = Diapason([1, 10])
another_diapason = Diapason([10, 45])
my_diapason.touch(another_diapason) # True
```
diapason intersects another when they have more than one common point
```python
from diapasons import Diapason

my_diapason = Diapason([1, 10])
another_diapason = Diapason([5, 45])
my_diapason.intersects(another_diapason) # True
```
diapason contains another when all the points of one are "on the body" of the other
```python
from diapasons import Diapason

my_diapason = Diapason([1, 10])
another_diapason = Diapason([2, 4, 5])
print(another_diapason in my_diapason) # True
```
diapason equal another when equal they start and end points
```python
from diapasons import Diapason

my_diapason = Diapason([1, 10])
another_diapason = Diapason([1, 4, 5, 10])
print(another_diapason == my_diapason) # True
```
diapason crosses another then they touch each other in one point
```python
from diapasons import Diapason

my_diapason = Diapason([1, 10])
another_diapason = Diapason([10, 15, 30])
print(another_diapason.crosses(my_diapason)) # True
```
diapason overlaps another when
```python
from diapasons import Diapason

my_diapason = Diapason([1, 10])
another_diapason = Diapason([2, 4, 5])
print(my_diapason.overlaps(another_diapason)) # True
```
