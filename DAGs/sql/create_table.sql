-- CREATE DATABASE IF NOT EXISTS `city_traffic`;
CREATE TABLE IF NOT EXISTS  'objects' (
   'track_id' INT Primary KEY,
   'type' varchar(20),
   'traveled_d' REAL,
   'avg_speed' REAL,
   'lat' REAL,
   'lon' REAL,
   'speed' REAL, 
   'lon_acc' REAL,
   'lat_acc' REAL,
   'time' REAL,
);