lst=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
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
plaintxt=input("Enter plain text:")
cte=logic(plaintxt,"encryption",3)
print("Cipher text is "+cte+"\n-----ENCRYPTION DONE-----")
print("-----DECRYPTION-----")
while True:
    ch=int(input("Do you want to decrypt it....press 1 for it otherwise 0:"))
    if ch==1:
        ptd=logic(cte,"decryption",3)
        print("Plain text is "+ptd)
        print("-----DECRYPTION DONE-----")
        break
    elif ch==0: break
    else: print("Invalid input")
