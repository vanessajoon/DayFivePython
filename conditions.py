#LOGICAL OPERATORS
# And statement
# To check whether a customer is eligible for a loan using the and statement
hasHighIncome = False
hasGoodIncome = True

if hasHighIncome == True and hasGoodIncome == True:
    print('Eligible for the loan')
else:
    print('I am sorry, you are not eligible for the loan')

# Or Statement
# To check whether a customer is eligible for a loan using the or statement
hasHighIncome = False
hasGoodCredit = True
if hasHighIncome == True or hasGoodCredit == True:
    print('You are eligible for the loan')
else:
    print('I am sorry, you are not eligible for this loan')

# Not statement changes your answer from true to false
hasGoodCredit = True
hasCriminaRecord = True

if hasGoodCredit and not hasCriminaRecord:
    print('Eligible for Loan')
else:
    print('You are not eligible for this loan')
