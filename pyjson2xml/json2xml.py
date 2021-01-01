#! /usr/local/bin/python

import json
import sys 
from functs import generate_key, read_key, encrypt, decrypt

jsonfile = sys.argv[1]
filename = jsonfile.split('.')[0]

def json2xml(json_obj, Line_spacing=""):
   result_list = list()
   json_obj_type = type(json_obj)
   if json_obj_type is list:
       for sub_elem in json_obj:
           result_list.append(json2xml(sub_elem, Line_spacing))
  
       return "\n".join(result_list)
   if json_obj_type is dict:
       for tag_name in json_obj:
           sub_obj = json_obj[tag_name]
           result_list.append("%s<%s>" % (Line_spacing, tag_name))
           result_list.append(json2xml(sub_obj, "\t" + Line_spacing))
           result_list.append("%s</%s>" % (Line_spacing, tag_name))

       return "\n".join(result_list)
   return "%s%s" % (Line_spacing, json_obj)

jsonfile = open(filename+'.json', "r")
json_obj = jsonfile.read()
xml_doc = json2xml(json.loads(json_obj))
xml_file = open(filename + '.xml', "w")
xml_file.write(xml_doc)
generate_key()

