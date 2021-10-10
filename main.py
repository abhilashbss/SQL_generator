
from TextProcessorWrapper import create_table_wrapper
from Utils import file_io


def create_sql_command(file_path):
    file_handler = file_io.FileHandler(file_path)
    ddl_creator = create_table_wrapper.TableCreationWrapper(file_handler.read())
    ct_objects = ddl_creator.process()

    for ct in ct_objects:
        print(ct.generate_create_table_command())

if __name__ == '__main__':
    create_sql_command("/home/abhilashbss/PycharmProjects/SQL_generator/resources/ddl_text")

