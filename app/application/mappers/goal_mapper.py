from app.domain.goal.goal import Goal
from app.application.dto.responses.goal_response import GoalResponse


class GoalMapper:
    """
    Maps Goal entity to GoalResponse DTO.
    """

    @staticmethod
    def to_response(goal: Goal) -> GoalResponse:

        return GoalResponse(
            id=str(goal.id),
            title=str(goal.title),
            status=goal.status.value,
        )