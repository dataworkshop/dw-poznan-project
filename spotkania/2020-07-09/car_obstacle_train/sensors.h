#pragma once

int rightDistance = 0, leftDistance = 0, middleDistance = 0;
int Echo = A4;
int Trig = A5;

int SERVO_LEFT_POSITION = 90;
int SERVO_CENTER_POSITION = 45;
int SERVO_RIGHT_POSITION = 0;

int SERVO_WAIT_TIME = 500;

#define LED 13


#include <Servo.h>  //servo library (INSTALL servo LIBRARY FROM: TOOLS->MANAGE LIBRARIES-> Servo (by Micheal Margolis)
Servo myservo;      // create servo object to control servo, the blue controller under eyes

//Line Tracking IO define
#define LT_R digitalRead(10)
#define LT_M digitalRead(4)
#define LT_L digitalRead(2)


int LAST_DISTANCE_MAX_CM = 100;
int LAST_DISTANCE = LAST_DISTANCE_MAX_CM;
int DISTANCE_LEFT = 0;
int DISTANCE_RIGHT = 0;

//Ultrasonic distance measurement Sub function
int Distance_test(bool save) {
   digitalWrite(LED, 1);
    
  digitalWrite(Trig, LOW);   
  delayMicroseconds(2);
  digitalWrite(Trig, HIGH);  
  delayMicroseconds(20);
  digitalWrite(Trig, LOW);   
  float Fdistance = pulseIn(Echo, HIGH);  
  Fdistance= Fdistance / 58;  
  digitalWrite(LED, 0);
  
  
  if(save) {
    if(Fdistance < LAST_DISTANCE_MAX_CM) { //only close objects we save, sometimes it is mistake taken
      LAST_DISTANCE = (int)Fdistance;
    }
    return LAST_DISTANCE;
  }
  return Fdistance;
}  

void look_around() {
  stop();                        
  myservo.write(SERVO_RIGHT_POSITION);          
  delay(SERVO_WAIT_TIME);      
  DISTANCE_RIGHT = Distance_test(false);
                                    
  myservo.write(SERVO_LEFT_POSITION);              
  delay(SERVO_WAIT_TIME); 
  DISTANCE_LEFT = Distance_test(false);

  delay(SERVO_WAIT_TIME);
  myservo.write(SERVO_CENTER_POSITION);   

  delay(500);
}

void set_servo(int pos) {
  delay(SERVO_WAIT_TIME);
  myservo.write(pos);
  unsigned int pos_distance = Distance_test(false);

  Serial.println();
  Serial.print("pos: ");Serial.print(pos); 
  Serial.print("\tdistance: ");Serial.print(pos_distance); 
  Serial.println("");
}

void setup_sensors() {
  myservo.attach(3,700,2400);  // attach servo on pin 3 to servo object
  myservo.write(SERVO_CENTER_POSITION);  //setservo position according to scaled value

  pinMode(Echo, INPUT);    
  pinMode(Trig, OUTPUT);  

  pinMode(10,INPUT);
  pinMode(4,INPUT);
  pinMode(2,INPUT);

  pinMode(LED, OUTPUT); 
}

void sensors_print_header()
{
  Serial.print("Left\tMiddle\tRight\tDistance\tDistanceLeft\tDistanceRight");
}

void sensors_print(float *sensors) {
  sensors[0] = (float)LT_L;
  sensors[1] = (float)LT_M;
  sensors[2] = (float)LT_R;

  sensors[3] = (float)Distance_test(true);
  sensors[4] = (float)DISTANCE_LEFT;
  sensors[5] = (float)DISTANCE_RIGHT;
 
  
  Serial.print(sensors[0]); Serial.print("\t");
  Serial.print(sensors[1]); Serial.print("\t");
  Serial.print(sensors[2]); Serial.print("\t");
  Serial.print(sensors[3]); Serial.print("\t");

  
  Serial.print(sensors[4]); Serial.print("\t");
  Serial.print(sensors[5]); 

  DISTANCE_LEFT = 0;
  DISTANCE_RIGHT = 0;
}
