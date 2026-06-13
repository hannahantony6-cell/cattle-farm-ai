#AI Cattle Farm Management System

An intelligent multi-agent AI system that helps cattle farmers 
monitor cow health, track milk production, optimize feed and 
calculate profits automatically.

## Live Demo
👉 https://cattle-farm-ai-blukzqtmfxe8swegfzxmzb.streamlit.app

##  What it does

- 3 specialized AI agents analyze each cow simultaneously
- Health Monitor detects diseases early
- Milk Production Tracker identifies declining trends
- Feed Optimizer calculates perfect daily nutrition
- Vaccination Reminder tracks and alerts upcoming vaccines
- Milk Production Chart visualizes 7-day trends
- Profit Calculator shows income vs expense per cow

## Demo Screenshots

### Main Dashboard
<img width="1912" height="915" alt="image" src="https://github.com/user-attachments/assets/4c4bef01-eca5-4444-a361-347295501653" />

### AI Agent Analysis
<img width="1918" height="821" alt="image" src="https://github.com/user-attachments/assets/0f206b1e-0d53-46a9-82a8-3592a6ee3903" />

### Vaccination Reminder
<img width="1798" height="618" alt="image" src="https://github.com/user-attachments/assets/24d1e51e-a8de-458d-bb6f-620d79f570ca" />


### Milk Production Chart
<img width="1913" height="882" alt="image" src="https://github.com/user-attachments/assets/4c7d3d4f-395f-4242-9c37-7c61e5f92867" />


### Profit Calculator
<img width="1896" height="636" alt="image" src="https://github.com/user-attachments/assets/9227b607-4369-4773-a9ef-0884aa0a341d" />
<img width="1882" height="838" alt="image" src="https://github.com/user-attachments/assets/5fcf0c0e-3aac-4637-9d67-49a1ec632b00" />


##  Multi-Agent Architecture
Farmer enters cow details

↓

Agent 1 — Health Monitor

Analyzes symptoms, detects disease

↓

Agent 2 — Milk Production Tracker

Identifies production trends

↓

Agent 3 — Feed Optimizer

Calculates optimal nutrition

↓

Results displayed on dashboard

##  Tech Stack

| Technology | Purpose |
|------------|---------|
| Streamlit | Frontend UI |
| Python | Backend logic |
| LangChain | AI framework |
| Groq API | AI inference engine |
| LLaMA 3.3 70B | Large language model |
| Plotly | Data visualization |

##  Key Features

###  Health Monitoring Agent
- Analyzes symptoms using veterinary AI knowledge
- Detects diseases like BRD, FMD, Mastitis
- Recommends medication and vet visit if needed
- Classifies as CRITICAL / SICK / MODERATE / HEALTHY

###  Milk Production Agent
- Tracks daily production trends
- Identifies reasons for production drop
- Gives recommendations to improve yield
- Classifies as EXCELLENT / GOOD / BELOW AVERAGE / CRITICAL DROP

###  Feed Optimizer Agent
- Calculates optimal feed based on weight, age, breed
- Splits into morning and evening portions
- Recommends supplements and vitamins
- Adjusts for pregnancy and health status

### Vaccination Reminder
- Tracks 7 major cattle vaccines
- Calculates next due date automatically
- Alerts when vaccine is overdue or due soon
- Shows complete vaccination schedule

###  Milk Production Tracker
- 7-day production chart
- Average, highest, lowest stats
- Visual trend analysis

###  Profit Calculator
- Monthly income vs expense breakdown
- Net profit per cow calculation
- Income vs Expense vs Profit bar chart
- Alerts if cow is unprofitable

##  How to run locally

**Step 1 — Clone the repo**
git clone https://github.com/hannahantony6-cell/cattle-farm-ai.git

cd cattle-farm-ai

**Step 2 — Install dependencies**
pip install -r requirements.txt

**Step 3 — Run the app**
streamlit run app.py

**Step 4 — Enter your Groq API key**

Get your free API key at: https://console.groq.com
Enter it in the sidebar when the app opens!

## Sample Test Case

| Field | Value |
|-------|-------|
| Cow ID | COW-001 |
| Breed | Holstein Friesian |
| Age | 4 years |
| Weight | 400 kg |
| Temperature | 39.5°C |
| Milk Today | 8 liters |
| Average Milk | 14 liters |
| Symptoms | reduced appetite, nasal discharge, lethargy |
| Pregnancy | Not Pregnant |
