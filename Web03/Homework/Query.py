from modul.river import River
import mlab

mlab.connect()
# Câu 7
# river = River.objects(continent = "Africa")
# for i in river:
#     print("Name: {} - Length: {}".format(i.name, i.length))

# Câu 8
river = River.objects(continent = "S. America", length__lt = 1000)
for i in river:
    print("Name: {} - Length: {}".format(i.name, i.length))