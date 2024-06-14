from easynmt import EasyNMT
import pickle
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, Union, List
from fastapi import FastAPI, HTTPException, Query, Request

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


#**************************************************************************************#

@app.get("/")
def greet():
    return {"message": "bonjour Leo le lengendaire"}


def load():

    pickle_in = open("best_model.pkl","rb")
    model=pickle.load(pickle_in)
    
    return model


# Chargement du model

model = load()

##model= EasyNMT('opus-mt')

@app.get("/translate")
def translate_get(target_lang: str, text: List[str] = Query([]), source_lang: Optional[str] = None):
  
  return model.translate(text, target_lang=target_lang, source_lang=source_lang)

@app.post("/translate")
async def translate_post(request: Request):
    data = await request.json()
    return translate_get(**data)
