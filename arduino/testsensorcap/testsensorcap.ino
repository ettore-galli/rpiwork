int ANALOG_IN = 0;
int POLL_DELAY_MS = 10;

void setup() {
  Serial.begin(115200);
}

void loop() {
  int N = 20;
  long val;
  for (int m=0; m<N; m++){
    val += analogRead(ANALOG_IN) / 16;
  }
  val /= N;
  char stars[78];
  for (int i=0; i< val; i++){
    stars[i] = '*';
  }
  Serial.println(stars);
  delay(POLL_DELAY_MS);
}
