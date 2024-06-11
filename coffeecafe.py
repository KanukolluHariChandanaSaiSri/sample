# Automated Espresso Bean Inventory Management System for Chandana's Café
#
# Overview of the Project:
# Project Purpose:
#     To automate the management of espresso bean stock in a coffee machine, 
#     resulting in consistent availability and optimal inventory levels.
#
# Key Features:
#     - IoT Simulation: Uses data from IoT devices to update bean usage and stock levels in real time.
#     - Predictive Analytics: Uses historical usage data to predict when beans will run out, 
#       triggering automatic refill alerts.
#     - Dashboard: Allows for real-time visibility of stock levels and predictive reordering times, 
#       making inventory management more efficient.
#
# Special Features:
#     - Automated Alerts: Notifies you when stock is low, which may trigger an order for more beans.
#     - Adaptive Thresholds: Dynamically adjusts predictions and alerts based on recent usage trends, 
#       thereby improving operational decisions.
#     - User-Friendly Interface: A simple dashboard providing a quick overview of stock levels 
#       and operational metrics.
#
# Real-world Application Potential:
#     Integrating this system can improve operational efficiency by reducing manual checks and 
#     ensuring uninterrupted service. It is a valuable tool for coffee shops looking to optimize 
#     their operations through technology.


#CODE:




# Initial stock of espresso coffee beans in grams
espresso_beans_stock = 5000  
# History of espresso bean usage to simulate input from an IoT device and for predictive analytics
espresso_usage_history = []  

def update_espresso_stock(usage):
    # Simulates updating the stock of espresso beans based on reported usage from an IoT device.
    # Args:
    # usage (int): The amount of espresso beans used.
    global espresso_beans_stock
    espresso_beans_stock -= usage  # Reduce stock by the reported usage
    espresso_usage_history.append(usage)  # Keep track of usage for analytics
    print(f"Stock updated: Current espresso beans stock is {espresso_beans_stock} grams")

def check_espresso_stock():
    # Checks if the espresso bean stock is below the threshold and alerts for refill.
    if espresso_beans_stock <= predictive_reorder_threshold():
        print("Alert: Low espresso bean stock. Please reorder via the app.")

def predictive_reorder_threshold():
    # Calculates a predictive reorder threshold based on recent espresso bean usage history.
    # Returns:
    # int: The calculated threshold at which a reorder alert should be triggered.
    if len(espresso_usage_history) > 3:
        # Calculate average usage of the last 3 entries for better prediction
        average_usage = sum(espresso_usage_history[-3:]) / 3
        # Set threshold based on average usage to predict future needs
        return espresso_beans_stock - average_usage * 3
    return 1000  # Default threshold if not enough historical data

def simulate_iot_espresso_interaction():
    # Simulates an interaction from an IoT device reporting espresso bean usage.
    # Note: In real application, this would be replaced by actual data input from IoT devices.
    usage = 100  # Simulate usage reported by the device (e.g., after making several cups of coffee)
    update_espresso_stock(usage)

def display_espresso_dashboard():
    # Displays a simple dashboard showing current stock levels and predictions for espresso beans.
    print(f"Dashboard - Current Espresso Beans Stock: {espresso_beans_stock} grams")
    if len(espresso_usage_history) > 3:
        # Provide an estimate on when to reorder based on current usage trends
        print(f"Predicted need for reorder in the next {espresso_beans_stock / (sum(espresso_usage_history[-3:]) / 3):.2f} checks")

# Main function to run the simulation
def main():
    # Main function to run the simulation.
    # It simulates 20 cycles of espresso bean usage and monitoring.
    for _ in range(20):  # Simulate 20 checks
        simulate_iot_espresso_interaction()
        check_espresso_stock()
        display_espresso_dashboard()

main()