import pythoncom, win32com.client
import comtypes.client as cc

def CreateInstanceFromDll(dll, clsid_class, iid_interface=pythoncom.IID_IDispatch, pUnkOuter=None, dwClsContext=pythoncom.CLSCTX_SERVER):
    from uuid import UUID
    from ctypes import OleDLL, c_long, byref
    e = OleDLL(dll)
    clsid_class = UUID(clsid_class).bytes_le
    iclassfactory = UUID(str(pythoncom.IID_IClassFactory)).bytes_le
    com_classfactory = c_long(0)
    hr = e.DllGetClassObject(clsid_class, iclassfactory, byref(com_classfactory))
    MyFactory = pythoncom.ObjectFromAddress(com_classfactory.value, pythoncom.IID_IClassFactory)
    i = MyFactory.CreateInstance(pUnkOuter, iid_interface)
    d = win32com.client.__WrapDispatch(i)
    return d

def GetDBString():
    a1 = win32com.client.DispatchEx('{5EEEA87D-160E-4A2D-8427-B6C333FEDA4D}')

    # objApi = pythoncom.LoadTypeLib(r'C:\Program Files (x86)\Tencent\RTXCSDK\tlb\RTXCModuleInterface.tlb')
    objApi = CreateInstanceFromDll(r'C:\Program Files (x86)\Tencent\RTXC\RTXAX.dll','5EEEA87D-160E-4A2D-8427-B6C333FEDA4D')
    # objApi = cc.CreateObject("RTXClient.RTXAPI")
    objApp = objApi.GetObject("AppRoot")

    objVer = objApp.GetAppObject("Version")
    # 在AppRoot中获取Version对象
    compilever = objVer.GetCompileVer
    compilever = "编译版本号：" + compilever

    licensever = objVer.GetLicenseVer
    licensever = "License版本号：" + licensever
    msg = compilever & vbCrLf & licensever
    return msg


print(GetDBString())
