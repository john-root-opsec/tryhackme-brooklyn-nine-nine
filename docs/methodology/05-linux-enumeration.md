# 05 — Linux Enumeration After SSH

## Objective

After establishing an authorized SSH session, understand the permissions and filesystem context of the authenticated Linux account.

## Identity and session context

The first questions are:
- which account is active;
- which groups apply to that account;
- which directory is the current working directory;
- which home directories and files are visible;
- what permissions are granted to the current user.

A remote shell operates with the authenticated account's identity unless a separate privileged execution mechanism is used.

## Home directories and files

The instructor reviews the Linux home-directory structure and moves through user directories. The learning objectives are:
- understand how user home directories are organized;
- distinguish ownership from access permissions;
- identify which files are readable by the current account;
- avoid assuming that a visible file is automatically sensitive or exploitable.

Room-specific directory names, file names and file contents must remain in private notes while the room is active.

## Permission review

Interpret the owner, group and other permission bits. Remember that directory traversal requires execute permission on the directory, and access to a file depends on both the file and its parent directories.

## Root versus a regular user

A regular account has only the access granted by its identity, groups and explicit privilege rules. Root is the superuser account. A user may have access to selected privileged commands without having unrestricted root access.

## Defensive relevance

- Protect user home directories and sensitive files.
- Remove stale accounts and unused access.
- Review group membership and file ownership.
- Monitor unusual access to other users' directories.
- Apply least privilege to interactive and service accounts.
