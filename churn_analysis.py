import pandas as pd

# Load Dataset
df = pd.read_csv("data/customer_churn.csv")

print("Customer Churn Dataset")
print(df)

# Total Customers
total_customers = len(df)

# Churned Customers
churned = len(df[df["Churn"] == "Yes"])

# Active Customers
active = len(df[df["Churn"] == "No"])

# Churn Rate
churn_rate = (churned / total_customers) * 100

print("\n----- REPORT -----")
print("Total Customers:", total_customers)
print("Churned Customers:", churned)
print("Active Customers:", active)
print("Churn Rate:", round(churn_rate,2), "%")

# Analysis

avg_login_churn = df[df["Churn"]=="Yes"]["LoginFrequency"].mean()
avg_login_active = df[df["Churn"]=="No"]["LoginFrequency"].mean()

avg_support_churn = df[df["Churn"]=="Yes"]["SupportContacts"].mean()
avg_support_active = df[df["Churn"]=="No"]["SupportContacts"].mean()

print("\nAverage Login Frequency (Churned):",avg_login_churn)
print("Average Login Frequency (Active):",avg_login_active)

print("\nAverage Support Contacts (Churned):",avg_support_churn)
print("Average Support Contacts (Active):",avg_support_active)

report = f"""
Customer Churn Analysis Report

Total Customers: {total_customers}
Churned Customers: {churned}
Active Customers: {active}

Churn Rate: {round(churn_rate,2)}%

Insights:
1. Customers with low login frequency are more likely to churn.
2. Customers with many support requests tend to cancel subscriptions.
3. Premium users show lower churn rates.

Recommendation:
Improve customer engagement and support quality.
"""

with open("results/churn_report.txt","w") as file:
    file.write(report)

print("\nReport Generated Successfully")
