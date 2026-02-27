echo "ALERT: CPU overload detected!" >> log.txt
gcloud compute instances start autoscalevm --zone=asia-south1-b

