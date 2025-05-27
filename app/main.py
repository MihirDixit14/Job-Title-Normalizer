from fastapi import FastAPI
from pydantic import BaseModel
from .normalization import normalize_title

app=FastAPI(title="Job Title Normalizer API")

class TitleRequest(BaseModel):
    title:str


                                        