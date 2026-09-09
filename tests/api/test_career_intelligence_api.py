from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def create_professional():
    response = client.post(
        "/professionals",
        json={
            "full_name": "Career Intelligence Test",
            "primary_goal": "Build an AI career",
        },
    )

    assert response.status_code == 201

    return response.json()["id"]


def test_analyze_career():
    professional_id = create_professional()

    response = client.post(
        f"/career-intelligence/{professional_id}/analysis",
        json={
            "required_skills": [
                "Python",
                "Java",
                "FastAPI",
            ],
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert "career_score" in data
    assert "profile_completion" in data
    assert "skill_gaps" in data
    assert "career_readiness" in data


def test_get_career_analysis():
    professional_id = create_professional()

    response = client.get(
        f"/career-intelligence/{professional_id}/analysis"
    )

    assert response.status_code == 200

    data = response.json()

    assert "career_score" in data
    assert "profile_completion" in data
    assert "skill_gaps" in data
    assert "career_readiness" in data


def test_get_career_insights():
    professional_id = create_professional()

    response = client.get(
        f"/career-intelligence/{professional_id}/insights"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    if data:
        assert "title" in data[0]
        assert "description" in data[0]
        assert "category" in data[0]


def test_get_career_recommendations():
    professional_id = create_professional()

    response = client.get(
        f"/career-intelligence/{professional_id}/recommendations"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    if data:
        assert "action" in data[0]
        assert "reason" in data[0]
        assert "priority" in data[0]


def test_get_career_recommendations_for_target_role_skill_gaps():
    professional_id = create_professional()

    response = client.get(
        f"/career-intelligence/{professional_id}/recommendations",
        params={
            "required_skills": "Python, React, TypeScript",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert len(data) == 3

    target_gap = data[0]
    skill_advice = data[1]
    project_advice = data[2]

    assert target_gap["action"] == "Close target-role skill gaps"
    assert target_gap["priority"] == "HIGH"
    assert "React" in target_gap["reason"]
    assert "TypeScript" in target_gap["reason"]

    assert skill_advice["action"] == "Improve technical skills"
    assert skill_advice["priority"] == "HIGH"

    assert project_advice["action"] == "Build practical projects"
    assert project_advice["priority"] == "MEDIUM"



def test_get_career_roadmap():
    professional_id = create_professional()

    response = client.get(
        f"/career-intelligence/{professional_id}/roadmap"
    )

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    if data:
        assert "skill" in data[0]
        assert "priority" in data[0]
        assert "stage" in data[0]
def test_get_market_intelligence():
    """
    Verify the Market Intelligence API endpoint.

    The endpoint should:

        - return HTTP 200
        - return matched skills
        - return opportunity skills
        - return high-priority opportunities
    """

    professional_id = create_professional()

    response = client.get(
        f"/career-intelligence/{professional_id}/market-intelligence"
    )

    assert response.status_code == 200

    data = response.json()

    assert "matched_skills" in data
    assert "opportunity_skills" in data
    assert "high_priority_opportunities" in data

    assert isinstance(
        data["matched_skills"],
        list,
    )

    assert isinstance(
        data["opportunity_skills"],
        list,
    )

    assert isinstance(
        data["high_priority_opportunities"],
        list,
    )





