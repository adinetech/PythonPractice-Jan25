principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))
compound_frequency = int(input("Enter the number of times interest is compounded per year: "))

compound_interest = principal * (1 + rate / (100 * compound_frequency)) ** (compound_frequency * time) - principal

print("The compound interest is:", compound_interest)
