
CREATE TABLE IF NOT EXISTS  'objects' (
   'track_id' INT Primary KEY,
   'type1' varchar(20),
   'traveled_d' REAL,
   'avg_speed' REAL,
   'lat' REAL,
   'lon' REAL,
   'speed' REAL, 
   'lon_acc' REAL,
   'lat_acc' REAL,
   'time1' REAL,
);