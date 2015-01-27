%module BF
%{
#include "BF.h"
%}

%include "std_string.i"

class BF{
public:
};

class BFPtr {
public:
  BF* operator->();
};
