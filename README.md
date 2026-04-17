Based on the project guidelines and your successful implementation, here is a comprehensive description of your **SDN Topology Change Detector** project. [cite_start]You can use this content directly for your GitHub README and project documentation to fulfill the **Problem Statement** and **Problem Understanding** requirements[cite: 30, 31, 39].

### Project Title: SDN-Based Dynamic Topology Change Detector

---

### 1. Problem Statement
In traditional networking, detecting a link failure or a new switch connection can be slow, often relying on distributed protocols like Spanning Tree (STP). In a Software-Defined Networking (SDN) environment, we aim to centralize this intelligence. The objective of this project is to implement an SDN controller that dynamically monitors switch and link events, updates a global topology map in real-time, and logs these changes for network administration.

### 2. Objectives
* **Real-time Monitoring**: Automatically detect when a switch connects to the controller or when a link between two switches is established or severed.
* [cite_start]**Dynamic Forwarding**: Implement a "Learning Switch" logic that handles `packet_in` events to install explicit match-action flow rules, allowing hosts to communicate across the discovered topology[cite: 5, 10, 39].
* **Network Visibility**: Maintain an internal data structure (Topology Map) that represents the current state of the network at any given moment.

### 3. System Architecture
[cite_start]This project utilizes a decoupled SDN architecture consisting of two main planes[cite: 4, 39]:
* **Control Plane (POX Controller)**: Acts as the "brain" of the network. [cite_start]It uses the `openflow.discovery` module to send and receive LLDP packets, which helps in identifying links between OpenFlow-enabled switches[cite: 8, 10].
* **Data Plane (Mininet)**: Simulates the network hardware. [cite_start]It consists of Open vSwitches (OVS) and virtual hosts that follow the flow rules pushed by the POX controller[cite: 8, 24].

### 4. Technical Implementation (SDN Logic)
The project is built using Python and the OpenFlow 1.0 protocol. [cite_start]The core logic includes[cite: 9, 10, 39]:
* **Event Listeners**: The controller listens for `ConnectionUp` (switch joins) and `LinkEvent` (link added/removed) triggers.
* **Match-Action Flow Rules**: When a switch receives a packet it doesn't recognize, it sends a `packet_in` to the controller. [cite_start]The controller then calculates the output and installs a flow rule with a specific "Match" (source/destination) and "Action" (Forward/Flood)[cite: 5, 10, 39].

### 5. Test Scenarios and Validation
[cite_start]To ensure functional correctness, the project was validated through two primary scenarios[cite: 14, 15, 17]:
1.  [cite_start]**Normal Operation**: Successful end-to-end connectivity between hosts (`ping`) and throughput measurement using `iperf`[cite: 11, 37].
2.  **Failure Scenario**: Manually disabling a switch link in Mininet and verifying that the controller immediately detects the loss, logs the update, and modifies the topology map.

### 6. Tools Used
* [cite_start]**Mininet**: For network emulation and topology creation[cite: 8].
* [cite_start]**POX**: Python-based SDN controller for implementing network logic[cite: 8].
* [cite_start]**OpenFlow**: The communication protocol between the control and data planes[cite: 3, 9].
* [cite_start]**iperf**: For performance observation and throughput analysis[cite: 11, 37].
