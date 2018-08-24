from models.service import Service
import mlab

mlab.connect()

# all_service = Service.objects()

# first_service = all_service[3]

# print(first_service['name'])

id_to_find ='5b782f6e5981d8043837bf8f'

# a = Service.objects(id = id_to_find) ## => [Services object]
# a = Service.objects.get(id = id_to_find) ## => Services object
service = Service.objects.with_id(id_to_find) ## => Services object

# Nếu sử dụng Service.object.get() => nếu Id không có trong danh sách => code lỗi
# Nếu sử dụng Service.object.with_id(id_to_find) => Nếu không có ID trong danh sách => trả lại none

if service is not None:
    # service.delete() #Delete bản ghi trong database
    # print(service.name)
    print(service.to_mongo()) ## hàm to_mongo() => in ra toàn bộ thông tin object
    service.update(set__yob = 2009, set__name = 'DSH')
    service.reload()
    print(service.to_mongo())
else:
    print('Services object is not found')
