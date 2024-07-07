from .formatbin import get_transformed_data, process_binary_data

# from .filehandler import write_list_to_file, write_dict_to_filenames
from . import filehandler

__ALL__ = [
    process_binary_data,
    get_transformed_data,
    filehandler,
    #    write_list_to_file, write_dict_to_filenames
]
__version__ = "0.1.0"

__doc__ = f"""
formatbin - {__version__}
=======================================
A simple binary file formatter
"""

# if __name__ == '__main__':
#     main()
