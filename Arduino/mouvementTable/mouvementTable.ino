/*
 * file OutputVoltage.ino
 *
 * @ https://github.com/DFRobot/DFRobot_MCP4725
 *
 * connect MCP4725 I2C interface with your board (please reference board compatibility)
 *
 * Output a constant voltage value and print through the serial port.
 *
 * Copyright   [DFRobot](http://www.dfrobot.com), 2016
 * Copyright   GNU Lesser General Public License
 *
 * version  V0.1
 * date  2018-1-15
 */
#include "Wire.h"
#include "DFRobot_MCP4725.h"
#define  REF_VOLTAGE    3300

DFRobot_MCP4725 DAC1;
DFRobot_MCP4725 DAC2;

uint16_t OUTPUT_VOLTAGE_1 = 2000;     // unit : mV 
uint16_t OUTPUT_VOLTAGE_2 = 2000;     // unit : mV 

float t = 0;

void setup(void) {
  
  Serial.begin(115200);
  /* MCP4725A0_address is 0x60 or 0x61  
   * MCP4725A0_IIC_Address0 -->0x60
   * MCP4725A0_IIC_Address1 -->0x61
   */
  DAC1.init(MCP4725A0_IIC_Address0, REF_VOLTAGE);
  DAC2.init(MCP4725A0_IIC_Address1, REF_VOLTAGE);
  pinMode(22, OUTPUT);    // sets the digital pin 22 as output


}

void loop(void) {

  Serial.print("DFRobot_MCP4725 output: ");
  Serial.print(OUTPUT_VOLTAGE_1); 
  Serial.println(" mV");
  
  OUTPUT_VOLTAGE_1 = (cos(2 * 3.1415 * t) + 1.0f) * 1000;
  OUTPUT_VOLTAGE_2 = (sin(2 * 3.1415 * t) + 1.0f) * 1000 ;  
  
  
  
  if (Serial.available() > 0) {
    int data1 = Serial.parseInt();
    int data2 = Serial.parseInt();
    int data3 = Serial.parseInt();
    Serial.print("You sent me: ");
    Serial.println(data1);
    Serial.println(data2);
    DAC1.outputVoltage(data1);
    DAC2.outputVoltage(data2);
    if(data3 == 1){
      digitalWrite(22, HIGH);
    }
    else {
      digitalWrite(22, LOW);
    }
    
  }
}
