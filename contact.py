from uuid import uuid4
import json
class Contact:
      def __init__(self,name:str,phone:str,email:str,contact_id:str | None=None):
            self.contact_id=contact_id
            self.name=name
            self.phone=phone
            self.email=email
      @classmethod
      def from_dict(cls,data:dict):
            return cls(
                  name=data['name'],
                  phone=data['phone'],
                  email=data['email'],
                  contact_id=data['contact_id']
            )

with open('contacts.json') as jsonfile:
      data_list=json.load(jsonfile)
contacts=[]
for data in data_list:
      contacts.append(Contact,from_dict(data))
for contact in contacts:
      print(contact.to_dict())
