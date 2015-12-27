add_library('serial')
add_library("themidibus")

serialPort = None
val = 0
midiBus = None
ON = True
OFF = not ON
noteState = OFF

def setup():
    # Draw a grey square
    size(200, 200)
    background(204)
    
    # Connect to a MIDI bus (output only)
    print "Available MIDI Outputs: "
    for output in MidiBus.availableOutputs():
        print " -", output
    busName = "Bus 1"
    global myBus
    print "Connecting to", busName
    myBus = MidiBus(this, -1, busName)
    # TODO: Check connection was successful (constructor fails silently)
    
    # Connect to the Arduino using the serial port
    portName = "/dev/tty.SLAB_USBtoUART"
    print "Connecting to", portName
    global serialPort
    serialPort = Serial(this, portName, 9600)
    print "Connected!"

def draw():
    global val
    
    if (serialPort.available() > 0):
       val = serialPort.read()
        
    if (val == 0):
        fill(0)
        sendNote(OFF)
    else:
        fill(255)
        sendNote(ON)
        
    rect(50, 50, 100, 100)
    
    
def sendNote(state):
    global noteState
    channel = 0
    pitch = 64
    velocity = 127
    
    if (state == ON and noteState == OFF):
        myBus.sendNoteOn(channel, pitch, velocity)
        noteState = ON
    elif (state == OFF and noteState == ON):
        myBus.sendNoteOff(channel, pitch, velocity)
        noteState = OFF