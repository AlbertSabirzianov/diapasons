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
first_diapason.points # [1, 2, 3]
second_diapason.points # [3, 4, 5]
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
###

