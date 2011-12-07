#=[site officiel]=====================
#<<<<<fonctions by W3YZOH0RTH>>>>>
#=====[http://progject.free.fr/]=======
from math import sqrt,acos,pi,cos,sin
from os import chdir,getcwd,listdir
import xml.dom.minidom
import urllib
import socket

#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_ip_ext():
    ipxml = xml.dom.minidom.parse(urllib.urlopen('http://www.showmyip.com/xml/'))
    return ipxml.getElementsByTagName('ip')[0].childNodes[0].nodeValue

#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_ip_int():
    return socket.getaddrinfo(socket.gethostname(), None)[0][4][0]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def DISTANCE(x,y,x2=0,y2=0):
    """distance entre (x,y) a (x2,y2)"""
    return sqrt((x-x2)*(x-x2)+(y-y2)*(y-y2))

#:::::::::::::::::::::::::::::::::::::::::::::::::
def DIRECTION(x,y,x2=0,y2=0):
    """direction de (x,y) vers (x2,y2)"""
    if x!=x2 and y!=y2:
        if x < x2:
            direction = acos((x2-x)/DISTANCE(x,y,x2,y2))*180/pi
            if y<y2 : direction = 360 - direction
        else:
            direction = acos((x-x2)/DISTANCE(x,y,x2,y2))*180/pi
            if y < y2 : direction += 180
            else : direction = 180 - direction
    elif x < x2 : direction = 0
    elif x > x2 : direction = 180
    elif y < y2 : direction = 270
    elif y > y2 : direction = 90
    else : direction = 0
    return direction

#:::::::::::::::::::::::::::::::::::::::::::::::::
def RANGE(start=0,stop=0,step=1):
      if start != stop and step:
            if stop < start and step > 0:start, stop = stop, start
            elif stop > start and step < 0:start, stop = stop, start
            while start < stop:
                  start += step
                  yield start
      else:yield start

#:::::::::::::::::::::::::::::::::::::::::::::::::
def radian(degre):
    return degre*pi/180

#:::::::::::::::::::::::::::::::::::::::::::::::::
def CoSinus(degre):
    angle = radian(degre)
    return cos(angle),sin(angle)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def OUEX(a,b):
    """porte logique ou-exclusif"""
    return a and not b or not a and b

#:::::::::::::::::::::::::::::::::::::::::::::::::
def file_exists(name):
    path = name.replace("\\","/").split("/")
    if name.count("."):
        name = path[-1].split(".")
        ext = "."+name[-1]
        name = ".".join(name[:-1])
    else:
        name = path[-1]
        ext = ""
    path = "/".join(path[:-1])
    if path != "" : path += "/"
    erreur = temp_err = 0
    while erreur == temp_err:
        temp_name = name+(" ("+str(erreur)+")")*bool(erreur)+ext
        for f in list(find_files(path)):
            if f == temp_name:
                erreur += 1
                break
        temp_err += 1
    return path+temp_name

#:::::::::::::::::::::::::::::::::::::::::::::::::
def name_exists(name):
    return dir_exists(file_exists(name))
#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_name_file(name):
    return name.replace("\\","/").split("/")[-1]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_ext_file(name):
    return name.split(".")[-1]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_path_file(name):
    return "/".join(name.replace("\\","/").split("/")[:-1])+"/"

#:::::::::::::::::::::::::::::::::::::::::::::::::
def dir_exists(name):
    path = name.replace("\\","/").split("/")
    name = path[-1]
    path = "/".join(path[:-1])
    if path != "" : path += "/"
    erreur = temp_err = 0
    while erreur == temp_err:
        temp_name = name+(" ("+str(erreur)+")")*bool(erreur)
        for f in list(find_dirs(path)):
            if f == temp_name:
                erreur += 1
                break
        temp_err += 1
    return path+temp_name

