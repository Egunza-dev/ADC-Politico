
class Office:

    offices = [
        {
            "id" : 1,
            "type" : "state" ,
            "name" : "President"
        },
        {
            "id" : 2 ,
            "type" : "legislative" ,
            "name" : "MP"
        },
        {
            "id" : 3 ,
            "type" : "federal" ,
            "name" : "Senator"
        },
        {
            "id" : 4 ,
            "type" : "local government" ,
            "name" : "Governor"
        }
    ]




    def __init__(self, office_type, name):
        
        __class__.validate_post(office_type, name)
        self.office_type = office_type
        self.name = name
        self.id = __class__.offices[-1]["id"] + 1
        __class__.offices.append(self.__repr__())

    @classmethod
    def get_offices(cls):
        return __class__.offices

    @classmethod
    def get_office(cls, office_id):
        for office in __class__.offices:
            if office['id'] == office_id:
                return [office]
        return None

    def __repr__(self):
        return {"id":self.id,
                "type":self.office_type,
                "name":self.name
                }

    @classmethod
    def validate_post(cls, office_type, name):
        if not office_type:
            raise AssertionError("Office type should be provided!")
        elif not name:
            raise AssertionError("Office name should be provided!")







