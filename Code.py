import csv
import plotly.express as px
import numpy as np

# def plotIceCream():
#     with open("Ice Cream Data.csv") as f:
#         IceCream_Data = csv.DictReader(f)
#         fig = px.scatter(IceCream_Data, x="Temperature", y="Ice-cream Sales")
#         fig.show()


def getDataSource(data_path):
    Result = []
    Attendance = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            Result.append(float(row["Marks In Percentage"]))
            Attendance.append(float(row["Days Present"]))

    return {"x": Result,
            "y": Attendance}


def findCorrelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0, 1])


def setup():
    data_path = "Projects\C106\data1.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)


setup()
