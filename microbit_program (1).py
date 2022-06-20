#random project showing the techniques displayed by clicking the button a
#by sara ajamia (saajam)



from microbit import*
import music

while True:
    if button_a.is_pressed():
        music.play(music.CHASE)
        sleep(2000)
        display.scroll(Image.SKULL)
    
        
        
        
