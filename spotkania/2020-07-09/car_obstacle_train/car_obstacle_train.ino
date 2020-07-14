#include "engine.h"
#include "sensors.h"
#include "remote.h"
#include "obstacle_model_svm.h"
#include "model.h"

unsigned int run_mode = 0; // 0 - training, 1 - running SVM, 2 - running perceptron.

unsigned char action;
float last_sensors[6];

unsigned char svm_classes[] = {'*', 'D', 'L', 'R', 'U'};

void setup() { 
  KEYBOARD_ENGINE_STOP_AFTER_MS = 200;
  SERVO_CENTER_POSITION = 45;
  
  Serial.begin(9600); 
  setup_engine();
  setup_sensors();
  setup_remote();

  stop();
    
  Serial.println(); sensors_print_header(); Serial.print("\tAction"); Serial.println();
  sensors_print(&last_sensors[0]);
} 


void loop() {
  action = check_input();

  // If there is change of the action we treat
  if(action == ACTION_0) {
     run_mode = 0;
     KEYBOARD_ENGINE_STOP_AFTER_MS = 100;
     Serial.println(); Serial.print("MODE: "); Serial.print(run_mode) ; Serial.println(" SWITCH TO RUN MODE");
     action = ' ';
  } else if(action == ACTION_1) {
     run_mode = 1;
     KEYBOARD_ENGINE_STOP_AFTER_MS = 500;
     Serial.println(); Serial.print("MODE: "); Serial.print(run_mode) ; Serial.println(" SWITCH TO SVM MODE");
     action = ' ';
  } else if(action == ACTION_2) {
     run_mode = 2;
     KEYBOARD_ENGINE_STOP_AFTER_MS = 500;
     Serial.println(); Serial.print("MODE: "); Serial.print(run_mode) ; Serial.println(" SWITCH TO PERCEPTRON MODE");
     action = ' ';
  }
  

  if(run_mode == 1) {
    action =  (unsigned char)svm_predict(&last_sensors[0]);
  }
  
  if(run_mode == 2) {
    action =  (unsigned char)model_predict(&last_sensors[0]);
  }
  
  if(action != ' ') {
    start_action(action);
    
    Serial.print("\t");Serial.print((char)action);   Serial.println();
    delay(KEYBOARD_ENGINE_STOP_AFTER_MS);
    stop();
    delay(KEYBOARD_ENGINE_STOP_AFTER_MS);
    sensors_print(&last_sensors[0]);
  }

  Distance_test(true);
  delay(200);  
}
