from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

def analyze_milk_production(cow_data: dict, api_key: str) -> dict:
    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.3-70b-versatile"
    )
    
    prompt = f"""You are a dairy farming AI expert. Analyze this cow's milk production.

Cow Details:
- Cow ID: {cow_data['cow_id']}
- Breed: {cow_data['breed']}
- Age: {cow_data['age']} years
- Today's Milk: {cow_data['milk_today']} liters
- Average Milk: {cow_data['milk_average']} liters
- Last 7 days: {cow_data['milk_last_7_days']} liters
- Pregnancy Status: {cow_data['pregnancy_status']}

Respond in this exact format:
PRODUCTION STATUS: [EXCELLENT / GOOD / BELOW AVERAGE / CRITICAL DROP]
TREND: [INCREASING / STABLE / DECREASING]
REASON: [why production is at this level]
RECOMMENDATION: [what farmer should do to improve]"""

    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "agent": "Milk Production Tracker",
        "cow_id": cow_data['cow_id'],
        "analysis": response.content
    }