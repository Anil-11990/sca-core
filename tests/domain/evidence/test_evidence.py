from app.domain.evidence.entity import (
    Evidence,
)


def test_create_evidence():

    evidence = Evidence(
        title="SCA Core Architecture",
        description="Professional Operating System design",
        evidence_type="Project",
        reference_url="github.com/anil/sca",
    )


    assert (
        evidence.title
        ==
        "SCA Core Architecture"
    )

    assert (
        evidence.evidence_type
        ==
        "Project"
    )