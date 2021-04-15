# Write a function that calculates and returns the monthly payments
# for a loan. This function accepts three parameters in the exact order
# (principal, annual_interest_rate, duration):
def calculate_monthly_pay(principal, annual_interest_rate, duration):
    interest_rate = (annual_interest_rate / 100) / 12
    amount_payments = duration * 12

    if interest_rate == 0:
        result = principal / amount_payments
    else:
        result = principal * (interest_rate * (((1+interest_rate) **
                              amount_payments) / ((1+interest_rate)**amount_payments-1)))

    return result

# for testing purposes
# print(calculate_monthly_pay(10000.0, 20.0, 30))
# print(calculate_monthly_pay(1000.0, 4.5, 5))

# or
#
# def _calculate_payment(principle, interest_rate_per_year, duration):
    # if interest_rate_per_year==0:
    #     return principle/(duration*12)
    # r=interest_rate_per_year/100/12
    # n=duration*12
    # montly_payment=principle*(r*((1.0+r)**n))/(float((1.0+r)**n)-1.0)
    # return montly_payment
