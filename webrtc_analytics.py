import json
import matplotlib.pyplot as plt

# Load the WebRTC data from the file
file_path = "dump/webrtc_internals_dump.txt"
with open(file_path, 'r') as file:
    data = json.load(file)
