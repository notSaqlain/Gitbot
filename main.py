from GitBot import GitBot as gitbot

def main():
    webhook = gitbot("data.json", token="WTeR2z3pT71wxJsyDtYY")

    print("Event Type:", webhook.get_event_type())
    print("Issue IID:", webhook.get_issue_iid())
    print("User Name:", webhook.get_user_name())
    print("Project Name:", webhook.get_project_name())
    print("Issue Title:", webhook.get_issue_title())
    print("Issue State:", webhook.get_issue_state())
    print("Issue URL:", webhook.get_issue_url())
    print("Project ID:", webhook.get_project_id())

    current_state = webhook.get_issue_state()
    if current_state == "closed":
        new_state = "open"
    elif current_state == "opened":
        new_state = "closed"
    else:
        print("Unknown issue state.")
        return
    
    # new_state = "open" if gitbot.get_issue_state() == "closed" else "closed"

    print(f"\nNuovo issue state: {new_state}...")
    webhook.update_issue_state(new_state)

if __name__ == "__main__":
    main()
