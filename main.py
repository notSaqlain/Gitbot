from GitBot import GitBot as gitbot


def main():
    webhook = gitbot("data.json")

    print("Event Type:", webhook.get_event_type())
    print("User Name:", webhook.get_user_name())
    print("Project Name:", webhook.get_project_name())
    print("Issue Title:", webhook.get_issue_title())
    print("Issue State:", webhook.get_issue_state())
    print("Issue URL:", webhook.get_issue_url())
    print("Issue IID:", webhook.get_issue_iid())



if __name__ == "__main__":
    main()