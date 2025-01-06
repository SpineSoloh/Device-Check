import os
import platform
import psutil
import subprocess

def check_windows_updates():
    print("Checking for Windows updates...")
    try:
        result = subprocess.check_output("powershell.exe Get-WindowsUpdateLog", shell=True)
        print(result.decode())
    except Exception as e:
        print(f"Error checking for Windows updates: {e}")

def check_windows_defender():
    print("Checking Windows Defender status...")
    try:
        result = subprocess.check_output("powershell.exe Get-MpComputerStatus", shell=True).decode()
        print(result)
        if "AMServiceEnabled : True" in result and "RealTimeProtectionEnabled : True" in result:
            print("Windows Defender is active and real-time protection is enabled.")
        else:
            print("Warning: Windows Defender is not fully active or real-time protection is disabled.")
    except Exception as e:
        print(f"Error checking Windows Defender: {e}")

def check_linux_updates():
    print("Checking for Linux system updates...")
    try:
        result = subprocess.check_output("sudo apt-get update && sudo apt-get upgrade --dry-run", shell=True)
        print(result.decode())
    except Exception as e:
        print(f"Error checking for Linux updates: {e}")

def check_selinux_apparmor():
    print("Checking SELinux/AppArmor status...")
    try:
        selinux_status = subprocess.check_output("sestatus", shell=True).decode()
        print(f"SELinux status:\n{selinux_status}")
    except Exception as e:
        print("SELinux is not installed or active.")
    
    try:
        apparmor_status = subprocess.check_output("sudo apparmor_status", shell=True).decode()
        print(f"AppArmor status:\n{apparmor_status}")
    except Exception as e:
        print("AppArmor is not installed or active.")

def check_clamav_updates():
    print("Checking ClamAV database updates...")
    try:
        result = subprocess.check_output("sudo freshclam", shell=True)
        print(result.decode())
    except Exception as e:
        print(f"Error updating ClamAV: {e}")

def scan_for_malware():
    print("Scanning for malware...")
    if platform.system() == 'Windows':
        check_windows_defender()
    elif platform.system() == 'Linux':
        try:
            print("Running ClamAV scan...")
            result = subprocess.check_output("sudo clamscan --infected --recursive /", shell=True)
            print(result.decode())
        except Exception as e:
            print(f"Error running ClamAV scan: {e}")
    else:
        print("Unsupported OS for malware scan.")

def check_firewall_status():
    print("Checking firewall status...")
    try:
        if platform.system() == 'Windows':
            output = subprocess.check_output("netsh advfirewall show allprofiles", shell=True)
            print(output.decode())
        elif platform.system() == 'Linux':
            output = subprocess.check_output("sudo ufw status", shell=True)
            print(output.decode())
        else:
            print("Unsupported OS for firewall check.")
    except Exception as e:
        print(f"Error checking firewall: {e}")

def check_user_permissions():
    print("Checking for unnecessary admin/root users...")
    try:
        if platform.system() == 'Linux':
            result = subprocess.check_output("sudo awk -F: '($3 == 0) {print $1}' /etc/passwd", shell=True)
            print(f"Users with root privileges:\n{result.decode()}")
        elif platform.system() == 'Windows':
            result = subprocess.check_output("net localgroup administrators", shell=True)
            print(f"Users in Administrators group:\n{result.decode()}")
    except Exception as e:
        print(f"Error checking user permissions: {e}")

def monitor_logs():
    print("Monitoring system logs for anomalies...")
    try:
        if platform.system() == 'Linux':
            result = subprocess.check_output("sudo tail -n 50 /var/log/syslog", shell=True)
            print(f"Recent system logs:\n{result.decode()}")
        elif platform.system() == 'Windows':
            print("Log monitoring for Windows requires Event Viewer or a similar tool.")
    except Exception as e:
        print(f"Error monitoring logs: {e}")

def check_network_security():
    print("Checking for open ports...")
    try:
        if platform.system() == 'Linux':
            result = subprocess.check_output("sudo netstat -tuln", shell=True)
            print(f"Open ports:\n{result.decode()}")
        elif platform.system() == 'Windows':
            result = subprocess.check_output("netstat -an", shell=True)
            print(f"Open ports:\n{result.decode()}")
    except Exception as e:
        print(f"Error checking network security: {e}")

def main():
    print("Starting comprehensive security check...")
    if platform.system() == 'Windows':
        check_windows_updates()
    elif platform.system() == 'Linux':
        check_linux_updates()
        check_selinux_apparmor()
        check_clamav_updates()
    
    scan_for_malware()
    check_firewall_status()
    check_user_permissions()
    monitor_logs()
    check_network_security()
    print("Security check complete.")

if __name__ == '__main__':
    main()
