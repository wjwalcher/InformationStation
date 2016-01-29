
#include <Adafruit_GFX.h>   
#include <RGBmatrixPanel.h> 
#include <ArrayList.h>
// Similar to F(), but for PROGMEM string pointers rather than literals
#define F2(progmem_ptr) (const __FlashStringHelper *)progmem_ptr

#define CLK 8  // MUST be on PORTB! (Use pin 11 on Mega)
#define LAT A3
#define OE  9
#define A   A0
#define B   A1
#define C   A2

RGBmatrixPanel matrix(A, B, C, CLK, LAT, OE, true);

ArrayList *list = new ArrayList("Starting");
int    textX   = matrix.width(),
       textMin = sizeof(list) * -12,
       hue     = 0;


void setup() {
  matrix.begin();
  matrix.setTextWrap(false); 
  matrix.setTextSize(2);
}


void loop() {
  if(Serial.available()){ // only send data back if data has been sent
    char inByte = Serial.read(); // read the incoming data
    list->remove_selected_item(1);
    list->add_string_item(inByte);
  }
  // Clear background
  matrix.fillScreen(0);
  // Draw big scrolly text on top
  matrix.setTextColor(matrix.ColorHSV(hue, 255, 255, true));
  matrix.setCursor(textX, 1);
  matrix.print(F2(list));

  // Move text left (w/wrap), increase hue
  if((--textX) < textMin) textX = matrix.width();
  hue += 20;
  if(hue >= 1536) hue -= 1536;

  matrix.swapBuffers(true);
}
