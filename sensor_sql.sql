CREATE TABLE IF NOT EXISTS sensor_data ( 
    id INT AUTO_INCREMENT PRIMARY KEY, 
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, 
    temperature REAL, 
    humidity REAL, 
    pressure REAL, 
    moisture REAL );

CREATE TABLE IF NOT EXISTS plant_data(
    plant_name VARCHAR(255) PRIMARY KEY,
    temperature REAL NOT NULL,
    humidity REAL NOT NULL,
    moisture REAL NOT NULL
);