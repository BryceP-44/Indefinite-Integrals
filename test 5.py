from math import *
import parser
#import multiprocessing
global k
"""
x**6
2*cos(2*x)/sin(2*x)
exp(4*x)*4
2**(cos(x))
2*sin(2*x)
2*cos(2*x)
1/(cos(x)**2)
1/(sin(x)**2)
1/(cos(x))*tan(x)
idk but no work 2/sin(2*x)
3/(3*x*(9*x**2-16)**.5)
cos(x)/(9-((sin(x))**2))

#19 math domain error
"""

print("You must include the proper form of the integral with the u and du as it would appear in a table")

while True:
    ucount=0
    acount=0
    k=1
    ans="No Answer"
    #string="5*(5*x)**3"
    string=input("Integrate: ")
    print(" ")
    #print("Integrate : ",string)
    st1 = parser.expr(string)
    code1= st1.compile("file.py")
    #function is now in math form

    ulist=[] #u-sub list
    for i in range(11):
        ulist.append(str(i)+"*x")
    for i in range(11):
        if i!=0:
            ulist.append("(1*x)/("+str(i)+")")
    for i in range(11):
        if i!=0:
            ulist.append("1/("+str(i)+"*x)")
    for i in range(11):
        for j in range(6):
            ulist.append(str(i)+"*x**"+str(j))
    ulist.append(str("sin(x)"))
    ulist.append(str("cos(x)"))
    ulist.append(str("sin(2*x)"))
    ulist.append(str("cos(2*x)"))
    ulist.append(str("(sin(x))**2"))
    ulist.append(str("(cos(x))**2"))
            


    alist=[] #a constants list
    for i in range(51):
        alist.append(str(i))
    pil=str(pi/6)
    for i in range(10):
        alist.append(str(i)+str("*pi"))
    for i in range(24):
        alist.append(str(i)+str("*pi/6"))

    for i in range(-50,0):
        alist.append(str(i))
        
    alist.append(str(sqrt(3)/2))
    alist.append(str(sqrt(2)/2))
    alist.append(str(sqrt(3)))
    alist.append(str(sqrt(3)/3))
    
    #pi/6 1-12
    for i in range(101):
        alist.append(str(i/100))
    

    #print(alist)
    #print(ulist)
    #print(len(ulist))
    #print(len(alist))

        

    #put the math code into function form f(x)
    def f(k):
        x=k
        f = eval(code1)
        return(f)

    def Rie(start,end,divisions):
        x=start
        
        nInt=0
        delta=(end-start)/divisions
        for i in range(divisions+1):
            fi=f(x)
            nInt=nInt+(fi*delta)
            x=x+delta
        return nInt

    global r2
    global nInt
    r1=Rie(.69,.7,100000)# Rie at 1-2 with 100K
    r2=Rie(.42,.43,1000000)# rie at 100-101 with 1M
    r1str=str(r1)
    tr1=str("j" in r1str)
    if tr1=="True":
        r1=Rie(6.9,7,100000)
        r2=Rie(4.2,4.3,1000000)
        
    #print("level 1: ", r1)
    #print("level 2: ", r2) 

    def type1(ux,a):
        pans1="0"
        return 0

    def type2(ux,a):
        if a!=-1 and ux!=0:
            global pans2
            aans="(a+1)".format(a=alist[acount])
            aans = parser.expr(aans)
            code = aans.compile("file.py")
            aans=str(eval(code))
            uans=str(ulist[ucount])
            pans2="("+uans+"^"+aans+")/("+aans+")"
            return (1/(a+1))*ux**(a+1)
        else:
            return 0

    def type3(ux,a):
        if ux>0:
            global pans3
            uans=str(ulist[ucount])
            pans3="log|"+uans+"|"
            return log(abs(ux))
        else:
            return 0
        
    def type4(ux,a):
        global pans4
        uans=str(ulist[ucount])
        pans4="e^("+uans+")"
        return e**(ux)

    def type5(ux,a):
        if a>0 and a!=1:
            global pans5
            uans=str(ulist[ucount])
            aans=str(alist[acount])
            pans5="("+aans+"^("+uans+")"+")/(log("+aans+")))"
            if ux>110:
                return 0
            else:  
                return (1/(log(a)))*a**(ux)
        else:
            return 0
        
    def type6(ux,a):
        global pans6
        uans=str(ulist[ucount])
        pans6="-cos("+uans+")"
        return -cos(ux)
    
    def type7(ux,a):
        global pans7
        uans=str(ulist[ucount])
        pans7="sin("+uans+")"
        return sin(ux)

    def type8(ux,a):
        global pans8
        uans=str(ulist[ucount])
        pans8="tan("+uans+")"
        return tan(ux)
    
    def type9(ux,a):
        global pans9
        uans=str(ulist[ucount])
        pans9="-cot("+uans+")"
        if (ux%(2*pi)) !=0:     
            return (-1/(tan(ux)))
        else:
            return 0

    def type10(ux,a):
        global pans10
        uans=str(ulist[ucount])
        pans10="sec("+uans+")"
        if (ux%(pi/2)) !=0:
            return 1/(cos(ux))
        else:
            return 0

    def type11(ux,a):
        global pans11
        uans=str(ulist[ucount])
        pans11="-csc("+uans+")"
        if (ux%(pi)) !=0:
            return -1/(sin(ux))
        else:
            return 0
    
    def type12(ux,a):
        global pans12
        uans=str(ulist[ucount])
        pans12="log|sec("+uans+")|"
        if (ux%(pi/2)) !=0:
            return log(abs(1/(cos(ux))))
        else:
            return 0

    def type13(ux,a):
        global pans13
        uans=str(ulist[ucount])
        pans13="log|sin("+uans+")|"
        if (ux%(2*pi)) !=0:
            return log(abs(sin(ux)))
        else:
            return 0

    def type14(ux,a):
        global pans14
        uans=str(ulist[ucount])
        pans14="log|sec("+uans+")+tan("+uans+")|"
        if (ux%(pi)) !=0:
            return log(abs((1/(cos(ux)))+tan(ux)))
        else:
            return 0

    def type15(ux,a):
        global pans15
        uans=str(ulist[ucount])
        pans15="log|csc("+uans+")cot("+uans+")|"
        if (ux%(pi/2)) !=0 and (ux%(2*pi)) !=0:
            return log(abs((1/(cos(ux)))-(1/(tan(ux)))))
        else:
            return 0
        
    def type16(ux,a):
        global pans16
        uans=str(ulist[ucount])
        aans=str(alist[acount])
        pans16="arcsin(("+uans+")/("+aans+")"
        if a!=0 and ((ux)/(a))<=1 and (ux)/(a)>=-1:
            return asin((ux)/(a))
        else:
            return 0

    def type17(ux,a):
        global pans17
        uans=str(ulist[ucount])
        aans=str(alist[acount])
        pans17="1/("+aans+") * arctan("+uans+"/"+aans+")"
        if a!=0:
            return 1/a *atan(ux/a)
        else:
            return 0

    def type18(ux,a):
        global pans18
        uans=str(ulist[ucount])
        aans=str(alist[acount])
        pans18="1/("+aans+") * arcsec(("+uans+")/("+aans+")"
        if a!=0 and ux!=0 and ((a)/(ux))<1 and (a)/(ux)>=-1:
            return (1/a) * (acos(a/ux))
        else:
            return 0

    def type19(ux,a):
        global pans19
        uans=str(ulist[ucount])
        aans=alist[acount]
        aans="((a)*2)".format(a=alist[acount])
        aans = parser.expr(aans)
        code = aans.compile("file.py")
        aans=str(eval(code))
        pans19="1/("+aans+") * log|("+uans+"-"+aans+")/("+uans+"+"+aans+")|"
        if a!=0 and (ux-a)!=0 and (ux+a)!=0:
            return log(abs((ux+a)/(ux-a)))/(2*a)
        else:
            return 0
    
    def ux1(ucount): #at 1
        global ux
        repu1="(.69)"
        if k==18:
            repu1="(6.9)"
        ux=str(ulist[ucount])
        ux=ux.replace("x", repu1)
        st2 = parser.expr(ux)
        code2= st2.compile("file.py")
        ux=eval(code2)
        ux=str(ux)
        return ux

    def ux2(ucount): #must be in the bounds of all common functions so 0-1
        global ux
        repu2="(.7)"
        if k==18:
            repu2="(7)"
        ux=str(ulist[ucount])
        ux=ux.replace("x",repu2)
        st2 = parser.expr(ux)
        code2= st2.compile("file.py")
        ux=eval(code2)
        ux=str(ux)
        return ux

    def ux100(ucount): #at 100
        global ux
        repu3="(.42)"
        if k==18:
            repu3="(4.2)"
        ux=str(ulist[ucount])
        ux=ux.replace("x",repu3)
        st2 = parser.expr(ux)
        code2= st2.compile("file.py")
        ux=eval(code2)
        ux=str(ux)
        return ux

    def ux101(ucount): #at 100.1
        global ux
        repu4="(.43)"
        if k==18:
            repu4="(4.3)"
        ux=str(ulist[ucount])
        ux=ux.replace("x",repu4)
        st2 = parser.expr(ux)
        code2= st2.compile("file.py")
        ux=eval(code2)
        ux=str(ux)
        return ux

    def avals(acount):
        global a
        a=alist[acount]
        return a
    mycount=0
    
    
    
    def test(formvalue,r1,r2):
        if abs(((formvalue-r1)/(r1))/2)<.0001:
                #print("level 1 reached")
                st="type{k}({u},{a})-type{k}({j},{a})".format(k=k,u=ux101(ucount),a=avals(acount),j=ux100(ucount))
                #print(st)
                st2 = parser.expr(st)
                code2= st2.compile("file.py")
                level2=eval(code2) #this is the exact value of integral the rie should match
                #print(level2)
                #print(r2)
                #print(abs((level2-r2)/(r2))/1)
                if (abs((level2-r2)/(r2))/2)<.0001:
                    #print("level 2 reached")
                    global ans
                    ans="type{k}({u},{a})".format(k=k,u=ulist[ucount],a=alist[acount])
                    ans=str(ans)
                    global stop
                    stop="T"
                    #print(ans)
                    return ans

    stop="F"
    for i in range(len(alist)):#all values of a
        for i in range(len(ulist)): #all the values of ux
            jobs=[]
            for i in range(19): #all the types, should be 120 
                #typek(u,a)
                st="type{k}({u},{a})-type{k}({j},{a})".format(k=k,u=ux2(ucount),a=avals(acount),j=ux1(ucount))
                #st="type"+str(k)+"("+str(ux1(ucount))+","+str(a(acount))+")"
                #print(st)
                st2 = parser.expr(st)
                code2= st2.compile("file.py")
                formvalue=eval(code2)
                #print(formvalue)
                #p = multiprocessing.Process(target=test)
                #jobs.append(p)
                #p.start()
                ans=test(formvalue,r1,r2)
                if stop=="T":
                    break
                k=k+1
                mycount+=1
            if stop=="T":
                break
            k=1    
            ucount+=1
        if stop=="T":
            break
        ucount=0    
        acount=acount+1
        



    ans=str(ans)
    #print("Answer in Type form: ", ans)

    if ans=="None":
        print("No answer found.")

    ptype=ans.split("(")
    ptype=str(ptype[0])
    ptype=ptype.split("e")
    ptype=str(ptype[1])

    pst="print(pans{tnum})".format(tnum=ptype)
    pans = parser.expr(pst)
    code = pans.compile("file.py")
    pans=eval(code)

    print("\n",mycount,"Tries\n")

    """
    pux=ans.split("(")
    pux=str(pux[1])
    pux=pux.split(",")
    pux=str(pux[0])
    print(pux)
    """



























