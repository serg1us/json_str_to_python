import pprint

json_str= '{"Int":777, "Float":3.14, "String":Str, "True":true, "False":false, "Null":null}'

true = True
false = False
null = None

pprint(eval(json_str))
