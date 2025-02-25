import json

class GitBot:
    def __init__(self, file_path="webhook_data.json"):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def get_event_type(self):
        return self.data.get("event_type", "Unknown")

    def get_user_name(self):
        return self.data.get("user", {}).get("name", "Unknown")

    def get_user_username(self):
        return self.data.get("user", {}).get("username", "Unknown")

    def get_project_name(self):
        return self.data.get("project", {}).get("name", "Unknown")

    def get_issue_title(self):
        return self.data.get("object_attributes", {}).get("title", "Unknown")

    def get_issue_state(self):
        return self.data.get("object_attributes", {}).get("state", "Unknown")

    def get_issue_url(self):
        return self.data.get("object_attributes", {}).get("url", "Unknown")
