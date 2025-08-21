import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# -----------------------------
# 🟢 1. Thermal Monitoring Module
# -----------------------------
def get_temperatures():
    # Mock sensor values (replace with psutil / OS APIs if available)
    cpu_temp = random.randint(40, 95)
    gpu_temp = random.randint(35, 90)
    bat_temp = random.randint(30, 60)
    return cpu_temp, gpu_temp, bat_temp

# -----------------------------
# 🟢 2. Dynamic Task Scheduling Module
# -----------------------------
def schedule_task(cpu_temp, gpu_temp):
    if cpu_temp > 80:
        return "Migrating tasks to GPU (CPU hot)"
    elif gpu_temp > 75:
        return "Shifting load to CPU (GPU hot)"
    else:
        return "Normal scheduling"

# -----------------------------
# 🟢 3. Thermal-Aware Feedback & Control Module
# -----------------------------
def thermal_feedback(cpu_temp, gpu_temp, bat_temp):
    if cpu_temp > 85:
        return "⚠️ CPU overheating! Throttling applied."
    elif gpu_temp > 80:
        return "⚠️ GPU overheating! Lowering GPU frequency."
    elif bat_temp > 50:
        return "⚠️ Battery too hot! Reducing charge speed."
    else:
        return "✅ System stable"

# -----------------------------
# 🟢 Streamlit App (Integration)
# -----------------------------
st.set_page_config(page_title="Thermal-Aware Task Assignment", layout="wide")
st.title("🌡️ Thermal-Aware Task Assignment System")

# Containers for dashboard
col1, col2, col3 = st.columns(3)
alert_placeholder = st.empty()
schedule_placeholder = st.empty()
chart_placeholder = st.empty()

# Store history for graphs
cpu_history, gpu_history, bat_history = [], [], []

# Run monitoring loop
iterations = st.slider("Select number of cycles to simulate", 5, 50, 20)
interval = st.slider("Update interval (seconds)", 1, 5, 2)

for i in range(iterations):
    cpu_temp, gpu_temp, bat_temp = get_temperatures()

    # Show live metrics
    col1.metric("CPU Temp", f"{cpu_temp} °C")
    col2.metric("GPU Temp", f"{gpu_temp} °C")
    col3.metric("Battery Temp", f"{bat_temp} °C")

    # Scheduler output
    decision = schedule_task(cpu_temp, gpu_temp)
    schedule_placeholder.info(f"Scheduler Decision: {decision}")

    # Feedback alerts
    feedback = thermal_feedback(cpu_temp, gpu_temp, bat_temp)
    if "⚠️" in feedback:
        alert_placeholder.error(feedback)
    else:
        alert_placeholder.success(feedback)

    # Save history
    cpu_history.append(cpu_temp)
    gpu_history.append(gpu_temp)
    bat_history.append(bat_temp)

    # Live line graph
    fig, ax = plt.subplots()
    ax.plot(cpu_history, label="CPU")
    ax.plot(gpu_history, label="GPU")
    ax.plot(bat_history, label="Battery")
    ax.set_title("Temperature Trends")
    ax.set_xlabel("Time (cycles)")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    chart_placeholder.pyplot(fig)

    time.sleep(interval)
