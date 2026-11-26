<div align="center">

<img src="assets/motion/header-green-animated.gif?v=3" width="100%" alt="Brooklyn Nine-Nine — Precinct 99 Cyber Operations with a geographically accurate rotating Earth globe" />

**TRYHACKME / BROOKLYN NINE-NINE / LINUX PENETRATION TESTING**

<img src="https://img.shields.io/badge/PLATFORM-TRYHACKME-39FF88?style=for-the-badge&labelColor=07110B&logo=tryhackme&logoColor=39FF88" alt="TryHackMe" />
<img src="https://img.shields.io/badge/FOCUS-OFFENSIVE_SECURITY-F5D90A?style=for-the-badge&labelColor=07110B" alt="Offensive Security" />
<img src="https://img.shields.io/badge/ENVIRONMENT-KALI_LINUX-39FF88?style=for-the-badge&labelColor=07110B&logo=kalilinux&logoColor=39FF88" alt="Kali Linux" />
<img src="https://img.shields.io/badge/STATUS-COMPLETED-9BFFBC?style=for-the-badge&labelColor=07110B" alt="Completed" />

<em>Observe the surface. Understand the signal. Document the evidence.</em>

</div>

---

<div align="center"><img src="assets/motion/01-case-file.svg" width="100%" alt="01 — Case File" /></div>

## CASE FILE / 001

**Brooklyn Nine-Nine** is a completed, authorized TryHackMe Linux penetration-testing exercise. This repository records the methodology, technical observations, security implications and lessons learned during the lab.

The workflow covered network reconnaissance, web inspection, image metadata review, web-path discovery, FTP access review, SSH authentication testing, Linux post-exploitation enumeration and a sudo misconfiguration that allowed a privilege-boundary escape.

This is an educational lab write-up, not a claim of commercial penetration-testing experience. It demonstrates how I approached a controlled environment, interpreted evidence and connected technical findings to defensive controls.

> **Lab status:** Completed. The original room-completion screenshot is not embedded because it contains personal identifying information. Any public copy must be redacted before publication.

### QUICK FACTS

| Item | Detail |
|:--|:--|
| Platform | TryHackMe |
| Room | Brooklyn Nine-Nine |
| Environment | Kali Linux connected to the assigned lab network |
| Assessment type | Guided Linux penetration-testing lab |
| Main focus | Reconnaissance, service enumeration, authentication and Linux privilege boundaries |
| Completion | Completed — 1 task / 60 points shown by the room completion screen |

---

<div align="center"><img src="assets/motion/02-field-toolkit.svg" width="100%" alt="02 — Field Toolkit" /><br /><img src="assets/tools/field-toolkit.svg" width="100%" alt="Custom icon grid for the tools used in the lab" /></div>

### TOOLKIT / WHAT EACH TOOL CONTRIBUTED

| Tool | Role in the assessment |
|:--|:--|
| **Kali Terminal / Bash** | Run commands, inspect output and manage downloaded files. |
| **OpenVPN** | Connect the workstation to the authorized TryHackMe network. |
| **Firefox / Developer Tools** | Inspect the HTTP page, source and referenced resources. |
| **ping** | Check basic reachability of the deployed lab host. |
| **Nmap** | Discover TCP ports and identify exposed services and versions. |
| **wget** | Retrieve the web image for local analysis. |
| **ExifTool** | Review metadata associated with the downloaded image. |
| **SecLists / Gobuster** | Enumerate candidate web paths and interpret HTTP responses. |
| **FTP client** | Review anonymous access, directory listing and file-transfer behavior. |
| **RockYou / Hydra** | Perform password auditing within the authorized training environment. |
| **SSH** | Establish a remote session as the discovered lab account. |
| **sudo / less / GTFOBins** | Review a privileged command rule and understand the risk of shell-capable utilities. |

---

<div align="center"><img src="assets/motion/03-lab-method.svg" width="100%" alt="03 — Lab Methodology" /></div>

## ATTACK METHODOLOGY

| Phase | Activity | Outcome |
|:--:|:--|:--|
| 01 | VPN and connectivity | Established the approved lab network path and verified reachability. |
| 02 | Network reconnaissance | Identified FTP, SSH and HTTP as exposed TCP services. |
| 03 | Web reconnaissance | Inspected page source, retrieved a referenced image, reviewed metadata and enumerated candidate paths. |
| 04 | FTP investigation | Identified anonymous access and retrieved a lab note for analysis. |
| 05 | SSH authentication | Conducted controlled password auditing and established the lab user session. |
| 06 | Linux enumeration | Inspected user context, home directories and the user-level objective. |
| 07 | Privilege escalation | Identified an over-permissive sudo rule for a general-purpose pager and verified elevated execution. |
| 08 | Completion | Reached the root-level objective and completed the TryHackMe room. |

