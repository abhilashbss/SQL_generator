import json
from DML import insert_table


# file json data format : """{"key1":{"key2":[1,2]}}"""
class InsertDataWrapper:
    def __init__(self, file_data):
        self.data_dict = json.loads(file_data)
        self.insert_object = insert_table.InsertDummyData(self.data_dict["table_name"], self.data_dict["row_count"])

    def create_insert_query(self):
        for col in self.data_dict["columns"]:
            self.insert_object.add_column(col["col_name"], col["data_type"])
            self.insert_object.set_column_range_property(col["col_name"], col["data_property"])
            self.insert_object.add_column_value_range(col["col_name"])
        return self.insert_object.create_insert_query()







