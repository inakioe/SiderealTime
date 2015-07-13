##-------------------------------------------------------------------------
## Sidereal Time
##-------------------------------------------------------------------------
# Author: Inaki Ordonez-Etxeberria
#
# Return the Sidereal Time (in hours) from Latitude and Longitude of the observatory, and date of observation. If the parameters are empty, the function assumes the position of the Isaac Newton Telescope in La Palma, at the moment of execution of the function. 

def SiderealTime(lat = '28.775867', lon = '-17.89733', date = 'now'):
    observatory = ephem.Observer()
    observatory.lon = lon
    observatory.lat = lat
    observatory.elevation = 2328
    if date  ==  'now':
        observatory.date = ephem.now()
    else:
        observatory.date = ephem.Date(date)
    return degrees(observatory.sidereal_time()) / 15
