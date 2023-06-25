from pydantic import BaseModel

class WeatherParam(BaseModel):
    temp_gfs: float
    temp_gem: float
    temp_access: float
