import pandas as pd

df = pd.read_csv("data/Toronto Island Ferry Tickets.csv")

df["Timestamp"] = pd.to_datetime(df["Timestamp"])

df["Total Activity Load"] = (
    df["Sales Count"]
    +
    df["Redemption Count"]
)

# Create Hour column

df["Hour"] = df["Timestamp"].dt.hour

# Average activity by hour

hourly_activity = (
    df.groupby("Hour")["Total Activity Load"]
    .mean()
    .sort_values(ascending=False)
)

print("\n===== Peak Hours Analysis =====")
print(hourly_activity)

# Chart

import matplotlib.pyplot as plt

plt.figure(figsize=(12,5))

hourly_activity.sort_index().plot(kind="bar")

plt.title("Average Ferry Activity by Hour")

plt.xlabel("Hour of Day")

plt.ylabel("Average Activity Load")

plt.tight_layout()

plt.show()