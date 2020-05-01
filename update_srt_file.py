import datetime

Delimiter = " --> "

def addSecs(tm, secs):
    fulldate = datetime.datetime(100, 1, 1, tm.hour, tm.minute, tm.second)
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()

with open("E:\TLOR2002.srt") as f:
    with open("E:\The.Lord.of.the.Rings.The.Two.Towers.2002.Extended.BluRay.1080p.DTSES6.1.x264-CHD.srt", "a") as f1:
        for line in zip(f):
            values = str(line).split(Delimiter)
            if len(values) > 1:
                time = values[0].split(',')
                time_str = datetime.datetime.strptime(time[0], '%H:%M:%S').time()
                b = addSecs(time_str, 3)
                values[0] = str(b)+','+time[1]
                time = values[1].split(',')
                time_str = datetime.datetime.strptime(time[0], '%H:%M:%S').time()
                b = addSecs(time_str, 3)
                values[1] = str(b)+','+time[1]
                line = Delimiter.join(values)
                f1.write(line)
            else:
                f1.write(str(line))
print('file written successfully')
