# 00 — Environment Setup

## Objective

Prepare a local Kali Linux workstation to reach only the target environment explicitly deployed by TryHackMe.

## Preparation checklist

- Confirm the room is active and identify the currently deployed target in the platform.
- Use the platform-provided VPN profile and an approved region.
- Keep the VPN profile outside Git and never share it.
- Confirm the AttackBox is stopped when using the local VPN connection, if platform connection rules require a single active connection.
- Start the lab machine and wait for initialization.
- Verify the VPN interface and route table.
- Confirm target reachability before beginning any scan.

## Local verification

```bash
ip -br addr
ip route
ip route get 192.0.2.10
```

The documentation-range address above is a placeholder, not a target.

## Connectivity checks

A limited ICMP check may help determine whether a host responds. Lack of an ICMP response does not prove that a host is down; firewalls may block it. A response proves reachability for that test path, not that an application is vulnerable.

## Recordkeeping

Describe the process generically. Keep VPN profiles, live target addresses and private lab evidence out of the repository while the room is active.

## Completion criteria

- VPN interface is present and active.
- Route selection points to the intended training network.
- The currently deployed lab host is reachable by an approved test.
- No VPN profile or credential has entered version control.
