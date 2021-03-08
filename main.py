import pandas as pd

daily_df = pd.read_csv("data/daily_report.csv")

totals_df = daily_df[["Confirmed", "Deaths", "Recovered"]
                     ].sum().reset_index(name="Count")
totals_df = totals_df.rename(columns={"index": "conditions"})

countries_df = daily_df[["Country_Region", "Confirmed", "Deaths", "Recovered"]]
countries_df = countries_df.groupby("Country_Region").sum().reset_index()


#
conditions = ["confirmed", "deaths", "recovered"]


def make_country_df(condition, country):
    df = pd.read_csv(f"data/time_{condition}.csv")
    df = df.loc[df["Country/Region"] == country]
    df = df.drop(columns=["Province/State", "Country/Region", "Lat", "Long"])
    df = df.sum().reset_index().rename(columns={"index": "Date", 0: condition})
    return df


final_df = None

for condition in conditions:
    print(condition)
    if final_df is None:
        final_df = make_country_df(condition, "Korea, South")
    else:
        country_df = make_country_df(condition, "Korea, South")
        final_df = final_df.merge(country_df)


def make_global_df(condition):
    df = pd.read_csv(f"data/time_{condition}.csv")
    df = df.drop(['Province/State', 'Country/Region', 'Lat',
                  'Long'], axis=1).sum().reset_index(name=condition)
    df = df.rename(columns={"index": "Date"})
    return df


def make_global_total_df(conditions):
    final_df = None
    for condition in conditions:
        condition_df = make_global_df(condition)
    # result = pd.concat([result, condition_df], axis=1, join="outer")
        if final_df is None:
            final_df = condition_df
        else:
            # result = pd.concat([result, condition_df], ignore_index=True, sort=False)
            final_df = final_df.merge(condition_df)
    return final_df
