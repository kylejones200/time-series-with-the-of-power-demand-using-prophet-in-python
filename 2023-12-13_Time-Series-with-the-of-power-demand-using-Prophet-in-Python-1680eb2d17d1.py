# Description: Short example for Time Series with the of power demand using Prophet in Python.

import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objs as go
import seaborn as sns
from data_io import read_csv
from prophet import Prophet

df = read_csv("data/Native_Load_2021.csv")
df["date"] = pd.to_datetime(df["date"])
df["ERCOT"].plot()

df1 = df[["date", "ERCOT"]]
df1.columns = ["ds", "y"]
m = Prophet()
m.fit(df1)
future = m.make_future_dataframe(periods=90, freq="D")
fcst = m.predict(future)
fig = m.plot(fcst)

forecast = m.predict(future)
forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]].tail()


def timeseries(df, x, yhat, lower, upper, actual, title_name, save=False):

    fig = go.Figure(
        [
            go.Scatter(
                name="Measurement",
                x=df[x],
                y=df["yhat"],
                mode="lines",
                line={"color": "rgb(31, 119, 180)"},
                showlegend=False,
            ),
            go.Scatter(
                name="Upper Bound",
                x=df[x],
                y=df[upper],
                mode="lines",
                marker={"color": "#444"},
                line={"width": 0},
                showlegend=False,
            ),
            go.Scatter(
                name="Lower Bound",
                x=df[x],
                y=df[lower],
                marker={"color": "#444"},
                line={"width": 0},
                mode="lines",
                fillcolor="rgba(68, 68, 68, 0.3)",
                fill="tonexty",
                showlegend=False,
            ),
        ]
    )
    fig.update_layout(yaxis_title="Production Rate", title=f"{title_name}", hovermode="x")
    fig.add_trace(
        go.Scatter(
            x=actual["ds"],
            y=actual["y"],
            mode="lines+markers",
            name="Actual values",
            showlegend=False,
        )
    )
    fig.show()
    if save:
        fig.write_html(f"{title_name}.html")


timeseries(
    forecast,
    "ds",
    "yhat",
    "yhat_lower",
    "yhat_upper",
    actual=df1,
    title_name="Ercot",
    save=True,
)

df["ERCOT"].plot(style=".", figsize=(15, 5), title="ERCOT")
plt.show()


def create_features(df, label=None):
    """
    Creates time series features from datetime index.
    """
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["hour"] = df["date"].dt.hour
    df["dayofweek"] = df["date"].dt.dayofweek
    df["quarter"] = df["date"].dt.quarter
    df["month"] = df["date"].dt.month
    df["year"] = df["date"].dt.year
    df["dayofyear"] = df["date"].dt.dayofyear
    df["dayofmonth"] = df["date"].dt.day
    df["weekofyear"] = df["date"].dt.isocalendar().week
    X = df[
        [
            "hour",
            "dayofweek",
            "quarter",
            "month",
            "year",
            "dayofyear",
            "dayofmonth",
            "weekofyear",
        ]
    ]
    if label:
        y = df[label]
        return X, y
    return X


X, y = create_features(df, label="ERCOT")

features_and_target = pd.concat([X, y], axis=1)

features_and_target.head()

sns.pairplot(
    features_and_target.dropna(),
    hue="ERCOT",
    x_vars=["hour", "dayofweek", "year", "weekofyear"],
    y_vars="ERCOT",
    height=5,
    plot_kws={"alpha": 0.15, "linewidth": 0},
)
plt.suptitle("Power Use MW by Hour, Day of Week, Year and Week of Year")
plt.show()

split_date = "01-Feb-2021"
ercot = df[["date", "ERCOT"]]
ercot.set_index("date", inplace=True)
ercot_train = ercot.loc[ercot.index <= split_date].copy()
ercot_test = ercot.loc[ercot.index > split_date].copy()

ercot_test.rename(columns={"ERCOT": "TEST SET"}).join(
    ercot_train.rename(columns={"ERCOT": "TRAINING SET"}), how="outer"
).plot(figsize=(15, 5), title="Ercot demand", style=".")

ercot_train.reset_index().rename(columns={"date": "ds", "ERCOT": "y"}).head()

model = Prophet()
model.fit(ercot_train.reset_index().rename(columns={"date": "ds", "ERCOT": "y"}))

ercot_test_fcst = model.predict(df=ercot_test.reset_index().rename(columns={"date": "ds"}))

# Plot the forecast
f, ax = plt.subplots(1)
f.set_figheight(5)
f.set_figwidth(15)
fig = model.plot(pjme_test_fcst, ax=ax)
plt.show()

# Plot the components of the model
fig = model.plot_components(ercot_test_fcst)

f, ax = plt.subplots(1)
f.set_figheight(5)
f.set_figwidth(15)
ax.scatter(pjme_test.index, ercot_test, color="r")
fig = model.plot(ercot_test_fcst, ax=ax)
