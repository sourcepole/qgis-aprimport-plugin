#ArcView APR file parser for Yapps
#http://theory.stanford.edu/~amitp/yapps/yapps2/manual/yapps2.html

#Helper for generate data structure for an entry like:
#(AVDict.4655
#        InternalName:   "Hydrologic Modeling v1.1 (sample)"
#        Key:    4656
#        Key:    4657
#        Value:  2688
#        Value:  4658
#)
#
# -> {'tag': 'AVDict', 'id': 4655, 'properties': {'InternalName': 'Hydrologic Modeling v1.1 (sample)', 'Value': ['2688', '4658'], 'Key': ['4656', '4657']}}

def add_property(properties, name, value):
    if properties.has_key(name):
        val = properties[name]
        if hasattr(val, "append"):
            val.append(value)
        else:
            properties[name] = [val, value]
    else:
        properties[name] = value

%%
parser AprParser:
    ignore:     '[ \t]+'
    token EOL:  '\r?\n'
    token INT:  '[0-9]+'
    token NUM:  '[-0-9.xa-fA-F]+'
    token NAME: '[a-zA-Z1-9]+'
    token STR:  r'([^\\"]|\\.)*' #'([^\\\\"]|\\\\.)*'
    #http://ksamuel.pythonanywhere.com/

    rule apr:      "/" NUM EOL              {{ entries = [ NUM ] }}
                   (
                   entry EOL+               {{ entries.append(entry) }}
                   )* "$"                   {{ return entries }}
    rule entry:    '\(' NAME "\." INT EOL   {{ e = {'tag': NAME, 'id': int(INT), 'properties': {} } }}
                   (
                     NAME ":" value EOL     {{ add_property(e['properties'], NAME, value) }}
                   )* EOL* '\)'             {{ return e }}
    rule value:    '"' STR '"'              {{ return STR }}
                   |                        {{ nums = [] }}
                   (                        
                     NUM                    {{ nums.append(NUM) }} #eval(NUM)
                   )+                       {{ return nums if len(nums)>1 else nums[0] }}
