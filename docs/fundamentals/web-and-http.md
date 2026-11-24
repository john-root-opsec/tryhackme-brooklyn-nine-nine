# Web & HTTP Fundamentals

## Purpose

Web reconnaissance examines how a web application presents content and how its server responds to requests. The browser is an investigative tool, but every observation must be interpreted carefully.

## URL anatomy

A URL may contain a scheme (such as `http` or `https`), hostname, optional port, path, query string and fragment. The fragment is processed by the client and is not sent as part of the HTTP request target.

## HTTP request and response

An HTTP request includes a method, target, protocol version, headers and sometimes a body. A response contains a status code, headers and sometimes a body.

Common methods:
- `GET` — retrieve a representation;
- `HEAD` — request response metadata without the usual response body;
- `POST` — submit data for processing;
- `PUT` and `DELETE` — request resource changes, subject to application semantics.

Status-code groups:
- `2xx` success;
- `3xx` redirection;
- `4xx` client-side request or authorization issue;
- `5xx` server-side failure.

A status code alone rarely explains full application behavior.

## Browser inspection

Developer tools help inspect the DOM, loaded scripts and images, network requests and response headers, cookies and storage, and console errors.

"View Source" and the live DOM are not identical. The source is the document delivered by the server; the live DOM may be modified by JavaScript after loading.

## Static assets and metadata

Images and documents may contain metadata such as timestamps, software identifiers, camera information or author fields. Metadata is not automatically secret, but it can disclose information an organization did not intend to publish.

Review only files within the authorized lab scope. Avoid uploading private or sensitive assets to third-party analysis services.

## Content discovery

Content-discovery tools request candidate paths and classify responses. Results require validation: custom error pages may look successful, redirects affect status codes, and rate limits or access controls can distort results. A discovered path is not necessarily a vulnerability.

## Security concepts

Web exposure can include directory listings, backup files, debug artifacts, source maps, verbose error messages and unsafe access controls. A finding requires evidence of impact, not merely an unusual URL.

## Defensive perspective

- Publish only required resources.
- Prevent unnecessary directory listing.
- Remove backups and development artifacts from production.
- Set appropriate cache, cookie and security headers.
- Monitor unusual request patterns and repeated path guessing.
- Keep server software and dependencies maintained.
