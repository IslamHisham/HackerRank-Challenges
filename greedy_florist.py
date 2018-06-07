Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l=['1']
>>> k=3*l
>>> k
['1', '1', '1']
>>> k=3*int(l)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    k=3*int(l)
TypeError: int() argument must be a string or a number, not 'list'
>>> l=[1]
>>> k=3*l
>>> k
[1, 1, 1]
>>> 
======================== RESTART: C:/Python27/test.py ========================
10

Traceback (most recent call last):
  File "C:/Python27/test.py", line 5, in <module>
    n,k=map(int,raw_input().strip().split())#k refers to then umber of customers,n is number of flowers needed
ValueError: need more than 1 value to unpack
>>> 
======================== RESTART: C:/Python27/test.py ========================
10 3
10 20 30 4 5 6 7 8 9 100

Traceback (most recent call last):
  File "C:/Python27/test.py", line 10, in <module>
    friends_share[0]=friends_share[0]+(n%k)
TypeError: 'int' object has no attribute '__getitem__'
>>> 
======================== RESTART: C:/Python27/test.py ========================
10 3
10 20 30 4 5 6 7 8 9 100
9
>>> 
======================== RESTART: C:/Python27/test.py ========================
10 3
10 20 30 4 5 6 7 8 9 100
[4, 3, 3]
>>> 
======================== RESTART: C:/Python27/test.py ========================
10 10
1 2 3 4 5 6 7 8 9 10
('answer is', 55)
55
>>> for iin range(4,-1,-1):
	
SyntaxError: invalid syntax
>>> for i in range(4,-1,-1):
	print (i)

	
4
3
2
1
0
>>> 
======================== RESTART: C:/Python27/test.py ========================
3 2
2 5 6
('friends share of flowers are:', [2, 1])

Traceback (most recent call last):
  File "C:/Python27/test.py", line 27, in <module>
    print(min_cost(n,k,base_costs))
  File "C:/Python27/test.py", line 17, in min_cost
    friend_costed=friend_costed+flower_cost(flower_num,base_cost[0])
NameError: global name 'base_cost' is not defined
>>> 
======================== RESTART: C:/Python27/test.py ========================
3 2
2 5 6
('friends share of flowers are:', [2, 1])

Traceback (most recent call last):
  File "C:/Python27/test.py", line 27, in <module>
    print(min_cost(n,k,base_costs))
  File "C:/Python27/test.py", line 18, in min_cost
    base_cost.remove(base_cost[0])
NameError: global name 'base_cost' is not defined
>>> 
======================== RESTART: C:/Python27/test.py ========================
3 2
2 5 6
('friends share of flowers are:', [2, 1])
('friends were costed:', [9, 6])
15
>>> 
======================== RESTART: C:/Python27/test.py ========================
5 2
2 10 50 55 90
('friends share of flowers are:', [3, 2])
('friends were costed:', [76, 200])
276
>>> 
