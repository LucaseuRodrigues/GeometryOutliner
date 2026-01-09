# from decorator import decorator


class Point():
    def __init__(self, lat, long):
        self.lat = lat
        self.long = long

    def dictmake(self):
        return {'lat': self.lat, 'long': self.long}


class PolygonInput():

    def __init__(self, total_points):
        self.totalPoints = total_points
        self.validPoints = []
        self.actualPoint = None

    def addPoint(self, lat, long):
        self.actualPoint = Point(lat, long)
        if not isinstance(lat, (int, float)) or not isinstance(long, (int, float)):
            return 'error: values are not numbers, please correct!'
        if lat < -90 or lat > 90:
            return 'error: wrong value, please correct!'
        if long < -180 or long > 180:
            return 'error: wrong value, please correct!'
        for ponto in self.validPoints:
            if self.actualPoint.lat == ponto.lat and self.actualPoint.long == ponto.long:
                return 'Erro: ponto duplicado, por favor corrija!'
        self.validPoints.append(self.actualPoint)
        self.actualPoint = None
        return 'validation complete, point added'

    def completePolygon(self):
        pass

    def finalList(self):
        pass
