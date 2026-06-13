from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

def analyze_health(cow_data: dict, api_key: str) -> dict:
    llm = ChatGroq(
        api_key=api_key,
        model="llama-3.3-70b-versatile"
    )
    
    prompt = f"""You are a veterinary AI expert. Analyze this cow's health.

Cow Details:
- Cow ID: {cow_data['cow_id']}
- Age: {cow_data['age']} years
- Breed: {cow_data['breed']}
- Symptoms: {cow_data['symptoms']}
- Temperature: {cow_data['temperature']}°C
- Last Vaccination: {cow_data['last_vaccination']}

Respond in this exact format:
HEALTH STATUS: [CRITICAL / SICK / MODERATE / HEALTHY]
POSSIBLE DISEASE: [disease name]
IMMEDIATE ACTION: [what farmer should do right now]
MEDICATION: [suggested medication]
VET REQUIRED: [YES / NO]"""

    response = llm.invoke([HumanMessage(content=prompt)])
    
    return {
        "agent": "Health Monitor",
        "cow_id": cow_data['cow_id'],
        "analysis": response.content
    }