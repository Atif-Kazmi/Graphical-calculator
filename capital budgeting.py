import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

# Function to run Monte Carlo simulation
def run_monte_carlo_simulation(initial_investment, project_duration, discount_rate, mean_cash_flows, std_dev, n_simulations):
    npv_results = []
    
    for i in range(n_simulations):
        cash_flows = []
        for j in range(project_duration):
            # Randomly vary cash flows based on normal distribution
            cash_flow = np.random.normal(mean_cash_flows[j], std_dev[j])
            # Calculate the discounted cash flow
            discounted_cash_flow = cash_flow / ((1 + discount_rate) ** (j + 1))
            cash_flows.append(discounted_cash_flow)
        
        # Calculate Net Present Value (NPV)
        npv = sum(cash_flows) - initial_investment
        npv_results.append(npv)
    
    return np.array(npv_results)

# Main Streamlit app function
def main():
    st.title("Capital Budgeting Monte Carlo Simulation")
    
    # Input: Initial investment
    initial_investment = st.number_input("Initial Investment ($)", min_value=0, value=100000)

    # Input: Project duration in years
    project_duration = st.slider("Project Duration (Years)", min_value=1, max_value=20, value=5)
    
    # Input: Discount rate
    discount_rate = st.number_input("Discount Rate (e.g., 0.08 for 8%)", min_value=0.0, max_value=1.0, value=0.08)
    
    # Input: Cash flow estimation for each year
    mean_cash_flows = []
    std_dev = []
    
    for year in range(1, project_duration + 1):
        mean_flow = st.number_input(f"Estimated Cash Flow for Year {year} ($)", value=30000)
        mean_cash_flows.append(mean_flow)
        
        std_deviation = st.number_input(f"Standard Deviation for Year {year} Cash Flow ($)", value=5000)
        std_dev.append(std_deviation)
    
    # Input: Number of simulations
    n_simulations = st.number_input("Number of Monte Carlo Simulations", min_value=1000, max_value=100000, value=10000)

    # Run the simulation when the user clicks the button
   
