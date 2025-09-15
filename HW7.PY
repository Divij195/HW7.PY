print("Enter the full date: in dd/Month/yyyy")
Date = int(input("dd:"))
typedMonth = str(input("Month:"))
Year = int(input("yyyy: "))
while not int(Year) in range(0,3000):
    Year = int(input("Please enter year (yyyy) limited to [0 - 3000] : "))

if typedMonth in ['January']:
    Month = 3
    while int(Year) % 4 == 0:
        Month = 2
elif typedMonth in ['February']:
    Month = 6
    while int(Year) % 4 == 0:
        Month = 5
elif typedMonth in ['March', 'November']:
    Month = 6
elif typedMonth in ['April', 'July']:
    Month = 2
elif typedMonth in ['May']:
    Month = 4
elif typedMonth in ['August']:
    Month = 5
elif typedMonth in ['September', 'December']:
    Month = 1
elif typedMonth in ['October']:
    Month = 3
elif typedMonth in ['June']:
    Month = 0
else:
    Month = 0

remYear = Year%400

if 300 <= remYear <= 400:
    Year = Year + 1
elif 200 <= remYear <= 300:
    Year = Year + 3
elif 100 <= remYear <= 200:
    Year = Year + 5
else:
    Year = Year + 0

print(remYear)

Day = (Date + int(Month) + remYear) % 7
print(Day)

