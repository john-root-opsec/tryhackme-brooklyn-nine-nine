# 00 — Environment Setup

## Objective

Prepare the local Kali Linux workstation and connect it to the TryHackMe room through the approved access path.

## Instructor workflow

1. Open the Brooklyn Nine-Nine room.
2. Start the lab machine and wait until the platform reports that it is running.
3. Note the current target address displayed by TryHackMe.
4. Use the AttackBox or connect the local Kali workstation through the TryHackMe OpenVPN configuration.
5. When using local Kali, keep the VPN profile in a private local directory and do not add it to Git.
6. Confirm the VPN interface and route.
7. Perform a basic reachability check before starting service discovery.

## Local checks

```bash
ip -br addr
ip route
```

The interface and route output should show that the VPN is active and that the training network is routed through the expected tunnel.

## ICMP reachability

A ping test can confirm that the target responds to ICMP from the current network path. It is not a port scan, and a lack of response does not necessarily mean the target is offline.

## Operational notes

- Use the current target address from the active room session.
- Do not reuse the address shown in the instructor's recording.
- Keep the OpenVPN terminal running while the VPN is required.
- Stop the AttackBox if the platform's connection rules require a single active VPN connection.
- Never commit the `.ovpn` file, passwords or other authentication material.

## Completion criteria

- Lab machine is running.
- Local Kali has an active approved connection.
- VPN interface and routing are present.
- Basic target reachability has been checked.
