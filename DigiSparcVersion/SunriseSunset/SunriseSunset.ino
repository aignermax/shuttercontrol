#include "TimeLord.h"
#include <TinyWireM.h>                  // I2C Master lib for ATTinys which use USI - comment this out to use with standard arduinos
#include <LiquidCrystal_I2C.h>          // for LCD w/ GPIO MODIFIED for the ATtiny85
#include <TinyRTClib.h>

RTC_DS1307 RTC;
#define GPIO_ADDR     0x27             // (PCA8574A A0-A2 @5V) typ. A0-A3 Gnd 0x20 / 0x38 for A - 0x27 is the address of the Digispark LCD modules.


LiquidCrystal_I2C lcd(GPIO_ADDR,16,2);  // set address & 16 chars / 2 lines

// Example by Nick Gammon
// http://forum.arduino.cc/index.php?topic=129249.msg972860#msg972860

// what is our longitude (west values negative) and latitude (south values negative)
float const LONGITUDE = 145.00;
float const LATITUDE = -37.00;

void setup()
  {
    // RTC einstellen
    TinyWireM.begin(); // initialize I2C lib - comment this out to use with standard arduinos
    RTC.begin();
  
    if (! RTC.isrunning()) {
      RTC.adjust(DateTime(__DATE__, __TIME__));    // following line sets the RTC to the date & time this sketch was compiled only for the first run
    }
    
    TimeLord tardis; 
    tardis.TimeZone(10 * 60); // tell TimeLord what timezone your RTC is synchronized to. You can ignore DST
    // as long as the RTC never changes back and forth between DST and non-DST
    tardis.Position(LATITUDE, LONGITUDE); // tell TimeLord where in the world we are
    
    byte today[] = {  0, 0, 12, 11, 2, 2017    }; // store today's date (at noon) in an array for TimeLord to use
  
     if (tardis.SunRise(today)) // if the sun will rise today (it might not, in the [ant]arctic)
     {
      // hour is (int) today[tl_hour] 
      // Minute: (int) today[tl_minute]
      
     }
     
     if (tardis.SunSet(today)) // if the sun will set today (it might not, in the [ant]arctic)
     {
      
     }
     
  }
  
void loop() 
  {
  }
