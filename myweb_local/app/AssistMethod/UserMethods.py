def readUser():
    result = []
    with open('app/static/UserData/Users/User','r',encoding='UTF-8') as f:
        for each in f.readlines():
            user = each.strip('\n').strip(' ').split(' ')
            if len(user) == 2:
                result.append(user)
    return result

def writeUser(addUser):
    exist = readUser()
    print(exist)
    flag = False
    strn = ''
    for No in range(len(exist)):
        if addUser[0] == exist[No][0]:
            exist[No][1] = addUser[1]
            flag = True
        strn += (str(exist[No][0])+' '+str(exist[No][1])+'\n')
    if flag is False:
        strn += (str(addUser[0])+' '+str(addUser[1])+'\n')
    with open('app/static/UserData/Users/User','w') as f:
        f.write(strn)

def checkUserAndPassword(username, password):
    exist = readUser()
    if [username,password] in exist:
        return True
    return False



