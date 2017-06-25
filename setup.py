import os.path

steamdir = "C:\Program Files (x86)\Steam\steamapps\common"

if os.path.exists(steamdir):
    print "Directory \"" + steamdir + "\" found."
else:
    print "Directory \"" + steamdir + "\" not found."
