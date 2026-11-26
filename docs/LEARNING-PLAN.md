# Learning Record — Brooklyn Nine-Nine

The TryHackMe Brooklyn Nine-Nine room has been completed. This page records the sequence studied and the practical topics covered; it is not a substitute for the detailed stage-by-stage analysis in the [documentation index](README.md).

## Completed workflow

| Order | Stage | Topics and tools | Status |
|:--:|:--|:--|:--|
| 01 | Environment setup | TryHackMe lab, Kali Linux, OpenVPN, ICMP reachability | Completed |
| 02 | Network reconnaissance | Nmap TCP SYN scan and service/version identification | Completed |
| 03 | Web reconnaissance | Browser inspection, HTML source, `wget`, ExifTool, SecLists and Gobuster | Completed |
| 04 | FTP investigation | FTP access mode, directory listing and file retrieval | Completed |
| 05 | SSH authentication | RockYou wordlist, Hydra and SSH session | Completed |
| 06 | Linux enumeration | Authenticated user context, home directories, files and permissions | Completed |
| 07 | Privilege escalation | Sudo policy, `less` behavior and root-context verification | Completed |
| 08 | Room completion | TryHackMe completion confirmation | Completed |

## Main learning outcomes

- Validate network reachability before interpreting scan results.
- Separate port discovery from service/version identification.
- Treat HTTP response codes as observations that require manual validation.
- Understand the difference between anonymous FTP authentication and actual file permissions.
- Explain why weak or reused passwords increase exposure to online authentication attacks.
- Distinguish a successful SSH login from administrative access.
- Interpret Linux ownership, directory traversal and sudo policy.
- Recognize that general-purpose utilities can become privilege-escalation paths when delegated through overly broad sudo rules.
- Verify the effective identity after a privileged operation rather than inferring success.

## Evidence standard

For every documented observation, identify whether it came directly from a screenshot, an existing repository note or a general technical explanation. Do not add unobserved commands or outputs.

## Scope and ethics

- The work was performed in the TryHackMe-provided educational environment.
- Use only the current target allocated by the room during testing.
- Do not reuse the techniques against third-party systems without explicit authorization.
- Never commit VPN profiles, credentials, private keys or secrets.