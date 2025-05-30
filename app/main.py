from fastapi import FastAPI, UploadFile, File
import pandas as pd
from typing import List, Dict
import numpy as np

app = FastAPI(title="Simple Job Board")


def normalize_title(title: str) -> str:
    return title.strip().lower().replace("sr.", "senior").replace("jr.", "junior")

@app.post("/upload-jobs")
async def upload_jobs(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file, encoding="utf-8")
    except UnicodeDecodeError:
        file.file.seek(0)
        df = pd.read_csv(file.file, encoding="latin1")
    required_columns = {"title", "description", "company"}
    if not required_columns.issubset(df.columns):
        return {"error": f"CSV must contain columns: {', '.join(required_columns)}"}
    df['normalized_title'] = df['title'].apply(normalize_title)
    # Fix for NaN, inf, -inf
    df = df.replace([np.inf, -np.inf], '').fillna('')
    jobs = df[["title", "description", "company", "normalized_title"]].to_dict(orient="records")
    return {"jobs": jobs}