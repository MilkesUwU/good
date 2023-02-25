#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Задача№1
a=int(input())
b=int(input())

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a//b)
print(a%b)


# In[4]:


#задача№2
a=int(input())
b=int(input())
c=int(input())

d=((a+2)/(b+5))**4-0.001*c
print(d)


# In[6]:


#задача№3
a=input()

print('='*30)
print('\t Сообщение: ' + a)
print('='*30)


# In[11]:


#задача№4
a=('Лермантов,Есенин,Маяковский')
b=['Лермантов','Есенин','Маяковский']

print(a[2])
print(b[2])


# In[12]:


#задача№5
a=[11,12,67,13]
del(a[2])
print(a)
a.append(4)
print(a)


# In[16]:


a={'Китай':'Пекин','Россия':'Москва','Германия':'Берлин','овощь':'огурец','фрукты':'Бананы'}
del(a['фрукты'])
del(a['овощь'])
print(a)


# In[ ]:


a=int(input())
b=int(input())
if (a>b):
    print('А больше')
elif (a<b):
    print('Б большее')
else:
    print('Они ровны')


# In[17]:


a=int(input())
if (a==1):
    print('Понедельник')
elif (a==2):
    print('Вторник')
elif (a==3):
    print('Среда')
elif (a==4):
    print('Четверг')
elif(a==5):
    print('Пятница')
elif(a==6):
    print('Cуббота')
elif(a==7):
    print('Воскресение')
else:
    print('Ошибка день недели. Введите чисто от 1 до 7')


# In[ ]:


a=int(input())
print(int(a) +' киллометр это'+ str(a*1000)+ 'Метров')


# In[19]:


a=int(input())
b=int(input())

S=a*b
P=(a+b)*2
print(S)
print(P)


# In[21]:


a=input()
print(a.upper())


# In[ ]:




