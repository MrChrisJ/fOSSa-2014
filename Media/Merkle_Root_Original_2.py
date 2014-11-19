# This is the code used in the WBN video - Merkle Roots and Merkle Trees

import hashlib

Round = 0

print
print
print
# Hash pairs of items recursively until a single value is obtained
def merkle(hashList, ):
    global Round
    Round = Round + 1
    if len(hashList) == 1:
        # I had a brain fart when I mentioned this in the video. This returns the root
        # because now there is only one item - hashList [0]. Wish I could change
        # a youtube video but you cant.
        print "AND OUR MERKLE ROOT IS"
        return hashList[0]
    newHashList = []
    print
    print "Number of Branches in Round", Round, "is", len(hashList)
    print
    print
    
    # Process pairs. For odd length, last item is hashed with itself
    for i in range(0, len(hashList)-1, 2):
        print "Branch",i+1, "is", hashList[i]
        print "Branch",i+2, "is", hashList[i+1]
        print "their hash is", hash2(hashList[i], hashList[i+1])
        print
        newHashList.append(hash2(hashList[i], hashList[i+1]))
    if len(hashList) % 2 == 1: # odd, hash last item twice
        print "Branch", len(hashList), "is", hashList[len(hashList)-1]
        print "And Branch",len(hashList),"is hashed with itself to get", hash2(hashList[-1], hashList[-1])
        newHashList.append(hash2(hashList[-1], hashList[-1]))
    print "DONE with Round", Round
    print "<========================================================>"
    print
    print
    return merkle(newHashList)

def hash2(first, second):
    # Reverse inputs before and after hashing due to big-endian / little-endian nonsense
    firstreverse = first.decode('hex')[::-1]
    secondreverse = second.decode('hex')[::-1]
    h = hashlib.sha1(hashlib.sha256(firstreverse+secondreverse).digest()).digest()
    return h[::-1].encode('hex')

txHashes2 = [
  "b5c02acc0425cb11ba0224360d452eae5bb94315",
  "8c8846af260f4efb823c820fb6cbe313e7cb9a44",
  "77b3ab658c3e7b567a644b3426bdc48922d415c1",
  "8da58daee5720958a5ed21a46fe5fa76a9cf57dd",
  "6eb8ab3e06cb4d9d234a82f0a8ef046b9d4cbaf4",
  "19d4cb90fdf006acfd703d9afbf844052a569ed6",

]

print merkle(txHashes2)
