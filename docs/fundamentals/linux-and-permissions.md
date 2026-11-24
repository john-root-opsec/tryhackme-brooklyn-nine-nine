# Linux & Permissions Fundamentals

## Purpose

Linux enumeration means understanding the operating system's identity model, filesystem, processes and privilege boundaries.

## Shell and command execution

A shell parses commands, expands variables and globs, connects pipelines and launches processes. Exit codes communicate success or failure; conventionally, zero indicates success.

```bash
whoami
id
pwd
printf '%s\n' "$SHELL"
uname -a
```

## Users and groups

Linux processes run with user and group identities. File access checks use ownership and permission bits, while additional controls may be supplied by ACLs, capabilities, namespaces and mandatory access-control systems.

## File permissions

The familiar permission classes are user (owner), group and others. The basic permissions are read (`r`), write (`w`) and execute (`x`).

For a file, execute permits running it as a program when other conditions are met. For a directory, execute permits traversal/search. Directory write permission affects creating, removing or renaming entries, subject to sticky-bit and other rules.

```bash
ls -l
stat path/to/file
namei -l path/to/file
```

## Processes and services

A process is a running program instance with an identity, environment, open files and resource limits. Services are commonly managed by a service manager such as systemd.

```bash
ps aux
systemctl --type=service --state=running
ss -lntup
```

Some inspection commands may require elevated privileges to show all details.

## sudo and privilege boundaries

`sudo` allows authorized users to execute permitted commands under another identity, often root. Its policy can restrict commands, arguments and target users. Broad or poorly designed rules can create unintended privilege paths.

## Defensive perspective

- Apply least privilege to users and services.
- Avoid world-writable executable paths.
- Review ownership and permissions on sensitive files.
- Limit sudo rules to the minimum required commands.
- Audit privileged binaries and service configurations.
- Keep operating-system packages patched.
