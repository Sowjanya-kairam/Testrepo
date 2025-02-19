text = "X-DSPAM-Confidence:    0.8475"
st = text.find(':')
l = len(text)
rt = text[st+1:l]
#print(rt)
#rt = rt.lstrip()
#print (rt)
flt = float(rt.lstrip())
print(flt)