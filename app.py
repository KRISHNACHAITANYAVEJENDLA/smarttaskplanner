from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from planner import generate_plan

app = FastAPI(title="Smart Task Planner API", version="1.0")

# Allow access from frontend
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
    plan = generate_plan(goal)
    return {"goal": goal, "plan": plan}
