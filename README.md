# WiFi Credential Extraction & Reverse Shell Demo

This repository presents a demonstration that reveals a potential security vulnerability in wireless networks. By leveraging a backdoor attack, the project not only extracts stored WiFi credentials from a target device but also establishes a reverse shell connection, granting the attacker command execution capabilities on the victim's machine.

## Overview

- **Technique**: Backdoor Attack & Reverse Shell
- **Programming Language**: Python
- **Tools Used**: Kivy for GUI, Kali Linux for demonstration
- **Vulnerabilities Exploited**: 
  1. Unsecured storage of WiFi credentials
  2. Reverse shell establishment on the target device

## How It Works

1. **Deployment**: A Python script is executed on the victim's device.
2. **Backdoor & Reverse Shell**: The script initiates a connection, creating both a backdoor and a reverse shell. This allows the attacker command execution privileges when the devices share a common WiFi network.
3. **Command Interface**: Through a specified port, the attacker can communicate with the victim's device.
4. **Retrieval**: Upon the command "show wifi passwords," the victim's device sends back stored WiFi names and passwords.
5. **Command Execution**: The attacker can execute commands on the victim's machine via the established reverse shell.
6. **Display & Control**: The attacker receives WiFi details and can control the victim's device, emphasizing the severity of the vulnerabilities.

## Code Breakdown

- **show()**: Retrieves and displays WiFi credentials stored on the victim's device using `netsh` commands.
- **main()**: Establishes a backdoor connection, handles commands from the attacker, and sets up the reverse shell.
- **App**: Kivy-based GUI, currently showcases a basic "Hello World" label.

## Usage

This repository is intended for educational and research purposes, emphasizing the importance of securing devices against potential threats and understanding the implications of reverse shell access.
