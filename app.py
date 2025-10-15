from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from planner import generate_plan

app = FastAPI(title="Smart Task Planner API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "✅ Smart Task Planner API is running"}

@app.get("/plan/")
def get_plan(goal: str = Query(..., description="Enter your goal text")):
    try:
        plan = generate_plan(goal)
        return {"goal": goal, "plan": plan}
    except Exception as e:
        return {"goal": goal, "plan": f"❌ Error: {str(e)}"}
