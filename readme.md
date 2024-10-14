# WebRTC Internals Dump Analytics

## Overview

This **Python analytics script** processes WebRTC internals dump files to extract and visualize important metrics related to network performance, video quality, and overall real-time communication health. It provides a detailed analysis of metrics such as frame rate, packet loss, latency, jitter, and more, giving developers and testers a deeper insight into how WebRTC-based applications behave under different conditions.

## Features
- **Extract Key WebRTC Metrics**: Automatically parses WebRTC internals dump to extract metrics such as:
  - Frames per second (FPS)
  - Packet loss
  - Jitter
  - Round Trip Time (RTT)
  - Freeze count
  - Bitrate (Bytes received)
  - Codec information
  - NACK (Negative Acknowledgments)
- **Visualize Network and Call Metrics**: Generates easy-to-understand plots for key performance indicators, helping you quickly identify issues affecting real-time communication.
- **Detailed Call and Network Analysis**: Focuses on both audio and video call quality metrics, including sync between audio and video streams.

---

## Table of Contents

1. [Installation](#installation)
2. [Usage](#usage)
3. [Metrics Explained](#metrics-explained)
4. [Examples](#examples)
5. [Contributing](#contributing)

---

## Installation

### Prerequisites
- Python 3.x
- Required Python libraries:
  - `pandas`
  - `matplotlib`

### Steps to Install:

1. Clone this repository:
    ```bash
    git clone https://github.com/imgoomes/webrtc-dump-analytics.git
    cd webrtc-dump-analytics
    ```

2. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have a **WebRTC internals dump file** to analyze.

---

## Usage

1. Place your WebRTC internals dump file in the project directory.

2. Run the analytics script:
    ```bash
    python webrtc_analytics.py /path/to/webrtc_internals_dump.txt
    ```

3. The script will extract the following metrics from the dump file and generate plots for each:
   - Frames per second (FPS)
   - Packet loss
   - Jitter
   - Round Trip Time (RTT)
   - Freeze count
   - Bitrate (Bytes received)
   - Codec information
   - NACK (Negative Acknowledgments)
   - Resolution changes
   - Audio input/output levels

4. The plots will be displayed, showing how each metric changes over time. Results will also be logged to the terminal.

---

## Metrics Explained

Here are the metrics the script extracts and visualizes:

1. **Frames Per Second (FPS)**:
   - Measures the smoothness of the video. Higher FPS means smoother video playback.

2. **Packet Loss**:
   - Indicates the number of packets lost during the WebRTC session. Packet loss directly affects audio and video quality.

3. **Jitter**:
   - Represents the variation in packet arrival times. High jitter can cause choppy audio and video.

4. **Round Trip Time (RTT)**:
   - Measures the time taken for a signal to travel from the sender to the receiver and back. Higher RTT causes noticeable delays in communication.

5. **Freeze Count**:
   - Tracks how often the video freezes during the session. Frequent freezes indicate network or performance issues.

6. **Bitrate (Bytes Received)**:
   - Represents the amount of data (in kilobytes) received for audio and video streams. Higher bitrate generally indicates better video and audio quality.

7. **Codec Information**:
   - Shows the types of codecs used for encoding and decoding audio and video. Different codecs have different performance characteristics.

8. **NACK (Negative Acknowledgments)**:
   - Monitors how often packets need to be re-sent. High NACK counts can indicate network issues or packet loss.

9. **Resolution Changes**:
   - Dynamic resolution changes in the stream due to network adaptation. Frequent changes might indicate unstable network conditions.

10. **Audio Input/Output Levels**:
    - Tracks the levels of audio input and output over time. Ensures that audio is consistently captured and transmitted.

---

## Examples

### Sample Usage

1. To analyze the WebRTC dump file:
    ```bash
    python webrtc_analytics.py webrtc_internals_dump.txt
    ```

2. You will see output like this in the terminal:
    ```
    Analyzing WebRTC metrics...
    Extracting Frames Per Second (FPS)...
    Generating FPS plot...
    Extracting Packet Loss data...
    Generating Packet Loss plot...
    ...
    Analysis completed.
    ```

3. Visual plots will be displayed for each metric, such as:
   - **FPS over Time**
   - **Packet Loss over Time**
   - **Round Trip Time (RTT) over Time**
   - **Jitter over Time**
   - **Bitrate (Bytes Received) over Time**

---

## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request for any bug fixes or feature enhancements.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

This README provides a clear overview of the **WebRTC Internals Analytics Script**, detailing the metrics it extracts and how to use it for performance analysis.