import pandas as pd
import numpy as np
import plotly.express as px


data = pd.read_csv("insurance.csv")
pd.set_option('display.max_columns', None)

#Check data for null values and display null count per column
print(data.isnull().sum())

# Sort the data by children, this allows for easier analysis later on
data.sort_values(["children"], axis=0,ascending=[True], inplace=True)

# Show the data being utilized
print(data)

#Create and present a graph representing the age
# and insurance premium relationship
figureAge = px.scatter(data_frame = data, x="charges",y="age", size="age", 
                    trendline="ols", title = "Relationship Age and Insurance Premiums")
figureAge.show()

#Create and present a graph representing the bmi
# and insurance premium relationship
figureBmi = px.scatter(data_frame = data, x="charges",y="bmi", size="age",
                    trendline="ols", title = "Relationship Age and Insurance Premiums")
figureBmi.show()

#Create and present a box chart representing the children, smoker,
# and insurance premium relationship
figSmCh = px.box(data, x="smoker", y="charges", color="children")
figSmCh.show()

#Create and present a box chart representing the region
# and insurance premium relationship
figReg = px.box(data, x="region", y="charges")
figReg.show()


