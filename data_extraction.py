from pathlib import Path
import pandas as pd

class AirQualityData:
    def __init__(self, path: str) -> None:
        self.data_frame = pd.read_csv(Path(path))
        self.__iterator = self.data_frame.iterrows()

        
    def get_data(self):
        # Dictionary used to store process data that will be sent
        process_data = dict()
        
        # Get csv next line raw data
        raw_data = next(self.__iterator)[1].to_dict()
        
        # Iterates over the raw data eliminating all unnecessary white space. 
        # Change the AQI value type from Str to Int. (For empty strings, the defined value is -1)
        for key, item in raw_data.items():
            if key == "date":
                process_data[key.lstrip()] = item    
            else:
                try:
                    process_item = int(item.lstrip())
                except ValueError:
                    if not item.lstrip():
                        process_item = -1
                
                process_data[key.lstrip()] = process_item
        return process_data
