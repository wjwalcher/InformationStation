#include <Adafruit_GFX.h>   
#include <RGBmatrixPanel.h> 

// Similar to F(), but for PROGMEM string pointers rather than literals
#define F2(progmem_ptr) (const __FlashStringHelper *)progmem_ptr

#define CLK 8  // MUST be on PORTB! (Use pin 11 on Mega)
#define LAT A3
#define OE  9
#define A   A0
#define B   A1
#define C   A2

RGBmatrixPanel matrix(A, B, C, CLK, LAT, OE, true);

void setup() {
  matrix.begin();
  matrix.setTextWrap(false); 
  matrix.setTextSize(2);
}

void loop() {
  const char str[] PROGMEM =  ;
  int    textX   = matrix.width(),
  textMin = sizeof(str) * -30,
  hue     = 0;
  // Clear background
  matrix.fillScreen(0);
  // Draw big scrolly text on top
  matrix.setTextColor(matrix.ColorHSV(hue, 255, 255, true));
  matrix.setCursor(textX, 1);
  matrix.print(F2(str));

  // Move text left (w/wrap), increase hue
  if((--textX) < textMin) textX = matrix.width();
  hue += 20;
  if(hue >= 1536) hue -= 1536;

  matrix.swapBuffers(true);
}
