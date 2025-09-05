import {get_descrition, get_acceptance_criteria} from "./get_jira_features"
import {jira} from "./jira/jira_test"

async def score_AC(ISSUE_KEY):
    score = 0
    description = get_descrition(ISSUE_KEY)
    acceptance_criteria = get_acceptance_criteria(ISSUE_KEY)
    print("Description:", description)
    print("Acceptance Criteria:", acceptance_criteria)
    # Here you can add the logic to score the acceptance criteria
    score = len(acceptance_criteria)  # Example scoring logic
    if (len(acceptance_criteria) < 15 or len(acceptance_criteria) == ''):
        if (len(description) < 30 or len(description) == ''):
            return "Both description and acceptance criteria are too short or empty. Please provide more details."
        else:
            return score = 3
    else
        return score = 4
    return score