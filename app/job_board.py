from typing import List, Dict

class JobBoard:
    def __init__(self):
        self.jobs: List[Dict] = []
    
    def load_jobs(self, jobs:List[Dict]):
        self.jobs=jobs

    def filter_by_normalized_title(self, normalized_title:str)->List[dict]:
        return [job for job in self.jobs if 'normalized_title' in job and job['normalized_title']==normalized_title]
    
    def fuzzy_search_titles(self, search_term: str) -> List[Dict]:

        search_term = search_term.strip().lower()
        return [
            {"title": job["title"], "company": job["company"]}
            for job in self.jobs
            if search_term in job.get("normalized_title", "").lower()
        ]

        
    def  get_all_normalized_titles(self)->List[str]:
        return sorted({job['normalized_title'] for job in self.jobs if 'normalized_title' in job})
    


