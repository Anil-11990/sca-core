from app.bootstrap.container import Container
from app.application.use_cases.create_professional import CreateProfessional


def test_container_creates_use_case():
    container = Container()

    use_case = container.create_professional_use_case()

    assert isinstance(use_case, CreateProfessional)