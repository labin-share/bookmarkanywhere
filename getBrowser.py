from win32gui import *
import win32api,win32con

#EnumWindows 调用
#hwnd:EnumWindows()获取到的句柄
#extra:EnumWindows()输出
def callBack(hwnd,extra):
    windows=extra
    temp=[]
    title=GetWindowText(hwnd)
    clname=GetClassName(hwnd)
    if clname=='IEFrame'and'Internet Explorer' in title:
        temp.append(title)
        windows[hwnd]=temp

#通过浏览器句柄查找地址栏/地址
#parent:浏览器句柄
#返回:查找到的地址
def findIEChildWindows(parent):
    hwndChildList=[]    #主窗口下控件句柄
    url=''              #地址集合
    try:
        #查找父句柄下的控件句柄
        #parent：父句柄
        #其他与EnumWindows()相同
        EnumChildWindows(parent,lambda hwnd, param: param.append(hwnd),hwndChildList)
        print(hwndChildList)
        fa='xxx'
        for l in hwndChildList:
            tltie=GetWindowText(l)          #标题
            clname=GetClassName(l)          #类名
            print("句柄:%s ;标题：%s;类名：%s"%(l,tltie,clname))
            #IE才有地址Edit控件
            if clname == 'Edit':
                print('%s oooooooooo'%(l))
                len=1000#SendMessage(l,win32con.WM_GETTEXTLENGTH)用此函数获取长度不知道为什么有些地址会出错
                print(isinstance(len,int))
                buffer=PyMakeBuffer(len)
                status=SendMessage(l,win32con.WM_GETTEXT,len,buffer)#获取内容
                #buffer转string
                address, length = PyGetBufferAddressAndLen(buffer)
                text = PyGetString(address, length)
                url=text[0:status]
                print('len:%d,status:%s'%(len,status))
                break
    except Exception as e:
        print(e)
    return url

#获取IE标题，地址
def findIExplorer():
    try:
        hwnd={}
        urlDict={}
        keys=[]
        EnumWindows(callBack,hwnd)
        keys=hwnd.keys()
        #print(hwnd)
        for k in keys:
            #print('%s %s----------------'%(k,hwnd[k]))
            clname=GetClassName(k)
            #print(clname)
            if clname == 'IEFrame':
                #print('~~~~~~~~~~~~~~~~~~~~~')
                url=findIEChildWindows(k)
                #print('url:%s'%(url))
                if url !='':
                    urlDict[hwnd[k][0]]=url
    except Exception as e:
        print('something happend i don''t know')
    return urlDict
##################################################################

#findChildWindows()

if __name__=='__main__':
    print(findIExplorer())
    