def usr_inp():
    flag = False

    while not flag:
        cc = input("Enter the 16 digits of the CC number")

        if len(str(cc)) == 16:
            flag = True
        else:
            print("Enter a valid size")

    return cc

def dump_cc1(cc):
    cc = cc
    m_cc = ""

    for i in range(0, 16, +2):
        m_cc = (m_cc) + (str(cc))[i]
    ##print(m_cc)

    return m_cc

def dump_cc2(cc):
    cc = cc
    m_cc = ""

    for i in range(1, 16, +2):
        m_cc = (m_cc) + (str(cc))[i]
    ##print(m_cc)

    return m_cc

def check_cc(m_cc):
    c=""
    m=1
    m_cc2=""
    for i in range(0,8,+1):
        c=str(m_cc)[i]
        m=int(c)*2
        if m != 0:
            m_cc2=m_cc2+str(m)
    ##print(m_cc2)

    m=0
    c=""
    for i in range(0,len(m_cc2)):
        c=m_cc2[i]
        m=m+int(c)
    ##print(m)

    return m

cc = usr_inp()
#print(cc)
m_cc1 = dump_cc1(cc)
#print(m_cc1)
m_cc1_sum = check_cc(m_cc1)
#print(m_cc1_sum)
m_cc2 = dump_cc2(cc)
#print(m_cc2)

c=""
m=1
m_cc3=""
for i in range(0,len(m_cc2)):
    c=str(m_cc2)[i]
    m=int(c)
    if m != 0:
        m_cc3=m_cc3+str(m)

#print(m_cc3)

c=""
m=0
for i in range(0,len(m_cc3)):
    c=m_cc3[i]
    m=m+int(c)
#print(m)

sum = m_cc1_sum+m
#print(sum)

c=""
m=0

c=str(sum)
f=c[len(c)-1]
#print(f)

m=int(f)
#print(m)

if m == 0:
    print("The credit card number is valid")
else:
    print("The credit card number is invalid")