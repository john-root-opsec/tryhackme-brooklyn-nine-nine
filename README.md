<div align="center">

<img src="assets/motion/header-green.svg" width="100%" alt="Brooklyn Nine-Nine — Precinct 99 Cyber Operations" />

<br />

**TRYHACKME / BROOKLYN NINE-NINE / LINUX PENETRATION TESTING**

<img src="https://img.shields.io/badge/PLATFORM-TRYHACKME-39FF88?style=for-the-badge&labelColor=07110B&logo=tryhackme&logoColor=39FF88" alt="TryHackMe" />
<img src="https://img.shields.io/badge/FOCUS-OFFENSIVE_SECURITY-F5D90A?style=for-the-badge&labelColor=07110B" alt="Offensive Security" />
<img src="https://img.shields.io/badge/ENVIRONMENT-KALI_LINUX-39FF88?style=for-the-badge&labelColor=07110B&logo=kalilinux&logoColor=39FF88" alt="Kali Linux" />
<img src="https://img.shields.io/badge/STATUS-IN_PROGRESS-9BFFBC?style=for-the-badge&labelColor=07110B" alt="In progress" />

<br />

<em>Observe the surface. Understand the signal. Document the evidence.</em>

</div>

---

<div align="center">
  <img src="assets/motion/01-case-file.svg" width="100%" alt="01 — Case File" />
</div>

## CASE FILE / 001

**Brooklyn Nine-Nine** is a practical cybersecurity learning project based on the TryHackMe training room. The repository combines the lab's learning notes with a custom cyber-operations frontend built with HTML, CSS, JavaScript and Three.js.

The goal is to develop a repeatable penetration-testing mindset: understand the environment, identify the attack surface, investigate exposed services, validate evidence, and explain the security implications.

> **Current status:** the lab is in progress. This repository does not publish room answers, flags, credentials, target-specific exploitation steps, or a walkthrough while the room's sharing restrictions apply.

---

<div align="center">
  <img src="assets/motion/02-field-toolkit.svg" width="100%" alt="02 — Field Toolkit" />
  <br />
  <img src="assets/tools/field-toolkit.svg" width="100%" alt="Custom icon grid for Terminal, Kali Linux, OpenVPN, Nmap, Gobuster, ExifTool, Hydra, FTP, SSH, and GTFOBins/less" />
</div>

### TOOLKIT / WHAT EACH TOOL IS FOR

| Tool | Role in the lab |
|:--|:--|
| **Terminal / Bash** | Run commands, inspect output, manage files and keep a reproducible workflow. |
| **Kali Linux** | Local security-testing workstation. |
| **OpenVPN** | Connect the local Kali machine to the authorized TryHackMe network. |
| **Nmap** | Discover reachable hosts, open ports and—when needed—service details. |
| **Gobuster** | Discover web paths and resources during authorized HTTP enumeration. |
| **ExifTool** | Inspect metadata in supported files and media. |
| **FTP client** | Interact with the FTP service and understand access permissions. |
| **Hydra** | Study authentication-testing risks in the authorized lab context. |
| **SSH** | Establish secure remote sessions when valid lab access is available. |
| **GTFOBins / less** | Reference Linux binaries and understand why unsafe privilege rules matter. |

<sub>These entries describe the planned study toolkit and its general purpose; they are not claims that every tool has already been used or that any finding has been confirmed.</sub>

### PROTOCOLS & SYSTEM CONCEPTS

<div align="center">

<img src="https://img.shields.io/badge/TCP%2FIP-NETWORKING-39FF88?style=flat-square&labelColor=101914" alt="TCP/IP" />
<img src="https://img.shields.io/badge/HTTP-WEB-39FF88?style=flat-square&labelColor=101914" alt="HTTP" />
<img src="https://img.shields.io/badge/FTP-FILE_TRANSFER-F5D90A?style=flat-square&labelColor=101914" alt="FTP" />
<img src="https://img.shields.io/badge/SSH-REMOTE_ACCESS-39FF88?style=flat-square&labelColor=101914" alt="SSH" />
<img src="https://img.shields.io/badge/LINUX-PERMISSIONS-F5D90A?style=flat-square&labelColor=101914" alt="Linux permissions" />
<img src="https://img.shields.io/badge/SUDO-PRIVILEGES-39FF88?style=flat-square&labelColor=101914" alt="Sudo privileges" />

