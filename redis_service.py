import hashlib
import shortuuid
from redis import Redis

from config import Config

redisClients = [
    Redis(host=Config.rhost1,port=Config.rport1,db=0),
    Redis(host=Config.rhost2,port=Config.rport2,db=0),
    Redis(host=Config.rhost3,port=Config.rport3,db=0),
]

def getRedisClient(key:str):
    
    hash_hex = hashlib.md5(key.encode('utf-8')).hexdigest()
    hash_int = int(hash_hex[:8], 16)
    client_index = hash_int % len(redisClients)
    
    return redisClients[client_index]

def getValue(key:str):

    RC = getRedisClient(key)
    url = RC.get(key)
    original_url = url.decode('utf-8')
    return original_url
    


def setValue(url:str):

    random_key = shortuuid.uuid()
    RC = getRedisClient(random_key)
    RC.set(random_key,url)    
    return random_key



# print(getValue("UGzgKkSQTsfFbFgK5pXaYA"))