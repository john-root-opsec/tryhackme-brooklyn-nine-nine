# 01 — Lab Environment & VPN Connectivity

## Objective

Prepare the local Kali Linux workstation and connect it to the TryHackMe room through the approved VPN path. This stage establishes the network context required for subsequent scans.

## Observed workflow

The supplied terminal evidence shows OpenVPN establishing a TLS-protected session with the TryHackMe VPN endpoint, creating a tunnel interface, receiving route configuration and assigning an address to the tunnel. A subsequent ICMP test received four replies with no packet loss.

The raw VPN profile name, local tunnel address and full connection transcript are not reproduced here. They are not required to explain the workflow.

## Local verification

The captured workflow checked the tunnel interface with:

```bash
ip -br addr show tun0
```

- `ip` inspects and manages network interfaces and routes.
- `-br` requests brief output.
- `addr` selects interface address information.
- `show tun0` limits output to that interface name. The interface name can differ between sessions.

Reachability was checked with ICMP:

```bash
ping -c 4 <LAB_TARGET>
```

- `ping` sends ICMP Echo Requests and reports Echo Replies.
- `-c 4` sends four requests and then stops.
- `<LAB_TARGET>` represents the current address provided by the active TryHackMe room.

The observed result was four replies and 0% packet loss. This supports basic IP reachability at that moment; it does not prove that a TCP service is listening.

## Interpretation

The VPN establishes a routed path into the authorized training network. ICMP provides a simple reachability check before service discovery. ICMP can be filtered independently of TCP, so a failed ping would not by itself prove that the host was offline.

## Operational security

- Keep VPN profiles and certificates outside source control.
- Do not reuse the target address shown in a recording; use the address assigned by the current room session.
- Avoid publishing local tunnel addresses or connection logs that reveal personal network context.

## Result

The evidence supports an active TryHackMe VPN connection and successful reachability testing, allowing the assessment to proceed.

## Practical evidence

![OpenVPN tunnel initialization and route setup](../evidence/01-vpn-tunnel.png)

*Evidence 01 — OpenVPN reports that initialization completed and the tunnel interface was brought up.*
