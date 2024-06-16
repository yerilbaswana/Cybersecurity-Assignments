#Brute force attack using John the Ripper
#Here, we are doing a brute force attack on a zip or rar file containing password hashes
#When using John the Ripper for a zip or rar file, we first have to get the hash from the file and store it in a txt file
zip2john passwds.zip > passwds.txt
#Now, the hash can be decrypted using following command
john --format=zip passwds.txt
#The same functionality can be extended for other kinds of algorithms being used for creating a hash.
#For instance, if a password is hashed using SHA-256, it can also be brute forced using John the Ripper.
john --incremental --format=raw-sha256 passwds.txt
#The incremental mode uses all possible combinations and is thus time consuming and should be used when no other choice is available
#Alternatively, a wordlist can also be used for the same by using option --wordlist=<nameof_wordlist>.
