class Observer:
    def update(self, data):
        pass

class Subject:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, data):
        for observer in self.observers:
            observer.update(data)

class WeatherStation(Subject):
    def __init__(self):
        super().__init__()
        self.temperature = 0
        self.humidity = 0

    def set_measurements(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
        self.notify((temperature, humidity))

class WeatherDisplay(Observer):
    def update(self, data):
        temperature, humidity = data
        print(f"Temperatura: {temperature}°C, Nishon: {humidity}%")

weather_station = WeatherStation()
weather_display = WeatherDisplay()

weather_station.attach(weather_display)
weather_station.set_measurements(25, 60)
```

Bu kod Observer patterni namoyish etadi. Observer pattern quyidagilardan iborat:

- `Observer` interfeysi: bu interfeysni implement qiluvchi klasslar ma'lumotlarni yangilash uchun `update` metodi orqali `Subject` klassidan ma'lumot oladi.
- `Subject` klassi: bu klass ma'lumotlarni yangilash uchun `attach`, `detach` va `notify` metodlarini taqdim etadi. `attach` metodi observer klassini ro'yxatga qo'shadi, `detach` metodi observer klassini ro'yxatdan olib tashlaydi, `notify` metodi ma'lumotlarni yangilash uchun observer klasslariga murojaat qiladi.
- `WeatherStation` klassi: bu klass `Subject` klassidan meros oladi va ma'lumotlarni yangilash uchun `set_measurements` metodi orqali ma'lumotlarni yangilaydi.
- `WeatherDisplay` klassi: bu klass `Observer` interfeysidan meros oladi va ma'lumotlarni yangilash uchun `update` metodi orqali ma'lumotlarni yangilaydi.
