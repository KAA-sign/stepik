n = int(input())
scopes = {'global': {'funcs': [], 'vars': []}}

def add(scopes, curent_namespace, what):
    if curent_namespace not in scopes:
        scopes[curent_namespace] = {}
        scopes[curent_namespace]['vars'] = []
        scopes[curent_namespace]['vars'].append(what)
    else:
        if 'vars' not in scopes[curent_namespace]:
            scopes[curent_namespace]['vars'] = []
            scopes[curent_namespace]['vars'].append(what)
        else:
            scopes[curent_namespace]['vars'].append(what)

def create(scopes, curent_namespace, parent_namespace):
    if curent_namespace not in scopes:
        scopes[curent_namespace] = {}
        scopes[curent_namespace]['funcs'] = []
        scopes[curent_namespace]['vars'] = []
        scopes[curent_namespace]['funcs'].append(curent_namespace)
        scopes[curent_namespace]['parent'] = parent_namespace
    else:
        if 'funcs' not in scopes[curent_namespace]:
            scopes[curent_namespace]['funcs'] = []
            scopes[curent_namespace]['parent'] = parent_namespace
            scopes[parent_namespace]['funcs'].append(curent_namespace)
        else:
            scopes[curent_namespace]['funcs'].append(curent_namespace)
            scopes[parent_namespace]['funcs'].append(curent_namespace)

def search(scopes, namespace, what):
    if what in scopes[namespace]['vars']:
        return namespace
    else:
        try:
            upper_namespace = scopes[namespace]['parent']
        except KeyError:
            return None
        return search(scopes, upper_namespace, what)

for i in range(n):
    command = input().split()
    if command[0] == 'add':
        add(scopes, command[1], command[2])
    elif command[0] == 'create':
        create(scopes, command[1], command[2])
    elif command[0] == 'get':
        print(search(scopes, command[1], command[2]))