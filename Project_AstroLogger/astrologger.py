#astrologer.py
import datetime
import json
from pathlib import Path

# ------------------------------------------------
# PARENT CELESTIAL OBJECT CLASS
# ------------------------------------------------
class CelestialObject:
    def __init__(self,name: str, ra: str, dec: str):
        self.name=name
        self.ra=ra
        self.dec=dec
        self.observed_date=datetime.datetime.now().isoformat()

    def display(self):
        print(f"----{self.name}----")
        print(f"    RA:{self.ra}")
        print(f"    DEC:{self.dec}")
        print(f"    Observed Date: {self.observed_date}")

    def to_dict(self):
        data = self.__dict__
        data['obj_type'] = self.__class__.__name__ # This adds the class name
        return data
    

# ------------------------------------------------
# CHILD CLASSES
# ------------------------------------------------

class Star(CelestialObject):
    def __init__(self, name: str, ra: str, dec: str, stellar_type: str, magnitude: float):
        super().__init__(name, ra, dec)
        self.stellar_type=stellar_type
        self.magnitude=magnitude

    def display(self):
        super().display()
        print(f"    Type: Star({self.stellar_type})")
        print(f"    Magnitude:{self.magnitude}")


class Galaxy(CelestialObject):
    def __init__(self, name: str, ra: str, dec: str, galaxy_type: str, distance_ly: float):
        super().__init__(name, ra, dec)
        self.galaxy_type = galaxy_type
        self.distance_ly = distance_ly

    def display(self):
        super().display()
        print(f"    Type: Galaxy ({self.galaxy_type})")
        print(f"    Distance (ly): {self.distance_ly}")
    

class Moon(CelestialObject):
    def __init__(self, name: str, ra: str, dec: str, host_planet: str):
        super().__init__(name, ra, dec)
        self.host_planet = host_planet

    def display(self):
        super().display()
        print(f"    Host Planet: ({self.host_planet})")
    

class Asteroid(CelestialObject):
    def __init__(self, name: str, ra: str, dec: str, composition: str, diameter_km: float):
        super().__init__(name, ra, dec)
        self.composition = composition
        self.diameter_km = diameter_km

    def display(self):
        super().display()
        print(f"    Composition: ({self.composition})")
        print(f"    Diameter (km): {self.diameter_km}")
    
class Comet(CelestialObject):
    def __init__(self, name: str, ra: str, dec: str, last_seen_date: str):
        super().__init__(name, ra, dec)
        self.last_seen_date = last_seen_date

    def display(self):
        super().display()
        print(f"    Last Seen Date: ({self.last_seen_date})")

class Nebula(CelestialObject):
    def __init__(self, name, ra, dec, nebula_type:str):
        super().__init__(name, ra, dec)
        self.nebula_type=nebula_type
    
    def display(self):
        super().display()
        print(f"    Nebula Type: {self.nebula_type}")

class Planet(CelestialObject):
    def __init__(self, name, ra, dec, host_star:str, orbital_period_days:float):
        super().__init__(name, ra, dec)
        self.host_star=host_star
        self.orbital_period_days=orbital_period_days

    def display(self):
        super().display()
        print(f"    Host Star: {self.host_star}")
        print(f"    Orbital Period Days: {self.orbital_period_days}")

class DwarfPlanet(CelestialObject):
    def __init__(self, name, ra, dec, host_star:str):
        super().__init__(name, ra, dec)
        self.host_star=host_star

    def display(self):
        super().display()
        print(f"    Host Star: {self.host_star}")
    

class BlackHole(CelestialObject):
    def __init__(self, name, ra, dec, mass_solar_masses: float):
        super().__init__(name, ra, dec)
        self.mass_solar_masses=mass_solar_masses
    
    def display(self):
        super().display()
        print(f"    Mass in Solar Masses: {self.mass_solar_masses}")

class Quasar(CelestialObject):
    def __init__(self, name, ra, dec, redshift:float):
        super().__init__(name, ra, dec)
        self.redshift=redshift
    
    def display(self):
        super().display()
        print(f"    Redshift: {self.redshift}")


# ------------------------------------------------
# LOGMANAGER CLASSES
# ------------------------------------------------

class LogManager:
    def __init__(self, log_file:str):
        self.log_file=log_file
        self.observations=[]
        
    def add_observation(self, obj):
        self.observations.append(obj)
        print(f"'{obj.name}' ready to be logged.")

    def save_log(self):
        # This part you did correctly
        data_to_save = [i.to_dict() for i in self.observations]
    
        # This is the missing part
        with open(self.log_file, 'w') as file_handle:
            json.dump(data_to_save, file_handle, indent=2)
    
        print(f"Log saved to {self.log_file}")



if __name__ == "__main__":
    # --- THIS IS THE FIX ---
    # Get the directory where this script is located
    script_dir = Path(__file__).parent
    # Create a full path to the log file in that same directory
    log_file_path = script_dir / "observations.json"
    
    # Now, create the manager with the full, reliable path
    manager = LogManager(log_file_path)
    # --- END OF FIX ---

    # 2. Create a few different celestial objects
    kepler186f = Planet(
        name="Kepler-186f",
        ra="19h 54m 36s",
        dec="+43° 57' 18\"",
        host_star="Kepler-186",
        orbital_period_days=130
    )

    quasar_3c273 = Quasar(
        name="3C 273",
        ra="12h 29m 06s",
        dec="+02° 03' 08\"",
        redshift=0.158
    )
    
    crab_nebula = Nebula(
        name="Crab Nebula",
        ra="05h 34m 31s",
        dec="+22° 00' 52\"",
        nebula_type="Supernova Remnant"
    )

    # 3. Add the objects to the manager's list
    manager.add_observation(kepler186f)
    manager.add_observation(quasar_3c273)
    manager.add_observation(crab_nebula)

    # 4. Save the entire log to the JSON file
    manager.save_log()

    print("--- Test Run Complete. Check observations.json ---")
    