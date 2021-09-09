import os
import getopt
import sys
sum = 0

def getfilesize(sumdir,unit,size):
    fileSize=0
    global sum
    file01=''
    filelist = os.listdir(sumdir)
    for content in  filelist:
        file01 = os.path.join(sumdir,content)
        flag = os.path.isfile(file01)
        if flag:
            fileSize+=os.path.getsize(file01)
        else:
            getfilesize(file01,unit,size)
    if unit=="m":
        if fileSize/1024/1024 > size:
            print("文件夹名：%s,文件夹大小：%.2fMb" %(os.path.dirname(file01),fileSize/1024/1024))
    elif unit=="g":
        if fileSize/1024/1024/1024 > size:
            print("文件夹名：%s,文件夹大小：%.2fGb" %(os.path.dirname(file01),fileSize/1024/1024/1024))
    sum+=fileSize
'''
添加帮助信息
'''
def usage():
    print("""Usage getDirSize.exe  -p|--path [dir]  <-M|--Mb [m]>|<-G|--Gb [g]>  -s|--size [number]
                -p|--path dirname
                -M|--Mb unit
                -G|--Gb unit
                -s|--size number
                -v|--version version message
          """)

if __name__ == "__main__":
    opts,args = getopt.getopt(sys.argv[1:],"p:hM:G:s:v",['path','help','Mb','Gb','size','version'])
    dir_path=''
    unit_m=''
    unit_g=''
    filter_size=0
    for opt_name,opt_value in opts:
        if opt_name in ('-p','--path'):
            dir_path=opt_value
        if opt_name in ('-h','--help'):
            usage()
            exit()
        if opt_name in ('-M','--Mb'):
            unit_m=opt_value
        if opt_name in ('-G','--Gb'):
            unit_g=opt_value
        if opt_name in ('-s','--size'):
            filter_size=int(opt_value)
        if opt_name in ('-v','--version'):
            print("current version: 1.0")
            exit()
    getfilesize(dir_path,unit_m,filter_size)
    print("文件夹总大小：%.2fGb" %(sum/1024/1024/1024))
