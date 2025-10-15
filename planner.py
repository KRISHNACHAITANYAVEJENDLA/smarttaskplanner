import datetime

def generate_plan(goal: str):
    tasks = [
        ("Research & Planning", "Analyze requirements and plan the execution.", 2),
        ("Design", "Create wireframes and mockups.", 2),
        ("Development", "Implement the core features.", 5),
        ("Testing", "Perform QA and bug fixes.", 2),
        ("Launch", "Deploy and review performance.", 1)
    ]

    start_date = datetime.date.today()
    plan = []
    for i, (name, desc, days) in enumerate(tasks, start=1):
        deadline = start_date + datetime.timedelta(days=sum(t[2] for t in tasks[:i]))
        plan.append(f"**Task {i}: {name}**  \n📄 {desc}  \n⏳ Duration: {days} days  \n📅 Deadline: {deadline}\n")

    plan_text = "\n".join(plan)
    return f"### Goal: {goal}\n\n{plan_text}"
