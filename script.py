import os

# Create the complete directory structure for QUIZZICLES website
project_structure = {
    'quizzicles': {
        'views': {
            'pages': [],
            'partials': []
        },
        'public': {
            'css': [],
            'js': [],
            'images': []
        },
        'db': [],
        'models': [],
        'routes': [],
        'config': []
    }
}

def create_directory_structure(base_path, structure):
    for item, content in structure.items():
        current_path = os.path.join(base_path, item)
        if isinstance(content, dict):
            os.makedirs(current_path, exist_ok=True)
            create_directory_structure(current_path, content)
        else:
            os.makedirs(current_path, exist_ok=True)

# Create the directory structure
create_directory_structure('.', project_structure)
print("✅ Directory structure created successfully!")

# List the created structure
def list_directory_structure(path, indent=0):
    items = []
    for item in sorted(os.listdir(path)):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            items.append('  ' * indent + f"📁 {item}/")
            items.extend(list_directory_structure(item_path, indent + 1))
    return items

print("\n📂 Project Structure:")
structure_list = list_directory_structure('./quizzicles')
for item in structure_list:
    print(item)