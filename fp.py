_true = lambda a, b: a

_false = lambda a, b: b

_if = lambda func: lambda a: lambda b: func(a, b)

_and = lambda a: lambda b: _if(a)(_if(b)(_true)(_false))(_false)

_or = lambda a: lambda b: _if(a)(_true)(_if(b)(_true)(_false))

_not = lambda a: _if(a)(_false)(_true)

_xor = lambda a: lambda b: _and(_or(a)(b))(_not(_and(a)(b)))

print(_if(_true)(1)(2))
print(_if(_false)(1)(2))

print(_and(_false)(_true) == _true)
print(_or(_true)(_true) == _true)
print(_not(_false) == _true)
print(_xor(_true)(_false) == _true)
