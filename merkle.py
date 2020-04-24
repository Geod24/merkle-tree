import sys
from produce import merkleProduce
from verify_incomplete import merkleVerify

if len(sys.argv) <= 2:
    sys.exit("EXIT_NO_ARGUMENTS")
    
elif sys.argv[1] == "produce":
    merkleProduce()
    
elif sys.argv[1] == "verify":
    merkleVerify()
    
else:
    sys.exit("EXIT_INVALID_MODE")
