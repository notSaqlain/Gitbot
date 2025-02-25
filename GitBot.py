import json

class GitBot:
    def __init__(self, file_path="data.json"):
        self.file_path = file_path
        self.data = self._load_data()

    def _load_data(self):
        try:
            with open(self.file_path, "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []


    def get_event_type(self):
        return self.data[-1].get("event_type", "Unknown") if self.data else "Unknown"

    def get_user_name(self):
        return self.data[-1].get("user", {}).get("name", "Unknown") if self.data else "Unknown"

    def get_user_username(self):
        return self.data[-1].get("user", {}).get("username", "Unknown") if self.data else "Unknown"

    def get_project_name(self):
        return self.data[-1].get("project", {}).get("name", "Unknown") if self.data else "Unknown"

    def get_issue_title(self):
        return self.data[-1].get("object_attributes", {}).get("title", "Unknown") if self.data else "Unknown"

    def get_issue_state(self):
        return self.data[-1].get("object_attributes", {}).get("state", "Unknown") if self.data else "Unknown"

    def get_issue_url(self):
        return self.data[-1].get("object_attributes", {}).get("url", "Unknown") if self.data else "Unknown"

    def get_issue_iid(self):
        return self.data[-1].get("object_attributes", {}).get("iid", "Unknown") if self.data else "Unknown"
