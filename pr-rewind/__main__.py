import time
import joystick
import lcdDisplay as lcd
import game


def main():
    try:
        lcd.display_init()
        js = joystick.Joystick()
        js.start()

        while True:
            game.char_pos(js.POS)
            game.monitor_button()
            game.msg()
            game.send()    
    except KeyboardInterrupt:
        if js is not None:
            js.stop()
    finally:
        lcd.lcd_cleanup()

if __name__ == "__main__":
    main()