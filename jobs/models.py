from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Optional

@dataclass
class JobListing:
    id: int
    title: str
    company: str
    location: str
    description: str
    salary_range: str
    is_active: bool = True
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

@dataclass
class Application:
    id: int
    job_id: int
    candidate_name: str
    candidate_email: str
    resume_url: str
    status: str = "PENDING"
    applied_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
