# Lloyds Banking Group: Net Zero Challenge 
Bright Network Virtual Intership - *July 2023*

The following repository is a prototype/solution for Lloyds Banking Group's Net Zero Carbon Emission Challenge. The program was organized by Bright Network and hosted by Lloyds Banking Group. The certification of completion can be found *[here](https://www.brightnetwork.co.uk/certificates/bright-network-ieuk-2023-on-de_kzw8daplahp6iy/)*.

## Requirements & Configurations
To run the program Python 3.1 or higher, Thonny IDE and the following hardware components are required: Raspberry Pi Pico W (RPI), BME280, Soil Moisture Sensor, Breadboard and Male to Male Cables.

### Hardware Setup
The hardware setup can be found *[here](https://github.com/FredAlcantara/IEUK-Intership-Experience/blob/main/documents/Presentation.pptx)*. ***Save the following file as raw format to see the contents.***
After setting up the device, open thonny and import `sensor.py` into the mirco-controller. This can be accomplished by creating a new file and saving it within the device. 

### Libraries
To run the program the necessary libraries will need to be installed.
Web Application: `flask` & `MySQL`.
Thonny IDE: `I2C`, `Pin`, `ADC`, `BME280`, `urequest`, `ujson` & `utime`.

### Database 
XMAPP will be required to access your local database. You can download XAMPP from the following *[link](https://www.apachefriends.org/download.html)* if have not done already. 
Open XMAPP and active Apach and MySQL. Afterwards download the SQL file found *[here](https://github.com/FredAlcantara/IEUK-Intership-Experience/blob/main/sensor_sql.sql)* and import it in your local database within the import tab.

**NOTE: The following code below will need to be amended the user's credentials to establish a connection with the users local database. This code can be found in `config.py`** 
> HOST = os.getenv('DATABASE_HOST')
> 
> DATABASE = os.getenv('DATABASE_NAME')
> 
> USER = os.getenv('DATABASE_USER')
> 
> PASSWORD = os.getenv('DATABASE_PASSWORD')

## Execution 
Any IDE can be used to run the program, however, Thonny is necessary for the micro-controller(RPI) as it contains built-in libraries which can be found within the manage packages.
Once everything is ready and setup, run the device in Thonny and it should automatically start sending data in your local database.
Afterwards run `app.py` by simply typing `py app.py` or `python app.py` within your terminal/console. An address should appear within your terminal/console and , and upon accessing it, a web page should be presented showcasing your recorded data.
**NOTE: Make sure the soil sensor is placed deep enough where reading can be collected.**

## Purpose 
In our current society, we enjoy the convenience of having almost everything accessible, including the delivery of groceries such as vegetables and fruits. However, this convenience also has a negative impact on the environment, mainly due to transportation emissions and excessive packaging. Utilising the system created promotes sustainable agriculture practices and the reduction of carbon emissions.
