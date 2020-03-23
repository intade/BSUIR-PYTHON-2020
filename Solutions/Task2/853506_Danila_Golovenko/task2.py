class MyJson:
    #Сериализация
    def to_json(self, obj):
        if isinstance(obj, (list, tuple)):
            return self._tuple_or_list_to_json(obj)
        elif isinstance(obj, dict):
            return self._dict_to_json(obj)
        else:
            return self._dict_to_json(self._class_to_dict(obj))

    def _tuple_or_list_to_json (self, obj):
        #базовые типы int, float, string, bool, None
        #для лист или тупла
        #для дикта
        #для кастомного класса
        temp_list = []
        for i in obj:
            if isinstance(i, (int, float, str, bool, type(None))):
                temp_list.append(self._basic_type_to_json(i))
            elif isinstance(i, (list, tuple)):
                temp_list.append(self._tuple_or_list_to_json(i))
            elif isinstance(i, dict):
                temp_list.append(self._dict_to_json(i))
            else:
                temp_list.append(self._dict_to_json(self._class_to_dict(i)))
        output_str = ', '.join(temp_list)
        return '[ ' + output_str + ' ]' 

    def _basic_type_to_json(self, obj):
        if isinstance(obj, str):
            return "'{}'".format(obj)
        elif isinstance(obj, type(None)):
            return "none"
        elif isinstance(obj, bool):
            if obj:
                return "true"
            return "false"
        elif isinstance(obj , (int, float)):
            return "{}".format(obj)
        

    def _dict_to_json(self, Dict):
        temp_list = []
        for key, value in Dict.items():
            if isinstance(value, (int, float, str, bool, type(None))):
                temp_list.append(self._jsno_element(key, self._basic_type_to_json(value)))
            elif isinstance(value, (list, tuple)):
                temp_list.append(self._jsno_element(key, self._tuple_or_list_to_json(value)))
            elif isinstance(value, dict):
                temp_list.append(self._jsno_element(key, self._dict_to_json(value)))
            else:
                temp_list.append(self._jsno_element(key, self._dict_to_json(self._class_to_dict(value))))

        output_str = ', '.join(temp_list)
        return '{ ' + output_str + ' }' 

    def _class_to_dict(self, obj):
        fields = [(f, obj.__getattribute__(f)) for f in dir(obj) if not callable(getattr(obj,f)) and not(f.startswith('__') or f.startswith('_'))]
        return dict(fields)

    def _jsno_element(self, k, v):
        return f"'{k}':{v}"

    #Десериализация

    def from_json(self, text=' '):
        if text[0] == '{':
            return self._json_to_dict(text, 1)[0] 
        elif text[0] == '[':
            return self._json_to_list(text, 1)[0]
#        if array_open_bracket or dict_open_bracket:
#            for e in range(sub_start, end):
#                if text[e] == '{':
#                    array_open_bracket = False 
#                    sub_end = e - 1
#                    #вызов функции для дикта
#                elif text[e] == '[':
#                    dict_open_bracket = False
#                    sub_end = e - 1
#                    #вызов функции для листа
#        if array_open_bracket or dict_open_bracket:
#            raise IOError("Неверная строка")

    def _json_to_list(self, text, start):
        output = []
        i = start
        while(i < len(text) - 1): 
            i += 1
            if text[i] == ']':
                return (output, i)
            if text[i] == ' ' or text[i] == ',':
                continue
            if text[i] == '[':
                elem = self._json_to_list(text, i+1)
                output.append(elem[0])
                i = elem[1]

            elif text[i] == '{':
                elem = self._json_to_dict(text, i+1)
                output.append(elem[0])
                i = elem[1]
            else:
                elem = self._json_to_basic(text, i)
                output.append(elem[0])
                i = elem[1]
#        raise IOError("Неверный формат")

    def _json_to_dict(self, text, start):
        output = {} 
        i = start
        while(i < len(text) - 1): 
            i += 1
            if text[i] == '}':
                return (output, i)
            try:
                elem = self._get_token(text, i)
                elem2 = self._get_token(text, elem[1]+1)
                output[elem[0]] =  elem2[0]
                i = elem2[1]
            except IOError as error:
                return (output, int(error.args[0]))
        raise IOError("Неверный формат") 

    def _json_to_basic(self, text, start):
        tokens = []
        quot = False
        isFloat = False
        for i in range(start, len(text)):
            if (text[i] == ':' or text[i] == ' ') and not quot:
                continue
            if ((text[i] == ',' or text[i] == ']' or text[i] == '}') and not quot):
                def toIntOrFloat(s, f):
                    try:
                        if f:
                            return float(s)
                        return int(s)
                    except ValueError:
                        return None 
                switcher = {'true' : True, 'false' : False, 'none' : None}
                str = ''.join(tokens)
                return (switcher.get(str, toIntOrFloat(str, isFloat)), i - 1)
            if (text[i] == "'" and quot):
                return (''.join(tokens), i)
            if text[i] == "'":
                quot = not quot 
                continue
            if text[i] == '.':
                isFloat = True
            tokens.append(text[i])
        raise IOError("Неверный формат")

    def _get_token(self, text, start):
        for i in range(start, len(text)):
            if text[i] == ' ' or text[i] == ',':
                continue
            if text[i] == '}' or text[i] == ']':
                raise IOError("{}".format(i))
            if text[i] == '[':
                return self._json_to_list(text, i+1)
            elif text[i] == '{':
                return self._json_to_dict(text, i+1)
            else:
                return self._json_to_basic(text,i)   
        
            


        

a = MyJson()
b = [5, 6, [45,65], True, False, None, {"sdf": 34}]
d = {5 : "afsd", 54 : 'wqe'}
print(a.to_json(d))
c = a.from_json(a.to_json(d))
print(c)