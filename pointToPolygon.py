def pointToPolygon(meters,lat,lng):
    newLatPlus = lat + (meters/float(111111))
    newLatMinus =  lat - (meters/float(111111))
    newLngPlus = lng + (meters/(float(111111 * math.cos(lat))))
    newLngMinus = lng - (meters/(float(111111 * math.cos(lat))))
    cor1 = [newLatMinus,newLngMinus]
    cor2 = [newLatMinus,newLngPlus]
    cor3 = [newLatPlus, newLngPlus]
    cor4 = [newLatPlus,newLngMinus]
    cornerList = [cor1,cor2,cor3,cor4]
    return(Polygon(cornerList))