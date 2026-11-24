# 01 — Web Reconnaissance

## Objective

Understand what a web server exposes before drawing conclusions about its security.

## Investigation sequence

1. Open the HTTP service in a browser within the authorized lab.
2. Observe page title, visible content, redirects and browser errors.
3. Inspect delivered source and compare it with the live DOM.
4. Review loaded scripts, stylesheets, images and other static resources.
5. Inspect relevant response headers and status codes in developer tools.
6. Where the exercise permits, review local asset metadata with an appropriate tool.
7. Study content-discovery concepts and validate any response that appears interesting.

## Concepts to understand

- HTTP request/response lifecycle
- URL paths and query parameters
- HTML source versus live DOM
- Static assets and metadata
- Cookies, sessions and browser storage
- Directory indexing and accidental file exposure
- Custom 404 responses and false positives in content discovery

## Tool roles

- **Browser / Developer Tools:** inspect rendered page, DOM, requests, headers and resources.
- **ExifTool:** read supported metadata fields in files.
- **Gobuster:** request candidate content paths in an authorized scope and classify responses.

## Interpretation rules

A hidden path, metadata field or comment is not automatically a vulnerability. Validate whether it exposes sensitive information, changes access control or creates a realistic security impact.

## Defensive perspective

Remove unnecessary files and metadata, prevent unintended directory listings, avoid publishing debug artifacts and monitor unusual path-enumeration behavior.

Use sanitized generic examples only. Do not publish active-room answers, secret values, target-specific paths or exploitation steps.
