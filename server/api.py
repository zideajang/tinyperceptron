import os

from typing import List

import glob
import yaml
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Form
from fastapi import HTTPException
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有方法
    allow_headers=["*"],  # 允许所有头
)

@app.get("/configs")
async def get_configs():
    folders = glob.glob("./configs/**")
    config_name_list = [os.path.basename(folder) for folder in folders if folder != "_base_"]
    return {
        "data":config_name_list
    }

@app.get("/config/{name}")
async def get_config(name:str):
    config_file = Path(f"./configs/{name}/metafile.yml")
    if not config_file.is_file():
        raise HTTPException(status_code=404, detail="Config file not found")
    try:
        with open(config_file, "r") as file:
            config_data = yaml.safe_load(file)
    except yaml.YAMLError as e:
        raise HTTPException(status_code=500, detail="Error reading YAML file")

    return  {
        "data":config_data
    }

@app.get("/api")
async def hello():
    return {
        "data":"hello world"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5600)