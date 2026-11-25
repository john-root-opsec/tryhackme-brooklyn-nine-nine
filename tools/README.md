<div align="center">

<img src="../assets/motion/02-field-toolkit.svg" width="100%" alt="Field toolkit" />

**PRECINCT 99 / TOOL REFERENCE**

<sub>TOOLS SHOWN IN THE INSTRUCTOR WORKFLOW</sub>

</div>

# Field Toolkit

This reference is limited to the tools and interfaces demonstrated or directly used in the instructor's workflow. It explains their role in the room without recording target-specific commands, credentials or findings.

## 01 / Environment & web inspection

| Tool | Role in the workflow | Technical focus |
|:--|:--|:--|
| **Kali Linux / Terminal** | Local assessment environment and command-line workspace. | Shell navigation, command execution, files and permissions. |
| **OpenVPN** | Connect the local workstation to the authorized TryHackMe network. | VPN interface, routing and reachability. |
| **Firefox / Developer Tools** | Open the HTTP service and inspect page behavior and source. | HTTP, HTML source, loaded resources and browser requests. |
| **ping** | Check basic reachability of the deployed lab host. | ICMP Echo Request/Reply and packet loss. |
| **wget** | Retrieve a referenced web resource for local inspection. | HTTP GET, response status and downloaded files. |
| **ExifTool** | Inspect metadata in the downloaded image. | Image metadata fields and information disclosure. |

## 02 / Web content discovery

| Tool / resource | Role in the workflow | Technical focus |
|:--|:--|:--|
| **SecLists** | Supply a candidate-path wordlist. | Wordlists, coverage and candidate generation. |
| **Gobuster** | Enumerate candidate web paths. | HTTP response codes, redirects, 403/404 behavior and false positives. |

## 03 / Network and services

| Tool / protocol | Role in the workflow | Technical focus |
|:--|:--|:--|
| **Nmap** | Discover TCP ports and identify service/version information. | SYN scan, port states, service probes and scan limitations. |
| **FTP client** | Review the file-transfer service and its access behavior. | Authentication modes, directory listing, data transfer and permissions. |

## 04 / Authentication and remote access

| Tool / resource | Role in the workflow | Technical focus |
|:--|:--|:--|
| **RockYou** | Provide a sample password wordlist for the controlled lab exercise. | Password quality, reuse and wordlist-based auditing. |
| **Hydra** | Demonstrate controlled authentication testing within the room. | Authentication attempts, rate limits, account monitoring and lockout considerations. |
| **SSH** | Establish a remote Linux session when authorized lab credentials are available. | Encrypted remote access, authentication and host identity. |

## 05 / Linux privilege review

| Tool / reference | Role in the workflow | Technical focus |
|:--|:--|:--|
| **sudo** | Inspect which privileged commands an account is allowed to execute. | sudoers policy, command scope and least privilege. |
| **GTFOBins** | Research the security implications of a permitted Unix binary. | Unsafe privilege delegation and shell-capable program behavior. |
| **Terminal pager** | Understand why granting privileged access to a general-purpose text utility can be dangerous. | Program features, execution context and privilege boundaries. |

## Usage principles

- Understand each tool option before running it.
- Use the current TryHackMe target address, not the address shown in a recording.
- Validate interesting HTTP responses rather than assuming every discovered path is useful.
- Do not infer a vulnerability from a port number or banner alone.
- Use Hydra and password wordlists only inside the explicitly authorized room.
- Never save VPN profiles, passwords, private keys or room flags in this repository.

This page describes the instructor's toolkit; it is not a list of additional tools we plan to introduce into the room.
