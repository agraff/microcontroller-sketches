Setting Up MIDI Device
----------------------

This sketch needs an IAC Driver device to send its MIDI outputs to. The steps to create one of these devices on a Mac are:

1. Applications -> Utilities -> Audio MIDI Setup
2. Window menu -> Show MIDI Studio
3. Double-click "IAC Driver" icon
4. Tick "Device is online"
5. Take a note of the Port name (e.g. "Bus 1") - the sketch connects to this port
6. Click Apply
7. Update the Python sketch, to set the `busName` variable to the port name noted in step 5

(tested on OS X 10.11.1)
