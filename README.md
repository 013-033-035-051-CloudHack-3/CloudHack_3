# CloudHack_3

## Team Details:

1) Abhijith S - PES1UG19CS013
2) Aditya Ramesh - PES1UG19CS033
3) Advit Gandhi - PES1UG19CS035
4) Amar Prakash Patil - PES1UG19CS051

## Problem Statement 3 - Breaking Down A Monolith

An arithmetic operations calculator enclosed in a monolithic architecture was provided, with the primary goal of converting it to a microservices-oriented architecture.

## Requirements

python <br>
docker <br>
flask <br>
flask-restful <br>
requests <br>

## Tasks

### Task 0 : Completing the Code

requirements.txt was completed with all required modules

Dockerfile for the landing-service was created, in which the requirements will be installed and the flask application (app.py) will be started

### Task 1 : Debugging

The inputs coming in were of String type by default, so these were converted to floating-point so as to handle a larger range of numbers in performing the arithmetic operations

By default no values were provided by index.html, causing the app to crash when localhost:5050 was loaded initially. Default values were used, and NoneType and ValueError exceptions were handled gracefully.

### Task 2 : Breaking the Monolith Architecture

Four arithmetic operations were initially residing under landing-service. To convert it into a microservices-oriented architecture, separate flask applications were created for each operation.

Each application consists of a class, and a GET method was defined for each class with two numbers as parameters.

The classes were added as a resource using add_resource function and an API endpoint was defined for each, with a different port.

Any reference to localhost was replaced by host.docker.internal, so the application does not require a static IP address. When run on any system, the calculator can be viewed at localhost:5050

Docker-compose file updated to recognise the newly added Flask applications as separate services, with unique port numbers and network aliases defined for each service.

3 more services (GCD, LCM and Exponent) were added to enhance the calculator

## Steps to Run :

Go to the microservices directory <br>
Execute the command **docker-compose build** <br>
Then execute **docker-compose run** <br>
Go to the web browser and open **localhost:5050** to access the landing page <br>
<br>
Choose any 2 numbers and an arithmetic operation and click submit, after which the result will be displayed on the same page <br>
Internally, the landing-page communicates with all the arithmetic operations flask apps via REST APIs which can also be accessed via the following URLs (num1 and num2 refer to any valid number): <br>
<br>
Addition : localhost:5051/num1/num2 <br>
Subtraction : localhost:5052/num1/num2 <br>
Multiplication : localhost:5053/num1/num2 <br>
Division : localhost:5054/num1/num2 <br>
GCD : localhost:5055/num1/num2 <br>
LCM : localhost:5056/num1/num2 <br>
Exponent : localhost:5057/num1/num2 <br>
