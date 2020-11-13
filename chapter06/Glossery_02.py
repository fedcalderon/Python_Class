Glossary = {'If Statement' : 'Runs a block of code only if certain conditions are met.', 'For Loop' :
    'A function that executes a block of code a specific '
                                                              'amount of times.',
            'List' : 'A list that can hold variables, strings, integers, ect.', 'String' : 'A line of text within '
                                                                                           'comments.',
            'Boolean' : 'A conditional test that evaluates to true or false.', 'Integer' : 'A whole number, not a '
                                                                                           'decimal.',
          'Print Statement' : 'A function that prints text to the console.', 'Variable' : 'A value assigned to a name.',
            'Dictionary' : 'Stores keys associated with values that can be anything from strings to variables.',
            'While Loop' : 'Iterates over a block of code as long as specific conditions are true.'}


for key, value in Glossary.items():
    print(f"\n{key}:\n{value}")