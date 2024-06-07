from typing import Any
from pydantic import BaseModel,Field
import yaml
import requests

class ModelWrapperConfig(BaseModel):
    name:str
    endpoint:str

class OpenMMLabDetWrapper:

    def __init__(self,config:Any) -> None:
        
        self.config = config
        with open('./config.yaml',"r") as file:
            self.config = yaml.safe_load(file)
        
        self.url = f"{config.get('baseurl')}:{config.get('port')}"
        self.config.update(config)
    
    def setup(self):
        pass


    def detect(self,model_name:str,image_path:str,threshold:float):
        """
        TODO: upload image, select model_name:List[]
        """

        with open(image_path, 'rb') as file:
            files = {'file': file}

            data = {
                'model_name': model_name,
                'threshold': threshold
            }
            response = requests.post(self.url + "/api/detect", files=files, data=data)
            if response.status_code == 200:
                return response.json()
            else:
                response.raise_for_status()
    # def pred_batch(self,model_name:str,image_path):
    #     pass