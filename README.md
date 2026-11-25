<div align="center">

<img src="assets/motion/header-green.svg?v=2" width="100%" alt="Brooklyn Nine-Nine — Precinct 99 Cyber Operations with a rotating Earth globe" />

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

**Brooklyn Nine-Nine** is a guided Linux penetration-testing lab documented in the same order demonstrated by the instructor. The practical workflow covers web reconnaissance, image metadata review, directory discovery, Nmap scanning, FTP investigation, password auditing, SSH access, Linux enumeration and privilege-boundary analysis.

This repository contains concise technical notes for the tools and concepts used in that workflow, together with the project's separate cyber-operations frontend built with HTML, CSS, JavaScript and Three.js. The emphasis is on understanding each step—not collecting answers.

> **Current status:** the lab is in progress. This repository does not publish room answers, flags, credentials, target-specific exploitation steps, or a walkthrough while the room's sharing restrictions apply.

---

<div align="center">
  <img src="assets/motion/02-field-toolkit.svg" width="100%" alt="02 — Field Toolkit" />
  <br />
  <img src="assets/tools/field-toolkit.svg" width="100%" alt="Custom icon grid for Terminal, Kali Linux, OpenVPN, Nmap, Gobuster, ExifTool, Hydra, FTP, SSH, and GTFOBins/less" />
</div>

### TOOLKIT / WHAT EACH TOOL IS FOR

| Tool | Role in the instructor's workflow |
|:--|:--|
| **Kali Terminal / Bash** | Run commands, inspect output and manage downloaded files. |
| **OpenVPN** | Connect the local Kali workstation to the authorized TryHackMe network. |
| **Firefox / Developer Tools** | Inspect the HTTP page, delivered source and browser requests. |
| **ping** | Check basic reachability of the deployed lab host. |
| **wget** | Retrieve a web image for local metadata inspection. |
| **ExifTool** | Review metadata embedded in the downloaded image. |
| **SecLists** | Provide candidate paths for web content discovery. |
| **Gobuster** | Enumerate candidate directories and files over HTTP. |
| **Nmap** | Perform TCP SYN scanning and service/version identification. |
| **FTP client** | Review FTP authentication, directory access and file-transfer behavior. |
| **RockYou** | Supply a known wordlist for the controlled password-auditing stage. |
| **Hydra** | Demonstrate password-based authentication testing in the authorized lab. |
| **SSH** | Access the Linux service using authorized lab credentials. |
| **sudo / GTFOBins** | Review delegated privileges and the security implications of permitted Unix binaries. |

<sub>This list follows the tools and interfaces shown in the lesson. It does not publish target-specific results, credentials, flags or exploitation commands.</sub>

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

| Phase | Instructor step | Technical focus |
|:--:|:--|:--|
| **00** | Environment setup | Start the lab, connect through VPN and verify host reachability. |
| **01** | Web reconnaissance | Inspect the page and HTML source; retrieve the image and review its metadata. |
| **02** | Directory discovery | Use SecLists and Gobuster to identify candidate web resources. |
| **03** | Network scanning | Use Nmap for TCP SYN scanning and service/version identification. |
| **04** | FTP investigation | Review FTP access behavior, directory listing and file-transfer permissions. |
| **05** | SSH authentication | Study RockYou, Hydra and remote SSH authentication. |
| **06** | Linux enumeration | Inspect the authenticated account, home directories and permission context. |
| **07** | Privilege review | Examine sudo policy and use GTFOBins to understand the permitted binary's risk. |

**Method:** follow the instructor's order → understand the protocol or operating-system feature → interpret the observed behavior → connect it to the relevant security control.

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
| [Fundamentals](docs/README.md#01--fundamentals) | Networking, HTTP, metadata, authentication and Linux concepts required for this room. |
| [Instructor Workflow](docs/README.md#02--instructor-workflow) | The practical sequence from web inspection through privilege review. |
| [Defensive Context](docs/README.md#03--defensive-context) | Detection and hardening notes tied to the services and techniques in the lesson. |
| [References & Templates](docs/README.md#04--references--templates) | Official manuals and concise technical-note templates. |

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
