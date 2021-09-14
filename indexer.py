import pathlib, re
from typing import Dict

INDEX = {}

def indexer(file: str):   
    file = open(file)    
    lines = file.readlines()
    
    for line in lines:
        fragment(line, file)
           
def fragment(line: str, file: str):
    for word in line.split(' '):
        word = word.lower()

        if word in INDEX:
            if not file.name in INDEX[word]:
                INDEX.get(word).append(file.name)
        else:
            INDEX[word] = [file.name]
     
def search(word: str, dict: Dict):
    results = []

    for rec in dict:
        if re.findall(r''+word+'',rec):
            for route in dict[rec]:
                results.append(route)
    return results       
   

def folder_travel(route: str):        
    route = pathlib.Path(route)

    for item in route.iterdir():
        if item.is_dir():           
            folder_travel(item)
        else:
            indexer(item)

        
if __name__ == '__main__':
    
    error = True

    while(error):
        try:
            print('Type route to scan: ./', end='')
            route = input()
            folder_travel(f'./{route}/')  
            print(f'Indexing files ./{route}/: ended')
            error = False     
        except:
            print('Error in route, try again')
    
    while(True):
        route_docs = []
        print('Search: ',end='')
        user_input = input()
        user_input = user_input.split(' ')
        
        for word in user_input:   
                   
            for route in search(word.lower(),INDEX):
                route_docs.append(route)

        if len(route_docs) == 0:
            print('\nNo search results\n')
        else:
            print('\nMatching documents: ')
            for doc in set(route_docs):
                print(doc)
        print(len(route_docs))
        print('\n')