from jira import JIRA
import json

jira_url = "https://copilotsetup.atlassian.net/"
API_TOKEN = "ATATT3xFfGF0IiCd3v_at_KO86q2wbm_UQkBNxhxzqjJnt0kDLHjaUa4SeAWM8xfu1Nx1G6ECV1UowEIKAmPU4OeD9pJr1sXYASiGJujMEpyNpkEnmSdHV0hfjC_U5OgaBcPVy-piPRNVaUxJGTT0LKzc7CczbBd77RX-CkjgBSBTKHgpBO-Imc=0F1CA389"
email = "abhishekreddylovely@gmail.com"

option = {
    'server': jira_url
}

jira = JIRA(options=option, basic_auth=(email, API_TOKEN))

jql_query = 'project = "SCRUM2"'
issues = jira.search_issues(jql_query)
print(f"Total issues found: {len(issues)}")
for issue in issues:
    print(f"{issue.key}: {issue.fields.summary}")

def get_description(ISSUE_KEY):
    print("This function retrieves the description from Jira.")
    if (len(issues) > 1):
        return "More Than One Issue Found"
    elif (len(issues) == 0):
        return "No Issues Found"
    for issue in issues:
        print(f"{issue.key}: {issue.fields.summary}")
        print(json.dumps(issue.fields.description, default=str))
    return json.dumps(issue.fields.description, default=str)

def get_acceptance_criteria(ISSUE_KEY):
    print("This function retrieves the description from Jira.")
    if (len(issues) > 1):
        return "More Than One Issue Found"
    elif (len(issues) == 0):
        return "No Issues Found"
    for issue in issues:
        print(f"{issue.key}: {issue.fields.summary}")
        print(json.dumps(issue.fields.description, default=str))
    return json.dumps(issue.fields.description, default=str)

get_description("SCRUM2")
#get_acceptance_criteria("SCRUM2")