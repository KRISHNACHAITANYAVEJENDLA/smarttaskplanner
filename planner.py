import os
from openai import OpenAI

def generate_plan(goal: str):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "❌ Error: Missing OPENAI_API_KEY environment variable."

    client = OpenAI(api_key=api_key)
    prompt = f"""
    Break this goal into actionable tasks with deadlines and dependencies.

    Format:
    Task Name | Description | Dependencies | Estimated Duration | Suggested Deadline

    Goal: {goal}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error generating plan: {str(e)}"
