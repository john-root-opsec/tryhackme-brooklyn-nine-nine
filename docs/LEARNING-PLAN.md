# Learning Plan — Brooklyn Nine-Nine

This plan follows the sequence demonstrated in the instructor's video and expands it into broader cybersecurity study. The video provides the practical order; the fundamentals and defensive tracks extend learning beyond this room.

## Learning cycle

1. **Context** — identify the question and authorized scope.
2. **Concepts** — understand the protocol, operating-system feature or security principle.
3. **Practice** — perform only the step permitted in the TryHackMe lab.
4. **Interpretation** — distinguish facts, assumptions and unknowns.
5. **Defensive view** — consider logging, detection, impact and mitigation.
6. **Documentation** — record general knowledge without restricted room answers.

## Instructor-aligned sequence

| Order | Stage | Main topics | Status |
|:--:|:--|:--|:--|
| 00 | Environment preparation | Kali Linux, OpenVPN, routes, scope and connectivity | Practised |
| 01 | Web reconnaissance | HTTP, browser inspection, source review, metadata and content discovery | Next |
| 02 | Network scanning | TCP, SYN scan, port states and Nmap interpretation | Initial scan practised |
| 03 | Service / FTP review | Service identification, FTP behavior and file permissions | Pending |
| 04 | SSH / authentication | SSH, password security, wordlists and authentication controls | Pending |
| 05 | Linux enumeration | Identity, filesystem, users, groups, processes and permissions | Pending |
| 06 | Privilege escalation concepts | Sudo policy, binary behavior and privilege boundaries | Pending |
| 07 | Defensive review | Detection, hardening, remediation and reporting | Pending |

"Practised" records the general learning activity. It does not mean the room is complete or that a specific vulnerability has been confirmed.

## Broader learning tracks

### Networking
- IPv4 addressing and CIDR
- TCP versus UDP
- Ports, sockets and routing
- DNS, HTTP, FTP and SSH
- Packet inspection and network segmentation

### Web security
- URLs, HTTP methods, headers and status codes
- Browser developer tools and source inspection
- Static assets and metadata
- Content discovery and web exposure
- Authentication and session fundamentals

### Linux and identity
- Shell navigation and command pipelines
- Users, groups and file permissions
- Processes, services and environment variables
- Sudo policy and least privilege
- SSH keys and secure remote administration

### Offensive security methodology
- Scoping and authorization
- Reconnaissance and enumeration
- Evidence validation
- Risk reasoning
- Reproducible technical reporting

### Defensive security
- Authentication and service logs
- Network monitoring
- Detection opportunities
- Secure configuration
- Remediation and verification

## Evidence quality rules

Label statements as:
- **Observed:** directly visible in output or behavior.
- **Interpreted:** a reasoned explanation supported by an observation.
- **Hypothesis:** a possibility requiring validation.
- **Unknown:** information not established by available evidence.

Never turn a hypothesis into a finding without validation.

## Current progress

- [x] Local Kali environment prepared
- [x] OpenVPN connection established
- [x] Lab reachability checked
- [x] Initial TCP port-discovery exercise performed
- [ ] Web reconnaissance study
- [ ] Service enumeration study
- [ ] FTP security concepts
- [ ] SSH and authentication concepts
- [ ] Linux enumeration concepts
- [ ] Privilege-boundary concepts
- [ ] Defensive analysis and remediation

## Rules

- Test only the machine and services deployed for the authorized room.
- Do not publish VPN profiles, credentials, flags, target-specific exploitation steps or active-room walkthroughs.
- Do not commit raw packet captures or sensitive operational notes.
- Keep examples in the knowledge base generic and reusable.
