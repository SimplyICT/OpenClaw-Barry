# ASGARDIAN ROUTER CHEAT SHEET

As Bruce (Orchestrator), I route David's natural language requests to the specialized agents based on the following triggers. You can also use the **Quick Commands** for direct dispatch.

## 🎯 Natural Language Routing
| Request Type | Trigger Keywords | Target |
| :--- | :--- | :--- |
| **Strategy & Command** | "decide", "approve", "summarize risk", "what is the plan" | **Thor** (SOC Manager) |
| **Building & Hardening** | "install", "harden", "config", "setup", "fix infrastructure" | **Erik Selvig** (Security Engineer) |
| **Alert Triage** | "is this bad?", "look at this alert", "enrich this IP" | **Loki** (Tier 1 Triage) |
| **Active Investigation** | "investigate", "scope the impact", "contain this", "stop it" | **Lady Sif** (Tier 2 IR) |
| **Proactive Hunting** | "hunt for", "any shadows?", "look for persistence", "find bypasses" | **Heimdall** (Tier 3 Hunting) |
| **Forensic Evidence** | "reconstruct", "timeline", "what happened?", "prove it", "exfiltration?" | **Phil Coulson** (Forensics) |

## ⚡ Quick Command Shortcuts
Use these exact shortcuts to bypass the router and speak directly to a specialist:

- `!thor` : Dispatch strategic oversight or incident command.
- `!erik` : Dispatch system engineering, hardening, or configuration tasks.
- `!loki` : Dispatch alert enrichment, triage, or log filtering.
- `!sif`  : Dispatch active incident investigation or threat containment.
- `!heim` : Dispatch proactive hunting or stealth detection.
- `!phil` : Dispatch forensic reconstruction or timeline analysis.

## 🛡️ Routing Rules
1. **Persona Lock:** The dispatched agent will respond using their dedicated `IDENTITY.md` and `SOUL.md`.
2. **Memory Access:** The agent will automatically pull from their `/memory/agents/<Name>.md`.
3. **Workspace Isolation:** All work will be performed in `/agents/<Name>/`.
