#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[11]:


# #  E:5 по математике  (Про последовательность)

# import numpy as np

# x_1 = 1
# n = 2
# X = [1]
# def get_x(x_1, n):
#     x_2 = round(((n/(n-1))**2)*x_1, 0)
#     #x_2 = int(((n/(n-1))**2)*x_1)
    
#     print(int((n/(n-1))**2),  round(n/(n-1)**2, 0), 'del')
    
#     X.append(x_2)
#     return x_2, n+1

# for i in range(10):
#     x_1, n = get_x(x_1,n)


# X = np.array(X)
# print(X)
# X = 1/X
# print(round(np.sum(X)*1000,0))

# int(1.999)


# In[ ]:





# In[ ]:





# In[ ]:





# # A

# In[12]:



# in_str = input().split()
# price, size, loss, curr = (int(i) for i in in_str)


# # print(price,size,loss,curr)

# def cor(x):
#     if x<0: return 0
#     else: return x
    
# # if curr < size:
# # 	print(price)
# # 	exit()

# print(price + cor(curr - size) * loss)


# # B

# In[13]:


# N = int(input())
# pies = [N]


# def cut(pie):
#     if pie%2==0:return pie//2, pie//2
#     elif pie==1: return 1, 0
#     else:return pie//2, pie//2 +1

# def replace_pie(pies):
#     new_pies = []#[0]*(len(pies)*2)
#     for pie in pies:
#         if pie!=1:
#             a, b = cut(pie)
#             new_pies.append(a), new_pies.append(b)
#         else: new_pies.append(pie)
            
#     return new_pies

# cuts = 0
# while len(pies)!=N:
#     pies = replace_pie(pies)
#     cuts+=1
#     #print(pies,cuts)
# print(cuts)


# # C

# In[14]:


# def count_clients(from_,to):
# 	counter = 0
# 	last = 0
# 	for i in range(from_,to):
# 		# print(i, house[i])
# 		if house[i] > 0:
# 			counter +=1
# 			last = house[i]
# 	return counter, last


# in_str = input().split()
# n,t = (int(i) for i in in_str) # floors, time


# in_str = input().split()
# floors = [int(i) for i in in_str]
# client = int(input())

# client_floor = floors[client-1]
# # print(client_floor)

# house = l = [0]*floors[n-1]

# last_floor = floors[len(floors)-1]

# ind = 0;
# for i,h in enumerate(house):
# 	if i == floors[ind]:
# 		house[i-1] = floors[ind]
# 		ind +=1


# point1 = client_floor - t
# point2 = client_floor + t
# if point1 < 0:
# 	# cacl from 1 floor
# 	print(last_floor - 1)
# 	exit()


# c1,l1 = count_clients(point1, client_floor)
# c2,l2 = count_clients(client_floor,point2)

# print(client_floor, c1,l1, c2,l2 )
# if c1 > c2:
# 	print( last_floor + l1 -2 )
# else:
# 	print(last_floor + l2 -2)
# 	# start from client -n 

# # if c1 + c2 == 0:
# 	# start from client floor



# # print('--


# In[15]:


# 6 4
# 1 2 3 6 8 25
# 5


# # D

# In[ ]:





# In[ ]:





# Переговорка и ее план имеют форму прямоугольника. Первая строка входного файла содержит два вещественных числа: координаты 
# X и Y переговорки (1≤X≤1000,1≤Y≤1000 ). 
# 
# Координаты углов переговорки равны (0,0), (X,0), (X,Y), (0,Y).Во второй строке файла даются восемь вещественных чисел, описывающих положение углов плана переговорки. Сначала вводятся координаты того угла плана, который соответствует углу переговорки с координатами (0,0), затем — (X,0), (X,Y), наконец, (0,Y). Гарантируется, что входные данные корректны, то есть план является прямоугольником, линейные размеры которого соответствуют размерам переговорки, а также он не выходит за границы перегородки.
# 
# Все числа во входном файле вещественные, заданы с точностью 5 знаков после десятичной точки. План выполнен в масштабе не менее 0.0001 и строго менее 1.
# 
# 10 5
# 3.0 2.5 1.0 2.5 1.0 1.5 3.0 1.5
# 
# 2.5000 2.0833

# In[29]:


# #in_str = input().split()
# x, y = 10, 5 #float(in_str[0]), float(in_str[1])

# in_str = [3.0, 2.5, 1.0, 2.5, 1.0, 1.5, 3.0, 1.5] #input().split()

# X = in_str[0::2]
# Y = in_str[1::2]

# #print(x,y)
# #print(in_str)
# x_min = min(X)
# y_min = min(Y)
# x_max = max(X)
# y_max = max(Y)




# x = x_min + (x_max - x_min)/2
# y = y_min + (y_max - y_min)/2
# print(x, y)


# In[ ]:





# In[ ]:





# In[ ]:





# ## E

# In[9]:


# N = int(input())
# L = []
# for i in range(N): L.append(int(input()))

# diners =L

# costs = []
# diner_num = 0



# def skip_list(L, new_L = []):
#     for i in L:
#         if i>100: new_L.append(-i)
#         else: new_L.append(i)
#     return new_L
# def bask_skip_list(L, new_L = []):
#     for i in L:
#         if i<0: new_L.append(abs(i))
#         else: new_L.append(i)
#     return new_L

# def argmax(L): return L.index(max(L))

# def conca(A,B,x):
#     A[x+1:]=B
#     return A

# def reduce_cost(diners):
#     out = argmax(diners)
#     dinner = diners.copy()
#     dinner[out] = 0
#     return dinner

# def skip_reduce_cost(diners):
#     skip_dinner = skip_list(diners)
#     out = argmax(skip_dinner)
#     skip_dinner[out] = 0
#     skip_dinner = bask_skip_list(skip_dinner)
#     return skip_dinner  
 
# def prob(diners, diner_num,whe):
#     if diner_num + 1< N:
#         diner = diners[diner_num]
#         if diner > 100:
#             sub_diners = diners[diner_num+1:].copy()
#             red_sub_diners = reduce_cost(sub_diners) 
#             din = conca(diners, red_sub_diners, diner_num)
#             costs.append(sum(din))
#             prob(din, diner_num+1,'red')
#             skip_red_sub_diners = skip_reduce_cost(sub_diners)
#             din = conca(diners, skip_red_sub_diners, diner_num)
#             costs.append(sum(din))
#             prob(din, diner_num+1,'skip')

#         else:
#             costs.append(sum(diners))
#             prob(diners, diner_num+1,'0')
            
#     return 0        
    
# prob(diners, diner_num,'0')   
# print(min(costs))



# # test1 =  np.array([35, 40, 101, 59, 63, 0, 99, 99])
# # test2 =  np.array([35, 40, 101, 59, 63, 101, 0, 0]) ###
# # test3 =  np.array([35, 40, 101, 59, 0, 101, 0, 99])

# # np.sum(test1),np.sum(test2),np.sum(test3)


# In[31]:


in_str = input().split()
x, y = int(in_str[0]), int(in_str[1])

print(x+y)


# In[ ]:




