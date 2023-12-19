from trigrams import trigrams
import random
ciphertext = "OFHVG PMRZR DLJEA BTRNE KGJYT LKUVO JJXNU OTWPR VAJIW JGKNJ GBXLW VHUGY JZRGJ LQZFE CYDRR QHVZE HGJLR VWFCN JSIYQ DNKAN UHMRR QYYNK XRPSJ KXRTM WFQZC PXZIG QATDL NTWJI HROHS UMAIA MRXUG JTEXV PBJJX UGPSM IFVPL RXVQU NEMGU OJGVB OPXVH GQZJE HUKTY YIGGE YFJNP LSTVL RAJUX RNLLI EZULS KJEQT YYIZC UTIXB VOJSS BMZJC PRTZN EEYTL XWSEF DNKLG JLMFT RVOFK LRYVZ CHOGH GCIGQ KJTMC JLWZX VHVZE HGJLY VPRIY FDMGU LQWMA VOJGS YKJJR VPJPA VWNPK NTEAU LJNLL OHNJM REVZC HAVIW VEXKA YYIUC ZYPXL RPSXE AFAMV EODYJ MMNVL IGLEC ZNEKZ CRJJM GJHWU XBTLF UEQFL IKSJJ PHYMG KZJEG EAWYV HHUPS XEGTH SJTBU PYZSA EPUYI ETLFU MAIVK WFLEV QLQAU PSJXR CKTWV BYZNK ANUVS CCJJL SZWCQ AYVHG JLURX GGYSK LNVPB FVXGK TLXJJ HYNEF IVNEK BPPPE SJAVZ NMYNI JRFYG ATSVR CRNKF HVPBF RQGYM FAGJL SVAEG JWLMG UDNCP TGATE EAADF PLRTL NJQNK ZNVWY GAYVV GQAMV GUKLK UINTL XKGUK LKYEE RLWZY AFLWJ XNPKY YEGVO JDIQK JFCIK CTNEI ECUIK LRCAY FVAGF LVRRT HQYEI GITKL NEJJG XRFFT LVEGJ TDQRP KFKMB PATII PQYIK LREHZ JIBHT WZWYG ZIVEG JHXDM FCKAV RGWYJ RRQVO FKCBW KTESG RSFEX BEVSU YPVHS PJHTA MVVVP CJJXV IHYZS AKUYF XUGJN IGHOZ YRRPG ZXLVE QBSUM AIAMV EPEPI VRGCZ MVEQQ MYYIY KIWRV LCAYY IZCUT IMBDQ JTXZQ ZYJXE QULCC GQAMZ WQGJN JMBPD MZPRY LHRRA QAPES JHVWT IEVHN ELBYA MVYAH VWKYA CAJPS HPNRR RPCTJ KSOGS DZRTC AYYIS QVYFJ GJLQR HQGYY YIOQV PYIUC KYROR PMWFQ GJLXY IYXLX NEFLB XKSAG VKKLR XLWPZ NNBFS PRKAJ DWVPV ZIGBN SJTXV QUFEH GJLNE ZRUAN XEGKV SJFLR PSBIE VVSJI FVHGC MFJLI KLNVP YNEFG EYIIZ GSDCM XGSDK LNVOJ NEFGU LRKRF PSKLR HAFKX UGAND IBHON JJNNS LZZRP AMRXU GZJVQ FVVMR ZRDLJ EIAIH LVHOA HSVWG CIQZW UGKLR RTQMG FSXVO NVZRU ATMMF KAZJX UGYJD YFVZZ IIYAI JRVVU RYYEG VOJPA VNSXV RQCUT KLRTP SYMFR SFTIG QKTKL RKYGZ HQKUL ZJGJH YNIEG UTKIA QBLYX UGUHF RFKKJ IXUGT TJXEG JJEXQ KZHFZ RTFGP TVPRJ IXBPZ YYEGU VRVSS VOJKI YGNWR QFTLH VMIGK GPXUG HQIIF HVWUH RCSJI WJGYJ JIAVM WFQGJ LRRRB TPYJI YHMZI XUGYR FVRVO JPGBP KZTXR FAMVM EQDSK IFVZF EHRUA FSPVU OJUXU CAYYI AQAJW SHPKN EXUGZ UZRRQ MYYIO QVPNE FVFUV HBPVZ IZRTF TNRFJ VQVWN PKLZH QGUYP TRYYN KIEKA NJGYG HWKLN VZTDI GJPSX MFXLW PAEQU LZRBW YMFYF GOTCH NPKSF TBNPH VQNPD TIXUJ PXFJS KJJNS HNKTM IENVT BXUGJ NIGHO ZYRRP GZMFA RXLWT PBULM VQNAI JKSGJ LNEZR UANXE GKVSZ AVNSK FVJCY IKLRV LCKSS VOJDI FUHLV WRPAY FIAIS FEHSQ YDFYE QDSGI EWZFC MGFLK VEGGK RPSJP HYKIZ RAYFH REYDG XVVIZ KMSAV ZRVRR YJGEE GKYFA BTRBZ XUVOJ GMAML WKSAU HLVRG UAMVR VCTXL VRAVZ NMYNI JRFYG ATSVR CRYYI PKWMV VNPKX YIQUV RVPVI OYFRG JPXRA SWSFW JNKYD FYEUZ NEGRT LQPQV UZRRM FKLXK CYGZ".upper()
alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
cipherFilter = [v for v in ciphertext if v in alpha]

key = random.choices(alpha, k=6)

def fitness(arr):
  total = 0
  for i in range(len(arr) - 2):
    total += trigrams["".join(arr[i: i + 3])]
  return total

def vigenere(key, ciphertext):
  plaintext = []
  for i, v in enumerate(ciphertext):
    newChar = ord(v) - ord(key[i % len(key)])
    newChar %= 26
    plaintext.append(alpha[newChar])
  return plaintext

stability = 0
while stability != 10:
  testKey = key.copy()
  fitnessArr = [[], [], []]
  randChar = random.randint(0, len(key) - 1)

  for char in alpha:
    testKey[randChar] = char
    buffer = vigenere(testKey, cipherFilter)

    fitnessArr[0].append(buffer)
    fitnessArr[1].append(fitness(buffer))
    fitnessArr[2].append(testKey.copy())

  best = fitnessArr[1].index(max(fitnessArr[1]))
  stability = (fitnessArr[2][best] == key and stability + 1 or 0)
  key = fitnessArr[2][best]

  print("".join(fitnessArr[0][best]), fitnessArr[1][best])
  print(stability, key)
