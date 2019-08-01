#define USE_ARDUINO_INTERRUPTS true // when a certain signal is detected, an Interrupt interrupts whatever the Arduino is doing
#include <MPU6050.h> // include the accelerometer library
#include <LiquidCrystal.h> // include the LCD screen library
#include <PulseSensorPlayground.h> // include the pulse sensor library

#include <Wire.h> // include Wire for serial communication

const int MPU_addr=0x68;  // I2C address of the MPU-6050
int16_t AcX,AcY,AcZ;
int16_t lastAcX, lastAcY,lastAcZ;
int steps = -1;
float height = 183; // enter your height
float steplength;
float distance;
const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

int Pulse = 0; // pulse sensor at analog pin 0
int LED13 = 13; // LED at digital pin 13
int Signal; 
int Threshold = 550;
PulseSensorPlayground pulseSensor;

void setup() {
  Wire.begin();
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x6B); // PWR_MGMT_1 register
  Wire.write(0); // set to zero (wakes up the MPU-6050)
  Wire.endTransmission(true);
  Serial.begin(9600); // initiates serial communication
  pulseSensor.analogInput(Pulse); // pin 0 is the input of the pulse sensor
  pulseSensor.blinkOnPulse(LED13); // LED flashes with heart beats
  pulseSensor.setThreshold(Threshold);
  pulseSensor.begin(); // initiate pulse sensor
  lcd.begin(16, 2); // initiate LCD
  steplength = height/3; // a person's step length is one third of their height
}

void loop(){
  
  int myBPM = pulseSensor.getBeatsPerMinute();
  
  Wire.beginTransmission(MPU_addr);
  Wire.write(0x3B);  // starting with register 0x3B (ACCEL_XOUT_H)
  Wire.endTransmission(false);
  Wire.requestFrom(MPU_addr,14,true);  // request a total of 14 registers
  
  AcX=Wire.read()<<8|Wire.read();  // 0x3B (ACCEL_XOUT_H) & 0x3C (ACCEL_XOUT_L)    
  AcY=Wire.read()<<8|Wire.read();  // 0x3D (ACCEL_YOUT_H) & 0x3E (ACCEL_YOUT_L)
  AcZ=Wire.read()<<8|Wire.read();  // 0x3F (ACCEL_ZOUT_H) & 0x40 (ACCEL_ZOUT_L)

  if(AcX>lastAcX+500 || AcY> lastAcY+500||AcZ> lastAcZ+500){
    steps++;
  }
  else if(AcX<lastAcX-500 || AcY <lastAcY-500 || AcZ<lastAcZ-500){ 
    steps++;
  }
  distance=(steplength*steps)/100;
  
  Serial.println(steps);
  lcd.setCursor(0,0);
  lcd.print("steps: ");
  lcd.print(steps);
  lcd.setCursor(0,1);
  lcd.print("Distance; ");
  lcd.print(distance);
  lcd.print("m");
  lcd.setCursor(10,0);
  lcd.print("HR:");
  lcd.print(myBPM);
  delay(1000);

  lastAcX=AcX;
  lastAcY=AcY;
  lastAcZ=AcZ;
}

enemy_x = 0
enemy_y = 0
enemy_sx = 0
enemy_sy = 10
enemy_sz = 100
player_sz=100
bullet_sy=10
score=1



text_color = color(96, 150, 186)

def setup():
    size(800, 800)
    
def draw():
    global score
    global enemy_x 
    global enemy_y 
    global enemy_sx 
    global enemy_sy 
    global enemy_sz
    global player_sz

   
    background(0, 0, 0)
    x_player = mouseX
    y_player = mouseY
    plane = loadImage("plane.png")
    image(plane, x_player, y_player, player_sz, player_sz)
    
    enemy=loadImage('oe.jpg')
    noStroke()
    image(enemy, enemy_x, enemy_y, enemy_sz, enemy_sz)
    enemy_y += enemy_sy
    
    if enemy_y > height:
        enemy_y = 0
        enemy_x = random(5, width)
        score += 1
        
    r_enemy = enemy_sz/2
    r_player = player_sz/2
    a = enemy_x - x_player
    b = enemy_y - y_player
    d = sqrt(a**2 + b**2)
    if d<= r_enemy + r_player:
        score-= 1
        enemy_y = 0
        enemy_x = random(0, width)
        
    fill(text_color)
    textSize(40)
    textAlign(LEFT)
    text(score, 20, 50)
    
    #def mousePressed()
  # 
