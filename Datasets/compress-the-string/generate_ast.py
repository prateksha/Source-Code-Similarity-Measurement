import ast
import sys
import pickle
from astor import to_source

# To modify the nodes(change identifier names) as we traverse the AST
class RemoveVariableNames(ast.NodeTransformer):
    def visit_Name(self, node):
        if(isinstance(node, ast.Name)):
            result = ast.Name(id='x')
            return ast.copy_location(result, node)
        return node

# To count the number of loops(While and For loop)
def count_loops(tree):
    loop_count = 0
    for node in ast.walk(tree):
        if(isinstance(node, (ast.For, ast.While))):
            loop_count += 1
    return loop_count

# To count the number of If
def count_if(tree):
    if_count = 0
    for node in ast.walk(tree):
        if(isinstance(node, ast.If)):
            if_count += 1
    return if_count

# To count the number of functions
def count_functions(tree):
    function_count = 0
    for node in ast.walk(tree):
        if(isinstance(node, ast.FunctionDef)):
            function_count += 1
    return function_count

# Perform the above operations on the source code
def mutate(filename):
    file = open(filename)
    contents = file.read()
    # Generate the AST
    parsed = ast.parse(contents)
    nodeVisitor = RemoveVariableNames()
    transformed = nodeVisitor.visit(parsed)
    return ast.parse(to_source(transformed))

level0 = []
level1 = []
level2 = []

def find_levels(node, level=0):
    if level==0:
        level0.append(ast.dump(node))
    elif level==1:
        level1.append(ast.dump(node))
    elif level==2:
        level2.append(ast.dump(node))

    for _, value in ast.iter_fields(node):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    find_levels(item, level=level+1)
        elif isinstance(value, ast.AST):
            find_levels(value, level=level+1)

# def node_types():
#     for n in level1:
#         if isinstance(n, ast.Assign):
#             level1_assign.append(ast.dump(n))

def get_children(node):
    parent = ast.dump(node)
    children = []
    for child_node in ast.iter_child_nodes(node):
        children.append(ast.dump(child_node))
    return parent, children

parents1 = []
parents2 = []
children1 = []
children2 = []

def get_parent_children_relation(root, level=0):
    for _, value in ast.iter_fields(root):
        if isinstance(value, list):
            for item in value:
                if isinstance(item, ast.AST):
                    p, c = get_children(item)
                    if level == 0:
                        parents1.append(p)
                        children1.append(c)
                    elif level == 1:
                        parents2.append(p)
                        children2.append(c)       
                    get_parent_children_relation(item, level=level+1)
        elif isinstance(value, ast.AST):
            p, c = get_children(value)
            if level == 0:
                parents1.append(p)
                children1.append(c)
            elif level == 1:
                parents2.append(p)
                children2.append(c)
            get_parent_children_relation(value, level=level+1)

filename = sys.argv[2]
input_tree = mutate(filename)
count_l = count_loops(input_tree)
count_if = count_if(input_tree)
count_f = count_functions(input_tree)
find_levels(input_tree)
program_number1 = sys.argv[1]

filename_prognum = "program"+program_number1
get_parent_children_relation(input_tree)


pc_1 = list(zip(parents1, children1))
pc_2 = list(zip(parents2, children2))
pc_1.sort
pc_2.sort

program_name = open(("program"+program_number1+".txt"), "w")
program_name.write(filename)
output_file_counts = open((filename_prognum+"_count.txt"), "w")
output_file_counts.write('%d' % count_l)
output_file_counts.write('\n')
output_file_counts.write('%d' % count_if)
output_file_counts.write('\n')
output_file_counts.write('%d' % count_f)
output_file_counts.write('\n')


output_file_lev0 = open((filename_prognum+"_lev0.txt"), "w")
for ele in level0:
    output_file_lev0.write(ele)
    output_file_lev0.write('\n')

output_file_lev1 = open((filename_prognum+"_lev1.txt"), "w")
output_file_lev2 = open((filename_prognum+"_lev2.txt"), "w")
for ele in pc_1:
    output_file_lev1.write(ele[0])
    output_file_lev1.write('\n')
    for item in ele[1]:
        output_file_lev2.write(item)
        output_file_lev2.write('\n')

# print("-----------------------------LEVEL1 -> LEVEL2-----------------------------------------------------")
# for i in range(len(parents1)):
#     print("Parent = ", parents1[i], "\nChildren = ", children1[i])
#     print("\n")
# print("------------------------------LEVEL2 -> LEVEL3----------------------------------------------------")
# for i in range(len(parents2)):
#     print("Parent = ", parents2[i], "\nChildren = ", children2[i])
#     print("\n")
# print("-------------------------------------------------------------------------------------------")
