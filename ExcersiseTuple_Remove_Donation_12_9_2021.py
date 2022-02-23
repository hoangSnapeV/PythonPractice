#version 1 event
def remove_event(list1):
    list_even = []
    for i in range(len(list1)):
        num1 = list1[i]
        if num1 % 2 == 1:
            list_even.append(num1)
    
    print("Range of even =", list_even)
# version 2 
def remove_event_1(list_2):

    for i in range(len(list_2) -1, -1, -1):
        num1 = list_2[i]
        if num1 % 2 == 0:
            list_2.remove(num1) # remove nên dùng lùi
        
    print("Range of even_1 =", list_2) 

#list1
list1 = [1, 2, 5, 7 , 10, 12]
remove_event(list1)
#list_2_1
list_2 = [0, 3, 5, 4, 6, 1, 10, 8]
remove_event_1(list_2)

#------------
# find_donator

def find_donator(name, donate_list):
    total = 0
    for i in range(len(donate_list)):
        name1 = donate_list[i][0] 
        money = donate_list[i][1] 

        #print("money =", money)
        #print("name", name1)
        if  name1 == name:
            total += money
    return total


#find_donator("Vu", donate_list)
donate_list = [("Duong", 109090), ("Huy", 1097), ("Vu", 98000), ("Duong", 80090), ("Vu", 698000)]
result = find_donator("Vu", donate_list)
print("total =", result)



