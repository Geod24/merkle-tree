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
        hashArr.append(hashlib.sha256())
        hashArr[-1].update(hashlib.sha256(arr[x].encode('utf-8')).digest())
        pprtArr.append(hashArr[-1].hexdigest().upper())

    # Balance tree by repeating the last element

    if arrlen < 2**lvl:
        for y in range(arrlen,2**lvl):
            hashArr.append(hashArr[arrlen-1])
            pprtArr.append(hashArr[arrlen-1].hexdigest().upper())

    finArr.append(hashArr) # First array in array contains the original hashes

    # The arrays below are clones and for printing only

    mprtArr = []
    prtArr = []
    prtArr.append(pprtArr)

    # Add to final array

    i = 0
    for z in range(len(lvlArr)):
        while i < len(hashArr)-1:
            firstHash = hashlib.sha256()
            firstHash.update(hashArr[i].digest())
            firstHash.update(hashArr[i+1].digest())
            midArr.append(hashlib.sha256(firstHash.digest()))
            mprtArr.append(midArr[-1].hexdigest().upper())
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
