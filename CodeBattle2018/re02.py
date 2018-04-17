import hashlib
import string
listHash=["98BDE47147A051BFDEC5D5755104B9ECEA2C08F8","BF858113165236AD76C3976B4C6E622B4B29D94F","DA0EE0BA67381E16B539FCE3E86D496FB1710FA4","4D33CC5D794C06B18B71282FF14160914EBBCC26"]
def sha1Hash(toHash):
        try:
            messageDigest = hashlib.sha1()
            stringM = str(toHash)
            byteM = bytes(stringM)
            messageDigest.update(byteM)
            return messageDigest.hexdigest()
        except TypeError:
            raise "String to hash was not compatible"
#print sha1Hash("aaaa").upper()
for a in string.printable:
	for b in string.printable:
		for c in string.printable:
			for d in string.printable:
				text=str(a)+str(b)+str(c)+str(d)
				#print t
				if sha1Hash(text).upper() in listHash:
					print text

#c4n_n01_R3ver53!
