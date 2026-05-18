# ORBITAL_REPAIR.md - EMERGENCY ORIENTATION

## CRITICAL REPOSITORY SEPARATION
**Identity/Orchestration:** [https://github.com/simplyict/openclaw-bruce](https://github.com/simplyict/openclaw-bruce) (READ ONLY for identity files/SOUL)
**Active Work Site:** [https://github.com/simplyict/mission-control-site](https://github.com/simplyict/mission-control-site) (ACTIVE DEVELOPMENT)

**Operational Error:** You are incorrectly pushing "Mission Control" code to the "OpenClaw-Bruce" repository. This is causing repository pollution and logic drift.

## CORRECT WORKFLOW
1. **Pull Identity:** Read from `openclaw-bruce` (Local/Cloud).
2. **Execute Work:** Switch context to `mission-control-site` repository (on GPU Node).
3. **Commit/Push:** Send updates ONLY to the `mission-control-site` repo.

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
