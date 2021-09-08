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


min_max_avg(names, amounts)

#2
print("--------")
names1 =["Vu", "Hang", "Mai"]
amounts1 = [50000, 100000,200000]
min_max_avg(names1, amounts1)

