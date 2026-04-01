import pandas as pd

def build_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    # filling missing values
    df['Courier_Experience_yrs'] = df['Courier_Experience_yrs'].fillna(
        df['Courier_Experience_yrs'].median()
    )
    df['Weather'] = df['Weather'].fillna('Unknown')
    df['Traffic_Level'] = df['Traffic_Level'].fillna('Unknown')
    df['Time_of_Day'] = df['Time_of_Day'].fillna('Unknown')
    df['Vehicle_Type'] = df['Vehicle_Type'].fillna('Unknown')

    # feature engineering
    df["distance_experience"] = df["Distance_km"] / (df["Courier_Experience_yrs"] + 1)
    

    df["distance_prep_interaction"] = df["Distance_km"] + df["Preparation_Time_min"]

    

    df["is_peak_hour"] = df["Time_of_Day"].isin(["Evening", "Night"]).astype(int)
    vehicle_speed = {
    "Bike": 1.2,
    "Scooter": 1.0,
    "Bicycle": 0.7
    }

    df["vehicle_speed_factor"] = df["Vehicle_Type"].map(vehicle_speed)
    df['vehicle_speed_factor'] = df['vehicle_speed_factor'].fillna(1.0)

    df["distance_vehicle"] = df["Distance_km"] / df["vehicle_speed_factor"]
    df = df.drop(columns=['Order_ID'], errors='ignore')
    return df