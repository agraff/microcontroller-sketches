add_library('serial')
add_library("themidibus")

ON = True
OFF = not ON

serialPort = None
midiBus = None
noteCount = 5
previousNoteState = [OFF] * noteCount

def setup():
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
    if (serialPort.available() > 0):
        serialValue = serialPort.read()
        print "Raw serial value:", serialValue
 
        for noteIndex in range(noteCount):
            noteState = (serialValue & 0x01 == 1)
            if (noteState != previousNoteState[noteIndex]):
                sendNote(noteIndex, noteState)
            
            previousNoteState[noteIndex] = noteState
            serialValue = serialValue >> 1

        print previousNoteState
        
    
def sendNote(noteIndex, state):
    channel = 0
    pitch = 60 + noteIndex
    velocity = 127
    
    if (state == ON):
        myBus.sendNoteOn(channel, pitch, velocity)
    else:
        myBus.sendNoteOff(channel, pitch, velocity)