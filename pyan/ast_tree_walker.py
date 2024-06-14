import ast

def extract_function_call_args(node):
    if isinstance(node, ast.Call):
        # Extract positional arguments
        positional_args = [ast.dump(arg) for arg in node.args]

        # Extract keyword arguments
        keyword_args = {kw.arg: ast.dump(kw.value) for kw in node.keywords}

        return positional_args, keyword_args
    return None, None

def traverse_ast(node):
    if isinstance(node, ast.Return):
        # Check if the return value is a function call
        positional_args, keyword_args = extract_function_call_args(node.value)
        if positional_args or keyword_args:
            print("Function call in return statement:")
            print("Positional Args:", positional_args)
            print("Keyword Args:", keyword_args)

    # Recurse into child nodes
    for child_node in ast.iter_child_nodes(node):
        traverse_ast(child_node)

def extract_function_call_args(node):
    try:

        # Extract positional arguments
        positional_args = [ast.dump(arg) for arg in node.args]

        # Extract keyword arguments
        keyword_args = {kw.arg: ast.dump(kw.value) for kw in node.keywords}

        return positional_args, keyword_args
    except (AttributeError, TypeError) as e:
        return None, None

def extract_arguments(node):
    argument_values = []

    # if isinstance(node, ast.Call):
    #     for arg in node.args:
    #         argument_values.extend(extract_arguments(arg))
    #     for keyword in node.keywords:
    #         argument_values.extend(extract_arguments(keyword.value))
    #
    # elif isinstance(node, ast.Return):
    #     if node.value:
    #         argument_values.extend(extract_arguments(node.value))

    if isinstance(node, ast.Call):
        if isinstance(node.func, ast.Name):
            argument_values.append('::' + node.func.id)
        elif hasattr(node.func, 'attr'):
            argument_values.append('::' + node.func.attr)

    # elif isinstance(node, ast.Str):
    if isinstance(node, ast.Str):
        argument_values.append(node.s)

    elif isinstance(node, ast.Num):
        argument_values.append(node.n)

    # Add more conditions to handle other types of argument values as needed

    # Recursively traverse the tree
    for child_node in ast.iter_child_nodes(node):
        argument_values.extend(extract_arguments(child_node))

    return argument_values
