import huffmanCoding

def huffmanDecode(encodedText, huffmanCodes):
    reverseCodes = {code: char for char, code in huffmanCodes.items()}
    
    decodedText = ''
    tempCode = ''
    
    for bit in encodedText:
        tempCode += bit
        
        if tempCode in reverseCodes:
            decodedText += reverseCodes[tempCode]
            tempCode = ''
            
    return decodedText
    
