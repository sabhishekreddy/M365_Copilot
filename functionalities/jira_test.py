#import jira
import json
from jira import JIRA

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
    print(json.dumps(issue.fields.description, default=str))