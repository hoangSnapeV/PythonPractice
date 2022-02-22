names = ["Duong", "Mai", "Hoa", "Dao"]
amounts = [109000, 60000, 10000, 1200000]
def min_max_avg(names, amounts):
    smallest = amounts[0]
    largest = amounts[0]
    avg = 0
    for index1 in range(len(names)):
        name = names[index1]
        amount = amounts[index1]
        print("Ten la: ", name, " Money:", amount)
        
        # largest = amount bị sai đoạn này :v
        if largest < amount:
            largest = amount
        print("largest =",largest)

        if smallest > amount:
            smallest = amount
            print("small= ", smallest)

        print("smallest =", smallest)
    
        avg = (avg + amount) / len(names)


    print("money average =", avg)

    ad = amounts.index(largest)
    asd = amounts.index(smallest)
    print("giau nhat", names[ad])
    print("ngheo nhat", names[asd])
#Check_MoneySuppoter_Cach1
def CheckVersion1(moneySup, money, names, amounts):
    if moneySup in names and money in amounts:
        return True
    else:    
        return False
 #Check_MoneySuppoter_cach2
def CheckVersion2(moneySup, money, names, amounts):
    for i in range(len(names)):
        if moneySup == names[i] and money == amounts[i]:
            return True
    return False

min_max_avg(names, amounts)

#2
print("--------")
names1 =["Vu", "Hang", "Mai"]
amounts1 = [50000, 100000,200000]
min_max_avg(names1, amounts1)

#check1
check1 = CheckVersion1('Yen', 200000, names, amounts)
print(check1)
#Check2
check2 = CheckVersion1('Duong', 109000, names, amounts)
print("check2 = ",check2)




