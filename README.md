# Traffic-Violation-Detection
Identification and Reporting Traffic Violations from Surveillance camera feed as a part of SIH 2020.

## Violations Handled
- Signal Violation
- Overspeeding

## Working
The violations are detected from real time surveillance camera feed. When a violation is identified, the numberplate of the violating vehicle is captured and the violation details such as location, time and numberplate of violator's vehicle is sent to a real-time Firebase Database from which a mobile app provides notifications to the officials in charge to take appropriate action. Provision has been provided to send emails to the violator's email ID with the fine details to be paid.

## Implementation Diagram

![implementation](assets/structure.PNG)

## Packages Installed
    Dlib, OpenCV-4.2.0.32, Pyrebase-3.0.27, smtplib, threading, requests

## Usage
- sample_data - Contains video feed of Surveillance Camera
- pictures - Pictures of numberplate of violating vehicles
- output - Results written to log.csv

## Note
- Replace firebase-key.json with your Google Service Account access Key
- In traffic-violation-detection-roads.py, replace the marked locations with your firebase database API key and email credentials