
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9',' ']
morse_signs= ['•–' ,'-•••' ,'–•-•' ,'–••' ,'•' ,'••–•' ,'––•' ,'••••' ,'••' ,'•–––' ,'–•–' ,'•–••' ,'–-' ,'–•' ,'––-' ,
              '•-–•' ,'-–•-' ,'•-•' ,'•••' ,'–' ,'••–' ,'•••–' ,'•-–' ,'–••-' ,'–•––' ,'––••' ,'-----' ,'•----' ,
              '••---' ,'•••--' ,'••••-' ,'•••••' ,'–••••' ,'––•••' ,'–––••' ,'––––•','']

texto = input("Input the phrase that you want to convert to Morse code: ")
a_descifrar=list(texto)
codigo = []

for letter in a_descifrar:
    for item in letters:
        if item == letter.upper():
            position = letters.index(item)
            codigo.append(morse_signs[position]+'/')

morse = "".join(str(x) for x in codigo)

print(f"You wrote: {texto}, which translated to Morse code is: {morse}")


