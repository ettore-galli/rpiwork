int SOUND_OUT = 14;
int ANALOG_IN = 0;
int POLL_DELAY_MS = 10;

int _BASE_TICKS = 500000;


volatile int _led_status = HIGH;
volatile int _ticks = _BASE_TICKS;

void ICACHE_RAM_ATTR onTimerISR() {
  _led_status = !_led_status;
  digitalWrite(SOUND_OUT, _led_status);
  timer1_write(_ticks);
}


void setupOuput() {
  _led_status = HIGH;
  pinMode(SOUND_OUT, OUTPUT);
}


void setupTimer() {
  timer1_attachInterrupt(onTimerISR);
  timer1_enable(TIM_DIV16, TIM_EDGE, TIM_SINGLE);
  timer1_write(_ticks);
}


void setup() {
  setupOuput();
  setupTimer();
  Serial.begin(115200);
}


int frequencyToTicks(float frequency){
  float t = 1.0 / frequency; // s
  return int(1000000 * t * 5); // [us]/[s] * [s] * [ticks]/[us]
}

int sensorValueToTicks(int value) {
  return frequencyToTicks(2*value);
}


void loop() {
  _ticks = sensorValueToTicks(analogRead(ANALOG_IN));
  // timer1_write(_ticks);
  Serial.println(_ticks);
  delay(POLL_DELAY_MS);
}
