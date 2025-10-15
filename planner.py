import datetime

def generate_plan(goal: str):
    tasks = [
        ("Research & Planning", "Understand requirements and plan the process.", 2),
        ("Design Phase", "Create structure, visuals, and mockups.", 2),
        ("Development", "Implement the main functionality.", 5),
        ("Testing & QA", "Perform testing and quality assurance.", 2),
        ("Launch & Review", "Deploy and review outcomes.", 1)
    ]

    start_date = datetime.date.today()
    plan = []
    for i, (name, desc, days) in enumerate(tasks, start=1):
        deadline = start_date + datetime.timedelta(days=sum(t[2] for t in tasks[:i]))
        plan.append(
            f"**Task {i}: {name}**  \n📄 {desc}  \n⏳ Duration: {days} days  \n📅 Deadline: {deadline}\n"
        )

    plan_text = "\n".join(plan)
    return f"### Goal: {goal}\n\n{plan_text}"
