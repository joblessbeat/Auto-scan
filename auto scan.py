from pywinauto import Application
import keyboard
from datetime import datetime

# create entry point for automation
app = Application(backend='uia')

# start WFS
app.start(r'C:\Windows\system32\WFS.exe')
app.connect(path=r'C:\Windows\system32\WFS.exe')

# main menu dialog
wfs = app.top_window()

# choose scan from main window
wfs.NewScanButton.click()
wfs.OK.click()

# new scan dialog
wfs.child_window(title="Scan", auto_id="1", control_type="Button").click()

# wait for scan to end
wfs.wait('ready', timeout=60)

# open save file menu
wfs.child_window(title="File", control_type="MenuItem").click
wfs.SaveAs.click()

# actual time (part of saved file name)
now = datetime.now()
time = now.strftime('%H.%M.%S')

# enter file name
file_name_field = wfs.child_window(title="File name:", auto_id="1152", control_type="Edit")
file_name_field.type_keys(f'my_scan {time}', with_spaces=True)

# save and close
wfs.Save.click()
wfs.child_window(title="Close", control_type="Button").click()