# from decorator import decorator
from math import pi
from math import cos


class Point:
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def dictmake(self):
        return {'lat': self.lat, 'long': self.long}

    def __repr__(self):
        return f'Point (lat={self.lat}), (long={self.long})'


class PolygonInput():

    def __init__(self, total_points):
        self.validate_total_points(total_points)
        self.totalPoints = total_points
        self.validPoints = []
        self.completed = False

    def validate_total_points(self, total_points):
        if type(total_points) is not int:
            raise ValueError('Error: Total points must be an integer.')
        if total_points < 3:
            raise ValueError('Error: There are less points than the needed, please correct!')

    def is_completed(self):
        if self.completed:
            raise ValueError('error: Something went wrong, please try again')

    def validate_number(self, lat, long):
        if not isinstance(lat, (int, float)) or not isinstance(long, (int, float)):
            raise ValueError('error: values are not numbers, please correct!')

    def is_duplicate(self, lat, long):
        for ponto in self.validPoints:
            if lat == ponto.lat and ponto.long == long:
                raise ValueError('Error: point is duplicated, please correct!')

    def coordinate_validation(self, lat, long):
        if lat < -90 or lat > 90:
            raise ValueError('error: lat wrong value, please correct!')
        if long < -180 or long > 180:
            raise ValueError('error: long wrong value, please correct!')

    def add_point(self, lat, long):
        self.is_completed()
        self.validate_number(lat, long)
        self.coordinate_validation(lat, long)
        self.is_duplicate(lat, long)
        point = Point(lat, long)
        self.validPoints.append(point)
        return 'validation complete, point added'

    def complete_polygon(self):
        self.is_completed()
        if len(self.validPoints) < 3:
            raise ValueError('Error: a polygon requires at least 3 points')
        if len(self.validPoints) < self.totalPoints:
            raise ValueError('Error: There is less valid points than totalpoints')
        if len(self.validPoints) > self.totalPoints:
            raise ValueError('Error: There is more valid points than totalpoints')
        self.completed = True
        return 'Polygon completed, congratulation!'

    def points_return(self):
        if not self.completed:
            raise ValueError('Error: The list cannot be created, the value state is wrong')
        return tuple(self.validPoints)


class Polygon:

    def __init__(self, points):
        self._points = tuple(points)

    def __str__(self):
        return (f"These are the points received {self._points}")

    def _ref_point(self):
        lat0 = self._points[0].lat
        lat_ref = lat0
        long0 = self._points[0].long
        return (lat0, long0, lat_ref)

    def _lat_scale(self):
        _, _, lat_conv = self._ref_point()
        lat_rad = lat_conv * (pi / 180)
        return lat_rad

    def _meters_deg_value(self):
        lat_ref = self._lat_scale()
        meters_lat_deg = 111_380
        meters_long_deg = 111_320 * cos(lat_ref)
        return (meters_lat_deg, meters_long_deg)

    def _coord_difference(self):
        dcoord = []
        points = self._points
        lat0, long0, _ = self._ref_point()
        for x in points:
            lat = x.lat - lat0
            long = x.long - long0
            delta = (lat, long)
            dcoord.append(delta)
        return tuple(dcoord)

    def _rad_meters_conversion(self):
        dvalue = self._coord_difference()
        lat_meters, long_meters = self._meters_deg_value()
        lib = []
        for x, y in dvalue:
            delta_lat = x * lat_meters
            delta_long = y * long_meters
            delta = (delta_lat, delta_long)
            lib.append(delta)
        return tuple(lib)

    def perimeter(self):
        meters_list = self._rad_meters_conversion()
        print(meters_list)

    def area(self):
        pass
