import sys
import hashlib

# Create initial array of arguments

arr = [arr for arr in sys.argv[2:]]
arrlen = len(arr)

def produce():

# Array initialization
    
    lvlArr = [0] # Array of levels

    # The double SHA-256 hashed strings are stored into:
    
    hashArr = [] # Array of hash objects
    pprtArr = [] # Array of hashes converted to hex, for printing

    # Process of completing tree
    
    midArr = [] # temporary middle array for appending to final array
    finArr = [] # Final array
 

    # SET LEVEL
    # The array length is tested against progressive powers of 2
    # If array length is less than the next power, loop breaks and level is set

    lvl = 0
    while arrlen > 2**lvl:
        lvl += 1
        if arrlen <= 2**lvl:
            break

    # MAKE LEVEL ARRAY
    
    lvlCount = 1
    while lvlCount <= lvl:
        lvlArr.append(lvlCount)
        lvlCount += 1
        if lvlCount > lvl:
            break

    # ADD TO INITIAL LIST

    for x in range(arrlen):
        a = hashlib.sha256(arr[x].encode('utf-8'))
        a2 = hashlib.sha256()
        a2.update(a.digest())
        a3 = a2.hexdigest().upper()
        hashArr.append(a2)
        pprtArr.append(a3)

    # BALANCE TREE BY REPEATING LAST ELEMENT
    

    if arrlen < 2**lvl:
        for y in range(arrlen,2**lvl):
            b = hashlib.sha256(arr[arrlen-1].encode('utf-8'))
            b2 = hashlib.sha256()
            b2.update(b.digest())
            b3 = b2.hexdigest().upper()
            hashArr.append(b2)
            pprtArr.append(b3)
    
    finArr.append(hashArr) # contains the original nodes
    mprtArr = []
    prtArr = []
    prtArr.append(pprtArr)
    i = 0
    
    # ADD TO FINAL LIST
      
    for z in range(len(lvlArr)):
        while i < len(hashArr)-1:
            tmp1 = hashArr[i]
            tmp2 = hashArr[i+1]
            newHash = hashlib.sha256()
            newHash.update(tmp1.digest())
            newHash.update(tmp2.digest())
            midArr.append(newHash)
            mprtArr.append(newHash.hexdigest().upper())
            i += 2
            if i > (len(hashArr)-1):
                finArr.append(midArr)
                prtArr.append(mprtArr)
                hashArr = midArr
                midArr = []
                mprtArr = []
                i = 0
                break
    
    # PRINT

    ind = 1
    while (ind <= len(lvlArr)):
        print("Level " + str(lvlArr[ind-1]) + ":")
        
        for z in range(len(prtArr[-ind])):
            print(prtArr[-ind][z])
                
        ind += 1

        if ind > len(lvlArr):
            break


if len(sys.argv) < 2:
    sys.exit("EXIT_NO_ARGUMENTS")

elif sys.argv[1] == "produce":
    produce()
    sys.exit()

else:
    sys.exit("EXIT_SYS_FAILURE")
