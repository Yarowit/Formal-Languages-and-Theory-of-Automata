/*
 * Kod maszyny wirtualnej do projektu z JFTT2023
 *
 * Autor: Maciek Gębala
 * http://ki.pwr.edu.pl/gebala/
 * 2023-11-15
*/
#include <iostream>

#include <utility>
#include <vector>

#include "colors.hh"

using namespace std;

extern void run_parser( vector< pair<int,int> > & program, FILE * data );
extern void run_machine( vector< pair<int,int> > & program );

int main( int argc, char const * argv[] )
{
  vector< pair<int,int> > program;
  FILE * data;

  if( argc!=2 )
  {
    cerr << cRed << "Sposób użycia programu: interpreter kod" << cReset << endl;
    return -1;
  }

  data = fopen( argv[1], "r" );
  if( !data )
  {
    cerr << cRed << "Błąd: Nie można otworzyć pliku " << argv[1] << cReset << endl;
    return -1;
  }

  run_parser( program, data );

  fclose( data );

  run_machine( program );

  return 0;
}
