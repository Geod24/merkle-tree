import sys
import hashlib

def merkleProduce():
    # Initialize array of arguments
    
    arr = [arr for arr in sys.argv[2:]]
    arrlen = len(arr)

    lvlArr = [] # Array of levels

    # The double SHA-256 hashed strings will be stored into:
    
    hashArr = [] # Array of hash objects
    pprtArr = [] # Array of hashes converted to hex, for printing only

    # Process of completing tree
    
    midArr = [] # Temporary middle array for appending to final array
    finArr = [] # Final array : array of arrays
 
    # Set tree level

    lvl = 0
    while arrlen > 2**lvl:
        lvl += 1
        if arrlen <= 2**lvl:
            break

    # Make level array
    
    lvlCount = 0
    while lvlCount <= lvl:
        lvlArr.append(lvlCount)
        lvlCount += 1
        if lvlCount > lvl:
            break

    # Add elements to the hash array

    for x in range(arrlen):
        a = hashlib.sha256(arr[x].encode('utf-8'))
        a2 = hashlib.sha256()
        a2.update(a.digest())
        a3 = a2.hexdigest().upper()
        hashArr.append(a2)
        pprtArr.append(a3)

    # Balance tree by repeating the last element
    
    if arrlen < 2**lvl:
        for y in range(arrlen,2**lvl):
            b = hashlib.sha256(arr[arrlen-1].encode('utf-8'))
            b2 = hashlib.sha256()
            b2.update(b.digest())
            b3 = b2.hexdigest().upper()
            hashArr.append(b2)
            pprtArr.append(b3)
    
    finArr.append(hashArr) # First array in array contains the original hashes

    # The arrays below are clones and for printing only
        
    mprtArr = []
    prtArr = []
    prtArr.append(pprtArr)
    
    # Add to final array
    
    i = 0
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
                finArr.append(midArr) # Append array to final array
                prtArr.append(mprtArr)
                hashArr = midArr # Prepare for next level combination
                midArr = [] # Empty temporary array
                mprtArr = []
                i = 0
                break
    
    # Print by level

    ind = 1
    while (ind <= len(lvlArr)):
        print("Level " + str(lvlArr[ind-1]) + ":")
        
        for j in range(len(prtArr[-ind])):
            print(prtArr[-ind][j])
        ind += 1

        if ind > len(lvlArr):
            break

    sys.exit("EXIT_SUCCESS")
    
