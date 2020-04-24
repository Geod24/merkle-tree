import sys
import hashlib

# INCOMPLETE verify function
# Program runs, but only to demonstrate the mechanism
# NEED TO: convert string objects to hash
# NEED TO: find better library for hashing

def merkleVerify():
    merkleRoot1 = sys.argv[2] # [2] : str -> hash
    nVals = sys.argv[3]
    iVal = sys.argv[4]
    valHash1 = sys.argv[5] # [5] : str -> hash

    # Error cases
    
    if nVals.isnumeric() == False:
        sys.exit("EXIT_INVALID_DATATYPE")
    elif iVal.isnumeric() == False:
        sys.exit("EXIT_INVALID_DATATYPE") 
    
    numVals = int(nVals) # [3] : str -> int
    idxVal = int(iVal) # [4] : str -> int

    # Set tree level
    
    vLvl = 0
    while numVals > 2**vLvl:
        vLvl += 1
        if numVals <= 2**vLvl:
            break

    if numVals % (2**vLvl) != 0:
        sys.exit("EXIT_INCOMPLETE_TREE")
    elif idxVal > numVals - 1:
        sys.exit("EXIT_INVALID_INDEX")
    elif len(sys.argv[6:]) != vLvl:
        sys.exit("EXIT_INVALID_PATH")

    ### *TEST* Make sample hashes
    
    merkleRoot = hashlib.sha256(merkleRoot1.encode('utf-8'))
    rootHex = merkleRoot.hexdigest()
    valHash = hashlib.sha256(valHash1.encode('utf-8'))

    # Store path elements into array
    # One element for each level
    
    pathArr = [] # [6+] : str -> hash
    testPrint = [] # *TEST* Dummy array that stores hex values for printing

    ### *TEST* Make sample hashes and append to array
    
    for p in range(6,len(sys.argv)):
        pathArr.append(hashlib.sha256(sys.argv[p].encode('utf-8')))
        testPrint.append((hashlib.sha256(sys.argv[p].encode('utf-8'))).hexdigest())

    # Make level array
    
    vLvlArr = []
    vLvlCount = 0
    while vLvlCount <= vLvl:
        vLvlArr.append(vLvlCount)
        vLvlCount += 1
        if vLvlCount > vLvl:
            break

    print(testPrint) # *TEST* original path

    # Combine target hash and hash from path
    
    nHash = hashlib.sha256()
    nHash.update(valHash.digest())
    nHash.update(pathArr[0].digest())
    del pathArr[0]
    del testPrint[0]
    pathArr.insert(0,nHash) # replace
    testPrint.insert(0,nHash.hexdigest())

    print(testPrint)
    # *TEST* Hash at [0] now a comb. of target hash and first hash in path

    j = 0
    while len(pathArr) > 1: # Combine until root
        tmp3 = pathArr[j]
        tmp4 = pathArr[j+1]
        nnHash = hashlib.sha256()
        nnHash.update(tmp3.digest())
        nnHash.update(tmp4.digest())
        pathArr.insert(0,nnHash) # Insert into [0]
        testPrint.insert(0,nnHash.hexdigest())
        del pathArr[1] # Delete [1] and [2](next step)
        del testPrint[1]
        del pathArr[1] # [2] from above is [1] now
        del testPrint[1]
    
        print(testPrint) # *TEST* Observe the hashes merging

        # The array has one less element now
        
        if len(pathArr) <= 1:
            break
    
    #if merkleRoot1 == pathArr[0]:
    sys.exit("EXIT_SUCCESS")
    
    #else:
        #print("Invalid Merkle path")
        #sys.exit("EXIT_FAILURE")
