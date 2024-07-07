from .formatbin import process_binary_data, create_files
# from .filehandler import write_list_to_file, write_dict_to_filenames
from . import filehandler

__ALL__ = [process_binary_data, create_files, filehandler
           #    write_list_to_file, write_dict_to_filenames
           ]
__version__ = '0.1.0'

__doc__ = f"""
formatbin - {__version__}
=======================================
A simple binary file formatter
"""

# if __name__ == '__main__':
#     main()
