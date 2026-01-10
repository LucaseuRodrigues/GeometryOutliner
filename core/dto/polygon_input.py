# from decorator import decorator


class Point():
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def dictmake(self):
        return {'lat': self.lat, 'long': self.long}

    def __repr__(self):
        return f'Point (lat={self.lat}), (long={self.long})'


class PolygonInput():

    def __init__(self, total_points):
        self.totalPoints = total_points
        self.validPoints = []
        self.actualPoint = None
        self.completed = False

    def addPoint(self, lat, long):
        if self.completed:
            return 'error: Something went wrong, please try again'
        self.actualPoint = Point(lat, long)
        if not isinstance(lat, (int, float)) or not isinstance(long, (int, float)):
            return 'error: values are not numbers, please correct!'
        if lat < -90 or lat > 90:
            return 'error: lat wrong value, please correct!'
        if long < -180 or long > 180:
            return 'error: long wrong value, please correct!'
        for ponto in self.validPoints:
            if self.actualPoint.lat == ponto.lat and self.actualPoint.long == ponto.long:
                return 'Erro: ponto duplicado, por favor corrija!'
        self.validPoints.append(self.actualPoint)
        self.actualPoint = None
        return 'validation complete, point added'

    def completePolygon(self):
        if self.completed:
            return 'error: Something went wrong, please try again'
        if len(self.validPoints) < 3:
            return 'Error: a polygon requires at least 3 points'
        if len(self.validPoints) < self.totalPoints:
            return 'Error: There is less valid points than totalpoints'
        if len(self.validPoints) > self.totalPoints:
            return 'Error: There is more valid points than totalpoints'
        self.completed = True
        return 'Polygon completed, congratulation!'

    def finalList(self):
        if not self.completed:
            raise 'Error: The list cannot be created, the value state is wrong'
        return tuple(self.validPoints)


class Polygon():

    def __init__(self, points):
        self.Points = points

    def perimeter(self):
        x = 0

    def area(self):
        pass