#:::::::::::::::::::::::::::::::::::::::::::::::::
def find_dirfile(path=getcwd()):
      """path=getcwd() ---> tuple(dirs,files)"""
      if path == "" : path = getcwd()
      dos = listdir(path)
      fichier = []
      dossier = []
      for i in dos :
            try:
                  open(path+"/"+i).close()
                  fichier.append(i)
            except:
                  path_start = getcwd()
                  try:
                        chdir(path+"/"+i)
                        dossier.append(i)
                  except:pass
                  chdir(path_start)
      return [dossier,fichier]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def find_files(path=getcwd()):
      """path=getcwd() ---> generateur(path) ---> files in path"""
      if path == "" : path = getcwd()
      path = path.replace("\\","/")
      if path[-1] != "/" : path += "/"
      files = listdir(path)
      for i in files:
            try:
                  open(path+"/"+i).close()
                  yield i
            except:pass

#:::::::::::::::::::::::::::::::::::::::::::::::::
def find_allfiles(path=getcwd()):
      if path == "" : path = getcwd()
      for p in find_paths2(path):
            for f in find_files(p) : yield p+"/"+f

#:::::::::::::::::::::::::::::::::::::::::::::::::
def find_allfiles2(path=getcwd()):
      """generateur renvoyant toutes les paths filles du dossier parent"""
      if path == "" : path = getcwd()
      path = path.replace("\\","/")
      dirfile = find_dirfile(path)
      yield (path,dirfile[1])
      for i in dirfile[0]:
            try:
                  for d,f in find_allfiles2(path+"/"+i):yield (d,f)
            except:
                  yield ("erreur",[])
                  
#:::::::::::::::::::::::::::::::::::::::::::::::::
def find_dirs(path=getcwd()):
      """path=getcwd() ---> generateur(dirs)"""
      if path == "" : path = getcwd()
      path = path.replace("\\","/")
      if path[-1] != "/" : path += "/"
      dirs = listdir(path)
      path_start = getcwd()
      for i in dirs:
            try:
                  chdir(path+"/"+i)
                  yield i
            except:pass
            chdir(path_start)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def find_allpath(path=getcwd()):
    """retourne toutes les urls du dossier parent (les urls peuvent etre en plusieurs exemplaires)"""
    if path == "" : path = getcwd()
    path = path.replace("\\","/")
    list_path = []
    list_dossiers = [path]
    for i in find_dirs(path):
        list_dossiers.append(path+"/"+i)
        recup=find_allpath(path+"/"+i)
        if recup != []:
            for x in recup:
                list_dossiers.append(x)
                
    return list_dossiers

#:::::::::::::::::::::::::::::::::::::::::::::::::
def find_paths2(path=getcwd()):
      """generateur renvoyant toutes les urls filles du dossier parent"""
      if path == "" : path = getcwd()
      path = path.replace("\\","/")
      yield path
      for i in find_dirs(path):
            try :
                  for p in find_paths2(path+"/"+i) : yield p
            except :
                  yield "erreur"
                
#:::::::::::::::::::::::::::::::::::::::::::::::::
def find_paths(path=getcwd()):
    """version ameliore de "find_allpath(), les urls ne sont qu'en un seul exemplaire"""
    if path == "" : path = getcwd()
    p = find_allpath(path)
    paths = []
    for i in p :
          if not paths.count(i) : paths.append(i)
    return paths
            
#:::::::::::::::::::::::::::::::::::::::::::::::::
def PARTITEST(parti="",recup=0):
    """string="",bool=0 ---> ["partitions",[list_dirs],[list_files]]"""
    partition = ""
    dirs = []
    files = []
    if parti == "":
        parti = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in parti:
        try:
            if recup:
                find=find_dirfile(i+":")
                dirs.append(find[0])
                files.append(find[1])
            else:
                chdir(i+":")
            partition += i
        except:
            ""
    if recup:
        return [partition,dirs,files]
    else:
        return partition
      
