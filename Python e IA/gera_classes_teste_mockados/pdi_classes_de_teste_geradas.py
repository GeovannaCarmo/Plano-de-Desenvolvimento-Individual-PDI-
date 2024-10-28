import tensorflow as tf
import re

def generate_tests(class_code):
    class_name = re.search(r'public class (\w+)', class_code).group(1)
    attributes = re.findall(r'private (\w+) (\w+);', class_code)

    test_methods = "" 
    for attr_type, attr_name in attributes:
        capitalized_attr_name = attr_name.capitalize() 
        if attr_type == "int": 
            test_value = "10"
        elif attr_type == "boolean":
            test_value = "true"
        else:
            test_value = 'null'

        test_methods += f"""
    @Test
    public void testGetSet{capitalized_attr_name}() {{
        {class_name} classObject = new {class_name}();
        classObject.set{capitalized_attr_name}({test_value});
        assertEquals({test_value}, classObject.get{capitalized_attr_name}());
    }}
"""

    test_class = f"""
public class {class_name}Test {{
{test_methods}
}}
"""
    return test_class

new_class_file_path = input("Insira o caminho do arquivo txt da nova classe: ")  
new_class_code = read_file(new_class_file_path) 
generated_test = generate_tests(new_class_code) 
print(generated_test)  
