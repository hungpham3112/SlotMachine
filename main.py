from lib import *

"""
-------------------------------------- 
| Authors: Phạm Thế Hưng             |
| Licenses: MIT                      |
| Emails: phamhung20022015@gmail.com |
-------------------------------------- 
"""


def main():
    file = "saved_money.txt"
    if not isempty(file):
        while True:
            user_choice = input(
                f"""
Found ${read_money(file)} from the last play, do you want to continue? (Y)es or (N)o: """
            )
            match user_choice.lower():
                case "y" | "yes":
                    current_money = float(read_money(file))
                    engine(current_money)
                    break
                case "n" | "no":
                    print(instruction())
                    engine()
                    break
                case _:
                    print("Just answer Yes or No")
                    clear()
                    continue
    else:
        engine()


if __name__ == "__main__":
    main()
