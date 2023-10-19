# Water-Quality-Prediction

This repository contains an analysis of a dataset related to water quality. The dataset includes various water quality metrics for 3276 different water bodies. The analysis involves exploring, cleaning, and visualizing the data to gain insights into the quality of water and its potability for human consumption.

## Dataset Information

The dataset is provided in a CSV file named `water_potability.csv` and contains the following columns:

1. **pH Value:** pH is a measure of the acidity or alkalinity of water.
2. **Hardness:** Represents the water's capacity to precipitate soap due to calcium and magnesium salts.
3. **Solids (Total Dissolved Solids - TDS):** Indicates the mineral content in water.
4. **Chloramines:** A common disinfectant in public water systems.
5. **Sulfate:** Concentration of sulfate in the water.
6. **Conductivity:** Measures the ability of water to transmit an electric current.
7. **Organic Carbon:** Total Organic Carbon (TOC) in water.
8. **Trihalomethanes:** Chemicals found in water treated with chlorine.
9. **Turbidity:** A measure of solid matter in the suspended state.
10. **Potability:** Indicates whether the water is safe for human consumption (1 for Potable, 0 for Not Potable).

## Basic Operations

To get started with the dataset, you can load it into a pandas dataframe using the following code:

```python
import pandas as pd
df = pd.read_csv("filepath/water_potability.csv")
```

Here are some basic operations performed on the dataset:

- Printing the first and last 5 rows of the dataset.
- Checking the dataset's shape (3276 rows and 10 columns).
- Calculating statistical measures for the dataset.
- Detecting and handling missing values, including filling missing values for the 'ph', 'Sulfate', and 'Trihalomethanes' columns using median imputation.

## Exploratory Data Analysis

Exploratory data analysis (EDA) was conducted to gain insights into the water quality data. Some of the EDA tasks performed include:

- Visualization of missing values in a heatmap.
- Checking the distribution of the target variable 'Potability' (safe or unsafe water).
- Visualizing the relationship between different columns.
- Calculating the correlation between columns and visualizing it using a heatmap.
- Creating histograms to understand the distribution of various parameters.

## Conclusion

This analysis provides an overview of the water quality dataset, addressing missing data and conducting exploratory data analysis to understand the relationships between various water quality parameters and the potability of water. The dataset can be used for further analysis, modeling, and prediction of water potability based on the given parameters.

Feel free to explore the Jupyter Notebook `Water_Quality_Prediction.ipynb` provided in this repository for a more detailed analysis of the dataset.