### KEY TECHNICAL OBSERVATIONS

- The target exposed FTP, SSH and HTTP during the observed scan.
- The HTTP page referenced a static image. Its source and metadata were inspected.
- Gobuster returned successful and forbidden HTTP responses; status codes required interpretation.
- FTP permitted anonymous authentication in the lab and exposed a text note.
- The note provided a clue that informed the password-auditing stage.
- SSH access was obtained as the lab user after controlled authentication testing.
- Linux enumeration showed that an authenticated user context and root privileges are separate boundaries.
- The sudo policy permitted passwordless execution of `less`; its shell-capable behavior enabled a root shell in the lab.
- Root context was verified with an identity check, and the root-level objective was reached.

See the [technical walkthrough](docs/README.md#02--assessment-walkthrough) for reasoning, command explanations and defensive implications.

---

<div align="center"><img src="assets/motion/04-learning-log.svg" width="100%" alt="04 — Learning Log" /></div>

## DOCUMENTATION

| Track | Contents |
|:--|:--|
| [Assessment walkthrough](docs/README.md#02--assessment-walkthrough) | The lab sequence, observed evidence and technical interpretation. |
| [Fundamentals](docs/README.md#01--fundamentals) | TCP/IP, HTTP, Linux permissions, FTP and SSH concepts. |
| [Defensive context](docs/README.md#03--defensive-context) | Detection ideas and hardening recommendations linked to findings. |
| [References & templates](docs/README.md#04--references--templates) | Official tool documentation and reusable reporting templates. |
| [Field toolkit](tools/README.md) | Tool roles and operational notes. |

**Main navigation:** [Documentation Index](docs/README.md) · [Learning Plan](docs/LEARNING-PLAN.md) · [Tool Reference](tools/README.md) · [Three.js Frontend](site/)

### FRONTEND / VISUAL SYSTEM

<div align="center">
<img src="https://img.shields.io/badge/HTML5-STRUCTURE-E34F26?style=flat-square&logo=html5&logoColor=white" alt="HTML5" />
<img src="https://img.shields.io/badge/CSS3-INTERFACE-1572B6?style=flat-square&logo=css3&logoColor=white" alt="CSS3" />
<img src="https://img.shields.io/badge/JAVASCRIPT-INTERACTION-F7DF1E?style=flat-square&logo=javascript&logoColor=111111" alt="JavaScript" />
<img src="https://img.shields.io/badge/THREE.JS-3D_RENDERING-39FF88?style=flat-square&logo=threedotjs&logoColor=white&labelColor=101914" alt="Three.js" />
<img src="https://img.shields.io/badge/VITE-BUILD_TOOL-646CFF?style=flat-square&logo=vite&logoColor=white" alt="Vite" />
<img src="https://img.shields.io/badge/MARKDOWN-DOCUMENTATION-39FF88?style=flat-square&logo=markdown&logoColor=white&labelColor=101914" alt="Markdown" />
</div>

The animated banner and cyber-operations frontend are retained as presentation assets. The interactive globe uses synthetic demonstration data; it does not represent live attacks, real network traffic or threat-intelligence feeds.

---

<div align="center"><img src="assets/motion/05-ethics.svg" width="100%" alt="05 — Rules of Engagement" /></div>

## RULES OF ENGAGEMENT & PUBLICATION SAFETY

- All testing described here was performed only in the TryHackMe educational environment.
- Do not reuse techniques against third-party systems without explicit authorization.
- Credentials, VPN profiles, private keys, tokens and flags are not included.
- Review screenshots for personal identifiers, passwords, private network details and answer-bearing data before publishing.
- Findings are described as observations from an educational lab, not as a production security assessment.

## SKILLS DEMONSTRATED

**Network reconnaissance · TCP service enumeration · HTTP source inspection · Metadata analysis · Web content discovery · FTP access review · Password-auditing concepts · SSH · Linux user enumeration · Sudo policy review · Privilege-boundary analysis · Technical reporting**

<div align="center">
**JOHN ROOT**  
<sub>CYBERSECURITY / OFFENSIVE SECURITY / PENETRATION TESTING</sub>
<br />
<em>Learn deliberately. Test ethically. Verify everything.</em>
</div>