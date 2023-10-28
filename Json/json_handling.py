import json

class Data():
    def __init__(self, json_file):
        self.json_file = json_file

        with open(json_file, 'r', encoding='utf-8') as file:
            # Store the JSON data
            data = json.load(file)
        self.get = data

    def save(self, data1, data2=None):
        self.get.append(data1)
        if not data2 == None:
            self.get.append(data2)
        with open(self.json_file, 'w', encoding='utf-8') as file:
                json.dump(self.get, file, indent=4)

    def remove(self, data):
        self.get.remove(data)
        with open(self.json_file, 'w', encoding='utf-8') as file:
                json.dump(self.get, file, indent=4)
    
    def save_and_retrive(self, data1, data2=None):
        self.get.append(data1)
        if not data2 == None:
            self.get.append(data2)
        with open(self.json_file, 'w', encoding='utf-8') as file:
                json.dump(self.get, file, indent=4)
        
        with open(self.json_file, 'r', encoding='utf-8') as file:
            # Store the JSON data
            data = json.load(file)
        return data
    
    def is_empty(self) -> bool:
        if self.get == []:
             return True
        else:
             return False
        