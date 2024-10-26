money_capital = 20000
salary = 5000
spend = 6000
increase = 0.05

months = 0
i = money_capital

while i >= 0:
  months += 1
  i += salary
  spend *= (1 + increase)
  i -= spend

print("Количество месяцев, которое можно протянуть без долгов:", months)

