'''
Name: Gurusaran Sathish
Project: Input, Output, Processing
Extra: Was able to format my text without use of fstrings. 
'''
#Prints the string in center of 60 space field
print("|{:^60}|".format(":This is your Saving Account Interest Calculator:"))
repeat = True
#variables are calculated here
checker = 0
month_to_Target = 0
monthly_VAR = 0
# Input is all gathered as float)
DEPOSIT = float(input("Enter Deposit: "))
MONTHLY = float(input("How Often Deposited in Months, else 0: "))
if MONTHLY == 0:
    repeat = False
YEARS = float(input("Enter How Many Years in Savings Account: "))
INTEREST = (
    float(input("Enter Amount of Interest for Bank (e.g. 2 for 2%): ")))/100
TARGET_AMOUNT = float(input("Enter Target Amount of Money: "))
INFLATION = 0.02
FUTURE_VALUE = 0
REAL_VALUE = 0
if repeat: #Checks if they deposit monthly and perform calculations accordingly
    FUTURE_VALUE += DEPOSIT
    for i in range(int(YEARS)*12):
        if MONTHLY == monthly_VAR:
            FUTURE_VALUE += DEPOSIT
            monthly_VAR = 0
        FUTURE_VALUE = FUTURE_VALUE*(1+INTEREST/12)
        monthly_VAR += 1

    REAL_VALUE = FUTURE_VALUE/((1+INFLATION/12)**(YEARS*12))
else: 
    FUTURE_VALUE = DEPOSIT*(1+INTEREST)**YEARS
    REAL_VALUE = FUTURE_VALUE/(1+INFLATION)**YEARS
checker += REAL_VALUE
while (checker < TARGET_AMOUNT): #Adapted version of prev calculation to help calculate how long to reach target
    if MONTHLY == monthly_VAR:
        checker += DEPOSIT
        monthly_VAR = 0
    checker = checker*(1+INTEREST/12)
    monthly_VAR += 1
    month_to_Target += 1
print(f" The future value would be: ${FUTURE_VALUE:.2f}")
print(f" The real, purchasing power, would be: ${REAL_VALUE:.2f}")
print(
    f" It would take you another {int(month_to_Target)} months or {month_to_Target/12} years to reach your target amount of ${TARGET_AMOUNT:.2f} (Adujusted for Inflation).")
