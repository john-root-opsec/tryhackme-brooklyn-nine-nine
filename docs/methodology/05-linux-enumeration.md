# 06 — Linux Post-Exploitation Enumeration

## Objective

After SSH access, understand the authenticated user's local context, inspect visible home directories and permissions, and locate the user-level objective.

## 1. Establish the account context

The supplied SSH screenshot shows a shell prompt for the authenticated lab user. The next commands inspected the local filesystem and user home-directory layout. The evidence supports that the session was operating as the discovered user, not as root.

## 2. Inspect home directories

The terminal output shows navigation through `/home` and inspection of user directories. This is a basic post-exploitation step: determine what the authenticated identity can see and which files are accessible.

The screenshot shows a user-level text file being read from another home directory. The actual file contents and flag value are omitted from this public document.

## 3. Interpret Linux permissions

A file's accessibility depends on its owner and group, the file's permission bits, execute (traverse) permission on parent directories, supplementary groups and other security controls.

Listing a directory, traversing it and reading a file are distinct permissions.

## 4. User-level objective

The supplied evidence shows that the user-level flag file was located and read. This confirmed completion of the room's user objective before privilege escalation. The flag value is not included in this repository.

## Why this stage mattered

Post-exploitation enumeration establishes the actual privileges of the authenticated account and identifies whether local configuration or file permissions expose additional information. It also prevents treating SSH access as equivalent to administrator access.

## Defensive recommendations

- Restrict home-directory traversal and sensitive file readability.
- Review ownership and group membership.
- Remove stale accounts and unnecessary files.
- Monitor access to other users' home directories.
- Keep service and interactive accounts minimally privileged.

## Result

The supplied screenshot supports authenticated Linux access, user-directory enumeration and retrieval of the user-level objective. Sensitive file contents are not reproduced.

## Practical evidence

![Home directory enumeration and User Flag retrieval](../evidence/12-user-flag.png)

*Evidence 12 — Enumeration of `/home` leads to the `holt` directory and `user.txt`. The flag value is redacted.*
