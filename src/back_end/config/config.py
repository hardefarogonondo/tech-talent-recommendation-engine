from pydantic import BaseModel
from typing import Optional


class Requirements(BaseModel):
    age_range: str
    work_arrangement: str
    education_level: str
    role: str
    years_of_experience: int
    programming_languages: Optional[str] = None
    databases: Optional[str] = None
    cloud_platforms: Optional[str] = None
    web_frameworks: Optional[str] = None
    other_frameworks: Optional[str] = None
    developer_tools: Optional[str] = None
    development_environments: Optional[str] = None
    operating_systems: Optional[str] = None
    collaboration_tools: Optional[str] = None
    communication_tools: Optional[str] = None