#:::::::::::::::::::::::::::::::::::::::::::::::::
def str_comp(i1,i2,_type_=0):
      """compare les iterables i1 et i2 --> _type_ = 0 str() 0(==)  _type_ = 1(!=) ou 1 %=="""
      lim = abs(len(i2) - len(i1))
      size = len(i1)
      
      if len(i1) > len(i2) : i1 = i1[:len(i2)]
      elif len(i1) < len(i2):
            size = len(i2)
            i2 = i2[:len(i1)]       
      
      if _type_ : string = 0.
      else : string = ""
      
      for c1, c2 in zip(i1,i2):
            if c1 == c2:
                  if _type_ : string += 1
                  elif not _type_ : string += "0"
            else:
                  if not _type_ : string += "1"
                  
      if _type_:
            string = string/size * 100
      else:
            for i in range(lim) : string += "1"
            
      return string

#:::::::::::::::::::::::::::::::::::::::::::::::::
def LIMSTR(string,lim=20,ind=""):
    """string,int,ind= "END", "MIL" or ""---> str... """
    if ind == "END":
        caract = list(string)
        caract.reverse()
        string = ""
        for i in caract:
            string += i
    elif ind == "MIL":
        i = lim/2
        if len(string)/2 > i:
            string = "..."+string[len(string)/2-i:len(string)/2+i]+"..."
        
    if ind == "END" or ind == "":
        if len(string)>lim:
            string=string[:lim]+"..."
        if ind == "END":
            caract = list(string)
            caract.reverse()
            string = ""
            for i in caract:
                string += i
    return string

#:::::::::::::::::::::::::::::::::::::::::::::::::
def bin(c,base=256):
    """change UN caractere de base 'base' en base 2"""
    return  int_len(int_base(base_int(c,base),2),8)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def bins(string,base=256):
    """change une string de base 'base' en base 2"""
    return "".join([bin(c)for c in string])

#:::::::::::::::::::::::::::::::::::::::::::::::::
def base_to_base(string,base1=256,base2=16):
    """change une string de base1 en base2"""
    return  int_base(base_int(string,base1),base2)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def decode(unicod):
    """Convertie une chaine de type unicode en type string"""
    string = ""
    for c in unicod:
        try:
            string += str(c)
        except Exception,err:
            string += str(all_caract()[int("0x"+str(err)[41:43],16)])
    return string

#:::::::::::::::::::::::::::::::::::::::::::::::::
def str_val(string):
    valeur = 0
    for n,c in enumerate(string):
        valeur += ord(c)*256**n
    return valeur

#:::::::::::::::::::::::::::::::::::::::::::::::::
def base256(x):
    s=""
    while x != 0:
        s += chr(x%256)
        x = x/256
    if s == "": s = "0"
    return s

#:::::::::::::::::::::::::::::::::::::::::::::::::
def int_base(x,base=256):
    s=[]
    caract = _256_()[:base]
    while x != 0:
        s.append(caract[x%base])
        x = x/base
    if s ==[]:
        s.append(0)
    s.reverse()
    b=""
    for i in s:
        b+=str(i)
    return b

#:::::::::::::::::::::::::::::::::::::::::::::::::
def base_int(string,base=256):
    valeur = 0
    caract = _256_()[:base]
    for i in range(len(string)):
        valeur += caract.index(string[-i-1])*pow(base,i)
    return valeur

#:::::::::::::::::::::::::::::::::::::::::::::::::
def str_val_max(n):
    """nombre de caractere de la chaine ---> int maximum"""
    valeur = 0
    for i in range(n):
        valeur += 255*pow(256,i)
    return valeur

#:::::::::::::::::::::::::::::::::::::::::::::::::
def base_int_max(n,base):
    """nombre de caractere de la chaine ---> int maximum"""
    valeur = 0
    for i in range(n):
        valeur += (base-1)*pow(base,i)
    return valeur

#:::::::::::::::::::::::::::::::::::::::::::::::::
def all_caract():
      c = []
      for i in range(256) : c.append(chr(i))
      return c

