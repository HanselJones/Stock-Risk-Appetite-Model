# Stock Investment Recommendation System

This repository contains a machine learning-based stock recommendation system developed to provide personalized stock suggestions based on a customer's risk appetite. The project uses historical data from Yahoo.finance, clusters stocks into risk categories, and presents recommendations for low, medium, and high-risk portfolios. This project is built using Python, Jupyter notebooks, and Flask for backend development.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Data Processing](#data-processing)
- [Data Visualization](#data-visuzalization)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Future Enhancements](#future-enhancements)


## Project Overview

The goal of this project is to build a recommendation system for stock investments that categorizes stocks based on historical data and provides insights into stock risk levels. The project leverages KMeans clustering to group stocks into risk categories and Flask to build a web-based application for user interaction.

The system provides:
1. **Categorization of stocks** based on risk levels.
2. **Personalized recommendations** tailored to a user's risk tolerance.
3. **Data-driven insights** on stock performance to build investor confidence.

### Key Questions Addressed

1. How to categorize stocks by risk level?
2. How to personalize recommendations to each user’s risk profile?
3. How to evaluate the success of recommendations in terms of user satisfaction and portfolio performance?

## Features

- **Data Processing and Feature Engineering**: Calculate technical indicators (e.g., Moving Averages, RSI, Volatility) to aid in stock categorization.
- **Clustering for Risk Segmentation**: Use KMeans clustering to assign risk levels to stocks.
- **Flask API**: Provides endpoints to serve stock recommendations based on user input.
- **Recommendation Metrics**: Measure success through customer satisfaction, portfolio performance, and retention.

## Data Processing

The project processes Yahoo.finance stock data, calculating various features for stock analysis, including:

- **Technical Indicators**:
  - Simple Moving Average (SMA)
  - Exponential Moving Average (EMA)
  - Volatility
  - Relative Strength Index (RSI)
  - Bollinger Bands
  - Lag Features: Extract features such as opening, high, low, and closing prices with 1 to 3-day lags for trend analysis.
 
## Data Visualization
In this project we used tableau to perform visualizations apart from those found in the code(EDA part). Below is the link to our dashboard.
'https://public.tableau.com/views/Book1_17313034867730/Sheet5?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link'


## Usage

1. **Installation**:
    - Clone the repository.
    - Install the required packages with `pip install -r requirements.txt`.

2. **Run the Application**:
    - Start the Flask application using: python app.py
    - Access the web interface at `     `.

3. **Notebook Analysis**:
    - Open `stockprice.ipynb` to explore data processing and model training.

## Technologies Used

- **Python**: For data processing and model development
- **Jupyter Notebook**: For interactive data analysis
- **Flask**: Backend framework for API services
- **KMeans Clustering**: For stock categorization
- **Yahoo Finance API**: To retrieve stock data
- **Pandas, Numpy, Scikit-learn**: Data manipulation and model building

## Future Enhancements

- **Incorporate Sentiment Analysis**: Analyze market sentiment to refine recommendations.
- **Time Series predictions**: Predict stock prices based on historical trends
- **User Authentication**: Secure recommendations and user data access.



