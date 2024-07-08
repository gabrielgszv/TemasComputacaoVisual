import Polygons as p

poligonos = p.Polygons()

p1 = p.Point2D(0, 0)
p2 = p.Point2D(0, 100)
p3 = p.Point2D(200, 100)
p4 = p.Point2D(200, 0)

pa = p.Polygon([p1,p2,p3,p4], 'yellow')
poligonos.add_polygon(pa, 'pa')

p1 = p.Point2D(0, 100)
p2 = p.Point2D(50, 200)
p3 = p.Point2D(100, 100)

t = p.Polygon([p1,p2,p3], 'red')
poligonos.add_polygon(t, 't')

p1 = p.Point2D(100, 100)
p2 = p.Point2D(50, 200)
p3 = p.Point2D(150, 200)
p4 = p.Point2D(200, 100)

t1 = p.Polygon([p1,p2,p3,p4], 'red')
poligonos.add_polygon(t1, 't1')

p1 = p.Point2D(30, 0)
p2 = p.Point2D(30, 60)
p3 = p.Point2D(70, 60)
p4 = p.Point2D(70, 0)

po = p.Polygon([p1,p2,p3,p4], 'brown')
poligonos.add_polygon(po, 'po')


p.plot_polygons(poligonos)
