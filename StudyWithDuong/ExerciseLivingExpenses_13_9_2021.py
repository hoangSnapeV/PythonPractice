
# PaymentOfLivingExpenses of myself
def PaymentOfLivingExpenses(totalAmount, bills):
    sum_bill = 0
    for i in range(len(bills)):
        money = bills[i][1]
        sum_bill += money
    print("sum_bill= ", sum_bill)
    remainDebt = totalAmount - sum_bill

    if totalAmount > sum_bill:        
        print("Money leftover of month = ", remainDebt)
        print("enough to pay:", True)
        
    else:
        print("Debt of 1 month = ", remainDebt * -1)
        print("Enough to pay:", False)
        
#bill 1
bills = [("Electric", 200000), ("Water", 60000), ("Food", 120000), ("Entertainment", 300000)]
PaymentOfLivingExpenses(1500000, bills)
#bill 2
bills_1 = [("Necessity", 1500000), ("risk provisions", 1000000), ("Save", 500000), ("Hobby", 300000)]
PaymentOfLivingExpenses(4000000, bills_1)
