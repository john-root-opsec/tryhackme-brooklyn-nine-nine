# 07 — Privilege Escalation: Sudo Misconfiguration

## Objective

Review the authenticated user's sudo permissions, identify the security impact of the permitted program and verify whether the resulting execution context crosses the user/root boundary.

## 1. Review sudo policy

The supplied terminal evidence shows `sudo -l` reporting that the authenticated lab user could execute `/usr/bin/less` as root without being prompted for a password.

The important security properties were:

- the command was permitted through sudo;
- the execution identity was root;
- the rule did not require a password;
- `less` is an interactive pager with capabilities beyond passive text viewing.

This was a configuration finding, not a defect in the pager itself.

## 2. Why a pager can become a privilege path

`less` is designed to display text interactively. Its interactive feature set can invoke an external command or shell. When the pager runs with elevated privileges and policy does not constrain its behavior, that child process can inherit the elevated execution context.

GTFOBins is a reference for reviewing how legitimate Unix binaries may be misused when granted excessive privileges. The key lesson is to evaluate the full behavior of a program, not only its apparent primary purpose.

## 3. Observed verification

The supplied screenshots show the privileged pager being used to reach a shell and an identity check returning `root`. A subsequent capture shows access to the root directory and the root-level flag file.

This report describes the mechanism and result, but omits the exact shell-escape invocation and the flag value. A technical portfolio can explain the misconfiguration and impact without publishing reusable credentials or room answer tokens.

## 4. Finding summary

| Field | Assessment |
|:--|:--|
| Finding | Overly permissive sudo rule for a general-purpose pager |
| Affected control | Privileged command delegation |
| Security impact | The permitted user could escape the intended pager function and obtain a root shell in the lab |
| Root cause | Delegating a shell-capable interactive program with root privileges without adequate restrictions |
| Evidence | Sudo policy output, root identity verification and root-directory access |
| Remediation | Remove the rule or replace it with a narrowly scoped, non-interactive administrative operation |

## 5. Remediation

- Remove sudo permissions for general-purpose pagers and other shell-capable utilities where they are not required.
- Prefer a dedicated administrative command with fixed behavior.
- Restrict command arguments and target identities.
- Require authentication for privileged operations where feasible.
- Audit sudoers entries for programs that can invoke shells or external commands.
- Re-test the policy after remediation to confirm that the unintended privilege path is closed.

## Result

The supplied terminal evidence supports a successful transition from the authenticated lab user to root through an overly permissive sudo rule for `less`. Root identity was verified and the root-level objective was reached.

## Practical evidence

![whoami confirms root after the less shell escape](../evidence/13-root-verification.png)

*Evidence 13 — After invoking the shell escape from the permitted `less` context, `whoami` returns `root`.*

![Root flag file access](../evidence/14-root-flag.png)

*Evidence 14 — `/root/root.txt` is accessed. The flag value is redacted.*
