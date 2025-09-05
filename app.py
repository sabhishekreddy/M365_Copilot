# app.py
from microsoft_agents.hosting.core import (
   AgentApplication,
   TurnState,
   TurnContext,
   MemoryStorage,
)
from microsoft_agents.hosting.aiohttp import CloudAdapter
from start_server import start_server
from functionalities.get_jira_features import get_acceptance_criteria
from functionalities.copilot import summarize_response
from functionalities.copilot import score_Acceptance_Criteria
from functionalities.copilot import recommend_Acceptance_Criteria

AGENT_APP = AgentApplication[TurnState](
    storage=MemoryStorage(), adapter=CloudAdapter()
)

async def _help(context: TurnContext, _: TurnState):
    await context.send_activity(
        "Welcome to the Echo Agent sample 🚀. "
        "Type /help for help or send a message to see the echo feature in action."
    )

AGENT_APP.conversation_update("membersAdded")(_help)

AGENT_APP.message("/help")(_help)

async def _fetch_Acceptance_Criteria(context: TurnContext, _: TurnState):
    issue_key = "SCRUM2"
    print(f"Fetching acceptance criteria for issue: {issue_key}")
    acceptance_criteria = get_acceptance_criteria(issue_key)
    await context.send_activity(f"Acceptance Criteria for {issue_key}: {acceptance_criteria}")

AGENT_APP.conversation_update("message")(_fetch_Acceptance_Criteria)

AGENT_APP.message("/fetchAC")(_fetch_Acceptance_Criteria)

async def _summarize_Acceptance_Criteria(context: TurnContext, _: TurnState):
    issue_key = "SCRUM2"
    print(f"Fetching acceptance criteria for issue: {issue_key}")
    acceptance_criteria = get_acceptance_criteria(issue_key)
    a = summarize_response(acceptance_criteria)
    await context.send_activity(f"Summarized Acceptance Criteria for {issue_key}: {a}")

AGENT_APP.conversation_update("message")(_summarize_Acceptance_Criteria)

AGENT_APP.message("/SAC")(_summarize_Acceptance_Criteria)

#---------------------------------------------------------------------------#

async def _score_Acceptance_Criteria(context: TurnContext, _: TurnState):
    issue_key = "SCRUM2"
    print(f"Fetching acceptance criteria for issue: {issue_key}")
    acceptance_criteria = get_acceptance_criteria(issue_key)
    a = score_Acceptance_Criteria(acceptance_criteria)
    await context.send_activity(f"Scored Acceptance Criteria for {issue_key}: {a}")

AGENT_APP.conversation_update("message")(_score_Acceptance_Criteria)

AGENT_APP.message("/SRAC")(_score_Acceptance_Criteria)

#---------------------------------------------------------------------------#

async def _recommending_Acceptance_Criteria(context: TurnContext, _: TurnState):
    issue_key = "SCRUM2"
    print(f"Fetching acceptance criteria for issue: {issue_key}")
    acceptance_criteria = get_acceptance_criteria(issue_key)
    a = recommend_Acceptance_Criteria(acceptance_criteria)
    await context.send_activity(f"Recommended Acceptance Criteria for {issue_key}: {a}")

AGENT_APP.conversation_update("message")(_recommending_Acceptance_Criteria)

AGENT_APP.message("/RAC")(_recommending_Acceptance_Criteria)

#---------------------------------------------------------------------------#

@AGENT_APP.activity("message")
async def on_message(context: TurnContext, _):
    await context.send_activity(f"you said: {context.activity.text}")

if __name__ == "__main__":
    try:
        start_server(AGENT_APP, None)
    except Exception as error:
        raise error