%module IP
%{
#include "IP.h"
#include "Function.h"
%}

%include "std_string.i"
%include "std_map.i"

namespace std {
%template(map_int_FunctionPtr) map<int, FunctionPtr>;
}

class IP{
public:
IP();
void addTerm(LinearTermPtr a);
void addTerm(VarPtr v);
LinearTermPtr evaluate(std::map< int, FunctionPtr> &varFunctions);
};

class IPPtr {
public:
  IP* operator->();
};
