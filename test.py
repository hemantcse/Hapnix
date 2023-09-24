# # from itertools import combinations
# # S = input()
# # S = S.split(' ')
# # k = int(S[1])
# # A = []
# # for i in S[0]:
# #     A.append(i.upper())
# # A.sort()
# # print(A)
# # B = []
# # for i in list(combinations(A,k)):
# #     a = ''
# #     for j in i:
# #         a = a + j
# #         B.append(a)

# # for i in list(set(B)):
# #     print(i)



# from itertools import combinations
# S = input()
# S = S.split(' ')
# B = list(set(S[0]))
# k = int(S[1])
# A = []
# B = []
# for i in S[0]:
#     A.append(i.upper())
#     B.append(i.upper())
# A.sort()
# print(type(B))

# for i in range(2,k+1):
#     for i in list(combinations(A,i)):
#         a = ''
#         for j in i:
#             a = a + j
#             B.append(a)
# B = list(B)
# print(B)
# # if len(A)>=k:
# #     for i in A:
# #         print(i)
# # else:
# #     print(None)

# 

from collections import Counter
# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print(Counter(myList))
# print(Counter(myList).items())
# print(Counter(myList).keys())
# print(Counter(myList).values())


# from collections import Counter
# total_shoes_avalable = int(input())
# size_of_shoes = input()
# size_of_shoes = size_of_shoes.split(' ')
# size_available = []
# for i in size_of_shoes:
#     size_available.append(i)
# A = dict(Counter(size_available))
# cust_no = int(input())
# amount = 0
# for i in range(cust_no):
#     a = input()
#     a = a.split()
#     try:
#         A[a[0]] = A[a[0]] - 1
#         if A[a[0]]>=0:
#             amount = amount + int(a[1])
#     except:
#         amount = amount + 0
# print(amount)

# from collections import defaultdict
# d = defaultdict(list)
# print(d)
# d['python'].append("awesome")
# d['something-else'].append("not relevant")
# d['python'].append("language")
# for i in d.items():
#     print(i)   


# from collections import defaultdict
# a = input()
# a = a.split(' ')
# n = int(a[0])
# m = int(a[1])
# A = []
# for i in range(n):
#     A.append(input())
# B = []
# for j in range(m):
#     B.append(input())
# for i in B:
#         index = [index for (index, item) in enumerate(A) if item == i]
#         try:
#             for j in index:
#                 print(j+1,end=' ')
#             a = A.index(i)
#             print()
#         except:
#             print("-1")

# from collections import namedtuple
# Point = namedtuple('Point','x,y')
# a = input()
# pt1 = Point(a)
# print(pt1)
# pt2 = Point(3,4)
# dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# print(dot_product)

# from collections import namedtuple
# Car = namedtuple('Car','Price Mileage Colour Class')
# xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# print(xyz)



# from collections import namedtuple
# #N = int(input())
# s = namedtuple('s',input().split())
# s1 = s(*input().split())

# import cmath
# a = complex(input())
# print(cmath.sqrt(a))
# print(cmath.polar(a))
# for i in cmath.polar(a):
#     print(i)
# print(cmath.phase(a))
# print(cmath.rect(a))

# import cmath
# import math
# a = int(input())
# b = int(input())
# z = b/2-a/2j
# p = math.degrees(cmath.phase(z))
# if p*10%5==0:
#     print(math.ceil(p),"\xb0",sep='')
# else:
#     p = round(p)
#     print(p,"\xb0",sep='')
# 
# n,m = map(int,input().split(' '))
# b = set(map(int,input().split(' ')))
# print(b)
# c = set(map(int,input().split(' ')))
# print
# d = set(map(int,input().split(' ')))
# print(len(b.intersection(c))-len(b.intersection(d)))

# n, m = map(int, input().split(' '))
# arr = list(map(int, input().split(' ')))
# A = set(map(int, input().split(' ')))
# B = set(map(int, input().split(' ')))

# happiness = 0
# for i in arr:
#     if i in A:
#         happiness += 1
#     elif i in B:
#         happiness -= 1
# print(happiness)

# from collections import namedtuple
# N = int(input())
# s = namedtuple('s',input().split())
# marks = 0                                                
# for i in range(N):
#     b = input().split()
#     a = s(*b)
#     marks += int(a.MARKS) 
# print(marks/N)




    

