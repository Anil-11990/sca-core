from app.application.use_cases.create_professional import CreateProfessional
from app.domain.professional.professional import Professional


def test_create_professional():
    use_case = CreateProfessional()

    professional = use_case.execute(
        full_name="Anil Khanal",
        primary_goal="Build ANIrex AI"
    )

    assert isinstance(professional, Professional)
    assert str(professional.full_name) == "Anil Khanal"