from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

def process_packet(packet):
    """Function to process and analyze a captured packet."""
    print("\n=== Packet Captured ===")
    print(f"Time: {datetime.now()}")

    # Check if the packet has an IP layer
    if IP in packet:
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")

        # Determine the protocol
        if TCP in packet:
            print("Protocol: TCP")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")
        elif UDP in packet:
            print("Protocol: UDP")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")
        elif ICMP in packet:
            print("Protocol: ICMP")
        else:
            print("Protocol: Other")

        # Display payload if available
        payload = bytes(packet[IP].payload)
        if payload:
            print("Payload (raw):")
            print(payload[:50])  # Display the first 50 bytes
        else:
            print("No payload in this packet.")
    else:
        print("Non-IP packet detected.")

def main():
    print("Network Packet Analyzer (Packet Sniffer)")
    print("Press CTRL+C to stop capturing packets.\n")
    
    try:
        # Sniff packets and process them
        sniff(prn=process_packet, store=False)
    except KeyboardInterrupt:
        print("\nPacket capture stopped. Exiting...")
    except PermissionError:
        print("Permission denied: Run the script as Administrator or with root privileges.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
