# M Hemasri - AIE22028
# ML Lab 1 programs
# Amrita School of Engineering, Bengaluru
#Program to find the common elements of two lists



def common_member(a, b):
    a_set = set(a)
    b_set = set(b)

    #check for common elements
    if (a_set & b_set):
        return(a_set & b_set)
    else:
        return("No common elements") 
          
len_list1=int(input("Enter the length of the list 1: "))
list1=[]
for i in range(0, len_list1):
    ele = int(input())
    list1.append(ele)



len_list2=int(input("Enter the length of the list 2: "))
list2=[]
for i in range(0, len_list2):
    ele = int(input())
    list2.append(ele)

result=common_member(list1,list2)
print(result)
