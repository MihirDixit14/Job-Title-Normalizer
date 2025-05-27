from fastapi import FastAPI
from pydantic import BaseModel
from .normalizer import normalize_title

app=FastAPI(title="Job Title Normalizer API")

class TitleRequest(BaseModel):
    title:str

class TitleResponse(BaseModel):
    normalized_title:str
@app.post("/normalize-title",response_model=TitleResponse)
def normalize_title_endpoint(req: TitleRequest):
    normalized=normalize_title(req.title)
    return TitleResponse(normalized_title=normalized)




                                        