# col :
# id int : sequential
# string: combine permutations of strings given
# int : range random
# enum :  random
# Foreign key reference :
from collections import defaultdict

class InsertDummyData:
    def __init__(self, table_name, desired_row_count):
        self.table_name = table_name
        self.desired_row_count = desired_row_count
        self.column_datatype = {}
        self.column_value_range = defaultdict(list)
        self.col_range_properties = defaultdict(dict)
        self.insert_query = ""

    def add_column(self, column, data_type):
        self.column_datatype[column] = data_type

    def add_column_value_range(self, column, value_range):
        if self.column_datatype[column].strip().lower().startswith("var") and column.strip().lower().endswith("name"):
            self.column_value_range[column] = value_range.get_name_value_list(
                self.col_range_properties[column]["list_of_first_names"],
                self.col_range_properties[column]["list_of_middle_names"],
                self.col_range_properties[column]["list_of_last_names"])
            return

        if self.column_datatype[column].strip().lower().startswith("var"):
            self.column_value_range[column] = value_range.get_string_value_list(
                self.col_range_properties[column]["list_of_strings"])
            return

        if self.column_datatype[column].strip().lower().startswith("enum"):
            self.column_value_range[column] = value_range.get_enum_range(
                self.col_range_properties[column]["enum_values"])
            return

        if self.column_datatype[column].strip().lower().startswith("int") and column.strip().lower().endswith("id"):
            self.column_value_range[column] = value_range.get_int_seq_range(
                self.col_range_properties[column]["start"])
            return

        if self.column_datatype[column].strip().lower().startswith("int"):
            self.column_value_range[column] = value_range.get_int_value_range(
                self.col_range_properties[column]["start"],
                self.col_range_properties[column]["end"])
            return

        if self.column_datatype[column].strip().lower().startswith("date"):
            self.column_value_range[column] = value_range.get_date_value_range(
                self.col_range_properties[column]["from_date"],
                self.col_range_properties[column]["to_date"])
            return

    def set_column_range_property(self, column, dictionary):
        self.col_range_properties[column] = dictionary

    def create_insert_query(self):
        columns = self.column_datatype.keys()
        self.insert_query += "INSERT INTO " + self.table_name + " ( " + ",".join(columns) + " ) values "
        for index in range(self.desired_row_count):
            self.insert_query += " ( "
            for col in columns:
                if self.column_datatype[col].strip().lower().startswith("int"):
                    self.insert_query += self.column_value_range[columns][index] + ","
                else:
                    self.insert_query += "\'" + self.column_value_range[columns][index] + "\'" + ","
            self.insert_query = self.insert_query[:-1]
            self.insert_query += " ),"
        self.insert_query = self.insert_query[:-1]
        self.insert_query += ";"
        return self.insert_query




