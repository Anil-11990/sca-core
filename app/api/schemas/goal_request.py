from pydantic import BaseModel


class GoalRequest(BaseModel):
    title: str