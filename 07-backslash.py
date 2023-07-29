>>> import re
>>> re.search("\w+,", "one,two")
<re.Match object; span=(0, 4), match='one,'>
>>> re.search("\\w+,", "one,two")
<re.Match object; span=(0, 4), match='one,'>
>>> re.search("\w+\\two", "one\\two")
>>> re.search("\w+\\\\two", "one\\two")
<re.Match object; span=(0, 7), match='one\\two'>
>>> re.search("\w+\\eight", "one\\eight")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/re.py", line 199, in search
    return _compile(pattern, flags).search(string)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/re.py", line 302, in _compile
    p = sre_compile.compile(pattern, flags)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/sre_compile.py", line 764, in compile
    p = sre_parse.parse(p, flags)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/sre_parse.py", line 948, in parse
    p = _parse_sub(source, state, flags & SRE_FLAG_VERBOSE, 0)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/sre_parse.py", line 443, in _parse_sub
    itemsappend(_parse(source, state, verbose, nested + 1,
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/sre_parse.py", line 525, in _parse
    code = _escape(source, this, state)
  File "/Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/sre_parse.py", line 426, in _escape
    raise source.error("bad escape %s" % escape, len(escape))
re.error: bad escape \e at position 3
>>> re.search("\w+\\\\eight", "one\\eight")
<re.Match object; span=(0, 9), match='one\\eight'>
>>> content = r"one\eight"
>>> content
'one\\eight'
>>> re.search(r"\w+\\eight", r"one\eight")
<re.Match object; span=(0, 9), match='one\\eight'>
