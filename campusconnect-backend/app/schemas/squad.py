from typing import Optional, List
from pydantic import BaseModel, ConfigDict
from datetime import datetime

class CoBuilderRead(BaseModel):
    id: str
    name: str
    role: str
    skills: List[str]
    avatar: Optional[str] = None
    match_score: str
    status: str
    bio: Optional[str] = None
    invited: bool = False

    model_config = ConfigDict(from_attributes=True)

class SquadInviteCreate(BaseModel):
    cobuilder_id: str
    message: Optional[str] = None

class SquadInviteRead(BaseModel):
    id: str
    sender_email: str
    cobuilder_id: str
    status: str
    message: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
