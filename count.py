Amount = int(input("Enter the total amount of money - "))
note1 = Amount//100
note2 = (Amount%100)//50
note3 = ((Amount%100)%50)//10
print("notes of 100 ruppees : ",note1)
print("notes of 50 ruppees : ",note2)
print("notes of 10 ruppee : ",note3)
