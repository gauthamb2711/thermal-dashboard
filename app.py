import streamlit as st
import random
import time

st.title("🔥 Thermal-Aware Task Monitoring Dashboard")

# Placeholders for live updates
cpu_placeholder = st.empty()
gpu_placeholder = st.empty()
bat_placeholder = st.empty()
alert_placeholder = st.empty()

while True:
    # Simulated sensor data
    cpu_temp = random.randint(30, 90)
    gpu_temp = random.randint(30, 85)
    bat_temp = random.randint(25, 60)

    # Show values
    cpu_placeholder.metric("CPU Temperature", f"{cpu_temp} °C")
    gpu_placeholder.metric("GPU Temperature", f"{gpu_temp} °C")
    bat_placeholder.metric("Battery Temperature", f"{bat_temp} °C")

    # Alerts
    if cpu_temp > 80:
        alert_placeholder.error("⚠️ CPU Overheating! Tasks will be rescheduled...")
    elif gpu_temp > 75:
        alert_placeholder.warning("⚠️ GPU running hot! Throttling applied.")
    else:
        alert_placeholder.success("✅ System stable")

    time.sleep(2)
