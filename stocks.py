import yfinance as yf
from art import *
import threading

previous = yf.Ticker("NVDA").history(period="1d")["Close"].iloc[-1]
oldprice = 0

def printit():
    global oldprice
    threading.Timer(2.0, printit).start()
    price = yf.Ticker("NVDA").history(period="1d")["Close"].iloc[-1]
    price1 = yf.Ticker("UBI.PA").history(period="1d")["Close"].iloc[-1]
    price2 = yf.Ticker("CHWY").history(period="1d")["Close"].iloc[-1]
    price3 = yf.Ticker("MSFT").history(period="1d")["Close"].iloc[-1]
    price4 = yf.Ticker("SONY").history(period="1d")["Close"].iloc[-1]
    value = ((price - 235.0) * 22) + (price1 - 21.68) + (price2 - 41.29) + (price3 - 267.32) + (price4 - 88.25)
    percents = "NVDA: " + str((price - 235.0) * 22) + "$ UBI.PA: " + str(price1 - 21.68) + "$ CHWY: " + str(price2 -41.29) + "$ MSFT: " + str(price3 - 267.32) + "$ SONY: " + str(price4 - 88.25) + "$"
    print (percents)
    
    if(value > oldprice):
        print("                                                                                                                  ##%&&&          ")
        print("                       /##((/(////(#####%%*                                                                 ./&&&&&@@&&&&         ")
        print("                   #%%###(((((((#%%%%&&%%%%%                                                        .(##%&@&&&&&&&&@@&&&          ")
        print("                 ,@@&%%%###(((((#%%%&&&&%%&%%%(                                                  (###%&&%%&@@&&&@@&&@&%&&         ")
        print("                @@@&&&&&&%%#((/(#%%%%&&%%%%&&&%%                                               ,&&%%%&@&%%&@@%%%&@&&@&%&@         ")
        print("               %@@@@@@@@@&%#(//(#%%%(//##%%&&&&%*                                                ,(((#%&%%%%&&&&&&%%%%%&&         ")
        print("              &&@&&&&&&%%##((//(#%#####((#&%*(*.,                                                    (((%#######%#%%%%%%&&        ")
        print("             ,@&&%%#####((((////(%&&&&&&&%#%##(%&#                                                  /#%####%%%%%&&&%%%%%&&        ")
        print("             ,&%##(((((((((//////##%%%%%%&##%%%#%(                                                .###(#########/(#%%%##&&,       ")
        print("             .#((((//((//////*///(#######%%#%##((                                                *##(((((####%%     ,%%&&,        ")
        print("              /////////********///(####((/*(////,                                              (#%&%##%%%%%%#/                    ")
        print("               //*/*/***********//(#(###/,/##(//                                             (##&%&&%&&&&&%(,                     ")
        print("               ,////****,,,,*****//((#(,,,.,(//                                             ###&&&&(//(/(#                        ")
        print("                **////**,,,,,,,,****/(#%%&&&%,                                            ,%%&&&@@*#@@@..,                        ")
        print("                ///////**,,*,....,,**//(##%%%                 ./@@@.                    .,*/%&&@&@/#@@@.*,...  .,                 ")
        print("                 //((((//*****,,.    .,*(/(         *%@@@@@@ ,@@@@@@@% ,,(@@@@@@@, .*,@@@,@@@@@( %/#@@@..,@@&&  *&@@@@@(          ")
        print("                 ,*(((((/**///***,,.               ,@@@# .     /@@@.   #@@@*  .%@@@ .,@@@%  ,@@@#.*#@@@.&@@&..*#@@&.              ")
        print("                    ./(((//////**,,*/*              .&@@@@@& *(/@@@,,@,@@@% %@#,@@@* ,@@@,*@.@@@%.,#@@@@@@% (@@ (@@@@@@/          ")
        print("      ....             ,(((/(//***##@( ...         .*    %@@# */@@@* . /@@@/ .,&@@& .,@@@, , @@@%.,#@@@./&@@#..*.   ,@@@*         ")
        print(".........                (&%#(//(&&@@( .......,**, ,&@@@@@%*    /&@@@# . (&@@@@&#..%#,&@@, , &@@# *(@@&., %@@@*(@@@@@&(           ")
        print(".......                    (@@&&&%&@@( .......,*/(#%%(*.                        /&&&@&&&&#*                                       ")
        print("                             ,(((((*,% .....  ..,**/((((((/*,                  /%%%%%%%%%&(                                       ")
        print("            .                  ,/(//%* ......    ....,,,,,,,...              *##/((/(((#*                                         ")
        print("             .                   *(#@(  ....       ...  ... ...             /#///%(//#%                                           ")
        print("                       .           //&. .....      .     .. ....          /#(//(%%%%%,                                            ")
        print("                        .            /, .... .     .       .....        *((/(////(#,                                              ")
        print("                        .            /, .... .     .       .....        *((/(////(#,                                              ")
        print("                                         ......    .         ....      #(//((##(##                                                ")
        print(".                           ...  .             .   .                  *(*//(//##                                                  ")

        tprint(f"${value:.2f}" + "/" + "\\",font="varsity")
        

    if(value < oldprice):
        print("            %%%%(%#%%%%/  ,%%##//*/**,                                                                                   ")         
        print("     %%%%%%%%#%   (((////(((#((((/ %/*#                                                                                  ") 
        print("      (%%%%%(   ##((((///(((##((##(%%%/                                                                                  ") 
        print("        %%#&   ##%%##(/*/((/(//(///%%%/*                                                                                 ") 
        print("         .    /(((((///**/((##(((((#%%%*                                                                                 ") 
        print("              //////******/(((((((*#%%%(#                                                                                ") 
        print("               ************//(/*//,/#%#%*#                                                                               ") 
        print("                ****,,,,,,**////(/ ,#####/                                                                               ") 
        print("                 ****,,,....,**/*   /####*% ((##,               .                                                        ") 
        print("                 ,///*****,,.,      .#####(((#####*          &*##*/                                                      ") 
        print("               ,...(//*****,/,       /####(#########/.    /#(####((                                                      ") 
        print("           ,,..,....,%#((**(#,,.      ##########&######../########/                                                      ") 
        print("    .....,.,..........,/****,......., ,#####(%     (#########(#####                                                      ") 
        print("       .....,,,,......./***##,.... ...,.*##(         (######. %#####             #####                                   ") 
        print("    .......  .....,.,..../*(#,.,,,..,....(,            (#                       /$$                       /$$                         /$$                ") 
        print("    .........  ..  ..   ..***,.,,,,,. .....                                    | $$                      | $$                        | $$                ") 
        print("      ....,,*,,... .     ..**,..,,,.       ,              /$$$$$$$   /$$$$$$  /$$$$$$          /$$$$$$$ /$$$$$$    /$$$$$$  /$$$$$$$ | $$   /$$  /$$$$$$$") 
        print("     . .../(####((,.       ,,......    ....,*            | $$__  $$ /$$__  $$|_  $$_/         /$$_____/|_  $$_/   /$$__  $$| $$__  $$| $$  /$$/ /$$_____/") 
        print("     .....,.,(((((/((       . .. .,*(/ .......           | $$  \ $$| $$  \ $$  | $$          |  $$$$$$   | $$    | $$  \ $$| $$  \ $$| $$$$$$/ |  $$$$$$ ") 
        print("     ........,,,**.,,....,,,..,.,..*###(   ...,.         | $$  | $$| $$  | $$  | $$ /$$       \____  $$  | $$ /$$| $$  | $$| $$  | $$| $$_  $$  \____  $$") 
        print("        .  ...... .......,....,,....,//** .   ..         | $$  | $$|  $$$$$$/  |  $$$$/       /$$$$$$$/  |  $$$$/|  $$$$$$/| $$  | $$| $$ \  $$ /$$$$$$$/") 
        print("         . .....  ..  ..  ....           ...   ,,        |__/  |__/ \______/    \___/        |_______/    \___/   \______/ |__/  |__/|__/  \__/|_______/ ") 
        print("            .                                                                               *##((((                      ") 
        print("                                                                                              %#((((                     ") 
        print("                                     .                                                         ###(((#                   ") 
        print("      .....                         .,                                                           %#(((#    #(((          ") 
        print("     ......                          .,                                                           &(((((((((((#          ") 
        print("      ....                           ..,                                                            (((/(//(/(,          ") 
        print("        .                   .       ..                                                           (////////////           ")

        tprint(f"${value:.2f}" + "\\" + "/",font="varsity")
    
        
    
    oldprice = value
    
printit()
