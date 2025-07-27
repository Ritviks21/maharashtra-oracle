<p align="center">
  <img src="https://github.com/Ritviks21/maharashtra-oracle/raw/main/docs/images/ChatGPT%20Image%20Jul%2027%2C%202025%2C%2005_33_02%20AM.png" alt="The Sahyadri Strategist Project Banner">
</p>

<h1 align="center">The Sahyadri Strategist</h1>
<p align="center">
  <i>An AGI-Powered Strategic Forecaster for Complex Agricultural Crises</i>
</p>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Version">
    <img src="https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit">
    <img src="https://img.shields.io/badge/Qiskit-%236929C4.svg?style=for-the-badge&logo=IBM&logoColor=white" alt="Qiskit">
    <img src="https://img.shields.io/badge/Google%20Gemini-8E77F0?style=for-the-badge&logo=google&logoColor=white" alt="Gemini">
</p>

<p align="center">
  <a href="#-live-demo">Live Demo</a> •
  <a href="#-our-journey">Our Journey</a> •
  <a href="#-key-features">Key Features</a> •
  <a href="#-tech-stack">Tech Stack</a> •
  <a href="#-how-to-contribute">Contribute</a>
</p>

---

## 🚀 Live Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ritviks21-maharashtra-oracle-app-forivi.streamlit.app/)

**Click the badge above or follow this link to interact with the live application:** [https://ritviks21-maharashtra-oracle-app-forivi.streamlit.app/](https://ritviks21-maharashtra-oracle-app-forivi.streamlit.app/)

![Project Demo GIF]
(https://www.veed.io/view/d2b21a67-9038-4b65-a6e8-b49523d1da53)

---

## 📖 Project Overview

**The Sahyadri Strategist** is a state-of-the-art strategic forecasting tool built to simulate the complex, cascading effects of overlapping crises on a regional agricultural system. By fusing an interactive classical model, a quantum simulation engine, and a powerful generative AI, this project moves beyond simple prediction to provide actionable, strategic advice for policymakers.

---

## 🚀 Our Journey: The Story of the Project

This project evolved through three distinct phases, each teaching a valuable lesson about building intelligent systems.

<details>
<summary><strong>V1: The Simple Calculator - A Deterministic Start</strong></summary>
<br>
Our first version was a classical model that could only handle single, isolated events. It was a simple `if-this-then-that` calculator.
<br><br>
💡 **Lesson Learned:** Real-world crises are complex, overlapping, and unpredictable. A simple calculator cannot capture the "ripple effect."
</details>

<details>
<summary><strong>V2: The Quantum Leap - Seeing the Ripple Effect</strong></summary>
<br>
We rebuilt the core using **Qiskit** to create a "Quantum Battlefield." By entangling variables like Monsoon, Yield, and Demand, we could finally simulate the cascading impact of multiple, simultaneous events. The model became powerful, but its output was raw probability data—difficult for a human to interpret.
<br><br>
💡 **Lesson Learned:** Powerful simulation is useless without powerful interpretation. Data needs a storyteller to become wisdom.
</details>

<details>
<summary><strong>V3: The AGI Strategist - The Final, Intelligent Core</strong></summary>
<br>
This final version integrated **Google's Gemini** not as a simple reporter, but as an autonomous strategic advisor. The AI's task is to receive the complex probabilistic data from the quantum simulation and translate it into a high-level strategic briefing, complete with risk analysis and policy recommendations.
<br><br>
✅ **The Result:** A true strategic tool that doesn't just predict the future but helps you shape it, demonstrating a complete pipeline from user-defined scenario to actionable, AI-generated strategy.
</details>

---

## ✨ Key Features

- **Interactive Scenario Builder**: Set initial conditions using historical data presets or manually define a custom baseline with interactive widgets.
- **Complex Crisis Simulation**: A multi-select interface allows for combining multiple, overlapping events into a single simulation.
- **Quantum "Ripple Effect" Engine**: Uses a Qiskit-based quantum circuit to model the non-linear, second-order effects of crises.
- **AI-Powered Strategic Briefings**: The final output is a full strategic report containing an executive summary, risk analysis, and actionable policy recommendations.

---

## 🛠️ Tech Stack

| Streamlit | Qiskit | Gemini | Python | Pandas |
| :---: | :---: | :---: | :---: | :---: |
| <img src="https://github.com/Ritviks21/maharashtra-oracle/raw/main/docs/images/ChatGPT%20Image%20Jul%2027%2C%202025%2C%2005_45_17%20AM.png" width="48"> | <img src="https://github.com/Ritviks21/maharashtra-oracle/raw/main/docs/images/ChatGPT%20Image%20Jul%2027%2C%202025%2C%2005_45_50%20AM.png" width="48"> | <img src="https://github.com/Ritviks21/maharashtra-oracle/raw/main/docs/images/ChatGPT%20Image%20Jul%2027%2C%202025%2C%2005_48_43%20AM.png" width="48"> | <img src="https://github.com/Ritviks21/maharashtra-oracle/raw/main/docs/images/ChatGPT%20Image%20Jul%2027%2C%202025%2C%2005_47_24%20AM.png" width="48"> | <img src="https://github.com/Ritviks21/maharashtra-oracle/raw/main/docs/images/ChatGPT%20Image%20Jul%2027%2C%202025%2C%2005_50_44%20AM.png" width="48"> |

---

## 🚀 Getting Started

<details>
<summary>Click here for instructions to run this project yourself.</summary>

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/Ritviks21/maharashtra-oracle.git](https://github.com/Ritviks21/maharashtra-oracle.git)
    cd maharashtra-oracle
    ```

2.  **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set Up API Key**
    Create a `.streamlit/secrets.toml` file and add your Google Gemini API key:
    ```toml
    GEMINI_API_KEY = "YOUR_API_KEY_HERE"
    ```

4.  **Run the App**
    ```bash
    streamlit run app.py
    ```
</details>

---

## 🤝 How to Contribute

Contributions are always welcome! This project demonstrates a unique proof-of-concept, and there are many ways to expand on it.

### Areas for Contribution
* **Expand the Quantum Model**: Add more qubits to represent new variables (e.g., `Transportation`, `Global Prices`) and design their entangled relationships.
* **Integrate Real-Time Data**: Connect the app to a live weather API to set the initial monsoon state based on real-time data.
* **Enhance the AI's "Tools"**: Give the AI more "tools" to call, such as a function to look up historical data or current market prices, to enrich its strategic analysis.

---

## 🔗 Connect with Me

<p align="left">
<a href="https://github.com/Ritviks21" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/github.svg" alt="Ritviks21" height="30" width="40" /></a>
<a href="https://x.com/gemdata21" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/twitter.svg" alt="gemdata21" height="30" width="40" /></a>
<a href="https://huggingface.co/srits21" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hugging-face.svg" alt="srits21" height="30" width="40" /></a>
</p>
