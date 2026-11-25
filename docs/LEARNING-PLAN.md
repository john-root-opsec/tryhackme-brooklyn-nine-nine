# Learning Plan — Brooklyn Nine-Nine

This plan follows the order demonstrated in the instructor's video. The objective is to reproduce the learning process in the local Kali environment while understanding the protocols, tools and Linux security concepts behind each step.

## Instructor sequence

| Order | Stage | Topics and tools | Progress |
|:--:|:--|:--|:--|
| 00 | Environment setup | TryHackMe lab, Kali Linux, OpenVPN, ICMP reachability | Completed |
| 01 | Web reconnaissance | Browser inspection, HTML source, `wget`, ExifTool, SecLists and Gobuster | Next |
| 02 | Network scanning | Nmap SYN scan, TCP port states and service/version detection | Preliminary port check performed; revisit in sequence |
| 03 | FTP investigation | FTP service review, authentication mode, directory listing and file handling | Pending |
| 04 | SSH authentication | RockYou wordlist, Hydra and SSH concepts | Pending |
| 05 | Linux enumeration | Authenticated user context, home directories, files and permissions | Pending |
| 06 | Privilege escalation | `sudo -l`, permitted binary review and GTFOBins | Pending |

The progress labels describe our study workflow only. They do not claim that the room is complete or disclose any room-specific result.

## Stage objectives

### 00 — Prepare the lab

Confirm the currently deployed machine, establish the approved VPN connection from Kali, inspect the route and verify basic reachability. Keep the VPN profile outside the repository.

### 01 — Inspect the web service

Use the browser to examine the page and its source. Identify referenced static resources, retrieve the relevant image for local inspection, review its metadata with ExifTool, then understand directory/content discovery with Gobuster and a SecLists wordlist.

### 02 — Scan the network

Understand why a SYN scan requires suitable privileges, how Nmap reports TCP port states and why service/version detection is a separate step from basic port discovery.

### 03 — Review FTP

Understand the FTP service, authentication modes, directory listing and file permissions. Treat any retrieved file as evidence that must be reviewed carefully; do not publish room-specific contents.

### 04 — Study SSH authentication

Understand the role of a password wordlist such as RockYou and the purpose and limitations of Hydra in an explicitly authorized authentication audit. Study SSH session establishment and credential hygiene.

### 05 — Enumerate the Linux context

After an authorized SSH session, identify the current account and inspect the relevant user and filesystem context. Understand ownership, permissions and the difference between a normal account and root.

### 06 — Review privilege boundaries

Understand how sudo policy is inspected, why a narrowly scoped command can still be dangerous if it permits an unintended function, and how GTFOBins is used as a reference. Do not publish the room's exact privileged binary behavior or exploitation sequence while the room is active.

## Learning record

For every stage, answer:
- What question is this step intended to answer?
- Which tool or interface is being used?
- Which protocol or operating-system feature is involved?
- What does the output establish?
- What remains unknown?
- What defensive control would reduce the associated risk?

## Scope and evidence rules

- Use only the TryHackMe machine deployed for this room.
- Use the current target address shown by the platform; do not copy an address from the instructor's video.
- Do not commit VPN profiles, credentials, private keys, flags or raw evidence.
- Keep active-room answers and target-specific exploitation details in private notes.
- Mark observations, interpretations and hypotheses separately.
