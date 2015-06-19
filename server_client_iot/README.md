Device and Application side code

client.py -> send data from device to IoTF and listen to Commands from application.

server.py -> recieve data from IoTF that is indirectly from the device, also has the feature to send commands to the device.

here is the breif documentation,

client.py is a code which sends data IoTF just like Pi. Run it and it keeps sending the data(as in the client.py)

server.py is a code which sends a command and receives data. Run this separately.

run client.py(don't terminate it, i mean let it keep sending the data)
run server.py alongside client.py

You can see in the terminal of client.py the command being sent by sever.py
And, You can see the real time data being printed in terminal of server.py.

NOTE : FILL IN THE CONFIGURATION DETAILS IN THE TWO FILES BEFORE RUNNING
