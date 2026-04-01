import pandas as pd
import joblib
import sys, os
sys.path.append(os.path.abspath("."))
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error

from src.pipeline.training_pipeline import create_pipeline


def main():
   
    df = pd.read_csv("/Users/prachyasumandas/Documents/delivery_time_prediction/data/raw/Food_Delivery_Times.csv")

    
    X = df.drop(columns=['Delivery_Time_min'])
    y = df['Delivery_Time_min']

    
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    
    num_cols = [
        'Distance_km', 'Preparation_Time_min',
        'Courier_Experience_yrs', 'distance_experience', 
        'distance_prep_interaction',
        'is_peak_hour',
        'vehicle_speed_factor', 'distance_vehicle'
    ]

    cat_cols = [
        'Weather',
        'Traffic_Level',
        'Time_of_Day',
        'Vehicle_Type'
    ]

   
    pipeline = create_pipeline(num_cols, cat_cols)

    
    pipeline.fit(X_train, y_train)

    
    preds = pipeline.predict(X_test)

    print("R2 Score:", r2_score(y_test, preds))
    print("MAE:", mean_absolute_error(y_test, preds))

    
    joblib.dump(pipeline, "artifacts/model.pkl")
    print("Model saved successfully!")


if __name__ == "__main__":
    main()