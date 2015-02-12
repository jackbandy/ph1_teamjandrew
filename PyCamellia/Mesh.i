%module Mesh
%{
#include "Mesh.h"
%}

%include "std_string.i"
%include "std_set.i"
%include "std_vector.i"

namespace std {
  %template(IntVector) vector<int>;
  %template(UnsignedSet) set<unsigned>;
 }

typedef unsigned GlobalIndexType;

using namespace std;

%nodefaultctor Mesh;
class Mesh{
public:
  void saveToHDF5(string filename);
  int cellPolyOrder(GlobalIndexType cellID);
  set<GlobalIndexType> getActiveCellIDs();
  int getDimension();
  void hRefine(const set<GlobalIndexType> &cellIDs);
  GlobalIndexType numActiveElements();
  GlobalIndexType numFluxDofs();
  GlobalIndexType numFieldDofs();
  GlobalIndexType numGlobalDofs();
  GlobalIndexType numElements();
  void pRefine(const set<GlobalIndexType> &cellIDsForPRefinements);
  void registerSolution(SolutionPtr solution);
  vector<unsigned> vertexIndicesForCell(GlobalIndexType cellID);
  vector< vector<double> > verticesForCell(GlobalIndexType cellID);
  void registerSolution(SolutionPtr solution);
  void unregisterSolution(SolutionPtr solution);
};

class MeshPtr {
public:
  Mesh* operator->();
};

