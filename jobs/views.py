from jobs.services import JobBoardService

service = JobBoardService()

def handle_create_job(payload: dict):
    required = ["title", "company", "location", "description", "salary_range"]
    for r in required:
        if r not in payload:
            return {"error": f"Missing required field: {r}"}, 400
    job = service.post_job(
        payload["title"], payload["company"], payload["location"],
        payload["description"], payload["salary_range"]
    )
    return {"message": "Job posted successfully", "job": job.__dict__}, 201

def handle_list_jobs():
    jobs = service.list_jobs()
    return {"jobs": [j.__dict__ for j in jobs]}, 200

def handle_submit_application(job_id: int, payload: dict):
    required = ["candidate_name", "candidate_email", "resume_url"]
    for r in required:
        if r not in payload:
            return {"error": f"Missing required field: {r}"}, 400
    app = service.apply_to_job(job_id, payload["candidate_name"], payload["candidate_email"], payload["resume_url"])
    if not app:
        return {"error": "Job listing not found or inactive"}, 404
    return {"message": "Application submitted successfully", "application": app.__dict__}, 201
