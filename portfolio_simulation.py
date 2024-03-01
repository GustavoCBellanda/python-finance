monhthly_contributions = [1500, 3000, 15000, 20000, 30000, 30000]
years = [2, 2, 5, 5, 10, 5]
fees = [0.10, 0.12, 0.14, 0.15, 0.15, 0.15]
portfolio_value = 0
for contribution, year, fee in zip(monhthly_contributions, years, fees):
    for month in range(year * 12):
        portfolio_value += contribution + (portfolio_value * (fee / 12.0))
print(f"Total years: {sum(years)}")
print(
    f"R$ {portfolio_value:,.2f}".replace(",", "_")
    .replace(".", ",")
    .replace("_", ".")
)
