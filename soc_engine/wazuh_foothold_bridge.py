import sys
import os
import requests
import json
import time

# Ensure workspace is in path
sys.path.append('/data/workspace')

from soc_engine.threat_intel_bridge import check_file_hash
from soc_engine.remediation_playbook import get_remediation_text
from supabase import create_client

WAZUH_URL = "https://securesocentral.com.au"
WAZUH_USER = "wazuh-wui"
WAZUH_PASS = "cdcxsOTW165Tqa2N9.0FW4L*Y6*0VK2T"
SUPABASE_URL = "https://zhvxjuhgfudavxrfsasn.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpodnhqdWhnZnVkYXZ4cmZzYXNuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3Njc5OTQxOSwiZXhwIjoyMDkyMzc1NDE5fQ.-Y38GK4eJ6ddTRnMKnoCF1iQIdmiwAYEbvuSeKTDd4E"

def poll_manager():
    print("🛡️ ASGARD SENSOR v2: Polling for real-time fleet events...")
    # Specifically looking for ANY alert (not just FIM) that mentions our keyword.
    
    last_id = ""
    while True:
        try:
            import subprocess
            # Grab the last 10 alerts that match our keyword
            res = subprocess.check_output(["ssh", "clawbot@208.87.135.185", "sudo -n tail -n 50 /var/ossec/logs/alerts/alerts.json | grep 'asgard'"]).decode()
            
            for line in res.strip().split('\n'):
                if not line: continue
                alert = json.loads(line)
                alert_id = alert.get('id', '')
                
                if alert_id != last_id:
                    agent = alert.get('agent', {}).get('name', 'Unknown')
                    # Promotion to Squad Board
                    sb = create_client(SUPABASE_URL, SUPABASE_KEY)
                    msg = f"FOOTHOLD DETECTED || Agent: {agent} || {alert.get('rule',{}).get('description')}"
                    
                    sb.table("agent_logs").insert({
                        "agent_name": "Thor",
                        "task_description": msg,
                        "status": "RESPONDING",
                        "model_used": "Asgard-Autonomous-V2"
                    }).execute()
                    
                    last_id = alert_id
                    print(f"✅ AUTO-SIGNAL: Captured {agent}")
        except:
            pass
        time.sleep(5)

if __name__ == "__main__":
    poll_manager()
