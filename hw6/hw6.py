from vehicles import parts, Car, CargoShip, Jet

print('-------Car class-------')
car = Car.Car(100, 60,'mazda', 'beep', 10, 250, 1500)
car.provide_sound()
print(car.MODEL)

car.drive(5)
car.drive(3)
car.add_fuel(5000)

car.add_fuel(40)
car.drive(10)
car.drive(5)

car.engine.make_sound()
car.engine = parts.Engine('sport engine')
car.engine.make_sound()

print('\n-------Cargo ship class-------')
ship = CargoShip.CargoShip(10000, 3000, 'Win', 1000)
ship.provide_sound()
print(ship.NAME)
ship.upload(500)
ship.upload(1500)
ship.upload(5000)

ship.sail(2)
ship.sail(3)
ship.add_fuel(15000)
ship.sail(10)

ship.unload(500)
ship.unload(2500)
ship.unload(3000)
ship.upload(100000)

ship.engine.make_sound()
ship.engine = parts.Engine('powerful ship engine')
ship.engine.make_sound()

print('\n-------Jet class-------')
jet = Jet.Jet(5000, 1000, 'jet')
jet.provide_sound()
print(jet.MODEL)

jet.fly(0.5)
jet.fly(1)
jet.add_fuel(50000)
jet.add_fuel(40)
jet.add_fuel(40)

jet.engine.make_sound()
jet.engine = parts.Engine('jet engine')
jet.engine.make_sound()
