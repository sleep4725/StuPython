import os
s = 0
elementList = list()
def dirInformation(currentDir):
    global s
    global elementList
    #print (currentDir)
    os.chdir(currentDir)
    #print ("s => {},   current_dir => {}".format(s, os.getcwd()))
    pathList = currentDir.split('\\')
    for i in os.listdir(currentDir):
        if os.path.isdir(i):
            if i not in elementList:
                print (' '*s + '-'*s, i)
                elementList.append(i)
                s += 1
                #print ("path list -> {}".format(pathList))
                path = '\\'.join(pathList) + '\\' + i
                #print ("path => {}".format(path))
                #print ("{} 번째=============================================".format(s+1))
                return dirInformation(path)
        else:
            print (' '*s + '-'*s, i)


    if currentDir == 'C:\\Django-2.0.4\\django\\bin\\stu01':
        exit()
    else:
        path ='\\'.join(pathList[0:len(pathList)-1])
        s -= 1
        return dirInformation(path)

def main():
    dirInformation("C:\\Django-2.0.4\\django\\bin\\stu01")
    # for i in List:
    #     print (i)
    #     current_dir = os.getcwd()
    #     if os.path.isdir(i) is True:


if __name__ == "__main__":
    main()
