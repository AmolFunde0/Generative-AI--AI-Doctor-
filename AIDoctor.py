import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    # max_tokens=512
    # stop=["\n\n"]
)
st.title("AI Doctor🧑‍⚕️🩺")
age = st.number_input("Enter your age", min_value=0, max_value=120, value=30)
symptom_options = [
    "Fever",
    "Cough",
    "Headache",
    "Sore throat",
    "Runny nose",
    "Fatigue",
    "Shortness of breath",
    "Body ache",
    "Nausea",
    "Diarrhea",
    "Loss of taste or smell"
    "chest pain",
    "Eye irritation",
    "Dizziness",
    "Weekness",
    "heart palpitations",
    "uerinary problems",
    "digestive issues",
]
selected_symptoms = st.multiselect("Select symptoms", symptom_options)
other_symptoms = st.text_input("Other symptoms (optional)", placeholder="e.g., dizziness, rash")
symptoms = selected_symptoms.copy()
if other_symptoms:
    symptoms.append(other_symptoms)
    
st.write("Age:", age)
st.write("Symptoms:", ", ".join(symptoms) if symptoms else "None")
if st.button("Submit"):
    symptom_text = ", ".join(symptoms) if symptoms else "no reported symptoms"
    prompt = f"Act like an expert doctor in india. I will give you a patient age and symptoms. Patient is a {age} year old male and having symptoms: {symptom_text}. What is your diagnosis? give extra information about each medicine you suggest; give only medicines and doses, and also give the instructions and precautions. and aslo add the emojis if it make sense."
    response = llm.invoke(prompt)
    st.write("AI Doctor's Diagnosis:")
    st.write(response.content)
