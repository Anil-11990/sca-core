from app.api.schemas.goal_response import GoalResponse


def to_goal_response(goal):

    return GoalResponse(

        id=str(goal.id),

        title=str(goal.title),

        status=goal.status.value,

        progress=goal.progress,
    )