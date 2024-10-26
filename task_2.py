salary = 5000
spend = 6000
months = 10
increase = 0.03

total_spend = 0
for month in range(months):
    total_spend += spend * (1 + increase)**month

money_capital = total_spend - months * salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: {int(money_capital)}")

