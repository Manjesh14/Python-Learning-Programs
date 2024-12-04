#Write a recursive function to print all elements in a list.

list1=[1,2,3,4,5]

def elements(lists,index=0):
    if index == len(lists):
        return
    print(lists[index],end=' ')
    elements(lists,index+1)

elements(list1)