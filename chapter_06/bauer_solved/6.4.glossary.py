python_glossary = {
    '.title()': 'Uppercase for string',
    'del': 'Delete key-value from dictionary',
    'print()': 'Print stuff in the console',
    '.lower()': 'Lowercase for strings',
    '.items()': 'Generates a list of keys & values from a dictionary',
    '.keys()': 'Generates a list of keys a dictionary',
    'set()': 'Returns a set of unique values',
    'in': 'Operator that checks if value is in a data type',
    '==': 'Operator that checks if value is equal to another value',
}
# print(f".title() - {python_glossary['.title()']}\n"
#       f".lower() - {python_glossary['.lower()']}\n"
#       f"del - {python_glossary['del']}\n"
#       f"print() - {python_glossary['print()']}\n"
#       )
for term, description in python_glossary.items():
    print(f"{term} - {description}")