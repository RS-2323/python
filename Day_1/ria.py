Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\Om\Desktop\Ria(Shell.py)\$.py ==============
enter any input>>>5
$
>>> newstr = "monty python"
>>> newstr = [monty python]
SyntaxError: invalid syntax
>>> newstr = ["monty python"]
>>> newstr[::2]
['monty python']
>>> newstr[::-1]
['monty python']
>>> newstr[::1]
['monty python']
>>> newstr[::3]
['monty python']
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> newstr[::-2]
['monty python']
>>> len(
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> len(newstr)
1
>>> newstr = "monty python"
>>> len(newstr)
12
>>> newstr[::3]
'mtph'
>>> newstr[::-1]
'nohtyp ytnom'
>>> newstr[::2]
'mnypto'
>>> newstr[::-2]
'nhy to'
>>> newstr.find('r')
-1
>>> newstr.find(' ')
5
>>> 
KeyboardInterrupt
>>> newstr.find('t')
3
>>> newstr = "monty python"
>>> 
>>>  newstr = "monty python"
 
  File "<pyshell#19>", line 2
    newstr = "monty python"
    ^
IndentationError: unexpected indent
>>> newstr = "monty python"
>>> newstr.find('t')
3
>>> newstr.lstrip()
'monty python'
>>> newstr.rstrip()
'monty python'
>>> newstr.split()
['monty', 'python']
>>> 
KeyboardInterrupt
>>> newstr.strip()
'monty python'
>>> newstr.index('M')

Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    newstr.index('M')
ValueError: substring not found
>>> newstr.index('m')
0
7
>>> newstr.index('m')
0
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getslice__', '__gt__', '__hash__', '__init__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '_formatter_field_name_split', '_formatter_parser', 'capitalize', 'center', 'count', 'decode', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'index', 'isalnum', 'isalpha', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> dir(int)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> dir(bool)
['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__', '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__', '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__', '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
>>> dir(float)
['__abs__', '__add__', '__class__', '__coerce__', '__delattr__', '__div__', '__divmod__', '__doc__', '__eq__', '__float__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getformat__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__int__', '__le__', '__long__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__nonzero__', '__pos__', '__pow__', '__radd__', '__rdiv__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rmod__', '__rmul__', '__rpow__', '__rsub__', '__rtruediv__', '__setattr__', '__setformat__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', 'as_integer_ratio', 'conjugate', 'fromhex', 'hex', 'imag', 'is_integer', 'real']
>>> dir(None)
['__class__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
>>> help(str.swap)

Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    help(str.swap)
AttributeError: type object 'str' has no attribute 'swap'
>>> help(str.swapcase)
Help on method_descriptor:

swapcase(...)
    S.swapcase() -> string
    
    Return a copy of the string S with uppercase characters
    converted to lowercase and vice versa.

>>> 
