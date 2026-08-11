# AI Doctor Chatbot

A simple Streamlit-based AI doctor app that lets users enter age and select symptoms from a checklist. The selected symptoms are sent to a chatbot prompt to generate a focused diagnosis with medicine recommendations, dosing, instructions, and precautions.

## Features

- Age input using `st.number_input`
- Symptom selection using `st.multiselect`
- Optional additional symptoms via `st.text_input`
- Prompt generation for the chatbot with structured symptom input
- Displays AI-generated diagnosis and treatment advice

## How to Run

1. Install dependencies, including Streamlit and the `langchain_groq` package.
2. Run the app:
   ```bash
   streamlit run AIDoctor.py
   ```
3. Open the displayed URL in your browser.

## App Behavior

- The app collects the user's age and one or more symptoms.
- It formats the symptoms into a single prompt for the chatbot.
- The chatbot response is shown below the submit button.

## Screenshot

If you save a screenshot file in this folder, it will appear here.

![AI Doctor screenshot](screenshot.png)

> Note: Replace `screenshot.png` with your actual screenshot file name if needed.

## File Structure

- `AIDoctor.py` — the Streamlit app source file
- `README.md` — this documentation file
- `.env` — optional environment variables for API keys or settings

## Notes

- The prompt is intentionally designed to keep the chatbot output concise and focused on medicines, doses, instructions, and precautions.
- If you want to add more symptoms, simply update the `symptom_options` list in `AIDoctor.py`.
