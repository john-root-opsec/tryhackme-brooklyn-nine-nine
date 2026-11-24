<!--
  Brooklyn Nine-Nine — Cybersecurity Lab
  README presentation layer. The interactive Three.js experience lives in /site.
-->

<div align="center">

  <img
    src="assets/brooklyn-nine-nine-banner.jpg"
    alt="Brooklyn Nine-Nine — project banner"
    width="100%"
  />

  <br />

  <h1>PRECINCT 99 <span aria-hidden="true">/</span> CYBER OPERATIONS</h1>
  <p><strong>TRYHACKME • BROOKLYN NINE-NINE • LINUX PENETRATION TESTING LAB</strong></p>

  <p>
    <a href="https://tryhackme.com/room/brooklynninenine">
      <img src="https://img.shields.io/badge/TRYHACKME-LAB-yellow?style=for-the-badge&logo=tryhackme&logoColor=black" alt="TryHackMe room" />
    </a>
    <img src="https://img.shields.io/badge/FOCUS-OFFENSIVE_SECURITY-39FF88?style=for-the-badge&labelColor=111820" alt="Offensive Security" />
    <img src="https://img.shields.io/badge/ENVIRONMENT-KALI_LINUX-F5D90A?style=for-the-badge&labelColor=111820" alt="Kali Linux" />
    <img src="https://img.shields.io/badge/STATUS-IN_PROGRESS-FFB454?style=for-the-badge&labelColor=111820" alt="In progress" />
  </p>

  <p><em>THE NINTH-NINTH GOES CYBER.</em></p>

</div>

---

## ◈ CASE FILE / 001

**Brooklyn Nine-Nine** is a hands-on cybersecurity learning project based on the TryHackMe training room. This repository is being used to organize the project interface, technical references, and learning notes as the lab progresses.

The focus is on understanding the methodology behind a penetration test—not simply collecting answers. All practical testing is restricted to the authorized TryHackMe environment.

> **Current state:** the lab is in progress. No findings, credentials, flags, or successful exploitation claims are published here.

## ◈ OPERATIONS MAP

| WORKSTREAM | SCOPE |
|:--|:--|
| Network reconnaissance | Host discovery, TCP/IP and port concepts |
| Service enumeration | Understanding exposed FTP, SSH and HTTP services |
| Web reconnaissance | Directories, resources and application surface |
| Authentication security | Authentication mechanisms and password hygiene |
| Linux security | Users, groups, permissions and configuration |
| Privilege escalation | Linux privilege-boundary concepts |
| Security assessment | Evidence-based analysis and remediation |

## ◈ TOOLING / FIELD KIT

<p>
  <img src="https://img.shields.io/badge/Kali_Linux-557C94?style=flat-square&logo=kalilinux&logoColor=white" alt="Kali Linux" />
  <img src="https://img.shields.io/badge/Nmap-214478?style=flat-square" alt="Nmap" />
  <img src="https://img.shields.io/badge/Gobuster-168A45?style=flat-square" alt="Gobuster" />
  <img src="https://img.shields.io/badge/Hydra-C69B00?style=flat-square" alt="Hydra" />
  <img src="https://img.shields.io/badge/Wireshark-1679A7?style=flat-square&logo=wireshark&logoColor=white" alt="Wireshark" />
  <img src="https://img.shields.io/badge/SSH-30363D?style=flat-square" alt="SSH" />
  <img src="https://img.shields.io/badge/FTP-30363D?style=flat-square" alt="FTP" />
</p>

These are tools and technologies planned for study or reference; this list does not claim that every tool has already been used in the lab.

## ◈ LAB ENVIRONMENT

| PROPERTY | VALUE |
|:--|:--|
| Training platform | TryHackMe |
| Room | Brooklyn Nine-Nine |
| Attacker environment | Kali Linux / TryHackMe AttackBox |
| Target environment | TryHackMe-provided lab machine |
| Project category | Offensive Security |
| Documentation language | English |

## ◈ INTERACTIVE EXPERIENCE

The repository's visual companion is planned as a separate web experience built with **Three.js**, **three-globe**, **Vite**, HTML, CSS and JavaScript.

The globe will use clearly labelled synthetic demonstration data. It will not represent real network telemetry, live attacks, or threat intelligence.

**Interactive site:** coming after local implementation and verification.

## ◈ REPOSITORY LAYOUT

```text
tryhackme-brooklyn-nine-nine/
├── README.md
├── assets/
│   └── brooklyn-nine-nine-banner.jpg
├── site/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   └── src/
│       ├── main.js
│       ├── globe.js
│       └── style.css
├── docs/
└── tools/
```

## ◈ DEVELOPMENT LOG

- [x] Create the GitHub repository
- [x] Define the project scope and visual direction
- [ ] Add and verify the original project banner
- [ ] Build the responsive Three.js experience
- [ ] Capture a real preview image or GIF
- [ ] Add evidence-based technical notes as the lab progresses
- [ ] Review TryHackMe sharing rules before publishing any room-specific solution material

## ◈ ETHICS & DISCLOSURE

This repository is for education and professional development. Testing is performed only against systems and services explicitly provided for the authorized training lab.

Do not use these materials against systems without explicit permission. Room-specific answers, flags, credentials, and solution walkthroughs are intentionally excluded while publication is restricted by TryHackMe rules.

---

<div align="center">

**JOHN ROOT**  
*Cybersecurity • Offensive Security • Penetration Testing*

<sub>Observe carefully. Verify evidence. Document responsibly.</sub>

</div>
