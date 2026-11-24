# Hardening & Remediation

## Purpose

A penetration test is incomplete without explaining how to reduce the identified risk and verify that the correction works.

## Service exposure

- Disable services that are not required.
- Bind services to appropriate interfaces.
- Restrict administrative services to trusted networks.
- Use firewall rules and network segmentation.
- Maintain accurate service inventories.

## FTP and file transfer

- Avoid legacy cleartext FTP when secure alternatives are available.
- Disable unnecessary anonymous access.
- Restrict file permissions and transfer directories.
- Monitor upload, download and deletion events.
- Protect stored files and credentials.

## SSH

- Restrict allowed users and groups.
- Prefer strong key-based authentication with appropriate key protection.
- Disable unused authentication options.
- Monitor authentication activity.
- Keep server packages maintained.

## Linux privilege controls

- Apply least privilege.
- Review sudoers entries regularly.
- Avoid broad wildcard permissions.
- Audit SUID/SGID binaries and Linux capabilities.
- Protect privileged scripts and configuration files.
- Remove stale accounts and unnecessary services.

## Verification

A remediation is not complete when a configuration file is edited. Verify that the intended service behavior changed, legitimate users can still work, the risky access path is no longer available, logs show expected behavior and the change is documented.

## Risk communication

Describe the affected asset, security condition, potential impact, evidence, likelihood assumptions and recommended correction. Do not overstate exploitability when evidence is incomplete.
