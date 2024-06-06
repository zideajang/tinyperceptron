import requests
import yaml
with open('./config.yaml',"r") as file:
    config = yaml.safe_load(file)
    print(type(config))

url = f"{config.get('baseurl')}:{config.get('port')}"

def get_hello():
        
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}


def get_configs():
        
    response = requests.get(url + "/configs")
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}

res = get_configs()
print(res)

def get_config(config_name):
    print(f"{url}/config/{config_name}")
    response = requests.get( f"{url}/config/{config_name}")
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data"}

res = get_config("vfnet")
print(type(res))