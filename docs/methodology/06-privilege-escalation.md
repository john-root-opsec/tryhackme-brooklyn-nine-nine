# 06 — Privilege Escalation Concepts

## Objective

Understand how a user with limited permissions might reach a more privileged security context when the system is misconfigured.

## Core concepts

- Linux user and group identities
- sudoers policy
- Set-user-ID (SUID) and Set-group-ID (SGID) behavior
- Linux capabilities
- Writable paths and unsafe file ownership
- Scheduled tasks and service permissions
- Environment and path-handling risks
- Legitimate binary behavior and GTFOBins as a security reference

## The role of GTFOBins

GTFOBins documents ways standard Unix binaries may be abused when they are available with unsafe permissions or execution context. The existence of a binary on a system is not, by itself, evidence of a vulnerability.

The security question is whether the user's permitted execution context allows an unintended action that crosses a privilege boundary.

## About less

`less` is a terminal pager used to view text. Like other powerful utilities, its behavior can be security-relevant if an administrator grants an overly broad privilege rule. Review the permission context and policy rather than assuming every use of the program is dangerous.

## Defensive perspective

- Avoid unrestricted sudo rules.
- Restrict permitted commands and arguments.
- Remove unnecessary SUID/SGID permissions.
- Audit Linux capabilities.
- Ensure privileged scripts and parent directories are not writable by untrusted users.
- Keep software updated and review service accounts.

This page covers security principles. Do not publish room-specific command sequences, flags, credentials or walkthroughs while the room is active.
