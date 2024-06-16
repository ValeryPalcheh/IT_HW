import os
import time

   
digits = {
    "0": [
        "🔲🔲🔲🔲",
        "🔲    🔲",
        "🔲    🔲",
        "🔲    🔲",
        "🔲🔲🔲🔲",
    ],
    "1": [
        "  🔲🔲  ",
        "🔲🔲🔲  ",
        "  🔲🔲  ",
        "  🔲🔲  ",
        "🔲🔲🔲🔲",
    ],
    "2": [
        "🔲🔲🔲🔲",
        "      🔲",
        "🔲🔲🔲🔲",
        "🔲      ",
        "🔲🔲🔲🔲",
    ],
    "3": [
        "🔲🔲🔲🔲",
        "      🔲",
        "  🔲🔲🔲",
        "      🔲",
        "🔲🔲🔲🔲",
    ],
    "4": [
        "🔲    🔲",
        "🔲    🔲",
        "🔲🔲🔲🔲",
        "      🔲",
        "      🔲",
    ],
    "5": [
        "🔲🔲🔲🔲",
        "🔲      ",
        "🔲🔲🔲🔲",
        "      🔲",
        "🔲🔲🔲🔲",
    ],
    "6": [
        "🔲🔲🔲🔲",
        "🔲      ",
        "🔲🔲🔲🔲",
        "🔲    🔲",
        "🔲🔲🔲🔲",
    ],
    "7": [
        "🔲🔲🔲🔲",
        "      🔲",
        "    🔲  ",
        "  🔲    ",
        "  🔲    ",
    ],
    "8": [
        "🔲🔲🔲🔲",
        "🔲    🔲",
        "🔲🔲🔲🔲",
        "🔲    🔲",
        "🔲🔲🔲🔲",
    ],
    "9": [
        "🔲🔲🔲🔲",
        "🔲    🔲",
        "🔲🔲🔲🔲",
        "      🔲",
        "🔲🔲🔲🔲",
    ],
    ":": [
        "  ",
        "🔲",
        "  ",
        "🔲",
        "  ",
    ]
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    
    current_time = time.strftime("%H:%M:%S")
    
    display_time = []
    for i in range(5):
        line = ""
        for digit in current_time:
            line += digits[digit][i] + "  "
        display_time.append(line)    
 
    for line in display_time:
        print(line)
    
    time.sleep(1)
    
