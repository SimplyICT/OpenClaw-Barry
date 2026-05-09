import os
import sys
from datetime import datetime
from supabase import create_client, Client

def generate_consolidated_report(site_name, target_date):
    url = "https://zhvxjuhgfudavxrfsasn.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpodnhqdWhnZnVkYXZ4cmZzYXNuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3Njc5OTQxOSwiZXhwIjoyMDkyMzc1NDE5fQ.-Y38GK4eJ6ddTRnMKnoCF1iQIdmiwAYEbvuSeKTDd4E"
    supabase = create_client(url, key)
    
    # Logic: Pull EVERY device that has EVER been audited at this site
    res = supabase.table('audit_entries').select('*, devices(*)').eq('site_name', site_name).order('audit_date', desc=True).execute()
    raw_data = res.data

    if not raw_data:
        print(f"No records found.")
        return

    unique_devices = {}
    for entry in raw_data:
        sn = entry['serial_number']
        if sn and sn not in unique_devices:
            unique_devices[sn] = entry
    
    data = list(unique_devices.values())
    data.sort(key=lambda x: (str((x.get('devices') or {}).get('assigned_user_room') or '').lower()))

    report = []
    report.append(f"# Site Audit Report: {site_name}")
    report.append(f"Comprehensive Fleet Summary - Generated {datetime.now().strftime('%d %B %Y')}")
    report.append(f"\n## FLEET SUMMARY")
    report.append(f"• **Total Assets Audited:** {len(data)}")
    
    report.append("\n## DETAILED DEVICE AUDIT LOGS")
    
    for r in data:
        dev = r.get('devices') or {}
        report.append(f"\n### Room: {dev.get('assigned_user_room', 'Unassigned')}")
        report.append(f"**Asset:** {dev.get('brand_model', 'Unknown')} | **SN:** {r['serial_number']}")
        
        dtype = (dev.get('device_type') or "").lower()
        if "tablet" in dtype or "phone" in dtype:
            report.append(f"- **OS:** iOS {r.get('ios_version') or 'Latest'}")
            report.append(f"- **Media:** {r.get('photos_count', 0)} Photos | Date: {r.get('photos_date') or 'N/A'}")
            report.append(f"- **Sync:** Camera Sync Off: {'Yes' if r.get('camera_sync_off') else 'No'} | OneDrive: {'Yes' if r.get('onedrive_sync_on') else 'No'}")
        else:
            report.append(f"- **OS:** Windows {r.get('windows_os') or 'N/A'}")
            report.append(f"- **Compliance:** Updates: {r.get('update_status') or 'N/A'} | Security: {r.get('security_check') or 'N/A'}")

        if r.get('notes'):
            report.append(f"- **Notes:** {r['notes']}")

    final_report = "\n".join(report)
    fn = f"report_{site_name.replace(' ', '_')}_{target_date}.md"
    with open(fn, 'w') as f: f.write(final_report)
    print(f"Success: {len(data)} devices recorded.")

if __name__ == "__main__":
    if len(sys.argv) > 2: generate_consolidated_report(sys.argv[1], sys.argv[2])
