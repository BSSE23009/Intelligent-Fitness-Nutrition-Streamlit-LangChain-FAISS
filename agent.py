from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from dotenv import load_dotenv
from rag.query import answer_question
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from meal import get_nutrition_info
from motivation import instant_motivation
from workout import workout_schedule 
from workout import workout_recommender
from workout import suggest_alternatives
from workout import workout_duration
from workout import warmup_recommendation   
from workout import cooldown_recommendation
from meal import get_nutrition_info


load_dotenv()

llm = ChatOpenAI(model = "gpt-4o-mini", temperature=0.7)

tools = [
    workout_schedule,
    workout_recommender,
    suggest_alternatives,
    workout_duration,
    warmup_recommendation,
    cooldown_recommendation,
    instant_motivation,
    answer_question,
    get_nutrition_info
]


agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)




