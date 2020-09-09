## Joanne Lauer
## Icon Project

## This program will use looping and basic data structions to
## to display an icon in various scales and orientations.



orig_icon = [[0,0,0,0,0,0,0,0,0,0],[0,0,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,0,1,0,],
        [0,0,1,1,1,1,1,0,1,0,],[0,0,1,1,1,1,1,1,1,0],[0,0,1,1,1,1,1,0,0,0],
        [0,0,1,1,1,1,1,0,0,0],[0,0,1,1,1,1,1,0,0,0],[0,0,0,0,0,0,0,0,0,0],
        [0,1,1,1,1,1,1,1,0,0]]

def displayIcon(): 
    for lines in orig_icon:
        for pos in lines:
            if pos == 0:
                print(' ', end='')
            else:   
                print('#', end='')
        print('\r')
        
def displayLargerIcon():
    times = 2 
    for lines in orig_icon:
        for repeat in range(0,times):
            for pos in lines:
                if pos == 0:
                    print(' '*times, end='')
                else:   
                    print('#'*times, end='')              
            print('\r')
            
def displayInvertedIcon():
    for lines in orig_icon:
        for pos in lines:
            if pos == 0:
                print('#', end='')
            else:   
                print(' ', end='')
        print('\r')

def displayReverseIcon():
    for lines in reversed(orig_icon):
        for pos in reversed(lines):
            if pos == 0:
                print(' ', end='')
            else:
                print('#', end='')
        print('\r')          

def main():
    displayIcon()
    displayLargerIcon()
    displayInvertedIcon()
    displayReverseIcon()
    
main()    

