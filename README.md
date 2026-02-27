# Local VM Auto-Scaling to Google Cloud

## Project Overview
This project demonstrates automatic scaling from a local virtual machine to Google Cloud when CPU usage exceeds 75 percent.

## Objective
To monitor system resource usage on a local VM and automatically launch a cloud VM when CPU utilization crosses a defined threshold.

## Technologies Used
- Oracle VirtualBox
- Ubuntu 22.04
- Python (psutil)
- Shell scripting
- Google Cloud Platform (Compute Engine)
- gcloud CLI

## Architecture Flow
Local VM → Monitoring Script → Threshold Detection → Scaling Trigger → Cloud VM Launch

## How It Works
1. Local VM runs a sample web application.
2. Python monitoring script continuously checks CPU usage.
3. When CPU usage exceeds 75 percent:
   - trigger.sh executes.
   - Google Cloud CLI launches a VM instance.
4. Cloud VM acts as additional compute capacity.

## Commands Used

### Start Web Server
python3 -m http.server 8000

### Run Monitoring Script
python3 monitor.py

### Generate CPU Load
stress --cpu 2

## Output
- CPU threshold detection
- Automatic cloud VM launch
- Logging of scaling events

## Author
Arpit
