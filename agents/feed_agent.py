from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

def optimize_feed(cow_data: dict, api_key: str) -> dict:
    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.3-70b-versatile"
    )
    
    prompt = f"""You are an animal nutrition AI expert. Calculate optimal feed for this cow.

Cow Details:
- Cow ID: {cow_data['cow_id']}
- Weight: {cow_data['weight']} kg
- Age: {cow_data['age']} years
- Breed: {cow_data['breed']}
- Milk Production: {cow_data['milk_today']} liters/day
- Pregnancy Status: {cow_data['pregnancy_status']}
- Current Feed: {cow_data['current_feed']} kg/day
- Health Status: {cow_data['symptoms']}

Respond in this exact format:
RECOMMENDED FEED: [amount in kg per day]
MORNING FEED: [amount in kg]
EVENING FEED: [amount in kg]
SUPPLEMENTS: [vitamins or minerals needed]
WATER INTAKE: [liters per day]
SPECIAL NOTES: [any special dietary requirements]"""

    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "agent": "Feed Optimizer",
        "cow_id": cow_data['cow_id'],
        "analysis": response.content
    }