import streamlit as st
from PIL import Image
import io

st.set_page_config(layout="wide")
st.title("Culinary AI Assistant")

col1, col2 = st.columns([1, 2])

with col1: 
    st.header("Cooking Parameters")
    

    cooking_stage = st.selectbox(
        "Current Cooking Stage",
        ["Raw", "Prepping", "Midway", "Almost Done", "Well Done"]
    )
    
    time_elapsed = st.number_input("Time Elapsed (minutes)", min_value=0, max_value=240, value=15)
    temperature = st.number_input("Temperature (°C)", min_value=0, max_value=300, value=180)
    
    smell = st.text_input("Smell Description", "Savory, garlicky")
    utensil = st.selectbox(
        "Cooking Utensil",
        ["Skillet", "Oven", "Grill", "Pot", "Air Fryer", "Slow Cooker"]
    )
    
    recipe_name = st.text_input("Recipe Name", "Garlic Herb Chicken")
    
    if st.button("Analyze Cooking Progress", use_container_width=True):
        st.session_state.analysis_results = {
            'time_remaining': 12, 
            'doneness': '75% cooked',
            'recommendation': 'Reduce heat to 160°C and cook for 12 more minutes'
        }

with col2: 
    st.header("Food Image")
    
    uploaded_file = st.file_uploader(
        "Upload cooking progress photo",
        type=["jpg", "jpeg", "png"],
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        image = Image.open(io.BytesIO(uploaded_file.getvalue()))
        st.image(image, caption="Current Cooking State", use_column_width=True)
        
        if 'analysis_results' in st.session_state:
            st.subheader("Cooking Analysis")
            st.metric("Estimated Time Remaining", f"{st.session_state.analysis_results['time_remaining']} minutes")
            st.metric("Current Doneness", st.session_state.analysis_results['doneness'])
            st.write("**Recommendation:**", st.session_state.analysis_results['recommendation'])
