int buttonPin = 13;
int spaceButtonPin = 10; 

long pressStart = 0;
long lastRelease = 0;

bool buttonPressed = false;
bool lastSpaceState = false;

String currentSymbol = "";

// Letters and numbers
String letters[36] = {
"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
"0","1","2","3","4","5","6","7","8","9"
};

String morse[36] = {
".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-",
"..-","...-",".--","-..-","-.--","--..","-----",".----","..---","...--","....-",".....","-....","--...","---..","----."
};

void setup() {

  pinMode(buttonPin, INPUT_PULLUP);
  pinMode(spaceButtonPin, INPUT_PULLUP);

  Serial.begin(9600);
}

void decodeCharacter() {

  for(int i = 0; i < 36; i++) {
    if(currentSymbol == morse[i]) {
      Serial.print(letters[i]);
      break;
    }
  }

  currentSymbol = "";
}

void loop() {

  bool state = !digitalRead(buttonPin);
  bool spaceState = !digitalRead(spaceButtonPin);

  // BUTTON PRESSED
  if(state && !buttonPressed) {

    buttonPressed = true;
    pressStart = millis();
    delay(20);
  }

  // BUTTON RELEASED
  if(!state && buttonPressed) {

    buttonPressed = false;

    unsigned long pressTime = millis() - pressStart;

    if(pressTime < 250) {
      currentSymbol += ".";
    }
    else {
      currentSymbol += "-";
    }

    lastRelease = millis();
    delay(20);
  }

  // CHECK FOR LETTER GAP
  if(!buttonPressed && currentSymbol != "") {

    unsigned long gap = millis() - lastRelease;

    if(gap > 800) {
      decodeCharacter();
    }
  }

  if (spaceState && !lastSpaceState) { // triggers once when pressed
    if(currentSymbol != "") {
      decodeCharacter();
    }
    Serial.print(" "); // print single space
    delay(20);
  }

  lastSpaceState = spaceState; // update previous state

}
