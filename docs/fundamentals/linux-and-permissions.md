# Linux & Permissions — Lab Fundamentals

## Why this topic appears in the lesson

After the instructor demonstrates remote access, the workflow moves into the Linux environment. The focus is identifying the current account, understanding the home-directory layout and reviewing the permissions available to that account.

## Linux identity

Every Linux process runs with user and group identities. The identity determines which files and operations the process may access, subject to standard permissions and additional security controls.

Useful concepts:
- username and numeric user ID (UID);
- primary and supplementary groups;
- current working directory;
- home directory;
- process identity and effective identity.

A successful SSH login establishes a session as one account. It does not automatically provide administrative privileges.

## Filesystem navigation

Linux uses a hierarchical filesystem. User home directories are commonly located under `/home`, while system configuration and account information are stored in standard system paths.

When reviewing a directory:
- identify the owner and group;
- inspect permissions;
- distinguish files from directories;
- understand whether the current account can read, modify or traverse the item.

## Permission model

The traditional permission classes are:
- **user** — the file owner;
- **group** — members of the file's group;
- **others** — all other users.

The basic permission bits are read (`r`), write (`w`) and execute (`x`). Their effect differs for files and directories.

| Object | Permission | Meaning |
|:--|:--|:--|
| File | Read | Read the file contents. |
| File | Write | Modify the file contents. |
| File | Execute | Execute the file as a program, if its format and other controls permit it. |
| Directory | Read | List directory entries. |
| Directory | Write | Create, remove or rename entries, subject to other controls. |
| Directory | Execute | Traverse/search the directory. |

## Sudo policy

`sudo` allows a user to run explicitly permitted commands with another identity, often root. The `sudo -l` operation lists the commands the current account is allowed to run.

The security review must consider:
- which command is permitted;
- which target identity is allowed;
- whether a password is required;
- whether arguments are restricted;
- whether the permitted program can launch other commands or provide an unrestricted function.

A limited-looking rule can still be excessive if the selected program exposes functionality outside the intended task.

## Root and privilege boundaries

Root is the superuser identity on a conventional Linux system. Reaching root means crossing from a restricted user context into a highly privileged one.

Do not confuse:
- access to a user account;
- permission to read a particular file;
- permission to run a command through sudo;
- full administrative control.

These are separate authorization states.

## Defensive relevance

- Apply least privilege to user and service accounts.
- Restrict sudo rules to the minimum required command and arguments.
- Protect sensitive home directories and system files.
- Avoid granting privileged access to general-purpose utilities unless the behavior is fully constrained.
- Audit privileged rules and review them when responsibilities change.
