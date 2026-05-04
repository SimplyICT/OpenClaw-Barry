# Erik Selvig (Security Engineer) - Dedicated Memory
- role: infrastructure architecture & hardening
- focus: SIEM, EDR, IAM, telemetry, resilience
- context: builds the tools the SOC uses
---
## Engineering Logs
- 2026-05-04: System architecture defined. Focus on visibility and "secure by design" principles.
- 2026-05-04 00:32 UTC: Attempted systemd dashboard setup. Systemd unavailable; using manual background process on port 45680.
- 2026-05-04 00:39 UTC: Railway architecture pivot. Railway only exposes one port (usually 443). Moving dashboard to /src/public/dashboard.html to be served by the main web process.
