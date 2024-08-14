import streamlit as st

# Define emission factors (example values, replace with accurate data)
EMISSION_FACTORS = {
    "India": {
        "Transportation": 0.14,  # kgCO2/km
        "Electricity": 0.82,  # kgCO2/kWh
        "Diet": 1.25,  # kgCO2/meal
        "Waste": 0.1,  # kgCO2/kg
    },
    "United States of America": {
        "Transportation": 0.15,  # kgCO2/km
        "Electricity": 0.85,  # kgCO2/kWh
        "Diet": 1.3,  # kgCO2/meal
        "Waste": 0.05,  # kgCO2/kg
    },
}

# Set wide layout and page name
st.set_page_config(layout="wide", page_title="Personal Carbon Calculator")

# Streamlit app code
st.title("Personal Carbon Calculator App ⚠️")

# User inputs
st.subheader("🌍 Your Country")
country = st.selectbox("Select", ["India", "United States of America"])

col1, col2 = st.columns(2)

with col1:
    st.subheader("🚗 Daily commute distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("💡 Monthly electricity consumption (in kWh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🗑️ Waste generated per week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍽️ Number of meals per day")
    meals = st.number_input("Meals", 0, key="meals_input")

# Normalize inputs
if distance > 0:
    distance = distance * 365  # Convert daily distance to yearly
if electricity > 0:
    electricity = electricity * 12  # Convert monthly electricity to yearly
if meals > 0:
    meals = meals * 365  # Convert daily meals to yearly
if waste > 0:
    waste = waste * 52  # Convert weekly waste to yearly

# Calculate carbon emissions
transportation_emissions = EMISSION_FACTORS[country]["Transportation"] * distance
electricity_emissions = EMISSION_FACTORS[country]["Electricity"] * electricity
diet_emissions = EMISSION_FACTORS[country]["Diet"] * meals
waste_emissions = EMISSION_FACTORS[country]["Waste"] * waste

# Convert emissions to tonnes and round off to 2 decimal points
transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
diet_emissions = round(diet_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

# Calculate total emissions
total_emissions = round(
    transportation_emissions + electricity_emissions + diet_emissions + waste_emissions, 2
)

if st.button("Calculate CO2 Emissions"):

    # Display results
    st.header("Results")

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Carbon Emissions by Category")
        st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
        st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
        st.info(f"🍽️ Diet: {diet_emissions} tonnes CO2 per year")
        st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.success(f"🌍 Your total carbon footprint is: {total_emissions} tonnes CO2 per year")
        if country == "India":
            st.warning("In 2021, CO2 emissions per capita for India was around 1.8 tonnes of CO2 per capita.")
        else:
            st.warning("In 2021, CO2 emissions per capita for the USA was 14.24 tonnes of CO2 per capita. The global average is about 4.7 tonnes.")

st.title('EcoOptimizer Carbon Footprint Calculator')

# Introduction
st.write('''
This tool calculates the Software Carbon Intensity (SCI) for EcoOptimizer, 
an AI-powered energy management system for commercial buildings by EcoTech Solutions.
''')

# Inputs with default values from the case study
st.header('Input the following details:')
E = st.number_input('Energy consumed per transaction (E in kWh):', value=0.05, format="%.2f")
I = st.number_input('Carbon intensity of the energy (I in kg CO₂e per kWh):', value=0.4, format="%.2f")
M = st.number_input('Embodied carbon of the hardware (M in kg CO₂e):', value=200.0, format="%.2f")
R = st.number_input('Functional unit (Transactions processed per 1,000):', value=1000, format="%d")

# Calculation Button
if st.button('Calculate Software Carbon Intensity (SCI)'):
    days_in_service_life = 365 * 3  # 3 years
    daily_E = E * (R / 1000)  # Daily energy consumption for R transactions
    daily_emissions = daily_E * I  # Daily operational emissions
    daily_embodied_emissions = M / days_in_service_life  # Daily share of embodied carbon
    SCI = daily_emissions + daily_embodied_emissions
    st.subheader('Calculated SCI:')
    st.markdown(f"<span style='color:red'>{SCI:.3f} kg CO₂e per day for {R} transactions</span>", unsafe_allow_html=True)
    st.write('This measurement provides insight into the carbon footprint of your software, aiding in identifying areas for improvement and reduction.')
else:
    st.write('Enter the values and click calculate.')
