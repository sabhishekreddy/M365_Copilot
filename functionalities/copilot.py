import os
import json
import requests
from openai import OpenAI
from functionalities.prompts import scoringSystemPrompt
from functionalities.prompts import recommendationSystemPrompt

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key="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",
)

completion = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3-8B-Instruct:novita",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant who always respond asking aboute user wellbeing before answering the question.",
        },
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message.content)

def summarize_response(response):
    print("This function summarizes the response.")
    # Implement summarization logic here
    return client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct:novita",
        messages=[
            {
                "role": "system",
                "content": "Summarize the user's response briefly into given when them format",
            },
            {
                "role": "user",
                "content": f"Summarize the following response: {response}"
            }
        ],
    ).choices[0].message.content

def score_Acceptance_Criteria(response):
    print("This function scores the acceptance criteria.")
    # Implement scoring logic here
    return client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct:novita",
        messages=[
            {
                "role": "system",
                "content": f"{scoringSystemPrompt(response)}",
            },
            {
                "role": "user",
                "content": f"Score the following Acceptance Criteria: {response}"
            }
        ],
    ).choices[0].message.content

def recommend_Acceptance_Criteria(response):
    print("This function recommends improvements to the acceptance criteria.")
    # Implement recommendation logic here
    return client.chat.completions.create(
        model="meta-llama/Meta-Llama-3-8B-Instruct:novita",
        messages=[
            {
                "role": "system",
                "content": f"{recommendationSystemPrompt(response,"")}",
            },
            {
                "role": "user",
                "content": f"Recommends the Acceptance Criteria: {response}"
            }
        ],
    ).choices[0].message.content