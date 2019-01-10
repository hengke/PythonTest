import win32com.client

strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer,"root\cimv2")
colItems = objSWbemServices.ExecQuery("Select * from Win32_ComputerSystem")
for objItem in colItems:
    print("Admin Password Status: ", objItem.AdminPasswordStatus)
    print("Automatic Reset Boot Option: ", objItem.AutomaticResetBootOption)
    print("Automatic Reset Capability: ", objItem.AutomaticResetCapability)
    print("Boot Option On Limit: ", objItem.BootOptionOnLimit)
    print("Boot Option On WatchDog: ", objItem.BootOptionOnWatchDog)
    print("Boot ROM Supported: ", objItem.BootROMSupported)
    print("Bootup State: ", objItem.BootupState)
    print("Caption: ", objItem.Caption)
    print("Chassis Bootup State: ", objItem.ChassisBootupState)
    print("Creation Class Name: ", objItem.CreationClassName)
    print("Current Time Zone: ", objItem.CurrentTimeZone)
    print("Daylight In Effect: ", objItem.DaylightInEffect)
    print("Description: ", objItem.Description)
    print("Domain: ", objItem.Domain)
    print("Domain Role: ", objItem.DomainRole)
    print("Enable Daylight Savings Time: ", objItem.EnableDaylightSavingsTime)
    print("Front Panel Reset Status: ", objItem.FrontPanelResetStatus)
    print("Infrared Supported: ", objItem.InfraredSupported)
    z = objItem.InitialLoadInfo
    if z is None:
        a = 1
    else:
        for x in z:
            print("Initial Load Info: ", x)
    print("Install Date: ", objItem.InstallDate)
    print("Keyboard Password Status: ", objItem.KeyboardPasswordStatus)
    print("Last Load Info: ", objItem.LastLoadInfo)
    print("Manufacturer: ", objItem.Manufacturer)
    print("Model: ", objItem.Model)
    print("Name: ", objItem.Name)
    print("Name Format: ", objItem.NameFormat)
    print("Network Server Mode Enabled: ", objItem.NetworkServerModeEnabled)
    print("Number Of Processors: ", objItem.NumberOfProcessors)
    z = objItem.OEMLogoBitmap
    if z is None:
        a = 1
    else:
        for x in z:
            print("OEM Logo Bitmap: ", x)
    z = objItem.OEMStringArray
    if z is None:
        a = 1
    else:
        for x in z:
            print("OEM String Array: ", x)
    print("Part Of Domain: ", objItem.PartOfDomain)
    print("Pause After Reset: ", objItem.PauseAfterReset)
    z = objItem.PowerManagementCapabilities
    if z is None:
        a = 1
    else:
        for x in z:
            print("Power Management Capabilities: ", x)
    print("Power Management Supported: ", objItem.PowerManagementSupported)
    print("PowerOn Password Status: ", objItem.PowerOnPasswordStatus)
    print("Power State: ", objItem.PowerState)
    print("Power Supply State: ", objItem.PowerSupplyState)
    print("Primary Owner Contact: ", objItem.PrimaryOwnerContact)
    print("Primary Owner Name: ", objItem.PrimaryOwnerName)
    print("Reset Capability: ", objItem.ResetCapability)
    print("Reset Count: ", objItem.ResetCount)
    print("Reset Limit: ", objItem.ResetLimit)
    z = objItem.Roles
    if z is None:
        a = 1
    else:
        for x in z:
            print("Roles: ", x)
    print("Status: ", objItem.Status)
    z = objItem.SupportContactDescription
    if z is None:
        a = 1
    else:
        for x in z:
            print("Support Contact Description: ", x)
    print("System Startup Delay: ", objItem.SystemStartupDelay)
    z = objItem.SystemStartupOptions
    if z is None:
        a = 1
    else:
        for x in z:
            print("System Startup Options: ", x)
    print("System Startup Setting: ", objItem.SystemStartupSetting)
    print("System Type: ", objItem.SystemType)
    print("Thermal State: ", objItem.ThermalState)
    print("Total Physical Memory: ", objItem.TotalPhysicalMemory)
    print("User Name: ", objItem.UserName)
    print("WakeUp Type: ", objItem.WakeUpType)
    print("Workgroup: ", objItem.Workgroup)
