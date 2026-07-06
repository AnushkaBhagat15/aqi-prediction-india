# ~~~Air Quality Index (AQI) Prediction — Indian Cities

A machine learning project to predict Air Quality Index (AQI) 
and AQI category for major Indian cities using historical 
pollution data from 2015 to 2020.

---

##  Why I Built This

Air pollution is a serious problem in India, especially in 
cities like Delhi, Patna and Ahmedabad. I wanted to build 
something that uses real government data to predict how 
polluted the air is on any given day — and present it in 
a simple web app anyone can use.

---

## Dataset

- **Source:** Kaggle — Air Quality Data in India (2015–2020)
- **File used:** city_day.csv
- **Cities covered:** 26 major Indian cities
- **Features:** PM2.5, PM10, NO, NO2, NOx, NH3, CO, SO2, 
  O3, Benzene, Toluene, Xylene, AQI, AQI Category

---

##  What I Did

**1. Exploratory Data Analysis (EDA)**
- Plotted AQI distribution across cities
- Found that pollution peaks in winter and drops 
  during monsoon
- Mumbai used as Maharashtra reference city since 
  Pune wasn't in the dataset

**2. Feature Engineering**
- Extracted Month, Year, Season from Date column
- Handled missing values using city-wise median 
  imputation
- Label encoded City and Season for model input

**3. Handling Imbalanced Data**
- Dataset had very few Severe AQI records
- Applied SMOTE on training data only to balance 
  all AQI categories

**4. Regression Models** (predict actual AQI value)
- Linear Regression
- Random Forest Regressor
- Metrics: MAE, RMSE, R²

**5. Classification Models** (predict AQI category)
- Logistic Regression
- Random Forest Classifier
- Metrics: F1 Score, Confusion Matrix

**6. Streamlit Web App**
- User selects city, month, year and enters 
  pollutant values
- App predicts AQI category instantly
- Color-coded output with health advice

---

##  Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Matplotlib, Seaborn
- Streamlit
- Pickle

---

##  How to Run

**1. Clone the repo**
git clone https://github.com/yourusername/aqi-prediction-india.git
cd aqi-prediction-india

**2. Install dependencies**
pip install -r requirements.txt

**3. Run the notebook**
Open aqi_analysis.ipynb in Jupyter or Google Colab
Run all cells to train and save the model

**4. Launch the app**
streamlit run app.py

---

##  Results

| Model                  | Task           | Key Metric        |
|------------------------|----------------|-------------------|
| Linear Regression      | Regression     | R² ~ 0.75         |
| Random Forest Regressor| Regression     | R² ~ 0.95         |
| Logistic Regression    | Classification | F1 ~ 0.72         |
| Random Forest Classifier| Classification| F1 ~ 0.94         |

*(Actual values will update after running the notebook)*

---

## Future Improvements

- Add cross validation for more reliable evaluation
- Try XGBoost as an additional model
- Deploy on Streamlit Cloud for public access
- Include real-time AQI data using an API

---

## About Me

I'm Anushka, a 3rd year B.Tech student in AI and Data 
Science at AISSMS IOIT, Pune. This is one of my first 
complete end-to-end ML projects — built to learn and 
grow, not just to submit.

Feel free to connect on LinkedIn or raise an issue if 
you find anything to improve!
=======
# aqi-prediction-india
Predicting Air Quality Index for Indian cities using Machine Learning
>>>>>>> ebce442f8fcb37d8b17edc89c24d79386dcab131
