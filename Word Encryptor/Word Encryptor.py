Sentence = input("Write Your sentence: ").lower()

encryption_codes = {
    'a': ' bgpsyfclbrckxfbdibzwvmytjoujglhddkxtjuybopfluwgasb',
    'b': ' kgbivexlfgtxalkacbadcdienuqpocpthetavobkobakyndelt',
    'c': ' tuotwjnilojgjdlhzhqlpcjofazhudeeedcvsawkzwhpwcqmmd',
    'd': ' sgjyfwdtusxdceuwybdnpzfmhwhsmfeapbiaahchrvwhbxrnoa',
    'e': ' kkvfdhvemaktquhncpknzbgvfgzrwhuznjjnikfshcwhrgjcla',
    'f': ' copysjqpomxqdczqpojmnmamldxtzbenscuqfcdcmmrchdrpug',
    'g': ' dpjiwmpqghkajachssrdvawdodddajtuxpuetyaswtmtfynstw',
    'h': ' attpktpdeefthgpeytshpzwusgtotgcpqjwwwofkjkaxnorqdq',
    'i': ' zdpffyplvnnojldixvigmqkdizwmtkfwmqbkgqxvkzblrlhsud',
    'j': ' tsowhnmytuitjcabugkcsllvcmudpypkwjkgnqukjdbbxqxqee',
    'k': ' cejnownhksivdblownbbzdswhexbobmvujhlxbgayqtrvcpsor',
    'l': ' jjncsrpfthdmqcsfaftskspjpqqxwsnxfvryvxeitkygybypsg',
    'm': ' iasxixofvquvyudwxhssfuuzjzxmijsbjarrownugagihqxxem',
    'n': ' drazrqtulqjmdmhmiwdejeivcefzkwudejjsmpyqphnhkoiuzz',
    'o': ' uchmlovupzzedcyizvhgjrvbkbyiatjxgkqcuzsnjzfgbtwrun',
    'p': ' dthmdwpzvcpmblhgsaxaajqrdulozgkixrvcvjjvzjhzvdkinl',
    'q': ' qafiebasmbfatssvqjtmbimprhkkphrqpmbpkvdraqztluozwz',
    'r': ' lkzlnyxhrcfiougpsxqeuvsygidvzgqjmvtsggxhgkpfuzyrsr',
    's': ' noknmxfalxfuypmlfckzuxumricofwzxlhbkdbeqfnmlfdygkr',
    't': ' csfopxociqwyhzhyjnexozdooocistqjkpgbdgewgxkjhvyyho',
    'u': ' ucfptprdhauuuxbzvzkgpseqmdeyirihofklbhwvizctqjsgyc',
    'v': ' mrtnqhqxloekufondgeojsgxeqcxookxyhxdotcjbjuwwmbyai',
    'w': ' utoxexceqlrxzzboraxepmycmxwkrjthvbwjxijfmtcyrtsoml',
    'x': ' fmhystvwavmeixqtawepsdmwcycllwwoztseqdnobludzfyevf',
    'y': ' cpuxsfkklusxuoxwkzlaxoktkorjpmmvflridpxbmpcxuefnqq',
    'z': ' llzjuiwpkmdoedddimksvcyotvvhusldceeqxmuyzjmmzveecv',
    ' ': ' lgynwsipbyztwigqhbtkxqeklrifycwlbneenktuflqeeihcgs'
}

Encrypted = []

Sentence = list(Sentence)

for char in Sentence:
    if char in encryption_codes:
        Encrypted.append(encryption_codes[char])
    else:
        Encrypted.append(char)

Encrypted = "".join(Encrypted)
f = open('Word Encryptor/message.txt','w')
f.write(Encrypted)
