#Task - Automated network packet analysis
#The code captures the packets upto packet count of 100. It processes and extracts information from it such as source and destination
#port or IP addresses, packet number, sniff time, transport layer, etc. The information gathered from the packets can be further 
#customised according to the needs of the network analysis.

#pyshark is imported for packet capture and analysis
import pyshark

#We need to define the network interface to capture packets from
interface = 'eth0'

#This function processes each packet and extracts relevant information from it such as packet number, sniff item, 
#source and destination port and IP addresses, etc.
def process_packet(packet):
    try:
        #To print basic packet information
        print(f"Packet: {packet.number}, {packet.sniff_time}, {packet.transport_layer}")
        
        #Extracting and printing IP layer information
        if 'IP' in packet:
            ip_layer = packet['IP']
            print(f"Source IP: {ip_layer.src}, Destination IP: {ip_layer.dst}")
        
        #Extracting and printing TCP layer information
        if 'TCP' in packet:
            tcp_layer = packet['TCP']
            print(f"Source Port: {tcp_layer.srcport}, Destination Port: {tcp_layer.dstport}")
        
        #Extracting and printing UDP layer information
        if 'UDP' in packet:
            udp_layer = packet['UDP']
            print(f"Source Port: {udp_layer.srcport}, Destination Port: {udp_layer.dstport}")

        #Extracting and printing DNS queries
        if 'DNS' in packet:
            dns_layer = packet['DNS']
            if hasattr(dns_layer, 'qry_name'):
                print(f"DNS Query: {dns_layer.qry_name}")

        #Extracting and printing HTTP requests
        if 'HTTP' in packet:
            http_layer = packet['HTTP']
            if hasattr(http_layer, 'host'):
                print(f"HTTP Request: {http_layer.host}{http_layer.path}")

        #Extracting and printing HTTPS requests (SSL/TLS layer)
        if 'SSL' in packet or 'TLS' in packet:
            ssl_layer = packet['SSL'] if 'SSL' in packet else packet['TLS']
            if hasattr(ssl_layer, 'handshake_extensions_server_name'):
                print(f"HTTPS Request: {ssl_layer.handshake_extensions_server_name}")

            
    except AttributeError as e:
        # Handle packets that may not have the expected attributes
        print(f"Error processing packet: {e}")

#The packets are captured live thorugh the specified interface.
capture = pyshark.LiveCapture(interface=interface)

#The packets can also be saved for more analysis later by: 
#capture = pyshark.LiveCapture(interface=interface, output_file='capture.pcap')

#The live capture can be substituted by offline capture as well through the following: 
#capture = pyshark.FileCapture('capture.pcap')
#for packet in capture:
#    process_packet(packet)


print("Starting packet capture: ")

#sniff_continuously is used to specify the packet count to which the packets are to be captured continuously.
#process_packet is the function defined above and is responsible for the processing of the packets
for packet in capture.sniff_continuously(packet_count=100):  # Change packet_count as needed
    process_packet(packet)

print("Packet capture completed.")
