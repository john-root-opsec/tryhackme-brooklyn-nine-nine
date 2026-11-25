# Detection & Monitoring — Lessons from the Lab

## Objective

Connect the instructor's offensive workflow to the telemetry a system administrator or SOC analyst could use to detect similar activity.

## Web reconnaissance

Potential telemetry:
- HTTP access logs showing repeated requests for candidate paths;
- unusual request rates and repeated 403/404 responses;
- requests for backup files, metadata files or unexpected static resources;
- access to resources that are not part of normal site behavior.

A directory-discovery pattern may be a legitimate assessment or automated abuse. Correlate the source, time window, request sequence and authorization context.

## Network scanning

Potential telemetry:
- repeated connection attempts across multiple destination ports;
- sequential or high-volume SYN packets;
- firewall deny events;
- IDS/IPS network-scan alerts.

One SYN packet is not proof of malicious scanning. Look for patterns and correlate them with the approved testing window.

## FTP activity

Potential telemetry:
- anonymous or unusual authentication attempts;
- directory listings and file downloads;
- uploads, renames or deletions;
- repeated access to directories outside normal usage.

FTP logs should be correlated with file-system events where available.

## SSH authentication

Potential telemetry:
- repeated authentication failures;
- successful login after a sequence of failures;
- logins outside expected source networks or time windows;
- unusual account use or interactive sessions.

A failed login alone does not prove a brute-force attack. Review volume, timing, source diversity and account context.

## Privileged execution

Potential telemetry:
- sudo authorization and command-execution records;
- execution of utilities with elevated identity;
- changes to privileged files or system configuration;
- unexpected child processes launched by privileged utilities.

Correlate the command, effective identity, parent process and user session.

## Triage workflow

1. Preserve relevant logs and timestamps.
2. Identify the host, account, source and service.
3. Build a timeline across web, network, authentication and system events.
4. Determine whether the behavior was authorized.
5. Assess impact and scope.
6. Contain and remediate through the organization's process.
7. Record the detection gap and lessons learned.

## Evidence handling

Logs and packet captures may contain credentials, personal data or confidential information. Collect only what is necessary and store it in an approved location.
