class FileManager(object):
    """
    Provide a means to access local files.
    """

    CURRENT_DIR = os.path.dirname(__file__) + '/'
    
    ITEM_DATA_FILE = CURRENT_DIR + '../raw/items.json'

    def __init__(self, file_name=None):
        if file_name == None:
            return

        FileManager.CURRENT_DIR = os.path.dirname(__file__) + '/'

    def load_item_data(self, path):
        item_list = None

        with open(path) as item_data_file:
            item_list = json.load(item_data_file)

        return item_list

    def write_item_data(self, path, json_data):

        with open(path, 'w') as item_data_file:    
            item_data_file.write(json.dumps(json_data, indent=4, sort_keys=True))
