import os

def print_tree(startpath, prefix="", ignore_dirs=None):
    """
    Рекурсивно выводит структуру папок в виде дерева.
    """
    if ignore_dirs is None:
        ignore_dirs = {'.git', '__pycache__', 'node_modules', '.idea', 'venv', '.venv'}

    try:
        items = sorted(os.listdir(startpath))
    except PermissionError:
        return

    items = [item for item in items if item not in ignore_dirs and not item.startswith('.')]

    for index, item in enumerate(items):
        path = os.path.join(startpath, item)
        is_last = (index == len(items) - 1)
     
        connector = "└── " if is_last else "├── "
        
        if os.path.isdir(path):
            print(f"{prefix}{connector}{item}/")

            extension = "    " if is_last else "│   "
            print_tree(path, prefix + extension, ignore_dirs)
        else:
            print(f"{prefix}{connector}{item}")

if __name__ == "__main__":
    current_dir = os.getcwd()
    print(f"\n📁 {os.path.basename(current_dir)}/")
    
    # Запускаем обход
    print_tree(current_dir)
    print("\n")