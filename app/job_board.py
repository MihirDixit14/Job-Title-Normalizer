from typing import List, Dict

class JobBoard:
    def __init__(self):
        self.jobs: List[Dict] = []
    
    def load_jobs(self, jobs:List[Dict]):
        self.jobs=jobs

    def filter_by_normalized_title(self, normalized_title:str)->List[dict]:
        return [job for job in self.jobs if job.get('normalized_title')==normalized_title]
    
    def  get_all_normalized_title(self)->List[str]:
        return sorted({job['normalized_title'] for job in self.jobs if 'normalized_title' in job})

