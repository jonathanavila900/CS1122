
# Operation code to mnemonic dictionary
# You can use this to lookup the machine code
# and translate it to the mnemonic instruction
INS_REF = {
    0: "HLT",
    1: "ADD",
    2: "SUB",
    3: "STA",
    5: "LDA",
    6: "BRA",
    7: "BRZ",
    8: "BRP",
    9: "INP",
    10: "OUT"
}

def disassemble(num):
    # this function should take in an integer operation code
    # and convert it to a LMC mnemonic instruction and return
    # it as a string
    lstOfOps = [000,100,200,300,500,600,700,800]
    
    for i in (INS_REF):
        #opType = (num[1:])
        firstVal = num -(num % 100)
        if firstVal == lstOfOps[i]:
            strVal =str(num)
            print (INS_REF[i], )
            print(strVal[1:],' ')
            print(strVal[2])
            
                
    if firstVal == 900:
        if num[2] == 1:
            print ("INP")
        else:
            print("OUT")
    

def main():
    # The main function should read all operation codes from the
    # user until the HLT instruction is read. Once it is read,
    # all operation codes should be disassembled using "disasassembled"
    # and then printed out to the user
 #   pass
     num = int(input("Enter a numeric value: "))        
     while num != 000:
         disassemble(num)

main()

#if __name__ == "__main__":
  #  main()
