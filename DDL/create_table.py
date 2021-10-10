
class CreateTable:
    def __init__(self, table_name):
        self.table_name = table_name
        self.constraints = {}
        self.columns = {}
        self.enumerators = []
        self.create_table_command = ""

    def add_column(self, column, datatype):
        self.columns[column] = datatype

    def add_constraint(self, column, constraint):
        self.constraints[column] = constraint

    def get_col_constraint(self, column):
        if column in self.constraints.keys():
            return self.constraints[column]
        return ""

    def generate_create_table_command(self):
        self.create_table_command += "CREATE TABLE " + self.table_name + " ("
        for column in self.columns.keys():
            self.create_table_command += "\n"
            if self.columns[column].strip().lower().startswith("enum"):
                self.enumerators.append("CREATE TYPE " + column.strip() + "_enum AS" + self.columns[column] + " ;\n")
                self.create_table_command += column + " " + column.strip() + "_enum " + self.constraints[column] + ", "
            else:
                self.create_table_command += column + " " + self.columns[column] + " " \
                                             + self.get_col_constraint(column) + ","
        self.create_table_command = self.create_table_command[:-1]
        self.create_table_command += " );"
        self.create_table_command = " ".join(self.enumerators) + self.create_table_command
        return self.create_table_command