#:::::::::::::::::::::::::::::::::::::::::::::::::
def int_base2(x,base=256**2):
      """meme fonction que int_base(string,avec base>256)"""
      s=[]
      while x != 0:
            s.append(int_len(int_base(x%base),len(int_base(base))-1))
            x = x/base
      if s ==[]:
            s.append(0)
      s.reverse()
      b=""
      for i in s:
            b+=str(i)
      return b

#:::::::::::::::::::::::::::::::::::::::::::::::::
def base_int2(string,base=256**2):
      valeur = 0
      paquet = len(int_base(base))-1
      string = cut(string,paquet,1)
      for i,v in enumerate(string) : valeur += base_int(v)*pow(base,i)
      return valeur

#:::::::::::::::::::::::::::::::::::::::::::::::::
def bin_group(string,octet=8):
      return cut(bins(string),octet,1)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def _256_():
    return [ 
 "\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39", "\x61","\x62","\x63","\x64","\x65",
 "\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74",
 "\x75","\x76","\x77","\x78","\x79","\x7a","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49",
 "\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58",
 "\x59","\x5a","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2c","\x2e","\x3a",
 "\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x5b","\x5c","\x5d","\x5e","\x5f","\x60", "\x7b","\x7c","\x7d",
 "\x7e","\x09","\x00","\x01","\x02","\x03","\x04","\x05","\x06","\x07","\x08","\x0b","\x0c","\x0e",
 "\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18","\x19","\x1a","\x1b","\x1c","\x1d",
 "\x1e","\x1f","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86","\x87","\x88","\x89","\x8a","\x8b","\x8c",
 "\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95","\x96","\x97","\x98","\x99","\x9a","\x9b",
 "\x9c","\x9d","\x9e","\x9f","\xa0","\xa1","\xa2","\xa3", "\xa4","\xa5","\xa6","\xa7","\xa8","\xa9","\xaa",
 "\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3","\xb4","\xb5","\xb6","\xb7","\xb8","\xb9",
 "\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2", "\xc3", "\xc4","\xc5","\xc6","\xc7","\xc8",
 "\xc9", "\xca","\xcb","\xcc", "\xcd","\xce","\xcf","\xd0","\xd1","\xd2","\xd3","\xd4","\xd5","\xd6","\xd7",
 "\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0","\xe1","\xe2","\xe3","\xe4","\xe5","\xe6",
 "\xe7","\xe8","\xe9","\xea","\xeb","\xec","\xed","\xee","\xef","\xf0","\xf1","\xf2","\xf3", "\xf4","\xf5",
 "\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff", "\x2a","\x2b","\x2d","\x2f","\x0a","\x0d"]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def caract_text():
    return [ 
 "\x30","\x31","\x32","\x33","\x34","\x35","\x36","\x37","\x38","\x39", "\x61","\x62","\x63","\x64","\x65",
 "\x66","\x67","\x68","\x69","\x6a","\x6b","\x6c","\x6d","\x6e","\x6f","\x70","\x71","\x72","\x73","\x74",
 "\x75","\x76","\x77","\x78","\x79","\x7a","\x41","\x42","\x43","\x44","\x45","\x46","\x47","\x48","\x49",
 "\x4a","\x4b","\x4c","\x4d","\x4e","\x4f","\x50","\x51","\x52","\x53","\x54","\x55","\x56","\x57","\x58",
 "\x59","\x5a","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27","\x28","\x29","\x2c","\x2e","\x3a",
 "\x3b","\x3c","\x3d","\x3e","\x3f","\x40","\x5b","\x5c","\x5d","\x5e","\x5f","\x60", "\x7b","\x7c","\x7d",
 "\x7e","\x09","\x2a",

 "\x2b","\x2d","\x2f","\x0a","\x0d","\xa0","\xe8","\xe9",

 "\x00","\x01","\x02","\x03","\x04","\x05","\x06",
 "\x07","\x08","\x0b","\x0c","\x0e", "\x0f","\x10","\x11","\x12","\x13","\x14","\x15","\x16","\x17","\x18",
 "\x19","\x1a","\x1b","\x1c","\x1d","\x1e","\x1f","\x7f","\x80","\x81","\x82","\x83","\x84","\x85","\x86",
 "\x87","\x88","\x89","\x8a","\x8b","\x8c","\x8d","\x8e","\x8f","\x90","\x91","\x92","\x93","\x94","\x95",
 "\x96","\x97","\x98","\x99","\x9a","\x9b","\x9c","\x9d","\x9e","\x9f","\xa1","\xa2","\xa3", "\xa4",
 "\xa5","\xa6","\xa7","\xa8","\xa9","\xaa","\xab","\xac","\xad","\xae","\xaf","\xb0","\xb1","\xb2","\xb3",
 "\xb4","\xb5","\xb6","\xb7","\xb8","\xb9","\xba","\xbb","\xbc","\xbd","\xbe","\xbf","\xc0","\xc1","\xc2",
 "\xc3", "\xc4","\xc5","\xc6","\xc7","\xc8","\xc9", "\xca","\xcb","\xcc", "\xcd","\xce","\xcf","\xd0","\xd1",
 "\xd2","\xd3","\xd4","\xd5","\xd6","\xd7","\xd8","\xd9","\xda","\xdb","\xdc","\xdd","\xde","\xdf","\xe0",
 "\xe1","\xe2","\xe3","\xe4","\xe5","\xe6","\xe7","\xea","\xeb","\xec","\xed","\xee","\xef",
 "\xf0","\xf1","\xf2","\xf3", "\xf4","\xf5","\xf6","\xf7","\xf8","\xf9","\xfa","\xfb","\xfc","\xfd","\xfe","\xff"]
