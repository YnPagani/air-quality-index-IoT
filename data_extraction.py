from pathlib import Path
import pandas as pd

class AirQualityData:
    def __init__(self, path: str) -> None:
        self.__data_frame = pd.read_csv(Path(path))
        self.__iterator = self.__data_frame.iterrows()

        
    def get_data(self):
        return next(self.__iterator)[1].to_dict()        
        