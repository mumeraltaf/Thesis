def addLapNoiseTimes(x,sensitivity,ep):
    scale = sensitivity / float(ep)
    u=random.uniform(-0.5,0.5)
    Noise =  - copysign(1, float(u)) * scale * log(1 - 2*abs(u))
    return x-timedelta(hours=0, minutes=Noise)