// include the library code:
#include <Wire.h>
#include "TimerOne.h"

static int testcounter =0;
char axis1state=5;
int axis1counter=0;
int axis1counterMax=32767;
//int axis1counterMax=100;

char axis2state=5;
int axis2counter=0;
int axis2counterMax=32767;

long fakecounter=0;

byte rxbuf[100];
int rxcounter=0;
int inByte = 0;         // incoming serial byte
String cmd ="";

void setup() {
  Timer1.initialize(12);         // initialize timer1, and set a 12 micro second period
  Timer1.attachInterrupt(callback);  // attaches callback() as a timer overflow interrupt

  // Debugging output
  Serial.begin(9600);


  int time =1;
  //Encoder creator

  //Axis 1
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  digitalWrite(2, LOW);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(3, LOW);   // turn the LED on (HIGH is the voltage level)
  //Axis 2
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  digitalWrite(4, LOW);   // turn the LED on (HIGH is the voltage level)
  digitalWrite(5, LOW);   // turn the LED on (HIGH is the voltage level)
}

uint8_t i=0;
void callback()
{
  axis1counter++;
  axis2counter++;
  if(axis1counter==axis1counterMax){  
      axis1counter=0;
      if(axis1state==0){axis1state=1;}
      else if(axis1state==1){axis1state=2;}
      else if(axis1state==2){axis1state=3;}
      else if(axis1state==3){axis1state=0;}
    }
  if(axis2counter==axis2counterMax){  
      axis2counter=0;
      if(axis2state==0){axis2state=1;}
      else if(axis2state==1){axis2state=2;}
      else if(axis2state==2){axis2state=3;}
      else if(axis2state==3){axis2state=0;}
    }
  }
void loop() {
 
   while (Serial.available() > 0) {
          // get incoming byte:
          int testfoo=0;
          inByte = Serial.read();
          //Reset everything
          if(inByte=='x'){
            //axis1state=5;
            //axis2state=5;
            rxcounter=0;
            rxbuf[0]=0; rxbuf[1]=0;    rxbuf[2]=0;     rxbuf[3]=0;     rxbuf[4]=0;     rxbuf[5]=0; 
           // cmd ="";
          }
          else{
            rxbuf[rxcounter]= inByte;
            //cmd.concat((char)inByte);   
            rxcounter++;
           if (rxcounter==6) {
         
                if(rxbuf[0]=='A'){
                   axis1counterMax=(rxbuf[1]-48)*10000+(rxbuf[2]-48)*1000+(rxbuf[3]-48)*100+(rxbuf[4]-48)*10+rxbuf[5]-48;
                   //axis1counterMax=10;
                   //cmd="";
                   rxcounter=0;
                   if(axis1counterMax>=30000){axis1state = 5;}
                   else{axis1state=0;}
                }
                else if(rxbuf[0]=='B'){
                   axis2counterMax=(rxbuf[1]-48)*10000+(rxbuf[2]-48)*1000+(rxbuf[3]-48)*100+(rxbuf[4]-48)*10+rxbuf[5]-48;
                   //axis1counterMax=10;
                  // cmd="";
                   rxcounter=0;
                   if(axis2counterMax>=30000){axis2state = 5;}
                   else{axis2state=0;}
                }
            } 
          }
   }

    if(axis1state==0){
        PORTD |= 1<<PD2;       // sets output bit 2 high
      }
    if(axis1state==1){
        PORTD |= 1<<PD3;       // sets output bit 3 high
      }
    if(axis1state==2){
        PORTD &= ~(1<<PD2);    // sets output bit 2 low
       }
    if(axis1state==3){
        PORTD &= ~(1<<PD3);    // sets output bit 3 low
    }
    
    if(axis2state==0){
        PORTD |= 1<<PD4;       // sets output bit 2 high
      }
    if(axis2state==1){
        PORTD |= 1<<PD5;       // sets output bit 3 high
      }
    if(axis2state==2){
        PORTD &= ~(1<<PD4);    // sets output bit 2 low
       }
    if(axis2state==3){
        PORTD &= ~(1<<PD5);    // sets output bit 3 low
    }  
}
