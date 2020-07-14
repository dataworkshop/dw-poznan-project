#pragma once

#include <IRremote.h>
#include "engine.h"
#include "sensors.h"

unsigned long KEYBOARD_ENGINE_STOP_AFTER_MS = 100;

#define ACTION_UP 'U'
#define ACTION_DOWN 'D'
#define ACTION_LEFT 'L'
#define ACTION_RIGHT 'R'

#define ACTION_OK '^'
#define ACTION_STAR '*'
#define ACTION_HASH '#'

#define ACTION_0 '0'
#define ACTION_1 '1'
#define ACTION_2 '2'

#define ACTION_SERVE_LEFT 'q'
#define ACTION_SERVE_RIGHT 'e'
#define ACTION_SERVE_RESET 'r'
#define ACTION_LOOK_AROUND ACTION_STAR

unsigned int engine_servo_pos = SERVO_CENTER_POSITION;


////////// IR REMOTE CODES //////////
#define F 16736925  // FORWARD
#define B 16754775  // BACK
#define L 16720605  // LEFT
#define R 16761405  // RIGHT
#define S 16712445  // STOP
#define UNKNOWN_F 5316027     // FORWARD
#define UNKNOWN_B 2747854299  // BACK
#define UNKNOWN_L 1386468383  // LEFT
#define UNKNOWN_R 553536955   // RIGHT
#define UNKNOWN_S 3622325019  // STOP
#define KEY1 16738455
#define KEY2 16750695
#define KEY3 16756815
#define KEY4 16724175
#define KEY5 16718055
#define KEY6 16743045
#define KEY7 16716015
#define KEY8 16726215
#define KEY9 16734885
#define KEY0 16730805
#define KEY_STAR 16728765
#define KEY_HASH 16732845

#define RECV_PIN  12

IRrecv irrecv(RECV_PIN);
decode_results results;
unsigned long val;
unsigned long preMillis;
unsigned char ret;
unsigned char getstr;

void setup_remote() {
  irrecv.enableIRIn();  
}

unsigned char decode_key() {
   getstr = Serial.read();
   switch(getstr){
    case 'w': return ACTION_UP;
    case 's': return ACTION_DOWN;
    case 'd': return ACTION_RIGHT;
    case 'a': return ACTION_LEFT; 
    
    case 'j': return ACTION_STAR; 
    case 'k': return ACTION_HASH; 
    case 'l': return ACTION_OK; 
    
    case '0': return ACTION_0; 
    case '1': return ACTION_1; 
    case '2': return ACTION_2;

    case 'q': return ACTION_SERVE_LEFT;
    case 'e': return ACTION_SERVE_RIGHT;
    case 'r': return ACTION_SERVE_RESET;
   
    default: break;
  }
  return ' ';
}

unsigned char decode_irrecv() {
 if (irrecv.decode(&results)){ 
    val = results.value;
    irrecv.resume();
    switch(val){
      case F: 
      case UNKNOWN_F: return ACTION_UP;
      case B: 
      case UNKNOWN_B: return ACTION_DOWN;
      case L: 
      case UNKNOWN_L: return ACTION_LEFT;
      case R: 
      case UNKNOWN_R: return ACTION_RIGHT;
      case S: 
      case UNKNOWN_S: return ACTION_OK;
      case KEY_STAR: return ACTION_STAR;
      case KEY_HASH: return ACTION_HASH;
      case KEY0: return ACTION_0;
      case KEY1: return ACTION_1;
      case KEY2: return ACTION_2;
      default: break;
    }
  }
  return ' ';
}

unsigned char check_input() {
  ret = decode_irrecv();
  if(ret!=' ') return ret;
  return decode_key();
}

void stop_enginge_after(int limit) {
  if(millis() - preMillis > limit){
      stop();
      preMillis = millis();
  }
}

  
unsigned char start_action(unsigned char ret) {
  if(ret!=' ') {
    preMillis = millis();
    switch(ret) {
      case ACTION_UP: forward(); return ret;
      case ACTION_DOWN:  back(); return ret;
      case ACTION_LEFT: left();  return ret;
      case ACTION_RIGHT: right(); return ret;
      case ACTION_OK: stop(); return ret;
      case ACTION_LOOK_AROUND: look_around(); return ret;
      
      case ACTION_SERVE_LEFT:
          engine_servo_pos += 5;
          set_servo(engine_servo_pos);
          break;
      case ACTION_SERVE_RIGHT:
          engine_servo_pos -= 5;
          set_servo(engine_servo_pos);
          break;
      case ACTION_SERVE_RESET:
          engine_servo_pos = SERVO_CENTER_POSITION;
          set_servo(engine_servo_pos);
          break;
      default: break;
    }
  } else {
    stop_enginge_after(KEYBOARD_ENGINE_STOP_AFTER_MS);
  }
  return ' ';
}
