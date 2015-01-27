%module IP
%{
#include "IP.h"
%}

%include "std_string.i"

class IP{
public:
};

class IPPtr {
public:
  IP* operator->();
};
