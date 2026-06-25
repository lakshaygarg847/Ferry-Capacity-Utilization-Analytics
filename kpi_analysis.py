import pandas as pd

df = pd.read_csv("data/Toronto Island Ferry Tickets.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df["Total Activity Load"] = (
    df["Sales Count"] +
    df["Redemption Count"]
)

# Capacity Utilization Ratio

max_load = df["Total Activity Load"].max()

avg_load = df["Total Activity Load"].mean()

capacity_utilization_ratio = (
    avg_load / max_load
) * 100

print("\n===== Capacity Utilization Ratio =====")
print(round(capacity_utilization_ratio,2), "%")