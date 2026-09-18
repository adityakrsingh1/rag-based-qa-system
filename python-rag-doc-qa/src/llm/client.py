from typing import List
import requests

class LLMClient:
    def __init__(self, api_url: str, api_key: str):
        self.api_url = api_url
        self.api_key = api_key

    def generate_answer(self, context: str, question: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "context": context,
            "question": question
        }
        response = requests.post(self.api_url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json().get("answer", "")

    def batch_generate_answers(self, contexts: List[str], questions: List[str]) -> List[str]:
        answers = []
        for context, question in zip(contexts, questions):
            answer = self.generate_answer(context, question)
            answers.append(answer)
        return answers