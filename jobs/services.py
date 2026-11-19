from typing import List, Optional, Dict
from jobs.models import JobListing, Application

class JobBoardService:
    def __init__(self):
        self._jobs: Dict[int, JobListing] = {}
        self._applications: List[Application] = []
        self._job_counter = 1
        self._app_counter = 1

    def post_job(self, title: str, company: str, location: str, desc: str, salary: str) -> JobListing:
        job = JobListing(
            id=self._job_counter,
            title=title,
            company=company,
            location=location,
            description=desc,
            salary_range=salary
        )
        self._jobs[job.id] = job
        self._job_counter += 1
        return job

    def list_jobs(self, active_only: bool = True) -> List[JobListing]:
        jobs = list(self._jobs.values())
        if active_only:
            return [j for j in jobs if j.is_active]
        return jobs

    def apply_to_job(self, job_id: int, name: str, email: str, resume_url: str) -> Optional[Application]:
        if job_id not in self._jobs or not self._jobs[job_id].is_active:
            return None
        app = Application(
            id=self._app_counter,
            job_id=job_id,
            candidate_name=name,
            candidate_email=email,
            resume_url=resume_url
        )
        self._applications.append(app)
        self._app_counter += 1
        return app

    def get_applications_for_job(self, job_id: int) -> List[Application]:
        return [a for a in self._applications if a.job_id == job_id]
