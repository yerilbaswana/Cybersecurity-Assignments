#Task - Encrypt a JSON file containing passwords for a password manager application.
#For the purpose of encrypting a JSON file containing passwords, we use Fernet from cryptography library.
#The cryptography library is being used to simply the details of the encryption procedure.
#For the purpose of encryption we use Advanced Encryption Standard(AES)-128 bit.
#import json to handle json file
import json
from cryptography.fernet import fernet

#Function to encrypt json file
def encrypt_josn(json_file, key):
  #To generate a fernet cipher object along with the input key which is generated using fernet. This key will be used in both 
  #encryption and decryption.
  fernet = Fernet(key)
  #To read the json file to convert it into a string and then to byte for it to be encrypted.
  with open(json_file, 'r') as file:
        json_data = json.load(file)
  json_data_bytes = json.dumps(json_data).encode('utf-8')
  #Encrypting the data
  json_encrypted_data = fernet.encrypt(data_bytes)
  #Saving the encrypted data to a file whose name will be encrypted_ + the name of the input json file.
    with open('encrypted_'+json_file, 'wb') as file:
        file.write(json_encrypted_data)

#To generate a key for encryption and later will also be used for decryption
key = Fernet.generate_key();
#This key has to be saved as it is necessary for the decryption process. It is saved to json_keys.key
with open('json_keys.key', 'wb') as json_key:
    json_key.write(key)
#To encrypt the json file with passwords.
encrypt_json('passwords.json', key)

#This way encryption is done.
#Now, decryption of the json file
def decrypt_json(encrypted_json_file, key):
  ##To generate a fernet cipher object along with the input key which is generated using fernet. This key will be used in both 
  #encryption and decryption.
  fernet = Fernet(key)
  #Reading the input file
  with open(encrypted_json_file, 'rb') as file:
        json_encrypted_data = file.read()
  #Decrypting the data and converting bytes to JSON
  json_decrypted_data = fernet.decrypt(json_encrypted_data)
  json_data = json.loads(json_decrypted_data.decode('utf-8'))
  return json_data

#Reading the key from the json_keys.key file
with open('json_keys.key', 'rb') as json_key:
    key = json_key.read()

#To print the decrypted json file.
json_decrypted_data = decrypt_json('encrypted_passwords.json', key) 
print(json_decrypted_data)
