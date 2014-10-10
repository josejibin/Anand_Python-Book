def json_encode(data):
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    elif isinstance(data,dict):
        e='{'        
        for d in data:
          e+=json_encode(d)
          e+=":"
          e+=json_encode(data[d])+','
        e=e[:-1]
        e+='}'
        return e  
         
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))

def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s
a=json_encode([3,4,'f','g',{'h':3,'y':6}])
print a
