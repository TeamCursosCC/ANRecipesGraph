APP_NAME = "Recipes Engine"

function_list = []

def print_menu():
    if not function_list:
        print("Menu no configurado")
        return
    
    print("Menu")
    
    i = 0
    for f in function_list:
        i += 1
        f_doc = f.__doc__
        if f_doc:
            f_description = f_doc.split("\n")[0]
            print(f"\t{i}. {f_description}")
        else:
            print(f"\t{i}. {f.__name__}")
            pass
        pass
    print(f"\t0. Exit")
    pass
    
def add_menu_option(fn:callable, label:str = ""):
    if label:
        fn.__doc__ = label
    if not fn.__doc__:
        count = len(function_list) if function_list else 1
        fn.__doc__ = f"Opt_{count}"
    function_list.append(fn)
    pass

def main_loop():
    while True:
        print(f"\n\t<<<  {APP_NAME}  >>>\n")
        print_menu()
        choice = int(input("Enter your choice: "))
        if choice in range(1, len(function_list)+1):
            function_list[choice-1]()
        elif choice == 0:
            print("Bye")
            break
        else:
            print("Invalid choice, please try again.")
        print("\n")
        pass
    pass
        

if __name__ == "__main__":
    main_loop()