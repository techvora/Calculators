Amount = float(input(" Enter Your Principal -> "))
Rate = float(input(" Enter Percentage of Interest -> "))
Month = int(input("Enter the number of Month -> "))
Months = ["jan", "feb", "march", "apr", "may", "june", "july", "aug", "sep", "oct", "nov", "dec"]
yourinterest = 0
for i in range(0,Month):
    month = Months[i]
    monthly_interest = Amount * Rate / 100
    Amount += monthly_interest
    yourinterest += monthly_interest

    print(f'Your {month} Interest is -> {monthly_interest} & your {month} Currunt Principal is -> {Amount}')
print(f'YOUR MAIN PRINCIPLE IS {Amount} AND YOUR TOTAL INTEREST IS {yourinterest}')
