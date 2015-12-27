Getting Started
---------------

1. Build a Shrimp:
  - https://leanpub.com/makingtheshrimp

2. Install Arduino IDE:
  - https://www.arduino.cc/en/Main/Software

3. Install CP2102 driver (not needed for Linux):
  - https://www.silabs.com/products/mcu/Pages/USBtoUARTBridgeVCPDrivers.aspx

4. Connect the Shrimp to a USB port.

5. Open Arduino IDE and configure the connection. (The following steps work in Arduino IDE 1.6.7).
  - Tools -> Board -> Arduino Duemilanove or Diecimila
  - Tools -> Processor -> ATmega328
  - Tools -> Port -> /dev/cu.SLAB_USBtoUART

6. Load "Blink" Sketch:
 - Examples -> 0.1 Basics -> Blink
 - Upload
 - The LED at digital pin 13 (DIP package pin 19) should blink.


Pin-Out Diagram
---------------
https://www.arduino.cc/en/Hacking/PinMapping168