#:::::::::::::::::::::::::::::::::::::::::::::::::
def cut(string,part,sens=0):
      parts = []
      for i in range(len(string)):
            if sens:
                  if (i+1)*part+1 <= len(string) : parts.append(string[len(string)-(i+1)*part:len(string)-i*part])
                  else:
                        if string[:i*-part] != "":parts.append(string[:i*-part])
                        break
            else:
                  if (i+1)*part <= len(string) : parts.append(string[i*part:(i+1)*part])
                  else:
                        if string[i*part:] != "":parts.append(string[i*part:])
                        break                    
      return parts
            
#:::::::::::::::::::::::::::::::::::::::::::::::::
def FULLSCREEN(fen,yes,width=600,height=400):
    yes = str(yes)
    if yes and "0" != yes.lower() != "no":
        w, h = fen.winfo_screenwidth(), fen.winfo_screenheight()
        fen.overrideredirect(1)
    else:
        w, h = width, height
        fen.overrideredirect(0)
    fen.geometry("%dx%d+0+0" % (w, h))
    return w, h

#:::::::::::::::::::::::::::::::::::::::::::::::::
def read_line(fichier):
      """generateur(fichier) ---> fichier.ligne puis ferme fichier"""
      string = fichier.readline()
      while string != "":
            yield string
            string = fichier.readline()
      fichier.close()
#:::::::::::::::::::::::::::::::::::::::::::::::::
def size_file(name):
    """nom du fichier ---> taille du fichier en octet"""
    fichier = open(name,"rb")
    size = 0
    i = fichier.readline()
    while i != "":
        size += len(i)
        i = fichier.readline()
    fichier.close()
    return size

#:::::::::::::::::::::::::::::::::::::::::::::::::
def conv_oct(valeur,unite = ""):
    """valeur en octet[,unite = 'o','k','m' ou 'g'] ---> valeur en o, ko ou mo"""
    if float(valeur)/1024 < 1 and unite == "" or unite == "o":
        return str(valeur)+" o"
    elif float(valeur)/1024 < 1024 and unite == "" or unite == "k":
        return str(float(valeur)/1024)+" ko"
    elif float(valeur)/(1024*1024) < 1024 and unite == "" or unite == "m":
        return str(float(valeur)/(1024*1024))+" Mo"
    else:
        return str(float(valeur)/pow(1024,3))+" Go"

