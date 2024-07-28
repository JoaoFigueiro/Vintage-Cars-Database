import json
import requests


h_content = {'Content-Type': 'application/json'}

URL = 'http://localhost:3000/'
CARS_URL = URL + 'cars/'

def check_server(cid=None)->bool:
    """
    when invoked without arguments simply checks if server responds;
    invoked with car ID checks if the ID is present in the database;
    """   
    url = URL + cid if cid else URL 

    reply = requests.head(url) 

    return True if reply.status_code == requests.codes.ok else False   


def print_menu():
    """
    prints user menu - nothing else happens here;
    """
    print("+", "-" * 35, "+")
    print("|", "Vintage Cars Database".center(35), "|")
    print("+", "-" * 35, "+")
    print("M E N U")
    print("=" * 7)
    print("1. List cars")
    print("2. Add new car")
    print("3. Delete car")
    print("4. Update car")
    print("0. Exit")


def read_user_choice():
    """
    reads user choice and checks if it's valid;
    returns '0', '1', '2', '3' or '4' 
    """

    valid_choices = ['0', '1', '2', '3', '4']
    user_choice = input("Enter your choice (0..4): ")

    while user_choice not in valid_choices:
        user_choice = input("Enter your choice (0..4): ")

    return user_choice


def print_header():
    """
    prints elegant cars table header;
    """
    width = 20
    
    header_columns = ["id", "brand", "model", "production_year", "convertible"]
    header_columns = [column.ljust(width) for column in header_columns]

    header = "| ".join(header_columns)

    print(header)


def print_car(car):
    """
    prints one car's data in a way that fits the header;
    """
    print(
        str(car.get("id")).ljust(20),
        car.get("brand").ljust(20),
        car.get("model").ljust(20),
        str(car.get("production_year")).ljust(20),
        str(car.get("convertible")).ljust(20), 
        sep='| '
    ) 


def list_cars():
    """
    gets all cars' data from server and prints it;
    if the database is empty prints diagnostic message instead;
    """    
    cars = requests.get(CARS_URL)
    cars = cars.content.decode("utf-8")
    cars = json.loads(cars)

    if not cars: 
        print("*** Database is empty ***")
        return 
    
    print_header()

    for car in cars: 
        print_car(car) 
            

def name_is_valid(name: str)->bool:
    """
    checks if name (brand or model) is valid;
    valid name is non-empty string containing
    digits, letters and spaces;
    returns: True or False;
    """    
    if name.isascii():
        return True 
    else: 
        print(f"The name must containing only digits, letters and spaces!") 
        return False 
    

def enter_id():
    """
    allows user to enter car's ID and checks if it's valid;
    valid ID consists of digits only;
    returns int or None (if user enters an empty line);
    """
    car_id = input("Car ID (empty string to exit): ")
        
    if car_id.isspace(): 
        return 
    
    if not car_id.isdigit(): 
        print("Car ID must only contains digits!")
        return 
    
    try: 
        car_id = int(car_id)
    except TypeError: 
        print("Car ID must be an Integer!")
    else: 
        return car_id
        

def enter_production_year():
    """
    allows user to enter car's production year and checks if it's valid;
    valid production year is an int from range 1900..2000;
    returns int or None  (if user enters an empty line);
    """
    car_production_year = input("Car production year (empty string to exit): ")

    if car_production_year.isspace(): 
        return 

    try: 
        car_production_year = int(car_production_year)

        assert 1900 <= car_production_year
        assert 2000 >= car_production_year
    
    except TypeError: 
        print("Car production year must be an integer!")

    except AssertionError: 
        print(
            """ 
            Car production year must be greater than or equal to 
            1900 or less than or equal to 2000.
            """
        )            
    else: 
        return car_production_year

    enter_production_year()
      

