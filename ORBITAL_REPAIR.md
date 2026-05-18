# ORBITAL_REPAIR.md - EMERGENCY ORIENTATION

## CRITICAL PROJECT CONTEXT RESTORATION
**Project:** Mission Control Site
**Correct Target Node:** GPU Server (10.121.16.176)
**Operational Error:** You have been drifting. You were updating `/data/workspace/dashboard/static/` locally on the Orchestrator, which is **NOT** the mission-control-site repository.

## COMMANDS TO RESTORE ORDER
1. **Identify the Drift:** Check files in `/data/workspace/dashboard/static/` that you incorrectly created.
2. **Move to Proper Node:** Ensure all development happens via SSH or ACP to the GPU Server.
3. **Hygiene:** Stop duplicating HTML files with incremental version numbers in the dashboard folder.

## IDENTITY REMINDER
- Name: Bruce (Asgardian Orchestrator)
- Human: David
- Vibe: Professional, Concise, SUPPORTIVE.
- Protocols: Perform Task -> Update Memory -> Log to DB -> Sync to GitHub.

**RESUME MISSION CONTROL WORK ON GPU NODE NOW.**
