import sys
import hashlib

# INCOMPLETE verify function

def verify():
    merkleRoot1 = sys.argv[2] # [2] : str -> hash
    nVals = sys.argv[3]
    iVal = sys.argv[4]
    valHash1 = sys.argv[5] # [5] : str -> hash

    # error cases
    
    if nVals.isnumeric() == False:
        sys.exit("EXIT_WRONG_DATATYPE")
    elif iVal.isnumeric() == False:
        sys.exit("EXIT_WRONG_DATATYPE")
    
    numVals = int(nVals) # [3] : int
    idxVal = int(iVal) # [4] : int

    if idxVal > numVals - 1:
        sys.exit("EXIT_WRONG_INDEX")

    # make test hashes
    
    merkleRoot = hashlib.sha256(merkleRoot1.encode('utf-8'))
    rootHex = merkleRoot.hexdigest()
    valHash = hashlib.sha256(valHash1.encode('utf-8'))
    
    pathArr = [] # [6+] : str -> hash

    ### Path array means that 
    
    testPrint = [] # dummy array for testing the function

    for p in range(6,len(sys.argv)):
        pathArr.append(hashlib.sha256(sys.argv[p].encode('utf-8'))) # Make array of Merkle path
        testPrint.append((hashlib.sha256(sys.argv[p].encode('utf-8'))).hexdigest()) #for printing

    # set level
    
    vLvl = 0
    while numVals > 2**vLvl:
        vLvl += 1
        if numVals <= 2**vLvl:
            break

    #level array
    
    vLvlArr = [0]
    vLvlCount = 1
    while vLvlCount <= vLvl:
        vLvlArr.append(vLvlCount)
        vLvlCount += 1
        if vLvlCount > vLvl:
            break

    print(testPrint)

    # combine target hash and hash from path
    
    nHash = hashlib.sha256()
    nHash.update(valHash.digest())
    nHash.update(pathArr[0].digest())
    del pathArr[0]
    del testPrint[0]
    pathArr.insert(0,nHash) #replace path hash with combined hash
    testPrint.insert(0,nHash.hexdigest())

    print(testPrint)

    j = 0
    while len(pathArr) > 1: # apply hash function until root is found
        tmp3 = pathArr[j]
        tmp4 = pathArr[j+1]
        nnHash = hashlib.sha256()
        nnHash.update(tmp3.digest())
        nnHash.update(tmp4.digest())
        pathArr.insert(0,nnHash) # insert into index 0
        testPrint.insert(0,nnHash.hexdigest())
        del pathArr[1] # delete index 1 and 2
        del testPrint[1]
        del pathArr[1] # index 2 from above is index 1 now
        del testPrint[1]

        # the array has one less element now
        
        if len(pathArr) <= 1:
            break

    # test print
    
    print(testPrint)
    print('-' * 50)
    print(rootHex)
    print(testPrint[0])
    
    #if merkleRoot1 == pathArr[0]:
        #print("Valid Merkle path")
        #sys.exit("EXIT_SUCCESS")
    
    #else:
        #print("Invalid Merkle path")
        #sys.exit("EXIT_FAILURE")

if len(sys.argv) < 7:
    print(len(sys.argv))
    sys.exit("EXIT_NO_ARGUMENTS")

elif sys.argv[1] == "verify":
    verify()

else:
    sys.exit("EXIT_SYS_FAILURE")
