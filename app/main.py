from fastapi import FastAPI, UploadFile, File, Query
from typing import List, Dict
import numpy as np
from .job_board import JobBoard
from .normalizer import normalize_title 
import pandas as pd

app = FastAPI(title="Simple Job Board")
job_board = JobBoard()

def normalize_title(title: str) -> str:
    return title.strip().lower().replace("sr.", "senior").replace("jr.", "junior")

@app.get("/job-titles")
async def list_normalized_titles():
    return {"normalized_titles": job_board.get_all_normalized_titles()}
@app.get("/jobs")
async def get_jobs_by_normalized_title(normalized_title: str = Query(..., description="Canonical job title.")):

    norm = normalize_title(normalized_title)
    return {"matching_jobs": job_board.filter_by_normalized_title(norm)}
@app.get("/search-jobs")
async def search_jobs(query: str = Query(..., description="Fuzzy, case-insensitive search for job roles")):

    return {"matches": job_board.fuzzy_search_titles(query)}
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
 
    df = df.replace([np.inf, -np.inf], '').fillna('')
    jobs = df[["title", "description", "company", "normalized_title"]].to_dict(orient="records")
    job_board.load_jobs(jobs)
    return {"jobs": jobs}



