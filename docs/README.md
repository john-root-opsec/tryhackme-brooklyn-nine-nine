<div align="center">

<img src="../assets/motion/04-learning-log.svg" width="100%" alt="Documentation archive" />

**PRECINCT 99 / TECHNICAL KNOWLEDGE BASE**

<sub>INSTRUCTOR WORKFLOW • LINUX PENTESTING • SERVICE REVIEW</sub>

</div>

# Documentation Index

This knowledge base follows the practical sequence demonstrated in the Brooklyn Nine-Nine lesson. Each page explains the technique used in that stage and the technical concepts needed to understand its purpose and output.

## 01 / Fundamentals

| Document | What it covers |
|:--|:--|
| [Networking & TCP/IP](fundamentals/networking-and-tcp-ip.md) | ICMP reachability, TCP ports, SYN scans and Nmap port states. |
| [Web & HTTP](fundamentals/web-and-http.md) | HTTP pages, source inspection, static assets, metadata and directory discovery. |
| [Linux & Permissions](fundamentals/linux-and-permissions.md) | Shell basics, users, home directories, file permissions and sudo policy. |
| [Authentication & Access](fundamentals/authentication-and-access.md) | FTP access models, password auditing, wordlists and SSH authentication. |

## 02 / Instructor Workflow

| Order | Stage | Main activity |
|:--:|:--|:--|
| 00 | [Environment Setup](methodology/00-environment-setup.md) | Start the lab, connect Kali through the approved VPN path and verify reachability. |
| 01 | [Web Reconnaissance](methodology/01-web-reconnaissance.md) | Inspect the page and source, retrieve the referenced image, review metadata and discover web paths. |
| 02 | [Network Reconnaissance](methodology/02-network-reconnaissance.md) | Perform TCP SYN scanning and identify service/version information with Nmap. |
| 03 | [FTP Review](methodology/03-service-enumeration-and-ftp.md) | Review FTP authentication, directory access and exposed-file handling. |
| 04 | [SSH & Authentication](methodology/04-ssh-and-authentication.md) | Understand RockYou-based password auditing, Hydra and SSH access. |
| 05 | [Linux Enumeration](methodology/05-linux-enumeration.md) | Review the authenticated Linux context, user directories and permissions. |
| 06 | [Privilege Escalation](methodology/06-privilege-escalation.md) | Inspect sudo permissions, research the permitted binary with GTFOBins and understand the privilege boundary. |

## 03 / Defensive Context

| Document | Related lesson |
|:--|:--|
| [Detection & Monitoring](defense/01-detection-and-monitoring.md) | Web discovery, port scans, FTP access, SSH authentication and privileged activity. |
| [Hardening & Remediation](defense/02-hardening-and-remediation.md) | Restrict exposed services, protect files, harden authentication and narrow sudo permissions. |

## 04 / References & Templates

- [Official tool and protocol references](references/README.md)
- [Technical note template](templates/technical-note-template.md)
- [Security review template](templates/security-review-template.md)

## Documentation standard

For each stage, document:
1. **Objective** — what the instructor is trying to establish.
2. **Technique** — which tool or interface is used and why.
3. **Technical basis** — the protocol, Linux feature or security control involved.
4. **Interpretation** — what an observation proves and what it does not prove.
5. **Defensive relevance** — how the behavior could be detected or prevented.

## Publication boundary

This repository documents reusable techniques and concepts. Do not publish active-room flags, credentials, target-specific file contents, successful password results, exact exploitation chains or walkthrough steps. Keep sensitive lab evidence in private notes until TryHackMe permits publication.
