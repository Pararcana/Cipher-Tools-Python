from trigrams import trigrams
from itertools import permutations
ciphertext = "AIYNA GKRCT ELUOI SGAEE LLSON OKONS NAAOT OWDSM SEAAT OEPNC EDTLV UNTRL IDDTH HEPTE FAIAD GOSWR EMUIR EINMO USRSG SIEHN YARSR ESNOR ROEDR ELEON PESEE HUAEM AIOCR BRMEI ISFEL TNIRT EYLVA OTTTE SROTR NWAOI QIIKN EANTO AETNT TIEOE TNTFU NIDFE ETMSR TMHEO CDIEE AYECY FIOHE SAPEC NRLDW DNSII LNTGE IOAAD SEEBS EDOUA SLITR TESRO SOSTA LEEIA YAGLN YOESO EAROO AMEOS NISGA IAHAL NSTEC ITTEU CDRSI WLGMN ITEMP ENNED WVUFY LLSNV YRDEE ELTRT ALODP ISSDP RSNTY LASED EPTRP ODNCI CBNAR NAYHS POAAL VYLEO ARRDI LNSSY IIECO ADEUE ETEAP ADSAP BREPO LSTIF LECCI VERSA EDOOC WRSGO OEUEN NOCLQ EFEES NRRCA RDQOS AACRR PLNIE HSTEB EMTER SDNLY ATREO TNMER TNELN LAIUI TFEEN TGIFL ISWDE NCMSE".upper()

alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
keyLen = 7
ciphertext = [v for v in ciphertext if v in alpha]
block = len(ciphertext)//keyLen

def fitness(arr):
  total = 0
  for i in range(len(arr) - 2):
    total += trigrams["".join(arr[i: i + 3])]
  return total

def step(key, columns):
  plaintext = []
  for i in range(block):
    for j in key:
      plaintext.append(columns[j][i])
  return plaintext

def solve():
  columns = []
  solutions = [[], []]
  choices = [i for i in range(keyLen)]

  for i in range(keyLen):
    columns.append(ciphertext[block * i: block * (i + 1)])

  for key in permutations(choices, keyLen):
    plaintext = step(key, columns)
    solutions[0].append(plaintext)
    solutions[1].append(fitness(plaintext))

  return solutions[0][solutions[1].index(max(solutions[1]))]

print("".join(solve()))
#upload to git
