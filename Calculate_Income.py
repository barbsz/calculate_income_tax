def calculate_tax(income):
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 0.10
    else:
        tax = 1000 + (income - 20000) * 0.20
    return tax


income = 45000
tax = calculate_tax(income)
print(f"For an income of ${income}, the tax is ${tax:.2f}")
