<div align="center">

<img src="../assets/motion/02-field-toolkit.svg" width="100%" alt="Field toolkit" />

**PRECINCT 99 / TOOL REFERENCE**

<sub>TOOLS ARE METHODS — UNDERSTANDING THE OUTPUT IS THE SKILL</sub>

</div>

# Field Toolkit

This reference explains each tool's role in the learning path. It is an educational catalogue, not a record of completed actions or a target-specific walkthrough.

## 01 / Workstation & connectivity

| Tool | Purpose | Knowledge to develop |
|:--|:--|:--|
| **Terminal / Bash** | Execute commands and manage the local workflow. | Shell parsing, quoting, pipes, exit codes, processes and permissions. |
| **Kali Linux** | Security-testing operating system. | Package management, filesystem layout, services and tool environment. |
| **OpenVPN** | Connect the local workstation to the authorized training network. | Tunnel interfaces, routing tables, DNS behavior and VPN scope. |
| **Firefox Developer Tools** | Inspect web content and HTTP exchanges. | DOM, page source, network requests, headers, cookies and browser storage. |

## 02 / Reconnaissance & discovery

| Tool | Purpose | Knowledge to develop |
|:--|:--|:--|
| **Nmap** | Host discovery and port/service assessment. | TCP/UDP, SYN scans, port states, service identification and scan limitations. |
| **Gobuster** | Discover candidate web paths and resources. | HTTP response behavior, content discovery and false positives. |
| **ExifTool** | Read metadata from supported files. | Metadata formats, privacy leakage and evidence handling. |

## 03 / Services & authentication

| Tool / protocol | Purpose | Knowledge to develop |
|:--|:--|:--|
| **FTP client** | Interact with a file-transfer service in an authorized lab. | Control/data channels, anonymous access, permissions and cleartext risk. |
| **SSH** | Secure remote administration. | Host keys, public-key authentication, session security and access policy. |
| **Hydra** | Controlled authentication-security testing. | Password risk, rate limiting, lockout trade-offs and authentication monitoring. |
| **RockYou wordlist** | Dataset used to discuss password quality and guessability. | Password reuse, weak patterns and defensive controls. |

## 04 / Linux privilege concepts

| Reference | Purpose | Knowledge to develop |
|:--|:--|:--|
| **GTFOBins** | Reference how standard Unix binaries can become risky in permissive execution contexts. | Sudo policy, SUID/SGID, capabilities, least privilege and secure configuration. |
| **less** | Terminal pager used to view text. | How utility behavior interacts with execution permissions and privilege boundaries. |

## 05 / Defensive analysis

| Tool | Purpose | Knowledge to develop |
|:--|:--|:--|
| **Wireshark** | Inspect packet captures and protocol exchanges. | TCP handshakes, DNS/HTTP metadata, TLS visibility and evidence privacy. |
| **Linux logs / journal** | Review operating-system and service events. | Authentication events, timestamps, service activity and incident timelines. |

## Learning method

For each tool, ask:
1. What problem does the tool solve?
2. What protocol, API or operating-system feature does it rely on?
3. What does each important option change?
4. What does the output prove—and what does it not prove?
5. What could create a false positive?
6. What telemetry could a defender use to observe this activity?
7. What configuration would reduce the associated risk?

## Responsible-use boundary

Use tools only on systems you own or are explicitly authorized to test. A tool's availability does not grant permission to scan, enumerate or authenticate to third-party systems.

Do not commit VPN profiles, credentials, private keys, raw packet captures containing sensitive information, target-specific evidence, active-room solution material, downloaded wordlists or large external datasets.

For the concepts behind each phase, see the [Documentation Index](../docs/README.md).
