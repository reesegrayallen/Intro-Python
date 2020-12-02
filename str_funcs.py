# Reese Allen rga2uz


#3.1Ellipses
def ellipses(s):
    return(s[0]+s[1]+"..."+s[len(s)-2]+s[len(s)-1])

print(ellipses("superman"))



#3.2Eighteen
def eighteen(s):
    return(s[0] + str(len(s)-2) + s[len(s)-1])

print(eighteen("superwoman"))



#3.3Alliterative
def alliterative(s, t):
    y =["a","e","i","o","u"]
    if s[0].lower() in y:
        return False
    elif t[0].lower() in y:
        return False
    elif s[0].lower() != t[0].lower():
        return False
    else:
        return True

print(alliterative("hi", "hello"))
print(alliterative("apple", "arrogant"))
print(alliterative("batman", "robin"))


#3.4Between
def between(s,t):
    x = s.find(t)
    y = s.find(t,int(x),int(len(s)-1))
    return s[int(x):int(y)]

#this does not work yet

print(between("loan me a lovely loon to look at", "lo"))
