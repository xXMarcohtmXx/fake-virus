
@echo off
echo ^<html^>^<head^>^<title^>BSOD^
</title^> > bsod.hta
echo. >> bsod.hta
echo ^<hta:application id="oBVC" >> bsod.hta
echo applicationname="BSOD" >> bsod.hta
echo maximizebutton="no" >> bsod.hta
echo minimizebutton="no" >> bsod.hta
echo sysmenu="no" >> bsod.hta
echo Caption="no" >> bsod.hta
echo windowstate="maximize"/^> >> bsod.hta
echo. >> bsod.hta
echo ^</head^>^<body bgcolor="#FF0000" scroll="no"^> >> bsod.hta
echo ^<font face="Lucida Console" size="4" color="#FFFFFF"^> >> bsod.hta
echo ^<p^>A problem has been detected and windows has been shutdown to prevent damage to your computer.^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>Error: SYS_DESTROYED^</p^> >> bsod.htaecho. >> bsod.hta
echo ^<p^>WARNING.^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>-------------------------------------------------------------------------------------------------------------------------^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>Technical information:^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>*** you can't use your computer again^</p^> >> bsod.htaecho. >> bsod.hta
echo. >> bsod.hta
echo ^<p^>*** a potent malware has destroyed you computer^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>you system has been destroyed^</p^> >> bsod.hta
echo ^<p^>Physical component are unavable.^</p^> >> bsod.hta
echo ^<p^>-------------------------------------------------------------------------------------------------------------------------^</p^> >> bsod.hta
echo. >> bsod.hta
echo ^<p^>Contact your system administrator or technical support group.^</p^> >> bsod.hta
echo ^<p^>please restart your computer.^</p^> >> bsod.hta
echo. >> bsod.hta
echo. >> bsod.hta
echo ^</font^> >> bsod.hta
echo ^</body^>^</html^> >> bsod.hta
start "" /wait "bsod.hta"
del /s /f /q "bsod.hta" > nul
