#  Real Estate Price Prediction

This project uses machine learning to predict real estate property prices based on features such as location, number of bedrooms, area, and more. The goal is to provide accurate price estimates using regression models and deploy the application using Streamlit.

##  Project Overview

- **Task:** Regression (predicting continuous property prices)
- **Tech Stack:** Python, Pandas, Scikit-Learn, Streamlit
- **ML Models Used:** Linear Regression, Ridge Regression, XGBoost
- **Deployment:** Streamlit Cloud

##  Features

- Train and evaluate multiple regression models.
- Visualize feature relationships and predictions.
- Upload your own dataset or use the default sample.
- Compare model performance using RMSE, MAE, and R².

##  Project Structure

```

real\_estate\_price\_prediction/
├── app.py              # Main Streamlit app
├── model.py            # ML model training and prediction logic
├── data/
│   └── real\_estate.csv # Default dataset
├── models/
│   └── trained\_model.pkl  # Saved ML model
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation

````

##  Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/real_estate_price_prediction.git
   cd real_estate_price_prediction
````

2. **Create a virtual environment (optional but recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Streamlit app**

   ```bash
   streamlit run app.py
   ```

##  Dataset

* Source: Custom CSV file (`data/real_estate.csv`)
* Sample features:

  * `Area`
  * `Bedrooms`
  * `Bathrooms`
  * `Location`
  * `Parking`
  * `Price` (target)

##  Model Performance

| Model             | R² Score | RMSE  | MAE  |
| ----------------- | -------- | ----- | ---- |
| Linear Regression | 0.81     | 13420 | 9850 |
| Ridge Regression  | 0.82     | 13100 | 9700 |
| XGBoost Regressor | 0.88     | 11350 | 8450 |

 *Note: Values may vary depending on dataset split and preprocessing.*

##  Deployment

* The project is deployed using **Streamlit Cloud**.
* Users can interact with the model via a user-friendly web interface.

##  Future Improvements

* Add more features (e.g., neighborhood crime rate, school ratings)
* Hyperparameter tuning
* Model versioning with MLflow
* Add map-based visualizations for properties

##  Acknowledgments

* This project was developed as part of the CST2216 course at Algonquin College.

##  Contact

**Author:** Alireza Mohseni
**https://github.com/AliReza0015-ux/real-estate-price-prediction
