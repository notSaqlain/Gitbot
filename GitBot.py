import json
import requests

class GitBot:
    def __init__(self, file_path="data.json", token="WTeR2z3pT71wxJsyDtYY"):
        self.file_path = file_path
        self.token = token  # GitLab API token
        self.data = self._load_data()

    def _load_data(self):
        data_list = []
        try:
            with open(self.file_path, "r") as file:
                for line in file:
                    try:
                        data_list.append(json.loads(line))
                    except json.JSONDecodeError:
                        print("Warning: Skipping invalid JSON line.")
        except FileNotFoundError:
            print("File not found, starting with empty data.")
        return data_list

    def _get_dati_aggiornati(self):
        """Get the latest data entry."""
        return self.data[-1] if self.data else {}

    def get_event_type(self):
        return self._get_dati_aggiornati().get("event_type", "Unknown")

    def get_user_name(self):
        return self._get_dati_aggiornati().get("user", {}).get("name", "Unknown")

    def get_user_username(self):
        return self._get_dati_aggiornati().get("user", {}).get("username", "Unknown")

    def get_project_name(self):
        return self._get_dati_aggiornati().get("project", {}).get("name", "Unknown")

    def get_issue_title(self):
        return self._get_dati_aggiornati().get("object_attributes", {}).get("title", "Unknown")

    def get_issue_state(self):
        return self._get_dati_aggiornati().get("object_attributes", {}).get("state", "Unknown")

    def get_issue_url(self):
        return self._get_dati_aggiornati().get("object_attributes", {}).get("url", "Unknown")

    def get_issue_iid(self):
        return self._get_dati_aggiornati().get("object_attributes", {}).get("iid", "Unknown")

    def get_project_id(self):
        return self._get_dati_aggiornati().get("project", {}).get("id", "Unknown")

    
    
    def update_issue_state(self, new_state):
        project_id = self.get_project_id()
        issue_iid = self.get_issue_iid()

        if project_id == "Unknown" or issue_iid == "Unknown":
            print("Error: Missing project ID or issue IID.")
            return None

        url = f"https://code.servizi.gr-u.it/server-farm-unix/support/-/issues/{issue_iid}"
        # url = f"https://gitlab.com/api/v4/projects/{project_id}/issues/{issue_iid}"
        headers = {"PRIVATE-TOKEN": self.token}
        data = {"state_event": "reopen" if new_state == "open" else "close"}

        response = requests.put(url, headers=headers, json=data)

        if response.status_code == 200:
            print(f"Issue {issue_iid} successfully updated to '{new_state}'")
        else:
            print(f"Failed to update issue. Error: {response.text}")
