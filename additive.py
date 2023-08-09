lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def keyValidationAndRetrival(key):
    if key.isnumeric():
        key=int(key)
        return key
    else:
        if len(key)==1:
            if key.islower():
                key=lst.index(key)
                return key
            else:
                key=lst.index(key.lower())
                return key
        else: return False
def logic(data,type,key):
    result=""
    for alphabet in data:
        if alphabet==" ": pass
        elif alphabet.islower():
            if type=="encryption": result=result+lst[(lst.index(alphabet)+key)%26]
            else: result=result+lst[(lst.index(alphabet)-key)%26]
        else:
            if type=="encryption": result=result+lst[(lst.index(alphabet.lower())+key)%26]
    return result
print("-----ENCRYPTION-----")
plaintxt,keye,restrictedArea=input("Enter plain text:"),input("Enter key:"),0
if keyValidationAndRetrival(keye)==False:
    restrictedArea=1
    print("Invalid key....can't be encrypted")
else:
    cte=logic(plaintxt,"encryption",keyValidationAndRetrival(keye))
    print("Cipher text is "+cte+"\n-----ENCRYPTION DONE-----")
if restrictedArea==1: print("Decryption not possible")
else:
    print("-----DECRYPTION-----")
    while True:
        ch=int(input("Do you want to decrypt it....press 1 for it otherwise 0:"))
        if ch==1:
            keyd=input("Enter key:")
            if keyValidationAndRetrival(keyd)==False:
                print("Can't be decrypted")
                break
            else:
                ptd=logic(cte,"decryption",keyValidationAndRetrival(keyd))
                print("Plain text is "+ptd)
                print("-----DECRYPTION DONE-----")
                break
        elif ch==0: break
        else: print("Invalid input")
