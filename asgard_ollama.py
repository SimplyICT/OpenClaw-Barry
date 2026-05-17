import subprocess
import json
import sys
import os

OLLAMA_URL = "http://100.117.41.63:11434/api/generate"
PROXY = "socks5h://127.0.0.1:1055"

def log_to_supabase(agent_name, prompt, model):
    desc = prompt[:100] + "..." if len(prompt) > 100 else prompt
    try:
        subprocess.run([
            "python3", "/data/workspace/logger.py", 
            agent_name, desc, f"{model} (Local-SDWAN)", "Success"
        ], capture_output=True)
    except:
        pass

def query_local(prompt, model="llama3.1:8b", agent="Bruce"):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    cmd = [
        "curl", "-s", "--socks5-hostname", "127.0.0.1:1055",
        "-X", "POST", OLLAMA_URL,
        "-d", json.dumps(payload),
        "-H", "Content-Type: application/json"
    ]
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        if result.returncode == 0:
            log_to_supabase(agent, prompt, model)
            return json.loads(result.stdout).get("response", "No response.")
        else:
            return f"Curl Error: {result.stderr}"
    except Exception as e:
        return f"System Error: {str(e)}"

if __name__ == "__main__":
    # Internal agent name detection or default to Bruce
    agent_name = os.getenv("ASGARD_AGENT", "Bruce")
    if len(sys.argv) > 1:
        print(query_local(" ".join(sys.argv[1:]), agent=agent_name))
