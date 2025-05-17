print("Welcome to the Currency Converter!")
print("Available currencies: USD, EUR, NGN, GBP")

from_currency = input("Enter the currency you are converting FROM: ").upper()
to_currency = input("Enter the currency you are converting TO: ").upper()
amount = float(input("Enter the amount to convert: "))
exchange_rates = {
    ("USD", "NGN"): 1400,
    ("EUR", "NGN"): 1500,
    ("GBP", "NGN"): 1600,
    ("NGN", "USD"): 0.00071,
    ("NGN", "EUR"): 0.00066,
    ("NGN", "GBP"): 0.00062,
    ("USD", "EUR"): 0.92,
    ("EUR", "USD"): 1.08,
    ("USD", "GBP"): 0.78,
    ("GBP", "USD"): 1.28
}
if (from_currency, to_currency) in exchange_rates:
    rate = exchange_rates[(from_currency, to_currency)]
    converted_amount = amount * rate
    print(f"{amount} {from_currency} is equal to {converted_amount} {to_currency}")
else:
    print("Sorry, this currency conversion is not supported.")
