int LED_PIN = 14;

int led_status = HIGH;

void ICACHE_RAM_ATTR onTimerISR(){
  led_status = !led_status;
  digitalWrite(LED_PIN, led_status);
  Serial.println(led_status);
}

void setup() {

  pinMode(LED_PIN, OUTPUT); 
  
  timer1_attachInterrupt(onTimerISR);
  timer1_enable(TIM_DIV16, TIM_EDGE, TIM_LOOP);
  timer1_write(600000);

  digitalWrite(LED_PIN, HIGH);

  Serial.begin(115200);
}


void loop() {
  // put your main code here, to run repeatedly:

}
