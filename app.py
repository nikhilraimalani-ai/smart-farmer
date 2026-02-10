import streamlit as st
import google.generativeai as genai

# YOUR KEY IS NOW INSERTED HERE
API_KEY = "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"

# Setup Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# App Interface
st.set_page_config(page_title="AgroNova Smart Assistant", page_icon="🌱")
st.title("🌱 AgroNova: Smart Farming Assistant")
st.markdown("### Region-Specific Advice for India, Ghana, and Canada")

# User Inputs
col1, col2 = st.columns(2)
with col1:
    location = st.selectbox("Select Region:", ["India", "Ghana", "Canada"])
with col2:
    crop = st.text_input("What crop are you growing?", placeholder="e.g. Wheat, Maize")

stage = st.select_slider("Crop Stage:", options=["Sowing", "Growth", "Flowering", "Harvesting"])

if st.button("Generate Farming Plan"):
    # The prompt below handles Step 4 (Formatting & Reasoning) of your FA 2
    prompt = f"""
    Provide expert agricultural advice for growing {crop} in {location} during the {stage} stage.
    
    Requirements:
    1. Use a bulleted list for actions.
    2. For every action, provide a 'Why it matters' explanation (Reasoning).
    3. Use simple language for farmers.
    4. Ensure the advice is specific to the climate of {location}.
    """
    
    with st.spinner("Analyzing agricultural data..."):
        try:
            response = model.generate_content(prompt)
            st.success("Analysis Complete!")
            st.markdown("---")
            st.markdown(response.text)
        except Exception as e:
            st.error("Make sure your API key is active and has credits.")

# Step 5: Feedback Checklist (Required for FA 2 marks)
st.sidebar.markdown("### Validation Checklist")
st.sidebar.checkbox("Is the advice region-specific?")
st.sidebar.checkbox("Is the reasoning clear?")
st.sidebar.checkbox("Is the language simple?")