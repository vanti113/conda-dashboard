import pandas as pd

daily_df = pd.read_csv("data/daily_report.csv")

totals_df = daily_df[["Confirmed", "Deaths", "Recovered"]
                     ].sum().reset_index(name="Count")
totals_df = totals_df.rename(columns={"index": "conditions"})

countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()

print(countries_df)
