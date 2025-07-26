
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

def run_agricultural_simulation(quantum_event_gate, initial_state):
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
    quantum_event_gate(qc)
    qc.measure([0, 1, 2, 3], [0, 1, 2, 3])
    simulator = AerSimulator()
    job = simulator.run(qc, shots=1024)
    result = job.result()
    return result.get_counts(qc)

def generate_narrative_report(chronicler_model, event_description, simulation_results):
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
    prompt = f'''
    You are an expert economic analyst for Maharashtra.
    **Scenario Briefing:** Our simulation started from a baseline reflecting recent history. We then introduced a major event: "{event_description}"
    **Quantum Simulation Results:** Our model produced these probabilistic outcomes: {results_as_string}
    **Your Task:** Translate these probabilities into a clear news-style report explaining the likely impact.
    '''
    response = chronicler_model.generate_content(prompt)
    return response.text

# --- Part 2: Streamlit User Interface ---
st.set_page_config(page_title="Maharashtra Agricultural Oracle", page_icon="🔮")
st.title("🔮 The Maharashtra Agricultural Oracle")
st.write("This tool uses a quantum-inspired simulation and generative AI to forecast the impact of major events on the state's agriculture.")

chronicler_model = setup_api()

historical_data_csv = '''
year,rainfall_mm,subsidy_level
2022,1250,standard
2023,890,standard
2024,1100,high
2025,950,standard
'''
df = pd.read_csv(io.StringIO(historical_data_csv))
with st.expander("Show Most Recent Historical Data"):
    st.write("The simulation starts from the conditions of the most recent year's data:")
    st.dataframe(df.tail(1))

latest_data = df.iloc[-1]
initial_state = {}
if latest_data['rainfall_mm'] < 1000:
    initial_state['monsoon'] = 'Disrupted'
else:
    initial_state['monsoon'] = 'Normal'
if latest_data['subsidy_level'] == 'high':
    initial_state['subsidies'] = 'High'
else:
    initial_state['subsidies'] = 'Standard'

events = {
    "Severe Drought Hits": lambda qc: qc.x(0),
    "International Trade Ban Reduces Demand": lambda qc: qc.x(3),
    "Govt. Announces New High-Subsidy Package": lambda qc: qc.x(2),
    "No Major Event (Baseline Forecast)": lambda qc: qc.id(0)
}

st.sidebar.header("Select a Scenario")
selected_event_name = st.sidebar.selectbox("Choose a 'what if' event:", options=list(events.keys()))

if st.sidebar.button("Run Oracle Simulation"):
    if chronicler_model:
        with st.spinner("The Oracle is consulting the quantum realm..."):
            event_gate = events[selected_event_name]
            simulation_results = run_agricultural_simulation(event_gate, initial_state)
            st.subheader("Quantum Simulation Output")
            st.write(simulation_results)
        with st.spinner("The Chronicler is writing the report..."):
            final_report = generate_narrative_report(chronicler_model, selected_event_name, simulation_results)
            st.subheader(f"📜 Oracle's Report: {selected_event_name}")
            st.markdown(final_report)
    else:
        st.error("Cannot run simulation. Please check API key setup.")
