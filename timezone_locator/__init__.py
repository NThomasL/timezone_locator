import os
import fiona


#Get relative path to this location
def get_path(*paths):
    here = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(here, *paths)

#tz_world.shp location
geodata_file_path = get_path('geodata/tz_world.shp')

#Get timezone from coordinates
def get_timezone(lon, lat):
    try:
        #Convert to float if not already
        if type(lon) or type(lat) is not float:
            lon = float(lon)
            lat = float(lat) 
        # Register format drivers with a context manager
        with fiona.drivers():
            # Open the geodata source file (.shp)
            with fiona.open(geodata_file_path) as source:
                res = source.items(bbox=(lon, lat, lon, lat))
                for r in res:
                    #return name of timezone
                    return r[1]['properties']['TZID']
    except Exception as e:
        #TODO# Log error with logger
        print(e)
        return False

#Get all unique timezones in a list
def get_all_timezones():
    try:
        all_timezones = []
        # Register format drivers with a context manager
        with fiona.drivers():
            # Open the geodata source file (.shp)
            with fiona.open(geodata_file_path) as source:
                for s in source:
                    #Make check to avoid duplicates in list
                    if s['properties']['TZID'] not in all_timezones:
                        all_timezones.append(s['properties']['TZID'])
                        
                return all_timezones

    except Exception as e:
        #TODO# Log error with logger
        print(e)
        return False