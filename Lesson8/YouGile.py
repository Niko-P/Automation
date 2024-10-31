import requests


# Пользовательское исключение для ошибок API Yougile.
class YougileError(Exception):
    """Custom exception for Yougile API errors."""
    pass


class Yougile:
    def __init__(self, login, password, company_id):
        # Инициализация экземпляра Yougile с логином, паролем и ID компании
        self.login = login
        self.password = password
        self.company_id = company_id
        self.base_url = "https://ru.yougile.com"  # Базовый URL API Yougile
        self.token = self.get_auth_token()  # Получение токена аутентификации

    def get_auth_token(self):
        # Метод для получения токена аутентификации
        url = self.base_url + "/api-v2/auth/keys/get"
        headers = {"Content-Type": "application/json"}
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id,
        }
        response = requests.post(url, json=payload, headers=headers)

        if response.status_code == 200:
            response_data = response.json()
            if isinstance(response_data, list) and len(response_data) > 0:
                return response_data[0].get('key')
            else:
                raise YougileError(
                    "Unexpected response format: expected a list.")
        else:
            raise YougileError(
                f"Authentication error: {response.status_code} {response.text}"
            )

    def make_authorized_request(self, endpoint, data=None, method="GET"):
        # Метод для выполнения авторизованных запросов к API
        url = f"{self.base_url}{endpoint}"
        headers = {
            "Authorization": f"Bearer {self.token}",
        }

        # Выполнение запроса в зависимости от метода (POST, PUT, GET)
        if method == "POST":
            response = requests.post(url, json=data, headers=headers)
        elif method == "PUT":
            response = requests.put(url, json=data, headers=headers)
        elif method == "GET":
            response = requests.get(url, headers=headers)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        # Проверяем статус ответа и возвращаем JSON-данные, если запрос успешен
        if response.status_code in [200, 201]:
            return response.json()
        else:
            raise YougileError(
                f"Request failed: {response.status_code} {response.text}"
            )

    def create_project(self, project_name, users):
        # Метод для создания нового проекта
        if not project_name:
            raise ValueError("Project name is required.")

        # Проверяем формат данных пользователей
        if not isinstance(users, dict) or not all(
             isinstance(v, str) for v in users.values()):
            raise ValueError(
             "Invalid user data format. "
             "Expected a dictionary with string values."
            )

        endpoint = "/api-v2/projects"
        data = {"title": project_name, "users": users}
        return self.make_authorized_request(endpoint, data)

    def get_list_of_projects(self):
        # Метод для получения списка проектов
        endpoint = "/api-v2/projects"
        return self.make_authorized_request(endpoint, method="GET")

    def update_project(self, project_id, new_title):
        # Метод для обновления названия проекта
        if not new_title:
            # Если новое название не указано, вызываем ошибку
            raise ValueError("New title is required.")

        endpoint = f"/api-v2/projects/{project_id}"
        data = {"title": new_title}
        return self.make_authorized_request(endpoint, data, method="PUT")

    def get_project_by_id(self, project_id):
        # Метод для получения информации о проекте по ID
        endpoint = f"/api-v2/projects/{project_id}"
        return self.make_authorized_request(endpoint, method="GET")