#:::::::::::::::::::::::::::::::::::::::::::::::::
def size_dir(name=getcwd()):
    """nom du dossier ---> taille du dossier"""
    size = 0
    p = find_allpath(name)
    path = []
    for i in p:
        if not path.count(i):
            path.append(i)

    for p in path:
        fichiers = find_dirfile(p)[1]
        for f in fichiers:
            size += size_file(p+"/"+f)

    return size

#:::::::::::::::::::::::::::::::::::::::::::::::::
def nbr_dirfile(name=getcwd()):
    """path---> [nbr dossiers,nbr fichiers]"""
    nbr_fichier = 0
    nbr_dossier = 0
    p = find_allpath(name)
    path = []
    for i in p:
        if not path.count(i):
            path.append(i)

    for p in path:
        dirfile = find_dirfile(p)
        nbr_dossier += len(dirfile[0])
        nbr_fichier += len(dirfile[1])

    return [nbr_dossier,nbr_fichier]

#:::::::::::::::::::::::::::::::::::::::::::::::::
def tronquer(valeur,ou=0,_type="ajust"):
    """valeur, ou<0 x.xxx|x, ou>0 xx|xx.xx, ou=0 xxxx.|xxx, _type=type de troncature
"a"ou"ajust"arrondi, "c","ceil" ou "f","floor"
---> float ou<0 ou int ou>=0"""
    valeur=str(float(valeur)).split(".")
    if ou>=len(valeur[0]):
        valeur[0] = "0"*(ou-len(valeur[0])+1)+valeur[0]
    if -ou>=len(valeur[1]):
        valeur[1] = valeur[1]+"0"*(-ou-len(valeur[1])+1)
    if ou>0:
        val = list(valeur[0])
        val.reverse()
        test = int(val[ou-1])
        val = val[ou:len(valeur[0])]
        if _type!="f" and _type!="floor":
            val.reverse()
            if (_type=="c" or _type=="ceil") and test> 0 or (_type!="a" or _type!="ajust") and test>= 5:
                val = str(int("".join(val))+1)
            else:
                val = "".join(val)
        elif _type=="f" or _type=="floor":
            val.reverse()
        return int("".join(val))
    
    elif ou<0:
        val = valeur[1][:-ou]
        if _type!="f" and _type!="floor":
            test = int(valeur[1][-ou])
            lenght = len(val)
            if (_type=="c" or _type=="ceil") and test> 0  or (_type!="a" or _type!="ajust") and test>= 5:
                val=list(val)
                val = list(str(int("".join(val))+1))
            if lenght < len(val):
                valeur[0] = str(int(valeur[0])+1)
                val = "".join(val[1:len(val)])
            else:
                valeur[0] = str(int(valeur[0]))
                val = int_len("".join(val[0:len(val)]),-ou)

        elif _type=="f" and _type=="floor":
            val=valeur[1][:-ou]
        return float(".".join([valeur[0],val[:-ou]]))
    else:
        if _type!="f" and _type!="floor":
            if (_type=="c" or _type=="ceil") and int(valeur[1][0])> 0  or (_type!="a" or _type!="ajust") and int(valeur[1][0])>= 5:
                valeur[0] = str(int(valeur[0])+1)
        return int(valeur[0])

#:::::::::::::::::::::::::::::::::::::::::::::::::
def int_len(nombre,taille=2):
    """ int, lenght ---> str de longueur >= taille"""
    if taille-len(str(nombre)) > 0:
        return "0"*(taille-len(str(nombre)))+str(nombre)
    else:
        return str(nombre)
