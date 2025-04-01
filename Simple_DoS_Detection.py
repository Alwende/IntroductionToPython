from scapy.all import sniff, IP
import time
from collections import defaultdict

# Configuration
INTERFACE = "Realtek RTL8821CE 802.11ac PCIe Adapter"  # Replace with your network interface (e.g., "wlan0")
PACKET_THRESHOLD = 50  # Number of packets within the TIME_WINDOW to trigger an alert
TIME_WINDOW = 5  # Time window in seconds to track packets

# Global dictionary to store packet counts per IP and timestamp
ip_packet_counts = defaultdict(lambda: [])

def packet_handler(packet):
    if IP in packet:
        src_ip = packet[IP].src
        current_time = time.time()

        # Clean up old timestamps
        ip_packet_counts[src_ip] = [t for t in ip_packet_counts[src_ip] if current_time - t < TIME_WINDOW]

        # Increment packet count for the source IP
        ip_packet_counts[src_ip].append(current_time)

        if len(ip_packet_counts[src_ip]) > PACKET_THRESHOLD:
            print(f"Potential DoS attack detected from: {src_ip} (>{PACKET_THRESHOLD} packets in {TIME_WINDOW} seconds)")

if __name__ == "__main__":
    print(f"Starting DoS detection on interface: {INTERFACE}")
    print(f"Alerting on > {PACKET_THRESHOLD} packets from the same IP within {TIME_WINDOW} seconds...")
    try:
        sniff(iface=INTERFACE, store=False, prn=packet_handler)
    except PermissionError:
        print("Error: You need administrator/root privileges to run this script.")
        print("Try running with 'sudo python SimpleDoSDetection.py'")
    except Exception as e:
        print(f"An error occurred: {e}")