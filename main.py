class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered ore removed.
    def registerObserver(observer):
        pass
    def removeObserver(observer):
        pass
    
    # This method is called to notify all observers
    # when the Subject's state (measurements) has changed.
    def notifyObservers():
        pass
    
# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and 
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass


# WeatherData now implements the subject interface.
class WeatherData(Subject):
    
    def __init__(self):        
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
    
    
    def registerObserver(self, observer):
        # When an observer registers, we just 
        # add it to the end of the list.
        self.observers.append(observer)
        
    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)
    
    def notifyObservers(self):
        # We notify the observers when we get updated measurements 
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)
    
    def measurementsChanged(self):
        self.notifyObservers()
    
    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        
        self.measurementsChanged()
    
    # other WeatherData methods here.


class CurrentConditionsDisplay(Observer):
    
    def __init__(self, weatherData):        
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        
        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer 
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temeprature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()
        
    def display(self):
        print("Current conditions:", self.temerature, 
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)
        
# TODO: implement StatisticsDisplay class and ForecastDisplay class.

class StatisticsDisplay(Observer):
    def __init__(self, weatherData):
        self.temperature_samples = []
        self.humidity_samples = []
        self.pressure_samples = []

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.temperature_samples.append(temperature)
        self.humidity_samples.append(humidity)
        self.pressure_samples.append(pressure)
        self.display()

    def display(self):
        print("Statistics:")
        print("Temperature: min = {}, max = {}, average = {}".format(min(self.temperature_samples), max(self.temperature_samples), sum(self.temperature_samples)/len(self.temperature_samples)))
        print("Humidity: min = {}, max = {}, average = {}".format(min(self.humidity_samples), max(self.humidity_samples), sum(self.humidity_samples)/len(self.humidity_samples)))
        print("Pressure: min = {}, max = {}, average = {}".format(min(self.pressure_samples), max(self.pressure_samples), sum(self.pressure_samples)/len(self.pressure_samples)))
    
    
class ForecastDisplay(Observer):
    def __init__(self, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer so it gets data updates.

    def update(self, temperature, humidity, pressure):
        self.temeprature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        forcast_temp = self.temperature + 0.11 * self.humidity + 0.2 * self.pressure
        forcast_humadity = self.humidity - 0.9 * self.humidity
        forcast_pressure = self.pressure + 0.1 * self.temperature - 0.21 * self.pressure

        print("Forcast:")
        print("Of ", self.temerature, 
              "F degrees and", self.humidity,"[%] humidity",
              "and pressure", self.pressure)
    
class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forcast_display = ForecastDisplay(weather_data)

        # TODO: Create two objects from StatisticsDisplay class and 
        # ForecastDisplay class. Also, register them to the concrete instance
        # of the Subject class so they get the measurements' updates.
        
        # The StatisticsDisplay class should keep track of the min/average/max
        # measurements and display them.
        
        # The ForecastDisplay class shows the weather forecast based on the current
        # temperature, humidity and pressure. Use the following formulas :
        # forcast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        # forcast_humadity = humidity - 0.9 * humidity
        # forcast_pressure = pressure + 0.1 * temperature - 0.21 * pressure

        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)

        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100,1000)
    
        


if __name__ == "__main__":
    w = WeatherStation()
    w.main()

