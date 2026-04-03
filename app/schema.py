from pydantic import BaseModel,Field
from typing import Annotated,Literal

class DeliveryInput(BaseModel):
    Distance_km: Annotated[float, Field(gt=0,lt=50,title='distance from point to destination')]
    Weather: Annotated[Literal["Clear", "Foggy", "Rainy", "Snowy", "Windy"],Field(title= 'weather of the day')]
    Traffic_Level: Annotated[Literal["Low", "Medium", "High"],Field(title='traffic')]
    Time_of_Day: Annotated[Literal["Morning", "Afternoon", "Evening", "Night"],Field(title='time of the day')]='Evening'
    Vehicle_Type: Annotated[Literal["Bike","Scooter", "Car"],Field(title='vehicle type')]='Bike'
    Preparation_Time_min: Annotated[float,Field(gt=0,lt=200,title='preparation time')]=20
    Courier_Experience_yrs: Annotated[float,Field(gt= 0,lt = 50,title='experience')]=2