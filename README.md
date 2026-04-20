
# 1. Problem Statement
Traditional network management often lacks real-time visibility into physical link changes. This project implements a Software-Defined Networking (SDN) solution to dynamically detect and log topology changes (link additions and removals). Using a centralized POX controller, the system maintains an accurate network map and ensures functional forwarding between hosts through reactive flow provisioning.

# 2. Setup & Execution Steps
Prerequisites
Ubuntu 20.04 LTS
Mininet Network Emulator
POX Controller (Gar Branch / Python 3 compatible)

Execution Sequence
Cleanup: Clear previous network states.

```Bash
sudo mn -c
Start Controller: In a new terminal, launch the POX controller with the topology detector module.
```
```
Bash
cd ~/pox
python3 pox.py openflow.discovery detector
Start Topology: In a second terminal, launch the custom Mininet topology.
```
```
Bash
sudo mn --custom ~/sdn_project/topology.py --topo mytopo --controller remote
```
# 3. Expected Output
Controller: Should log "Switch connected" for each switch and "Link Added" for each established link.

Mininet: Should show a successful handshake with the remote controller and provide a CLI prompt.

Functionality: Hosts should be able to ping each other once the controller installs the necessary flow rules.

# 4. Proof of Execution
## A. Functional Correctness (Ping Test)
End-to-end connectivity is verified using the ping command. The initial packet loss observed is expected as the controller reactively installs flow rules upon the first PacketIn event.
[View Project Proof of Execution (DOCX)](https://docs.google.com/document/d/1-NPUBrB1jwa92FU-MYGR6P3o6qUY3YW5/edit)


## B. Performance Observation (iperf)
Network throughput was measured using iperf, showing a bandwidth of approximately 34.5 Gbits/sec between virtual hosts.

## C. Topology Monitoring (Controller Logs)
The POX terminal demonstrates real-time detection of link establishment and removal. The "Topology Map" updates dynamically as links are toggled.

## D. SDN Logic (Flow Table Entries)
Using ovs-ofctl dump-flows, we can verify that the controller successfully pushed explicit "Match-Action" rules to the switches, utilizing actions=FLOOD for broad discovery and forwarding.

# 5. Test Scenarios
Normal Operation: Initial discovery of switches s1 and s2 and the link between them, followed by successful iperf performance testing.

## Failure Scenario:
Manual link down/up simulation. The controller successfully detects the Link Removed event, updates the internal map to an empty state [], and re-detects the link upon restoration.

# 6. References
POX Controller Documentation
Mininet Walkthrough
OpenFlow Switch Specification v1.0.0
