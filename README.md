## Vintage-Cars-Database

# Requirements 

First of all, we need to have Node.js installed on our computer. Then, follow these steps on your command line interface:
1. `npm install -g json-server`
2. `json-server --watch files/cars.json` -- the json file available in this repository, on folder "files".

Ps. If you're using PowerShell you might run this command before the second step: `fnm env --use-on-cd | Out-String | Invoke-Expression`.

After these steps, you just need to run the `vintage_cars_database.py`.

# Objectives

Learn how to:

* use the requests module facilities;
* build large software solutions using top-down tactics;
* cooperate with a remote database using REST.

# Scenario

Your client has asked if you are able to write and deploy a software solution managing a small database that gathers data about vintage cars. Of course you are! It's a piece of cake for a programmer like you.

To be honest, all the blocks needed to construct such an application are already at your fingertips. Your task is to integrate them into one cooperating product.

Of course, you have to be more careful than us — our examples don’t need to be aware of some fatal events, but your product does.

We've provided the skeleton of the application in the editor. You don't have to follow the exact same trail as we suggest, but we’re convinced that it may help you to master the whole code, and to implement it in a number of small steps.

Don't forget to keep the server running when you start to run and debug your code!

Look carefully at the following terminal session — it will help you guess your client's needs. Of course, you can do it better and solve some issues in a smarter way than we have — feel free to experiment, but don’t lose sight of user satisfaction. This is the most valuable criteria of software usability.

```
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 1
*** Database is empty ***
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 2
Car ID (empty string to exit): 1
Car brand (empty string to exit): Porsche
Car model (empty string to exit): 911
Car production year (empty string to exit): 1963
Is this car convertible? [y/n] (empty string to exit): n
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 2
Car ID (empty string to exit): 2
Car brand (empty string to exit): Ford
Car model (empty string to exit): Mustang
Car production year (empty string to exit): 1972
Is this car convertible? [y/n] (empty string to exit): y
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 1
id        | brand          | model     | production_year     | convertible    | 
1         | Porsche        | 911       | 1963                | False          | 
2         | Ford           | Mustang   | 1972                | True           | 

+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4):  4
Car ID (empty string to exit): 2
Car brand (empty string to exit): Ford
Car model (empty string to exit): Mustang
Car production year (empty string to exit): 1973
Is this car convertible? [y/n] (empty string to exit): n
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 3
Car ID (empty string to exit): 1
Success!
Car ID (empty string to exit): 
+-----------------------------------+
|       Vintage Cars Database       |
+-----------------------------------+
M E N U
=======
1. List cars
2. Add new car
3. Delete car
4. Update car
0. Exit
Enter your choice (0..4): 0
Bye!
```
