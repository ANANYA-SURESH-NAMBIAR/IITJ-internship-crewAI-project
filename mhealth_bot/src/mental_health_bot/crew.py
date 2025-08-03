from crewai import Crew, Process
from crewai.config import AgentConfig, TaskConfig
import os

def create_crew():
    agents_config = AgentConfig.load(path='src/mental_health_bot/config/agents.yaml')
    tasks_config = TaskConfig.load(path='src/mental_health_bot/config/tasks.yaml')

    crew = Crew(
        agents=agents_config.agents,
        tasks=tasks_config.tasks,
        process=Process.sequential,
        verbose=True
    )
    return crew
