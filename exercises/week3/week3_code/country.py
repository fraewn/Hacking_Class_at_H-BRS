from Crypto.Cipher import AES
from Crypto.Util import Padding
from multiprocessing import Process, Queue

steps = 16777216 #FFFFFF

def setCoreSteps(numCores):
    coreSteps = 0
    coreSteps = int(steps/numCores/2)
    return coreSteps


def stage1(coreID, coreSteps,key2,pngheader,iv, q):
    candHinrunde = {}

    start = coreID * coreSteps
    end = start+(coreSteps-1)
    bruteKey = hex(start)[2:]
   
    while len(bruteKey) < 6:
        bruteKey= "0" + bruteKey

    for i in range(start, end):
        keyTemp = key2 + bruteKey

        keyBytes = bytes.fromhex(keyTemp)
        pre = AES.new(keyBytes, AES.MODE_CBC, iv)

        cipher = pre.encrypt(pngheader)
        candHinrunde[cipher] = keyBytes

        bruteKey = int(bruteKey, 16)
        bruteKey = bruteKey + 1
        bruteKey = hex(bruteKey)[2:]
        while len(bruteKey) < 6:
            bruteKey= "0" + bruteKey

    print("try to write into queue")
    q.put(candHinrunde)
    print("wrote into queue")
    return

def stage2(coreID, coreSteps,key2,cipher,iv, pl_list, cipherALL):

    start = coreID * coreSteps
    end = start+(coreSteps-1)
    bruteKey = hex(start)[2:]

    while len(bruteKey) < 6:
        bruteKey= "0" + bruteKey

    for i in range(start, end):
        keyTemp = key2 + bruteKey

        keyBytes = bytes.fromhex(keyTemp)
        pre = AES.new(keyBytes, AES.MODE_CBC, iv)

        text = pre.decrypt(cipher)
       
        if text in pl_list:
            keyOne = keyBytes
            keyTwo = pl_list[text]
            print("k1 :" + keyOne.hex() + "\nk2: " + keyTwo.hex())
            decrypt(cipherALL, keyOne, keyTwo, iv)
             
        bruteKey = int(bruteKey, 16)
        bruteKey = bruteKey + 1
        bruteKey = hex(bruteKey)[2:]
        while len(bruteKey) < 6:
            bruteKey= "0" + bruteKey

def decrypt(cipher, k1,k2, iv):
    aes1 = AES.new(k1, AES.MODE_CBC, iv)
    aes2 = AES.new(k2, AES.MODE_CBC, iv)

    plain = aes2.decrypt(aes1.decrypt(cipher))

    file = open("test.png", "wb")
    file.write(plain)
    file.close

def main():

    cipher = open("output.txt", "r").read()
    pngheader = '89504e470d0a1a0a' + '0000000d' + '49484452'
    pngheader = bytes.fromhex(pngheader)

    key1 = cipher[len(cipher)-54:len(cipher)-28]
    key2 = cipher[len(cipher)-27:len(cipher)-1]
    iv = cipher[0:32]
    iv = bytes.fromhex(iv)

    cipher = cipher[:len(cipher)-55]
    cipherALL = cipher[32:]
    cipherALL = bytes.fromhex(cipherALL)
    cipher = cipher[32:64]
    cipher = bytes.fromhex(cipher)

    cores = 8
    coreSteps = setCoreSteps(cores)


    ps = []
    q = Queue()
    setCoreSteps(cores)
   
    print("Hinrunde")
    for i in range(cores):
        ps.append(Process(target=stage1, args=(i, coreSteps, key2,pngheader, iv, q)))

    for p in ps:
        p.start()

    pl = {}
   
    for p in ps:
       pl.update(q.get())
   
    for p in ps:
        p.join()

    ps = []

    print("Rückrunde")

    for i in range(cores):
        ps.append(Process(target=stage2, args=(i, coreSteps, key1 ,cipher, iv, pl, cipherALL)))

    for p in ps:
        p.start()
   
    for p in ps:
        p.join()
        
        
if __name__ == "__main__":
    main()
