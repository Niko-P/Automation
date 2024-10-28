import pytest
from .YouGile import Yougile


@pytest.fixture
def yougile_instance():
    return Yougile(
        "yitak23563@mcatag.com",
        "ZZSa56NGf8a2K@-",
        "e9328c9a-5098-45e9-9c7e-bf04a6e29679",
    )


# Тест на успешное добавление проекта
@pytest.mark.positive_test
def test_add_project(yougile_instance):
    project_data = {"a3913c0a-809c-4c4f-a9ec-99022f6e6c80": "admin"}
    response = yougile_instance.create_project("Yogatime", project_data)

    assert "content" in response, "Expected 'content' in creation response"
    assert len(response["content"]) > 0, (
        "Expected content to contain at least one project"
    )
    project_id = response["content"][0]["id"]
    assert project_id is not None, "Expected project ID"


# Тест на получение списка проектов
@pytest.mark.positive_test
def test_get_list_of_projects(yougile_instance):
    projects = yougile_instance.get_list_of_projects()

    assert len(projects) > 0, "Project list should not be empty"


# Тест на обновление проекта
@pytest.mark.positive_test
def test_update_project(yougile_instance):
    project_name = "Test Project"
    project_data = {"a3913c0a-809c-4c4f-a9ec-99022f6e6c80": "admin"}
    create_response = yougile_instance.create_project(
        project_name, project_data
    )

    assert "content" in create_response, (
        "Expected 'content' in creation response"
    )
    assert len(create_response["content"]) > 0, (
        "Expected content to contain at least one project"
    )

    project_id = create_response["content"][0].get("id")
    assert project_id is not None, "Expected project ID in creation response"

    new_title = "Updated Test Project"
    update_response = yougile_instance.update_project(project_id, new_title)

    assert "id" in update_response, "Expected project ID in update response"
    assert update_response.get("id") == project_id, (
        "Expected project ID to match"
    )


# Тест на получение проекта по ID
@pytest.mark.positive_test
def test_get_project_by_id(yougile_instance):
    project_name = "Test Project"
    project_data = {"a3913c0a-809c-4c4f-a9ec-99022f6e6c80": "admin"}
    create_response = yougile_instance.create_project(
        project_name, project_data
    )

    assert "content" in create_response, (
        "Expected 'content' in creation response"
    )
    assert len(create_response["content"]) > 0, (
        "Expected content to contain at least one project"
    )

    project = create_response["content"][0]
    assert "id" in project, "Expected project ID in creation response"
    project_id = project["id"]

    project_details = yougile_instance.get_project_by_id(project_id)
    assert "id" in project_details, (
        "Expected project ID in project details response"
    )
    assert "title" in project_details, (
        "Expected title in project details response"
    )
    assert project_details["id"] == project_id, (
        "Project ID in details does not match created ID"
    )


# Тест на добавление проекта без названия
@pytest.mark.negative_test
@pytest.mark.xfail(
     reason="Expected ValueError when project name is missing."
     )
def test_add_project_missing_name(yougile_instance):
    invalid_project_data = {"a3913c0a-809c-4c4f-a9ec-99022f6e6c80": "admin"}

    with pytest.raises(ValueError, match="Project name is required."):
        yougile_instance.create_project("", invalid_project_data)


# Тест на добавление проекта без данных пользователей
@pytest.mark.negative_test
@pytest.mark.xfail(reason="Expected ValueError when user data is missing.")
def test_add_project_missing_users(yougile_instance):
    with pytest.raises(
        ValueError,
        match="Invalid user data format.",
    ):
        yougile_instance.create_project("Test Project", None)


# Тест на добавление проекта с некорректным форматом данных пользователей
@pytest.mark.negative_test
@pytest.mark.xfail(
    reason="Expected ValueError when user data format is invalid."
)
def test_add_project_invalid_users_format(yougile_instance):
    invalid_project_data = ["invalid_user_id"]

    with pytest.raises(
        ValueError,
        match="Invalid user data format.",
    ):
        yougile_instance.create_project("Test Project", invalid_project_data)
