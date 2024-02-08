# Lloyds Banking Group: Net Zero Challenge 
Bright Network Virtual Intership - *July 2023*

The following repo is a prototype/solution to Lloyds Banking Group's Net Zero Carbon emission challenge. The following program was organised by Bright Network and hosted by Lloyds Banking Group.
The certification of completion can be found *[here](https://www.brightnetwork.co.uk/certificates/bright-network-ieuk-2023-on-de_kzw8daplahp6iy/)*.

## Requirements & Configurations
To run the program Python 3.1 or higher, Thonny IDE and the following hardware components are required: Raspberry Pi Pico W, BME280, Soil Moisture Sensor, Breadboard and Male to Male Cables.

### Hardware Setup
Hardware setup can be found *[here](https://github.com/FredAlcantara/IEUK-Intership-Experience/blob/main/documents/Presentation.pptx)*. ***Save the following file as raw format to see the contents.***

### Libraries
To run the program the necessary libraries will need to be installed.
Web Application: `flask` & `MySQL`.
Thonny IDE: `I2C`, `Pin`, `ADC`, `BME280`, `urequest`, `ujson` & `utime`.

### Database 
XMAPP will be required to access your local database, the following *[link](https://www.apachefriends.org/download.html)* is the site where to download XMAPP if have not done so. 
Open XMAPP and active Apach and MySQL, afterwards download the SQL file found *[here](https://github.com/FredAlcantara/IEUK-Intership-Experience/blob/main/sensor_sql.sql)* and import it in your local database within the import tab.

