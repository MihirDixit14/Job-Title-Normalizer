from fastapi import FastAPI
from pydantic import BaseModel
from .normalization import normalize_title

app=FastAPI(title="Job Title Normalizer API")

class TitleRequest(BaseModel):
    title:str

class TitleResponse(BaseModel):
    normalize_title:str
@app.post("/normalization-title",response_model=TitleResponse)
def normalize_title_endpoint(req: TitleRequest):
    normalized=normalize_title(req.title)
    return TitleResponse(normalize_title=normalized)




                                        