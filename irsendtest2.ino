#include <IRremote.h> 
IRsend irsend; // IRRemote is limited to use digital pin 3
int data;
void setup()
{
  Serial.begin(115200);
  Serial.println("Hi!, I am Arduino");
}

void loop() {
  
  while (Serial.available())
    //scanf("%d", &d);
  if( (data = Serial.read()) != -1) {// read serial port
    unsigned long v = 0x0;
    switch(data){ // According to the read data, replace it with an infrared code representing six buttons
      case '1':
        v = 0x80FFC13E; //Power 
      break;
      case '0':
        v = 0x80FFC13E; //Power 
      break;
      case '2':
        v = 0x80FFE11E;// Speed
      break;
      case '3':
        v = 0x404050AF; //power on/off
      break;
      case '4':
        v = 0x4040D02F; //Channel up
      break;
      case '5':
        v = 0x4040708F; //Channel dwn
      break;
      case '6':
        v = 0x404008F7; //volume up
      break;
      case '7':
        v = 0x40408877; //volume dwn
      break;
    }
   
    if(v != 0x0){
      Serial.print("read ");
      Serial.print(data);
      Serial.print(", IR send ");
      Serial.println(v, HEX);
      irsend.sendNEC(v , 32); // Output infrared signal
    }
  }
}
