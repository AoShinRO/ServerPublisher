import os
import shutil
import sys

pasta_final = 'publish'

if os.path.exists(pasta_final):
    shutil.rmtree(pasta_final)

os.makedirs(pasta_final)

sv_files = [
    'db', 
    'conf',
    'npc',  
    'athena-start',    
    'mac.rathena-start.scpt',       
    'charserv.bat',
    'char-server.exe',  
    'char-server.pdb',
    'libmysql.dll',
    'logserv.bat',
    'login-server.exe',  
    'login-server.pdb',
    'mapserv.bat',
    'map-server.exe',  
    'map-server.pdb',
    'pcre8.dll',
    'runserver.bat',
    'serv.bat',
    'webserv.bat',
    'web-server.exe',  
    'zlib.dll',
]

total_it = len(sv_files)

for index, item in enumerate(sv_files):
    it = os.path.join('.', item)

    if os.path.isfile(it):
        shutil.copy2(it, pasta_final)
    elif os.path.isdir(it):
        shutil.copytree(it, os.path.join(pasta_final, item)) 

    prg = (index + 1) / total_it * 100

    sys.stdout.write(f"\rProgresso: {prg:.2f}%")
    sys.stdout.flush()

print("\nProgresso concluido com sucesso!")