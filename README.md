# WiFi Credential Extraction & Reverse Shell Demo

This repository presents a demonstration that reveals a potential security vulnerability in wireless networks. By leveraging a backdoor attack, the project not only extracts stored WiFi credentials from a target device but also establishes a reverse shell connection, granting the attacker command execution capabilities on the victim's machine.

## Overview

- **Technique**: Backdoor Attack & Reverse Shell
- **Programming Language**: Python
- **Tools Used**: Kivy for GUI, Kali Linux for demonstration
- **Vulnerabilities Exploited**: 
  1. Unsecured storage of WiFi credentials
  2. Reverse shell establishment on the target device

## Setup and Execution

1. **Deployment**: Run the `client.py` Python script on the victim's device.
2. **Connectivity**: Ensure both devices are connected to the same WiFi network.
3. **Configuration**: Obtain the victim's device IP address and specify it, along with the desired port number, in the `client.py` script.
4. **Reverse Shell**: On the attacker's machine, initiate a netcat listener using the command: `nc -lvp [portnumber]`.
5. **Command Interface**: Use the established connection to issue commands from the attacker's machine.
6. **Retrieval**: Upon the command "show wifi passwords," the victim's device sends back stored WiFi names and passwords.
7. **Command Execution**: The attacker can execute commands on the victim's machine via the established reverse shell.

## Code Breakdown

- **show()**: Retrieves and displays WiFi credentials stored on the victim's device using `netsh` commands.
- **main()**: Establishes a backdoor connection, handles commands from the attacker, and sets up the reverse shell.
- **App**: Kivy-based GUI, currently showcases a basic "Hello World" label.

## Usage

This repository is intended for educational and research purposes, emphasizing the importance of securing devices against potential threats and understanding the implications of reverse shell access.
