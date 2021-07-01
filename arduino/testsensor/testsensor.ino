/*
   https://dlbeer.co.nz/articles/pdm.html
*/

int SOUND_OUT = 14; // D5
int PULSE_PIN = 4; // D2
int ECHO_PIN =  5; // D1

int POLL_DELAY_MS = 10;





void setupOuput() {
  pinMode(SOUND_OUT, OUTPUT);
  pinMode(PULSE_PIN, OUTPUT);
  pinMode(ECHO_PIN, INPUT);
}


void setup() {
  setupOuput();
  Serial.begin(115200);
}


int sensorValueToRegisterFrequency(int value) {
  return value * 4;
}


int sense() {
  digitalWrite(PULSE_PIN, LOW);
  delayMicroseconds(2);
  digitalWrite(PULSE_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(PULSE_PIN, LOW);
  delayMicroseconds(2);

  const unsigned long duration = pulseIn(ECHO_PIN, HIGH);

  return duration;
}

const int DIM = 10;

unsigned long * senseMulti(int inBetweenDelay) {
  static unsigned long meas[DIM];
  for (int i = 0; i < DIM; i++) {
    meas[i] = sense();
    delay(inBetweenDelay);
  }
  return meas;
}


long processCleanupData(unsigned long meas[10]) {
  int DIM = 10;

  double sum = 0;
  double sumsq = 0;
  double avg = 0;
  double avgsq = 0;

  for (int i = 0; i < DIM; i++) {
    sum += meas[i];
    sumsq += 1.0 * meas[i] * 1.0 * meas[i];
  }

  avg = sum / DIM;
  avgsq = sumsq / DIM;

  double sigma = sqrt(avgsq - (avg * avg));

  double avgclean = 0;
  double sumclean = 0;

  int nclean = 0;

  for (int i = 0; i < DIM; i++) {
    if (meas[i] <= (avg*1.1)) {
      sumclean += meas[i];
      nclean ++;
    }
  }

  avgclean = nclean > 0 ? sumclean / nclean : 0.0;

  return int(avgclean);
}


 

void loop() {
  long t = processCleanupData(senseMulti(10)) ;
  Serial.println(t);
  
}
