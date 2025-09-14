import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Unemployment_in_India.csv')
data.columns = data.columns.str.strip()

data['Date'] = pd.to_datetime(data['Date'], dayfirst=True, errors='coerce')
print("Date conversion done:", data['Date'].head())

monthly_trends = data.groupby(data['Date'].dt.to_period('M'))['Estimated Unemployment Rate (%)'].mean()
print("Monthly trends calculated:", monthly_trends.head())

# Graph ke liye clear settings
plt.figure(figsize=(10, 6))  # Graph size set karo
monthly_trends.plot(title="Monthly Unemployment Rate Trends", xlabel="Month", ylabel="Unemployment Rate (%)")
plt.show()
plt.savefig('unemployment_trends.png')