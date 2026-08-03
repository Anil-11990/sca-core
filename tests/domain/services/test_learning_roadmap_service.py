from app.domain.services.learning_roadmap_service import (
    LearningRoadmapService,
)


def test_learning_roadmap_generation():

    service = LearningRoadmapService()


    roadmap = service.generate(
        [
            "Machine Learning",
            "LLM",
            "Docker",
        ]
    )


    assert roadmap == [
        "Phase 1: Learn Machine Learning",
        "Phase 2: Learn LLM",
        "Phase 3: Learn Docker",
    ]