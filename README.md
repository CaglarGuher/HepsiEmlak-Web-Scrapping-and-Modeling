# House Prices in Ankara, Turkey

## Overview
This is a project to analyze house prices in Ankara, Turkey. The dataset used in this project contains information about houses for sale in Ankara from Hurriyet Emlak website. 

The aim of this project is to clean and preprocess the data, and then perform exploratory data analysis to gain insights into the relationship between house prices and various features such as location, size, and age.

## Dataset
The dataset used in this project can be found in `total_house_prices.csv`. It contains 33 columns and 33,329 rows. The columns are as follows:

 - City
 - District
 - Neighborhood
 - Ad no
 - Last Update Date
 - Number of Rooms + Living Room
 - Gross / Net Area (m²)
 - Floor Location
 - Building Age
 - Heating Type
 - Number of Floors
 - Eligibility for Credit
 - Furniture Condition
 - Number of Bathrooms
 - Usage Status
 - Exchange
 - Facing
 - Rent Status
 - Title Deed Status
 - Building Type
 - Building Condition
 - Dues
 - Rental Income
 - Fuel Type
 - Authorized Office
 - Within the Site
 - Deposit
 - Closed Area (m²)
 - Open Area (m²)
 - Number of Buildings
 - Island Number
 - Parcel Number

## Preprocessing
The following preprocessing steps were performed on the dataset:

- Removed columns that are not relevant for the analysis (Ad No, Last Update Date, Exchange, Facing, Title Deed Status, Building Type, Building Status, Dues, Rental Income, Fuel Type, Authorized Office, Within Site, Deposit, Indoor Area, Outdoor Area, Number of Buildings, Plot Number, Parcel Number).
- Removed rows with missing values.
- Renamed columns to more descriptive names.
- Grouped the `Floor Location` column into categories (`first floor`, `interstage`, `basement`, `top floor`).
- Converted the `Age` column to float values.
- Removed rows with the last six unique `Heat_type` values.
- Removed rows with the last five unique `Eligibility for Credit` values.
- Converted the `Price` column to float values.
- Converted the `Num_Of_Room` column to integer values.
- Removed `m2` from `Area` and converted it to integer values.

## Exploratory Data Analysis
The following insights were gained from the exploratory data analysis:

- The average house price in Ankara is 821,791 TL.
- The most expensive district is Çankaya, with an average house price of 1,541,084 TL.
- The most common heating type is Kombi, with 19,447 houses using this type of heating.
- The most common usage type is "Boş", meaning empty, with 11,658 houses having this type of usage.
- The most common credit eligibility is "Uygun", meaning eligible, with 23,550 houses having this eligibility.

# Phase 1 Modeling
# House Price Prediction Project

This part  aims to predict house prices in various neighborhoods and districts of a city. Phase 1  uses linear regression and XGBoost algorithms for the prediction.

## Data

The data used in this project is in the form of an Excel file, with the following columns:

- `Neighborhood`: Name of the neighborhood where the house is located.
- `District`: Name of the district where the house is located.
- `Price`: Price of the house in Turkish Lira.
- `Area`: Total area of the house in square meters.
- `Room`: Number of rooms in the house.
- `Bathroom`: Number of bathrooms in the house.
- `Age`: Age of the house in years.
- `Floor`: Floor number of the house.
- `Total Floor`: Total number of floors in the building.
- `Heating`: Type of heating in the house.
- `Furnished`: Whether the house is furnished or not.
- `Status`: Whether the house is new or old.
- `Fuel Type`: Fuel type for heating.

## Results

The R-squared scores for linear regression and XGBoost algorithms were calculated for each neighborhood and district with more than 200 data points.

### Neighborhoods

| Neighborhood        | R-squared Score |
|---------------------|----------------|
| Etlik               | 0.6342         |
| Ayvalı              | 0.3093         |
| Atapark             | 0.5765         |
| Harbiye             | 0.5516         |
| Durali Alıç         | 0.5060         |
| Merkez              | 0.8297         |
| İlkadım             | 0.5891         |
| Akşemsettin         | 0.7945         |
| General Zeki Doğan  | 0.4074         |

### Districts

![Districts](districts.png)

The R-squared scores for each district were plotted on a scatterplot of the actual versus predicted prices. The scatterplot can be found in the file named `districts.png`.

## Dependencies

This project requires the following Python libraries:

- pandas
- numpy
- xgboost
- scikit-learn
- category_encoders
- matplotlib

To install these libraries, run the following command:

```bash
pip install pandas numpy xgboost scikit-learn category_encoders matplotlib
```


