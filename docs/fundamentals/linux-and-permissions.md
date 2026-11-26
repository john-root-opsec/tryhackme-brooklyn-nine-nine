# Linux & Permissions — Lab Fundamentals

## Linux identity

Every Linux process runs with user and group identities. These identities determine which files and operations the process may access, subject to standard permissions and additional security controls.

Useful concepts include username and UID, primary and supplementary groups, current working directory, home directory and effective process identity.

A successful SSH login establishes a session as one account. It does not automatically provide administrative privileges.

## Filesystem navigation and permissions

Linux uses a hierarchical filesystem. User home directories are commonly located under `/home`.

The traditional permission classes are:

- **user** — the file owner;
- **group** — members of the file's group;
- **others** — all other users.

The basic permission bits are read (`r`), write (`w`) and execute (`x`). Their effect differs for files and directories.

| Object | Permission | Meaning |
|:--|:--|:--|
| File | Read | Read file contents. |
| File | Write | Modify file contents. |
| File | Execute | Execute the file as a program, subject to format and other controls. |
| Directory | Read | List directory entries. |
| Directory | Write | Create, remove or rename entries, subject to other controls. |
| Directory | Execute | Traverse/search the directory. |

A file may be readable while its containing directory is not traversable; permission checks must consider the full path.

## Sudo policy

`sudo` allows a user to run explicitly permitted commands with another identity, often root. The `sudo -l` operation lists commands the current account is allowed to run.

A sound review considers which command is permitted, which target identity is allowed, whether a password is required, whether arguments are restricted and whether the program can launch other commands or provide an unrestricted function.

The lab demonstrated why a general-purpose interactive pager can be dangerous when delegated as root: its interactive features can exceed the intended text-viewing task.

## Root and privilege boundaries

Root is the superuser identity on a conventional Linux system. Reaching root means crossing from a restricted user context into a highly privileged one.

Do not confuse access to a user account, permission to read a particular file, permission to run a command through sudo and full administrative control. These are separate authorization states.

## Defensive relevance

- Apply least privilege to user and service accounts.
- Restrict sudo rules to the minimum required command and arguments.
- Avoid granting privileged access to general-purpose utilities that can invoke shells.
- Protect sensitive home directories and system files.
- Audit privileged rules when responsibilities or software change.