"""
MENU.PY

"""

def get_option():
    option = 1
    while True:
        try:
            print("""
                    1. Sales per client report.
                    2. Top sold products report.
                    3. Total sales report.
                    4. Export report.
                    5. Exit.
                """)
            option = int(input("Please, enter the option's number: "))
            if (option > 0 and option < 6):
                break
        except ValueError:
            print("Please, enter a valid option: ")
    
    return option


    
