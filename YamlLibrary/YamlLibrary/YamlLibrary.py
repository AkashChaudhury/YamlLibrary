import yaml
from yaml.loader import SafeLoader
import re


class YamlLibrary():

    def Convert_data_String(self, data):
        if data == None or data == isinstance(data, (int, float, bool)):
            return data.encode('ascii', 'ignore')

        data = data.encode('ascii', 'ignore')
        data = yaml.safe_load(data)
        return data

    def Get_Tree(self, data, key='.'):
        Yaml_data = self.Convert_data_String(data)
        output = self.get_tree_value(Yaml_data, key)
        return output

    def get_tree_value(self, Yaml_data, key):
        # Return Empty Keys
        if key == '.' or key == '/':
            return Yaml_data
        s = key

        # Find all Keys
        Keys_List = re.split('\.', s)

        # Find Lists in keys
        for keys in Keys_List:
            match = re.search('\[\d+\]', keys)
            if match:
                array_list = []
                array_string = re.findall('\[\d+\]', keys)

                # Separating Key
                Removed_key = re.search('\[\d+\]', keys)
                Removed_key = keys[:Removed_key.start()]

                for array in array_string:
                    number = re.findall('\d+', array)
                    number = int(number[0])
                    array_list.append(number)
                for array_num in array_list:
                    Yaml_data = Yaml_data[Removed_key][array_num]

            else:
                Yaml_data = Yaml_data[keys]
        return Yaml_data
