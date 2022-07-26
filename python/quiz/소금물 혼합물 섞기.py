n=1
slst,swlst=[],[]  #소금의 양과 소금물의 양을 받기 위한 리스트
while n<=5:
    inp=input("소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ")#ng n%
    if inp=='Done':
        break
    else:
        s,sw=inp[:inp.find("%")],inp[inp.find(" ")+1:inp.find("g")]  #s=%앞의 숫자(소금의 농도), sw=g앞의 숫자(소금물의 양)
        slst.append(float(s)/100*float(sw))  #소금의 양(s/100에 sw를 곱한 것)을 slst에 추가.
        swlst.append(float(sw))
    n+=1
print(str(round(sum(slst)*100/sum(swlst),2))+"%",str(round(sum(swlst),2))+"g")