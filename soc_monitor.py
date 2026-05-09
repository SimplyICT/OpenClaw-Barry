import os
import time
import requests
import sys
from supabase import create_client

# --- CONFIGURATION ---
WAZUH_URL = "https://securesocentral.com.au:55000"
WAZUH_USER = "wazuh-wui"
WAZUH_PASS = "cdcxsOTW165Tqa2N9.0FW4L*Y6*0VK2T"
SUPABASE_URL = "https://zhvxjuhgfudavxrfsasn.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpodnhqdWhnZnVkYXZ4cmZzYXNuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3Njc5OTQxOSwiZXhwIjoyMDkyMzc1NDE5fQ.-Y38GK4eJ6ddTRnMKnoCF1iQIdmiwAYEbvuSeKTDd4E"

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def log_to_supabase(agent, task, status):
    try:
        sb = create_client(SUPABASE_URL, SUPABASE_KEY)
        data = {
            "agent_name": agent,
            "task_description": task,
            "model_used": "Automated-SOC-Monitor",
            "status": status
        }
        sb.table("agent_logs").insert(data).execute()
    except: pass

def get_wazuh_token():
    try:
        res = requests.get(f"{WAZUH_URL}/security/user/authenticate", auth=(WAZUH_USER, WAZUH_PASS), verify=False, timeout=10)
        return res.json().get('data', {}).get('token')
    except: return None

def monitor_alerts():
    print("🛡️ SOC Online. Monitoring Wazuh feeds...")
    while True:
        token = get_wazuh_token()
        if token:
            headers = {'Authorization': f'Bearer {token}'}
            try:
                # Polling Manager for logs
                res = requests.get(f"{WAZUH_URL}/manager/logs", headers=headers, verify=False, timeout=10)
                if res.status_code == 200:
                    print("✅ Wazuh Link Active. Pulled Status.")
                else:
                    print(f"⚠️ Health Check Code: {res.status_code}")
            except Exception as e:
                print(f"Error: {e}")
        else:
            print("❌ Authentication Failed.")
        sys.stdout.flush()
        time.sleep(300)

if __name__ == "__main__":
    print("LOGGING START")
    sys.stdout.flush()
    monitor_alerts()
