from pydantic import BaseModel


class GoalResponse(BaseModel):

    id: str

    title: str

    status: str

    progress: int
