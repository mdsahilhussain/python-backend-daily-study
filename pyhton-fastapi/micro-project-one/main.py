from fastapi import FastAPI, HTTPException
from enum import Enum

app = FastAPI()

class ModelName(str, Enum):
    gpt = 'gpt'
    bert = 'bert'
    llama = 'llama'

fake_models_db ={
    'gpt': {'versions':['3.5', '4.0'], 'provider':'OpenAI'},
    'bert': {'versions':['base', 'large'], 'provider':'Google'},
    'llama': {'versions':['1.0', '2.0'], 'provider':'Meta'}
}

@app.get('/models')
def get_models():
    return fake_models_db

@app.get('/models/{model_name}')
def get_model(model_name: ModelName):
    if model_name not in fake_models_db:
        raise HTTPException(status_code=404, detail='Model not found')
    return fake_models_db[model_name]

@app.get('/models/{model_name}/versions/{version}')
def get_model_version(model_name: ModelName, version: str):
    
    if model_name not in fake_models_db:
        raise HTTPException(status_code=404, detail='Model not found')
    
    model = fake_models_db[model_name]
    
    if version not in model['versions']:
        raise HTTPException(status_code=404, detail="Version not found")
    return {
        "model": model_name,
        "version": version,
        'provider':model['provider']
    }