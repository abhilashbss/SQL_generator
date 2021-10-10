# File data format : TableName - col:datatype:constraint, col:datatype:constraint, ...

from DDL import create_table


class TableCreationWrapper:
    def __init__(self, file_data):
        self.file_data = file_data
        self.create_table_objects = []

    def process(self):
        for line in self.file_data.splitlines():
            table_name = line.split("-")[0].strip()
            columns = line.split("-")[1].split(",")
            if table_name == "":
                continue
            ct_object = create_table.CreateTable(table_name)
            for col in columns:
                column_name = col.split(":")[0].strip()
                data_type = col.split(":")[1].strip()
                if len(col.split(":")) > 2:
                    constraint = col.split(":")[2].strip()
                    ct_object.add_constraint(column_name, constraint)
                ct_object.add_column(column_name, data_type)
            self.create_table_objects.append(ct_object)
        return self.create_table_objects


