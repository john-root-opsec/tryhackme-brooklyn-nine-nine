# Detection & Monitoring

## Purpose

The defensive view asks how an organization could observe, investigate and respond to activity associated with exposed services and account access.

## Useful telemetry sources

| Source | Possible security value |
|:--|:--|
| Firewall logs | Allowed and denied connection attempts |
| Network flow records | Source/destination pairs, ports, timing and volume |
| Web server access logs | Paths, methods, status codes, user agents and request patterns |
| SSH authentication logs | Successful and failed login events |
| FTP server logs | Authentication and file-transfer activity |
| Linux audit records | Changes to sensitive files and privileged actions |
| Endpoint telemetry | Process execution, account changes and persistence indicators |

Exact log names and locations vary by distribution, service and configuration.

## Detection themes

- Repeated authentication failures
- Logins from unusual sources or at unusual times
- Access to sensitive files outside normal patterns
- Unexpected uploads or directory changes
- New or modified privileged execution rules
- Unexpected services listening on network interfaces

One event rarely proves malicious activity. Correlate source, identity, timing, host context and related events.

## Incident triage

1. Preserve relevant logs and timestamps.
2. Confirm which host, account and service are involved.
3. Establish a timeline.
4. Validate whether the behavior is expected.
5. Determine affected assets and potential impact.
6. Contain and remediate according to the organization's process.
7. Record lessons learned.

Collect only the data needed. Packet captures and logs may contain credentials, personal data or confidential business information.
