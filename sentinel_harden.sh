#!/bin/bash
# Sentinel Hardening Script - Top 5 Priorities
echo "[*] Starting Sentinel Hardening..."

# 1. Ensure unused filesystems kernel modules are not available
echo "[*] Disabling unused filesystems (afs, gfs2)..."
for fs in afs gfs2; do
  if ! grep -q "install $fs /bin/false" /etc/modprobe.d/cis.conf 2>/dev/null; then
    echo "install $fs /bin/false" >> /etc/modprobe.d/cis.conf
    modprobe -r "$fs" 2>/dev/null
  fi
done

# 2. Hardening /tmp mount options
echo "[*] Hardening /tmp mount options (nodev, nosuid, noexec)..."
# Try systemd-specific unmask and enable if it's not already managed
systemctl unmask tmp.mount 2>/dev/null
systemctl enable tmp.mount 2>/dev/null

# Attempt immediate remount
mount -o remount,nodev,nosuid,noexec /tmp 2>/dev/null

# Update /etc/fstab for persistent mount options
if grep -q "[[:space:]]/tmp[[:space:]]" /etc/fstab; then
    # Update existing entry by appending options if they aren't there
    sed -i '/[[:space:]]\/tmp[[:space:]]/ s/defaults/defaults,nodev,nosuid,noexec/' /etc/fstab
else
    echo "tmpfs /tmp tmpfs defaults,rw,nosuid,nodev,noexec,relatime 0 0" >> /etc/fstab
fi

echo "[*] Hardening complete. Please verify with 'findmnt /tmp' and 'lsmod'."
