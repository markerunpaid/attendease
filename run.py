# run.py
from app import create_app
import socket

app = create_app()

def get_local_ip():
    """Get the local IP address of this machine"""
    try:
        # Create a socket to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to an external address (doesn't actually send data)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "Unable to determine"

if __name__ == '__main__':
    print("\n" + "="*60)
    print("    AttendEase - Attendance Management System")
    print("="*60)
    
    # Try to get current IP
    current_ip = get_local_ip()
    
    print("\n📋 SETUP INSTRUCTIONS:")
    print("-" * 60)
    print("1. Connect your laptop to the ESP32 hotspot:")
    print("   SSID: ClassAttendance_Prof001")
    print("   Password: Class123")
    print("\n2. After connecting, your IP will likely be: 192.168.4.2")
    print(f"   (Current detected IP: {current_ip})")
    print("\n3. The ESP32 will automatically discover this server")
    print("   by scanning 192.168.4.2 through 192.168.4.20")
    print("\n4. Once discovered, students connecting to the hotspot")
    print("   will be redirected to the attendance portal")
    print("-" * 60)
    
    print("\n🚀 Starting Flask server on 0.0.0.0:5000...")
    print("   Health check endpoint: http://[YOUR-IP]:5000/health")
    print("="*60 + "\n")
    
    # Run Flask server
    # Listen on all interfaces so ESP32 can discover it
    app.run(host='0.0.0.0', port=5000, debug=True)