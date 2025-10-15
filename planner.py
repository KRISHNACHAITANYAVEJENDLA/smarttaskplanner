import os
from openai import OpenAI

def generate_plan(goal: str):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "❌ Error: OPENAI_API_KEY is missing or invalid."

    try:
        client = OpenAI(api_key=api_key)
        prompt = f"""
        Break down this goal into actionable tasks with dependencies, durations, and deadlines.
        Output each task in a clean markdown list.
        Goal: {goal}
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )

        plan = response.choices[0].message.content.strip()
        return plan if plan else "⚠️ No response from model."
    except Exception as e:
        return f"❌ Error generating plan: {str(e)}"