</div>

---

<div align="center">
  <img src="assets/motion/03-lab-method.svg" width="100%" alt="03 — Lab Methodology" />
</div>

### HOW THE LAB WILL BE STUDIED

| Phase | Focus | What we want to understand |
|:--:|:--|:--|
| **00** | Environment setup | VPN connectivity, target scope and local tooling. |
| **01** | Web reconnaissance | HTTP, browser inspection, source review and content discovery. |
| **02** | Network scanning | TCP, SYN scanning, port states and Nmap interpretation. |
| **03** | Service / FTP review | Service identification, FTP behavior and file permissions. |
| **04** | SSH / authentication | Remote access, password security and authentication controls. |
| **05** | Linux enumeration | Users, groups, processes, directories and permissions. |
| **06** | Privilege escalation | Sudo policy, binary behavior and privilege boundaries. |
| **07** | Defensive review | Detection, hardening, remediation and reporting. |

**Method:** learn the concept → perform the authorized lab exercise → interpret the output → document the defensive lesson.

---

<div align="center">
  <img src="assets/motion/04-learning-log.svg" width="100%" alt="04 — Learning Log" />
</div>

### PROJECT DOCUMENTATION

<div align="center">
  <img src="assets/motion/04-learning-log.svg" width="100%" alt="Learning log and documentation archive" />
</div>

**Documentation is divided into four tracks:**

| Track | What it contains |
|:--|:--|
| [Fundamentals](docs/README.md#01--fundamentals) | Networking, TCP/IP, HTTP, Linux, permissions and authentication. |
| [Lab Methodology](docs/README.md#02--lab-methodology) | Instructor-aligned sequence: environment, web, network, FTP, SSH, Linux and privilege concepts. |
| [Defensive Security](docs/README.md#03--defensive-security) | Detection, monitoring, hardening and remediation. |
| [References & Templates](docs/README.md#04--references--templates) | Official sources and reusable technical-note templates. |

**Main navigation:** [Documentation Index](docs/README.md) · [Learning Plan](docs/LEARNING-PLAN.md) · [Tool Reference](tools/README.md) · [Three.js Frontend](site/)

### FRONTEND / VISUAL SYSTEM

<div align="center">

<img src="https://img.shields.io/badge/HTML5-STRUCTURE-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/CSS3-INTERFACE-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3" />
<img src="https://img.shields.io/badge/JAVASCRIPT-INTERACTION-F7DF1E?style=flat-square&logo=javascript&logoColor=111111" alt="JavaScript" />
<img src="https://img.shields.io/badge/THREE.JS-3D_RENDERING-39FF88?style=flat-square&logo=threedotjs&logoColor=white&labelColor=101914" alt="Three.js" />
<img src="https://img.shields.io/badge/THREE--GLOBE-GEOGRAPHIC_VISUALS-39FF88?style=flat-square&labelColor=101914" alt="three-globe" />
<img src="https://img.shields.io/badge/VITE-BUILD_TOOL-646CFF?style=flat-square&logo=vite&logoColor=white" alt="Vite" />
<img src="https://img.shields.io/badge/MARKDOWN-DOCUMENTATION-39FF88?style=flat-square&logo=markdown&logoColor=white&labelColor=101914" alt="Markdown" />

</div>

The globe uses synthetic demonstration data for visual effect only. It does not display real network traffic, live attacks, or threat-intelligence feeds.

---

<div align="center">
  <img src="assets/motion/05-ethics.svg" width="100%" alt="05 — Rules of Engagement" />
</div>

### RULES OF ENGAGEMENT

- All testing is limited to the TryHackMe-provided training environment or systems with explicit authorization.
- Do not reuse lab techniques against third-party systems without permission.
- Do not commit VPN profiles, credentials, API keys, flags, or other secrets.
- Keep room-specific answers and walkthrough material unpublished while TryHackMe sharing restrictions apply.
- Treat all interface globe routes and telemetry-like visuals as **synthetic demo data**.

---

<div align="center">

**JOHN ROOT**  
<sub>CYBERSECURITY / OFFENSIVE SECURITY / PENETRATION TESTING</sub>

<br />

<em>Learn deliberately. Test ethically. Verify everything.</em>

</div>
