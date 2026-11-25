# 06 — Privilege Escalation Review

## Objective

Follow the instructor's final technical stage: inspect sudo permissions, research the security implications of the permitted Unix binary and understand how an overly broad privilege rule can cross a user/root boundary.

## Review sudo policy

The instructor uses sudo policy inspection to determine which commands the authenticated account is allowed to execute with elevated privileges.

The important fields are:
- the user and host context;
- the permitted command;
- the target execution identity;
- whether a password is required;
- argument restrictions or lack of restrictions.

A command being listed in sudo policy does not automatically mean unrestricted root access. The behavior of that program and the permitted arguments matter.

## Research the permitted binary

The instructor consults GTFOBins to understand how a legitimate Unix utility may behave when it is granted elevated execution rights.

GTFOBins is a reference for reviewing:
- whether a program can launch another command;
- whether it can open a shell or invoke a system function;
- whether the behavior depends on the execution context;
- what administrator configuration makes the behavior dangerous.

The exact room-specific binary behavior and exploitation sequence are intentionally omitted while the room is active.

## Verify privilege context

Security testing should distinguish between:
- the original authenticated account;
- a process running with elevated privileges;
- a shell operating as root.

Verification should establish the effective identity rather than relying on the fact that a command was accepted.

## Defensive relevance

- Keep sudo rules narrow and task-specific.
- Avoid granting unrestricted access to general-purpose utilities.
- Restrict command arguments where possible.
- Review rules that do not require a password.
- Audit privileged binaries and service accounts.
- Remove excessive permissions and validate the correction.

## Publication boundary

Do not publish the room's exact sudo rule, privileged binary, shell-escape sequence, root proof output or flags while the room is active.
