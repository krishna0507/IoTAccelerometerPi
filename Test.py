from adxl345 import ADXL345

import time
import sys
import pprint
import uuid
from uuid import getnode as get_mac

try:
        import ibmiotf.application
        import ibmiotf.device
except ImportError:
        # This part is only required to run the sample from within the samples
        # directory when the module itself is not installed.
        # If you have the module installed, just use "import ibmiotf.application" & "import ibmiotf.device"
        import os
        import inspect
        cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"../../src")))
        if cmd_subfolder not in sys.path:
                sys.path.insert(0, cmd_subfolder)
        import ibmiotf.application
        import ibmiotf.device

#THESE DETAILS TO BE FILLED IN 
organization = ""
deviceType = ""
deviceId = ""
authMethod = "token"
authToken = ""

# Initialize the device client.
try:
        deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
        deviceCli = ibmiotf.device.Client(deviceOptions)
except Exception as e:
        print(str(e))
        sys.exit()

# Keep sending the accelerometer values
deviceCli.connect()
while(1):
        adxl345 = ADXL345()
        axes = adxl345.getAxes(True)
        print "ADXL345 on address 0x%x:" % (adxl345.address)
        print "   x = %.3fG" % ( axes['x'] )
        print "   y = %.3fG" % ( axes['y'] )
        print "   z = %.3fG" % ( axes['z'] )

        data = { 'x' : axes['x'], 'y' : axes['y'], 'z' : axes['z']}
        deviceCli.publishEvent("greeting", data)
        time.sleep(1)


# Disconnect the device and application from the cloud
deviceCli.disconnect()
