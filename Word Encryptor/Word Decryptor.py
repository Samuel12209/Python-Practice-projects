with open('Word Encryptor/message.txt') as f: # Varies where the location of message.txt is
    code = f.read()

Sentence = code.split(' ')

encryption_codes = {
    'bgpsyfclbrckxfbdibzwvmytjoujglhddkxtjuybopfluwgasb': 'a',
    'kgbivexlfgtxalkacbadcdienuqpocpthetavobkobakyndelt': 'b',
    'tuotwjnilojgjdlhzhqlpcjofazhudeeedcvsawkzwhpwcqmmd': 'c',
    'sgjyfwdtusxdceuwybdnpzfmhwhsmfeapbiaahchrvwhbxrnoa': 'd',
    'kkvfdhvemaktquhncpknzbgvfgzrwhuznjjnikfshcwhrgjcla': 'e',
    'copysjqpomxqdczqpojmnmamldxtzbenscuqfcdcmmrchdrpug': 'f',
    'dpjiwmpqghkajachssrdvawdodddajtuxpuetyaswtmtfynstw': 'g',
    'attpktpdeefthgpeytshpzwusgtotgcpqjwwwofkjkaxnorqdq': 'h',
    'zdpffyplvnnojldixvigmqkdizwmtkfwmqbkgqxvkzblrlhsud': 'i',
    'tsowhnmytuitjcabugkcsllvcmudpypkwjkgnqukjdbbxqxqee': 'j',
    'cejnownhksivdblownbbzdswhexbobmvujhlxbgayqtrvcpsor': 'k',
    'jjncsrpfthdmqcsfaftskspjpqqxwsnxfvryvxeitkygybypsg': 'l',
    'iasxixofvquvyudwxhssfuuzjzxmijsbjarrownugagihqxxem': 'm',
    'drazrqtulqjmdmhmiwdejeivcefzkwudejjsmpyqphnhkoiuzz': 'n',
    'uchmlovupzzedcyizvhgjrvbkbyiatjxgkqcuzsnjzfgbtwrun': 'o',
    'dthmdwpzvcpmblhgsaxaajqrdulozgkixrvcvjjvzjhzvdkinl': 'p',
    'qafiebasmbfatssvqjtmbimprhkkphrqpmbpkvdraqztluozwz': 'q',
    'lkzlnyxhrcfiougpsxqeuvsygidvzgqjmvtsggxhgkpfuzyrsr': 'r',
    'noknmxfalxfuypmlfckzuxumricofwzxlhbkdbeqfnmlfdygkr': 's',
    'csfopxociqwyhzhyjnexozdooocistqjkpgbdgewgxkjhvyyho': 't',
    'ucfptprdhauuuxbzvzkgpseqmdeyirihofklbhwvizctqjsgyc': 'u',
    'mrtnqhqxloekufondgeojsgxeqcxookxyhxdotcjbjuwwmbyai': 'v',
    'utoxexceqlrxzzboraxepmycmxwkrjthvbwjxijfmtcyrtsoml': 'w',
    'fmhystvwavmeixqtawepsdmwcycllwwoztseqdnobludzfyevf': 'x',
    'cpuxsfkklusxuoxwkzlaxoktkorjpmmvflridpxbmpcxuefnqq': 'y',
    'llzjuiwpkmdoedddimksvcyotvvhusldceeqxmuyzjmmzveecv': 'z',
    'lgynwsipbyztwigqhbtkxqeklrifycwlbneenktuflqeeihcgs': ' ' # THIS IS A SPACE
}

Encrypted = []

Sentence = list(Sentence)

for char in Sentence:
    if char in encryption_codes:
        Encrypted.append(encryption_codes[char])
    else:
        Encrypted.append(char)

Encrypted = "".join(Encrypted)
print(Encrypted)