#:::::::::::::::::::::::::::::::::::::::::::::::::
def conv_octm(valeur,debit=128,unite="m"):
    """valeur en octet, debi en kb/s , unite = "m" ou "ms" ---> temps en mm:ss ou ms"""
    
    if unite != "ms":
        return conv_time(int(tronquer(valeur / (debit/8),3,"f")))
    else:
        return valeur / (debit/8)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def conv_msoct(valeur,debit=128):
    """valeur en ms, debit en kb/s ---> valeur en octet"""
    return valeur * (debit/8)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def conv_time(valeur,unite="s",conv="m"):
    """temps en unite= "s", "m" ou "h"---> temps en conv = "s", "m" ou "h" """
    if unite == "h":
        valeur = valeur * 3600
    elif unite == "m":
        valeur = valeur * 60
        
    if conv == "s":
        return valeur
    if conv == "h":
        h = valeur / 3600
        m = valeur  / 60 % 60
    else:
        m = valeur / 60
    s = valeur % 60
    if conv == "h":
        return int_len(h)+":"+int_len(m)+":"+int_len(s)
    else:
        return int_len(m)+":"+int_len(s)

#:::::::::::::::::::::::::::::::::::::::::::::::::
def conv_ms(string):
    """string de la forme hh:mm:ss ---> int ms"""
    liste = string.split(":")
    liste.reverse()
    ms = 0
    for i in range(len(liste)):
        ms += int(liste[i])*pow(60,i)
    return ms * 1000

#:::::::::::::::::::::::::::::::::::::::::::::::::
def get_nbrpre(limite=100):
    i=2
    try:
        nbrpre = open("nbr pre.txt","r")
        nombre_premier=[]
        i=0
        for n in nbrpre.readlines():
            if i<limite:
                i+=1
                n = n.replace("\n","")
                if n != "":
                    nombre_premier.append(int(n))
            else:
                break
        i=nombre_premier[-1]
        nbrpre.close()
    except:
        nombre_premier=[2,3]
    i_premier=0
    limite_premier =0
    while i <= limite:
        i_premier=0
        limite_premier = len(nombre_premier)
        
        while i%nombre_premier[i_premier] != 0:
            i_premier+=1
            
            if i_premier == limite_premier:
                nombre_premier.append(i)
                break        
        i+=1
    return nombre_premier
   
#:::::::::::::::::::::::::::::::::::::::::::::::::
def write_nbrpre(limite=100):
    i=2
    try:
        nbrpre = open("nbr pre.txt","r")
        nombre_premier=[]
        for n in nbrpre.readlines():
            n = n.replace("\n","")
            if n != "":
                nombre_premier.append(int(n))
        i=nombre_premier[-1]
        nbrpre.close()
        nbrpre = open("nbr pre.txt","a")
    except:
        nbrpre = open("nbr pre.txt","w")
        nbrpre.write("2\n3\n")
        nombre_premier=[2,3]
    i_premier=0
    limite_premier =0
    while i <= limite:
        i_premier=0
        limite_premier = len(nombre_premier)
        
        while i%nombre_premier[i_premier] != 0:
            i_premier+=1
            
            if i_premier == limite_premier:
                nombre_premier.append(i)
                nbrpre.write(str(i)+"\n")
                break        
        i+=1
    nbrpre.close()

#:::::::::::::::::::::::::::::::::::::::::::::::::
def PGCD(a,b):
    r = 0
    while a % b:
        r = a % b
        a, b = b, r
    if not r:
        r = b
    return r

#:::::::::::::::::::::::::::::::::::::::::::::::::
def racine(x,n=2):
    if n:
        return pow(x,1.0/n)
    else:
        return "n == 0"

#:::::::::::::::::::::::::::::::::::::::::::::::::
def classer(iterable,_type_=0):
    """classe la liste en decroissant(_type_=0) ou en croissant(_type_=1)"""
    liste, classement = [], []
    for i in iterable:liste.append(i)
    while len(liste) > 1:       
        classement.append(min(liste))
        liste.remove(min(liste))   
    classement.append(liste[0])
    if _type_:classement.reverse() 
    return classement

#=======================================================================================================
def get_key(dico,x):
    for key in dico.keys():
        if dico[key] == x:
            return key
