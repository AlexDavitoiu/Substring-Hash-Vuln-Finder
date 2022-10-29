import hashlib
import random
import string
import time



def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for i in range(length))

def md5_hash(password):
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def check_if_hash_is_valid(hash,password):
    hash_len = len(hash)
    
    new_string = hash[hash_len-7:hash_len]
    
    if new_string == "0000000":
        print(password + ":" + hash + " is valid")
        exit()
    else:
        #print(password + ":" + hash + " is not valid")
        pass

def main():
    while True:
        random_string = generate_random_string(20)
        hash = md5_hash(random_string)
        check_if_hash_is_valid(hash,random_string)

main()    