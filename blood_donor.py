from mysql import connector
import datetime
class BloodDonorManager:
    def __init__(self):
        self.connection = connector.connect(
            host="localhost",
            user="root",
            password="Anjana#@!123",
            database="blood_db_b3"

        )
        print("connected succcessfully")
    def get_object(self,id=None):
        try:
            self.cursor = self.connection.cursor()
            query = "SELECT * FROM donor WHERE id=%s"
            values = (id,)
            self.cursor.execute(query, values)
            record = self.cursor.fetchone()
            return record
        except Exception as e:
            return None
    def post(self,**kwargs):
        try:
            self.cursor = self.connection.cursor()
            query = "INSERT INTO donor (name, blood_group, phone, city, last_donation) VALUES (%s, %s, %s, %s, %s)"
            values =[v for v in kwargs.values()]
            self.cursor.execute(query,values)
            self.connection.commit()
            print("Donor added successfully")
        except Exception as e:
            print(e)
    def get(self):
        try:
            self.cursor=self.connection.cursor()
            query = "select * from donor"
            self.cursor.execute(query)
            records = self.cursor.fetchall()
            # print(records)
            for data in records:
                print(data)
        except Exception as e:
            print(e)
    def retrieve(self,id=None):
        try:
            record=self.get_object(id=id)
            if record ==None:
                print("record not found")
            else:
                print(record)
        except Exception as e:
            print(e)
    def delete(self,id=None):
        try:
            record = self.get_object(id=id)
            values = (id,)
            if record !=None:
                query="delete from donor where id=%s"
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor deleted successfully")
            else:
                print("Donor not found")
        except Exception as e:
            print(e)
    def put(self,id=None,**kwargs):
        try:
            record = self.get_object(id=id)
            if record!=None:
                self.cursor=self.connection.cursor()
                placeholder=""
                for k in kwargs.keys():
                    placeholder += k+ "=%s, "
                placeholder = placeholder.rstrip(", ")
                query = f"update donor set {placeholder} where id=%s"
                values = [v for v in kwargs.values()]
                values.append(id)
                self.cursor.execute(query,values)
                self.connection.commit()
                print("Donor details updated successfully")
            else:
                print("Donor not found")
        except Exception as e:
            print(e)


donor_instance=BloodDonorManager()               #create an object
# donor_instance.post(name="Biya",blood_group="AB+",phone="9123456789",city="Thrissur",last_donation=datetime.datetime.today())
donor_instance.get()
print("__details of blood donor__")
donor_instance.retrieve(id=1)
print(("___delete"))
donor_instance.delete(id=3)
print("__after updation__")
donor_instance.put(id=2,city="Alapuzha")

donor_instance.get()


