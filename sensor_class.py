class sensor_class:
    
    description = "Values of temperatur og humiditø"
    
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
    def set_temperature(self, measured_val: int):
        self.temperature = measured_val
    def set_humidity(self, measured_val: int):
        self.humidity = measured_val
        
