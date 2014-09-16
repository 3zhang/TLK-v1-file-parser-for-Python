# -*- coding: utf-8 -*-

#Author 3Zhang

import struct

b2i=lambda bstr:struct.unpack('i',bstr)[0]
b2h=lambda bstr:struct.unpack('h',bstr)[0]
i2b=lambda i:struct.pack('i',i)
h2b=lambda i:struct.pack('h',i)


#This is the version information of the header. Do not edit.
HEADER_C=b'\x54\x4c\x4b\x20\x56\x31\x20\x20\x00\x00'
COLORRED="\033[01;31m{0}\033[00m"


#a class to store each entry
class entry:
    def __init__(self,ent,n,string=None):
        self.No=n
        self.entype=b2h(ent[:2])
        self.soundinfo=ent[2:18]
        self.offset=b2i(ent[18:22])
        self.size=b2i(ent[22:])
        self.string=string
        
    def __repr__(self):
        return repr((self.No,self.entype,self.soundinfo,self.offset,self.size,self.string.decode('utf-8')))
    
    def __eq__(self, other):
        return (self.No,self.entype,self.soundinfo,self.offset,self.size,self.string) \
            == (other.No,other.entype,other.soundinfo,other.offset,other.size,other.string)


#read a tlk file. return a list of entries
def readialog(filepath):
    with open(filepath,'rb') as file:
        dg=file.read()
    header=dg[:18]
    str_o=b2i(header[14:18])
    strings=dg[str_o:]
    entries=dg[18:str_o]
    entry_l=[entries[i:i+26] for i in range(0,len(entries),26)]
    entry_l2=[entry(ent,i) for i,ent in enumerate(entry_l)]
    for i,ent in enumerate(entry_l2):
        entry_l2[i].string=strings[ent.offset:ent.offset+ent.size]
    return entry_l2
        
#Edit your dialog here. Note that string for each entry needs to be decode.
#Also, after you edit the strings, you need to encode them to binary strings.


#sort a list of entries and refresh its size and offset. You must do this after you finish editing the strings.
def refreshdialog(entryl):
    if sum([not isinstance(ent.string,bytes) for ent in entryl])>0:
        raise TypeError('String must be encoded to bytes!')
    entryl.sort(key=lambda x:x.No)
    if [ent.No for ent in entryl]!=list(range(0,len(entryl))):
        print(COLORRED.format('Warning: List index is not equal to stringref index!'))
    offset=0
    for i,ent in enumerate(entryl):
        size=len(ent.string)
        entryl[i].size=size    
        entryl[i].offset=offset if size>0 else 0
        offset+=size
        

#You must refresh the list of entries before you write them to file.
def writedialog(entryl,filepath):
    length=i2b(len(entryl))
    entries=[]
    for ent in entryl:
        entype=h2b(ent.entype)
        soundinfo=ent.soundinfo
        offset=i2b(ent.offset)
        size=i2b(ent.size)
        entb=entype+soundinfo+offset+size
        entries.append(entb)
    entries=b''.join(entries)
    soffset=i2b(18+len(entries))
    header=HEADER_C+length+soffset
    strings=[ent.string for ent in entryl]
    strings=b''.join(strings)
    dialog=header+entries+strings
    with open(filepath,'wb') as file:
        file.write(dialog)
    
        
    

        


