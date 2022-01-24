import requests
import matplotlib.pyplot as plt

api_key = "XYZ"

company ="FB"
years = 2

balance_sheet = requests.get(f'https://financialmodelingprep.com/api/v3/balance-sheet-statement/{company}?limit={years}&apikey={api_key}')
balance_sheet = balance_sheet.json()
# print(balance_sheet[0].keys())

total_current_assets= balance_sheet[0]['totalCurrentAssets']
print(f"Total Current Assets of {company}: {total_current_assets:,}")

total_current_liabilities= balance_sheet[0]['totalCurrentLiabilities']
print(f"Total Current Liabilities of {company}: {total_current_liabilities:,}")

total_debt = balance_sheet[0]['totalDebt']
cash_and_equivalents = balance_sheet[0]['cashAndCashEquivalents']
cash_debt_difference = cash_and_equivalents - total_debt
print(f"Cash Debt Difference: {cash_debt_difference:,}")