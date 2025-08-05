---
title: IoT Sensor Network
date: 2024-11-20
status: Testing Phase
image: images/network.png
text: NETWORK
lead: Alex Chen
members: 5
github: https://github.com/brh/sensor-mesh
---

# IoT Sensor Network

**Project Lead:** Alex Chen  
**Team Members:** 5 active contributors  
**Status:** Testing Phase  
**Started:** November 2024

## Overview

Creating a distributed mesh network of environmental sensors to monitor conditions and optimize workflows throughout the makerspace. This system provides real-time data on temperature, humidity, air quality, noise levels, and equipment usage patterns.

## Architecture

Our sensor network uses a hybrid approach combining WiFi and LoRaWAN technologies:

- **Edge Nodes:** ESP32-based sensors with multiple environmental sensors
- **Gateway Nodes:** Raspberry Pi 4 units managing local mesh networks
- **Central Hub:** Docker-based data processing and visualization platform
- **User Interface:** Web dashboard with real-time monitoring and alerts

## Deployed Sensors

Currently we have 24 sensor nodes deployed across the facility:

### Environmental Monitoring
- **Temperature/Humidity:** 12 nodes covering all work areas
- **Air Quality (PM2.5, VOCs):** 6 nodes near 3D printers and laser cutters
- **Sound Level:** 4 nodes monitoring noise in different zones
- **Light Levels:** 8 nodes for automated lighting optimization

### Equipment Monitoring
- **3D Printer Status:** Integrated with Octoprint instances
- **CNC Mill Usage:** Vibration and current monitoring
- **Laser Cutter Air Flow:** Ensuring proper ventilation
- **Power Consumption:** Smart outlets throughout the space

## Data Insights

Our network has already provided valuable insights:
- **Peak Usage Hours:** Identified optimal times for equipment maintenance
- **Energy Optimization:** Reduced power consumption by 15% through automated controls
- **Safety Improvements:** Early detection of ventilation issues and air quality problems
- **Space Utilization:** Data-driven decisions for workspace layout improvements

## Technology Stack

- **Hardware:** ESP32, Raspberry Pi 4, LoRa modules, various environmental sensors
- **Communication:** MQTT, LoRaWAN, WiFi mesh networking
- **Backend:** Python, InfluxDB time-series database, Grafana dashboards
- **Frontend:** React-based web application with real-time WebSocket updates

## Current Development

- 🔄 **Machine Learning Integration** - Predictive maintenance algorithms
- 🔄 **Mobile App** - Native iOS/Android apps for facility managers
- ⏳ **Integration APIs** - Connecting with building management systems
- ⏳ **Advanced Analytics** - Usage pattern recognition and optimization recommendations

## Achievements

- **99.2% Uptime** across all sensor nodes
- **Sub-second Latency** for critical alerts
- **15% Energy Savings** through automated optimizations
- **Featured Project** at MIT IoT Symposium 2024

## Get Involved

Looking for contributors with skills in:
- Embedded systems programming (ESP32, Arduino)
- Time-series databases and data visualization
- Machine learning for IoT applications
- PCB design and sensor integration
- React/TypeScript for frontend development

**Weekly meetings:** Tuesdays 6:30pm in the electronics lab  
**Contact:** alex.chen@bostonrobothackers.org