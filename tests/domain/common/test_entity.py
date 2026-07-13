from uuid import UUID

from app.domain.common.entity import Entity


def test_entity_receives_uuid():
    entity = Entity()

    assert isinstance(entity.id, UUID)


def test_new_entities_have_unique_ids():
    entity1 = Entity()
    entity2 = Entity()

    assert entity1.id != entity2.id


def test_entity_is_equal_to_itself():
    entity = Entity()

    assert entity == entity