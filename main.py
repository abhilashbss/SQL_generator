from TextProcessorWrapper import create_table_wrapper, insert_data_wrapper
from Utils import file_io


def get_create_sql_command(file_path):
    file_handler = file_io.FileHandler(file_path)
    ddl_creator = create_table_wrapper.TableCreationWrapper(file_handler.read())
    ct_objects = ddl_creator.process()

    for ct in ct_objects:
        print(ct.generate_create_table_command())


def get_insert_sql_command(file_path):
    file_handler = file_io.FileHandler(file_path)
    insert_object = insert_data_wrapper.InsertDataWrapper(file_handler.read())
    print(insert_object.create_insert_query())


if __name__ == '__main__':
    get_insert_sql_command("/home/abhilashbss/PycharmProjects/SQL_generator/resources/col_properties")