def enter_name(what: str):
    """
    allows user to enter car's name (brand or model) and checks if it's valid;
    uses name_is_valid() to check the entered name;
    returns string or None  (if user enters an empty line);
    
    :argument what: describes which of two names is entered currently 
    ('brand' or 'model');    
    """
    if what == "brand": 
        name = input("Car brand (empty string to exit): ")
    elif what == "model": 
        name = input("Car model (empty string to exit): ")

    if name.isspace(): 
        return 
    
    while not name_is_valid(name): 
        enter_name(what)
    
    return name 


def enter_convertible()->bool:
    """
    allows user to enter Yes/No answer determining if the car is convertible;
    returns True, False or None  (if user enters an empty line);
    """
    input_message = "Is this car convertible? [y/n] (empty string to exit): "
    
    is_convertible = input(input_message)

    if is_convertible.isspace(): 
        return 
    elif is_convertible.lower() == 'y':
        return True
    elif is_convertible.lower() == 'n':
        return False
    else: 
        print("Value must be 'y' or 'n' or an empty line to exit!")
        enter_convertible()
   

def delete_car():
    """
    asks user for car's ID and tries to delete it from database;
    """

    car_id = enter_id()

    if not car_id: 
        return 

    delete_url = CARS_URL + str(car_id)

    try: 
        response = requests.delete(url=delete_url)
    except Exception as e: 
        print(f"An excpetion has occurred! {e}")

    if response.status_code == requests.codes.ok: 
        print(f"Car ID: {car_id} deleted with success!")
    else: 
        print(f"Status Code: {response.status_code}")


def input_car_data(with_id: bool):
    """
    lets user enter car data;
    argument determines if the car's ID is entered (True) or not (False);
    returns None if user cancels the operation or a dictionary of the 
    following structure:
    {
        'id': int, 
        'brand': str, 
        'model': str, 
        'production_year': int, 
        'convertible': bool 
    }
    """
    car_id = enter_id() if with_id else None
    
    car_brand = enter_name("brand") 
    if not car_brand: 
        return 
    
    car_model = enter_name("model")
    if not car_model: 
        return 
    
    production_year = enter_production_year()
    if not production_year: 
        return 
    
    is_convertible = enter_convertible()
    if is_convertible is None: 
        return 
    
    car_data = {
        "brand": car_brand, 
        "model": car_model, 
        "production_year": production_year, 
        "convertible": is_convertible 
    } 

    if car_id:  
        car_data["id"] = str(car_id) 

    return car_data


def add_car():
    """
    invokes input_car_data(True) to gather car's info and adds it to the database;
    """
    car_data = input_car_data(True)

    if not car_data: 
        return 
    
    car_id = car_data.get("id")
    
    try: 
        response = requests.post(
            url=CARS_URL, 
            headers=h_content, 
            data=json.dumps(car_data)
        )
    except Exception as e: 
        print(f"An exception has occurred! {e}")

    if response.status_code == requests.codes.created: 
        print(f"Car ID: {car_id} inserted successfully!")


def update_car():
    """
    invokes enter_id() to get car's ID if the ID is present in the database;
    invokes input_car_data(False) to gather new car's info and updates the database;
    """
    car_id = enter_id()

    if not car_id: 
        return 
    
    car_data = input_car_data(False)

    if not car_data: 
        return 
    
    update_url = CARS_URL + str(car_id)

    try: 
        response = requests.put(
            url=update_url, 
            headers=h_content, 
            data=json.dumps(car_data)
        )
    except Exception as e: 
        print(f"An exception has occurred! {e}")

    if response.status_code == requests.codes.ok: 
        print(f"Car ID: {car_id} updated successfully!")    


while True:
    if not check_server():
        print("Server is not responding - quitting!")
        exit(1)
    print_menu()
    choice = read_user_choice()
    if choice == '0':
        print("Bye!")
        exit(0)
    elif choice == '1':
        list_cars()
    elif choice == '2':
        add_car()
    elif choice == '3':
        delete_car()
    elif choice == '4':
        update_car()
