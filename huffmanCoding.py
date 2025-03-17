import heapq #for priority queue

#step 1 define huffman node
class huffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        
    def __lt__(self, other):
        return self.freq < other.freq
    
#step 2 build main tree
def buildHuffmanTree(freqmap):
    heap = [huffmanNode(char, freq) for char, freq in freqmap.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        newNode = huffmanNode(None, left.freq + right.freq)
        newNode.left = left
        newNode.right = right
        heapq.heappush(heap, newNode)
        
    return heap[0]

#step 3 generate/assign huffman codes
def buildCodes(node, prefix="", codeMap={}):
    if node is None:
        return
    
    if node.char is not None:
        codeMap[node.char] = prefix
        
    buildCodes(node.left, prefix + '0', codeMap) #left (0)
    buildCodes(node.right, prefix + '1', codeMap) #right (1)
    
    return codeMap

def huffmanCoding(string):
    freqmap = {char: string.count(char) for char in set(string)}
    root = buildHuffmanTree(freqmap)
    codes = buildCodes(root)
    encodedString = ''.join([codes[char] for char in string])
    
    return codes, encodedString