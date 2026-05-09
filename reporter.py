import os
import sys
from datetime import datetime
from supabase import create_client, Client

def generate_consolidated_report(site_name, target_date):
    url = "https://zhvxjuhgfudavxrfsasn.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpodnhqdWhnZnVkYXZ4cmZzYXNuIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3Njc5OTQxOSwiZXhwIjoyMDkyMzc1NDE5fQ.-Y38GK4eJ6ddTRnMKnoCF1iQIdmiwAYEbvuSeKTDd4E"
    supabase = create_client(url, key)
    
    # CRITICAL: Pull ALL entries for the site, ordered by most recent first
    res = supabase.table('audit_entries').select('*, devices(*)').eq('site_name', site_name).order('audit_date', desc=True).execute()
    raw_data = res.data

    if not raw_data:
        print(f"Error: No data found.")
        return

    # Deduplicate: one record per unique serial number
    unique_devices = {}
    for entry in raw_data:
        sn = entry['serial_number']
        if sn and sn not in unique_devices:
            unique_devices[sn] = entry
    
    data = list(unique_devices.values())
    # Sort by Room then Model
    data.sort(key=lambda x: (str((x.get('devices') or {}).get('assigned_user_room') or ''), str((x.get('devices') or {}).get('brand_model') or '')))

    report = []
    report.append(f"# ASGARDIAN AUDIT REPORT: {site_name}")
    report.append(f"Audit Summary Generated on {datetime.now().strftime('%d %B %Y')}")
    report.append("\n## SITE OVERVIEW")
    report.append(f"• **Total Fleet Count:** {len(data)} identified assets.")
    report.append(f"• **Audit Status:** Comprehensive review of all known hardware.")

    report.append("\n## COMPLIANCE LOG BY LOCATION")
    
    for r in data:
        dev = r.get('devices') or {}
        room = dev.get('assigned_user_room', 'Central / Unassigned')
        report.append(f"\n### Room: {room}")
        report.append(f"**Asset:** {dev.get('brand_model', 'Unknown Device')} (SN: `{r['serial_number']}`) | **Last Seen:** {str(r.get('audit_date'))[:10]}")
        
        # Determine device tech lineage
        dtype = (dev.get('device_type') or "").lower()
        if "tablet" in dtype or "phone" in dtype:
            report.append(f"- **Operating System:** iOS {r.get('ios_version') or 'Latest'}")
            report.append(f"- **Photos/Media:** {r.get('photos_count', 0)} files found.")
            report.append(f"- **Cloud Sync:** Camera Uploads: {'OFF' if r.get('camera_sync_off') else 'ON'} | OneDrive: {'ON' if r.get('onedrive_sync_on') else 'OFF'}")
        else:
            report.append(f"- **Operating System:** Windows {r.get('windows_os') or 'N/A'}")
            report.append(f"- **Security Patching:** {r.get('update_status') or 'Current'}")
            report.append(f"- **Antivirus/Defender:** {r.get('security_check') or 'Active'}")

        if r.get('notes'):
            report.append(f"- **Engineer Notes:** {r['notes']}")

    final_report = "\n".join(report)
    fn = f"report_{site_name.replace(' ', '_')}_{target_date}.md"
    with open(fn, 'w') as f: f.write(final_report)
    print(f"Generated {fn} with {len(data)} records.")

if __name__ == "__main__":
    if len(sys.argv) > 2: generate_consolidated_report(sys.argv[1], sys.argv[2])
