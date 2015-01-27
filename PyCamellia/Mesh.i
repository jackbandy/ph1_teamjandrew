%module Function
%{
#include "Mesh.h"
%}

%include "std_string.i"

class Mesh{
public:
  void saveToHDF5(string filename);
  int cellPolyOrder(GlobalIndexType cellID);
  set<GlobalIndexType> getActiveCellIDs();
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
};
