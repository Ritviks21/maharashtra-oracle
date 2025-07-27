import streamlit as st
import google.generativeai as genai
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import pandas as pd
import io

# --- Part 1: Backend Functions ---
def setup_api():
    try:
        GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
        genai.configure(api_key=GEMINI_API_KEY)
        return genai.GenerativeModel('gemini-1.5-flash-latest')
    except Exception as e:
        st.error(f"Error setting up API key. Ensure it's in Streamlit Secrets. Error: {e}")
        return None

def run_agricultural_simulation(quantum_event_gates, initial_state):
    qc = QuantumCircuit(4, 4)
    if initial_state.get('monsoon') == 'Disrupted':
        qc.x(0)
    if initial_state.get('subsidies') == 'High':
        qc.x(2)
    qc.barrier()
    qc.cx(0, 1)
    qc.cx(1, 3)
    qc.cx(2, 1)
    qc.barrier()
    for gate_function in quantum_event_gates:
        gate_function(qc)
    qc.measure([0, 1, 2, 3], [0, 1, 2, 3])
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1024)
    result = job.result()
    return result.get_counts(qc)

def generate_narrative_report(chronicler_model, event_description, simulation_results, initial_state):
    state_mapping = {
        '0': {'Monsoon': 'Normal', 'Yield': 'Average', 'Subsidies': 'Standard', 'Demand': 'Stable'},
        '1': {'Monsoon': 'Disrupted', 'Yield': 'Poor', 'Subsidies': 'High', 'Demand': 'Volatile'}
    }
    formatted_results = []
    total_shots = sum(simulation_results.values())
    for state, count in simulation_results.items():
        demand_state = state_mapping[state[0]]['Demand']
        subsidy_state = state_mapping[state[1]]['Subsidies']
        yield_state = state_mapping[state[2]]['Yield']
        monsoon_state = state_mapping[state[3]]['Monsoon']
        probability = (count / total_shots) * 100
        formatted_results.append(
            f"- Outcome: Monsoon={monsoon_state}, Yield={yield_state}, Subsidies={subsidy_state}, Demand={demand_state}. Probability: {probability:.1f}%"
        )
    results_as_string = "\n".join(formatted_results)

    prompt = f"""
    You are a senior strategic advisor to the Maharashtra government, using a quantum simulation to forecast complex crises.

    **Intelligence Briefing:**

    **1. Initial Conditions:**
    The simulation started with a baseline of a '{initial_state['monsoon']}' monsoon and '{initial_state['subsidies']}' subsidies.

    **2. Crisis Scenario:**
    The following simultaneous events were introduced: {event_description}

    **3. Quantum Simulation Probabilities:**
    Our quantum model produced the following probabilistic outcomes:
    {results_as_string}

    **Your Task:**
    Do not just report the numbers. Provide a high-level strategic briefing for government leadership. Structure your response with the following markdown headings:

    ### Executive Summary
    In one paragraph, describe the most likely overall outcome of this combined crisis.

    ### Key Risks
    Based on the probabilities, list and explain the top 3 hidden or second-order risks (e.g., social unrest, supply chain collapse, specific market failures, political fallout).

    ### Strategic Recommendations
    Suggest 3 concrete, actionable policy recommendations to mitigate the predicted impact. Be specific.
    """
    response = chronicler_model.generate_content(prompt)
    return response.text

# --- Part 2: Streamlit User Interface ---

# --- UPDATED: New project name and icon ---
st.set_page_config(page_title="The Sahyadri Strategist", page_icon="🏔️")
st.title("🏔️ The Sahyadri Strategist")
st.write("A strategic forecasting tool using quantum simulation and generative AI.")

chronicler_model = setup_api()

st.sidebar.header("1. Set Initial Conditions")
historical_data_csv = """
year,rainfall_mm,subsidy_level
2022,1250,standard
2023,890,standard
2024,1100,high
2025,950,standard
"""
df = pd.read_csv(io.StringIO(historical_data_csv))
df['year'] = df['year'].astype(str)
year_options = ['Custom'] + df['year'].tolist()
selected_year = st.sidebar.selectbox("Select a Baseline Year or 'Custom'", year_options)

default_rainfall = 950
default_subsidy_index = 0
if selected_year != 'Custom':
    year_data = df[df['year'] == selected_year].iloc[0]
    default_rainfall = year_data['rainfall_mm']
    default_subsidy_index = 1 if year_data['subsidy_level'] == 'high' else 0

initial_rainfall = st.sidebar.slider("Annual Rainfall (mm)", 500, 2000, default_rainfall)
initial_subsidy = st.sidebar.selectbox("Initial Subsidy Level", ['Standard', 'High'], index=default_subsidy_index)

initial_state = {}
if initial_rainfall < 1000:
    initial_state['monsoon'] = 'Disrupted'
else:
    initial_state['monsoon'] = 'Normal'
if initial_subsidy == 'High':
    initial_state['subsidies'] = 'High'
else:
    initial_state['subsidies'] = 'Standard'

events = {
    "Severe Drought Hits": lambda qc: qc.x(0),
    "International Trade Ban Reduces Demand": lambda qc: qc.x(3),
    "Govt. Announces New High-Subsidy Package": lambda qc: qc.x(2),
    "No Major Event (Baseline Forecast)": lambda qc: qc.id(0)
}

st.sidebar.header("2. Create a Crisis Scenario")
selected_event_names = st.sidebar.multiselect(
    "Choose one or more events:",
    options=list(events.keys()),
    default=["No Major Event (Baseline Forecast)"]
)

if st.sidebar.button("Run Simulation"):
    if chronicler_model:
        with st.spinner("The Strategist is consulting the quantum realm..."):
            event_gates = [events[name] for name in selected_event_names]
            simulation_results = run_agricultural_simulation(event_gates, initial_state)
            st.subheader("Quantum Simulation Output")
            st.write(simulation_results)

        with st.spinner("The AI is writing the strategic briefing..."):
            event_description = " & ".join(selected_event_names)
            final_report = generate_narrative_report(chronicler_model, event_description, simulation_results, initial_state)
            st.subheader(f"📜 Strategic Briefing: {event_description}")
            st.markdown(final_report)
    else:
        st.error("Cannot run simulation. Please check API key setup.")
