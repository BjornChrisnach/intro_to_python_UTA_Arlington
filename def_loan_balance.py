def remain_loan_balance(principal, annual_interest_rate, duration, number_of_payments):
    interest_rate = annual_interest_rate / 100 / 12
    amount_payments = duration * 12

    if interest_rate == 0:
        result = principal * 1 - (number_of_payments / amount_payments)
    else:
        result = principal * (((1+interest_rate)**amount_payments) - ((1+interest_rate) **
                              number_of_payments)) / (((1+interest_rate)**amount_payments) - 1)

    return result

# for testing purposes
# print(remain_loan_balance(1000.0, 4.5, 5, 12))

# or
#
# def _calculate_balance(principal, interest_rate_per_year, duration, number_of_payments):
#     if interest_rate_per_year==0:
#         return principal-number_of_payments*(principal/(duration*12.0) )
#     r=interest_rate_per_year/100/12.0
#     n=duration*12
#     balance=principal*((1.0+r)**n - (1.0+r)**number_of_payments) / (((1.0+r)**n)-1)
#     return balance
