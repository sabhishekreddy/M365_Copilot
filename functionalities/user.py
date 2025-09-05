#write code to get user details from jira using jira api
import jira
from jira import JIRA
import json 

jira_url = "https://copilotsetup.atlassian.net/"
API_TOKEN = "ATATT3xFfGF0IiCd3v_at_KO86q2wbm_UQkBNxhxzqjJnt0kDLHjaUa4SeAWM8xfu1Nx1G6ECV1UowEIKAmPU4OeD9pJr1sXYASiGJujMEpyNpkEnmSdHV0hfjC_U5OgaBcPVy-piPRNVaUxJGTT0LKzc7CczbBd77RX-CkjgBSBTKHgpBO-Imc=0F1CA389"
email = "abhishekreddylovely@gmail.com"

option = {
    'server': jira_url
}

jira = JIRA(options=option, basic_auth=(email, API_TOKEN))

def get_user_details(email):
    users = jira.search_users(query=email)
    if not users:
        return f"No user found for {email}"
    user = users[0]  # pick the first match
    return {
        "displayName": user.displayName,
        "accountId": user.accountId,
        "emailAddress": getattr(user, "emailAddress", None)  # may be masked in Jira Cloud
    }

print(get_user_details("abhishekreddylovely@gmail.com"))