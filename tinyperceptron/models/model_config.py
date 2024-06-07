from typing import Any

from pydantic import BaseModel,BaseConfig,AnyHttpUrl
from pydantic import ConfigDict

class ModelConfig(BaseModel):
    model_config = ConfigDict(extra='ignore')
    end_point:AnyHttpUrl
    type:str
    name:str
    description:str
    paramerts:Any

class DefaultDetectionModelConfig(ModelConfig):
    pass

if __name__ == "__main__":
    pass