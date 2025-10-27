print("This is your \n Saving Account Interest Calculator")
repeat=True
checker=0
years_Target=0
monthly_Var=0
DEPOSIT=float(input("Enter Deposit: "))
monthly_DEPOSIT=DEPOSIT
MONTHLY=float(input("Enter Monthly Deposit: "))
if MONTHLY==0:
    repeat=False
YEARS=float(input("Enter How Many Years in Savings Account: "))
INTEREST=(float(input("Enter Amount of Interest for Bank: ")))/100
TARGET_AMOUNT=float(input("Enter Target Amount of Money: "))
INFLATION=0.02
if repeat:
    for i in range(int(YEARS)*12):
        FUTURE_VALUE+=(monthly_DEPOSIT*(1+INTEREST)**YEARS)/12
        monthly_VAR+=1
        if MONTHLY==monthly_VAR: 
            monthly_DEPOSIT+=DEPOSIT
            monthly_VAR=0
    REAL_VALUE=FUTURE_VALUE/((1+INFLATION))**YEARS    
else:
    FUTURE_VALUE = DEPOSIT*(1+INTEREST)**YEARS
    REAL_VALUE = FUTURE_VALUE/((1+INFLATION))**YEARS 
    
#while(checker<TARGET_AMOUNT){
 #   checker+=
#}
print(REAL_VALUE)
