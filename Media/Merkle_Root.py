# This is the code used in the WBN video - Merkle Roots and Merkle Trees

import hashlib

Round = 0

print()
print()
print()
# Hash pairs of items recursively until a single value is obtained
def merkle(hashList, ):
    global Round
    Round = Round + 1
    if len(hashList) == 1:
        # I had a brain fart when I mentioned this in the video. This returns the root
        # because now there is only one item - hashList [0]. Wish I could change
        # a youtube video but you cant.
        print("AND OUR MERKLE ROOT IS")
        return hashList[0]
    newHashList = []
    print()
    print("Number of Branches in Round", Round, "is", len(hashList))
    print()
    print()
    
    # Process pairs. For odd length, last item is hashed with itself
    for i in range(0, len(hashList)-1, 2):
        print("Branch",i+1, "is", hashList[i])
        print("Branch",i+2, "is", hashList[i+1])
        print("their hash is", hash2(hashList[i], hashList[i+1]))
        print()
        newHashList.append(hash2(hashList[i], hashList[i+1]))
    if len(hashList) % 2 == 1: # odd, hash last item twice
        print("Branch", len(hashList), "is", hashList[len(hashList)-1])
        print("And Branch",len(hashList),"is hashed with itself to get", hash2(hashList[-1], hashList[-1]))
        newHashList.append(hash2(hashList[-1], hashList[-1]))
    print("DONE with Round", Round)
    print("<========================================================>")
    print()
    print()
    return merkle(newHashList)

def hash2(first, second):
    # Reverse inputs before and after hashing due to big-endian / little-endian nonsense
    firstreverse = first.decode('hex')[::-1]
    secondreverse = second.decode('hex')[::-1]
    h = hashlib.sha256(hashlib.sha256(firstreverse+secondreverse).digest()).digest()
    return h[::-1].encode('hex')

txHashes2 = [
  "1e262cd7d110812f5726055a6e672b92cde43648b76adff51a12441fbdf7e667",
  "9ce61ca6806482e5dbe80c4d4416e37a4c33ab2e9359d66ff5c95fcc77bc35a5",
  "194b280915935d44270b5bd527a8add592ae9a1613a8f9ec40f1e31733cad9b9",
  "194b280915935d44270b5bd527a8add592ae9a1613a8f9ec40f1e31733cad9b9",
]
print(merkle(txHashes2))
