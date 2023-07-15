l=[10,35,30,45,50,60,33,81,91,100]
even_list=[]
odd_list=[]

for i in l:
    if i%2==0:
        even_list+=[i]
    else:
        odd_list+=[i]
print(even_list)
print(odd_list)