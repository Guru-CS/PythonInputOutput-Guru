'''
Name: Gurusaran Sathish
Project: Input, Output, Processing
Extra: Was able to format my text without use of fstrings. 
'''
# Prints the string in center of 60 space field
print("|{:^60}|".format(":This is your Saving Account Interest Calculator:"))
# variables are set here
repeat = True
checker = 0
month_to_Target = 0
print("*For Monthly Compounding*")
DEPOSIT = float(input("Enter Deposit: "))
MONTHLY = float(input("How Often Deposited in Months, else 0: "))
if MONTHLY == 0:
    repeat = False
YEARS = float(input("Enter How Many Years in Savings Account: "))
INTEREST = (
    float(input("Enter Amount of Interest for Bank (e.g. 2 for 2%): ")))/100
TARGET_AMOUNT = float(input("Enter Target Amount of Money: "))
INFLATION = 0.02
monthly_inflation = (1 + INFLATION) ** (1 / 12) - 1
FUTURE_VALUE = 0
REAL_VALUE = 0
AmtCompounded = 12
if repeat:  # Checks if they deposit monthly and perform calculations accordingly
    FUTURE_VALUE += DEPOSIT
    for i in range(int(YEARS)*AmtCompounded):
        if i % MONTHLY == 0 and i != 0:
            FUTURE_VALUE += DEPOSIT
        FUTURE_VALUE = FUTURE_VALUE*(1+INTEREST/AmtCompounded)
        REAL_VALUE = FUTURE_VALUE/(1+monthly_inflation)**(i+1)
else:
    FUTURE_VALUE += DEPOSIT
    for i in range(int(YEARS)*AmtCompounded):
        FUTURE_VALUE = FUTURE_VALUE*(1+INTEREST/AmtCompounded)
        REAL_VALUE = FUTURE_VALUE/(1+monthly_inflation)**(i+1)
checker += REAL_VALUE
# Adapted version of prev calculation to help calculate how long to reach target
while (checker < TARGET_AMOUNT):
    if month_to_Target % MONTHLY == 0 and repeat:
        checker += DEPOSIT
        monthly_VAR = 0
    checker = (checker*(1+INTEREST/AmtCompounded))/(1+monthly_inflation)
    month_to_Target += 1

print(f" The future value would be: ${FUTURE_VALUE:.2f}")
print(f" The real, purchasing power, would be: ${REAL_VALUE:.2f}")
print(f" It would take you another {int(month_to_Target)} months or {month_to_Target/12} years to reach your target amount of ${TARGET_AMOUNT:.2f} (Not Adujusted for Inflation).")
