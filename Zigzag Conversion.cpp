

#include <iostream>
#include <cstring>
using namespace std;

int
main ()
{
  string s1 = "PAYPALISHIRING";

  int len = s1.length ();
  int rows = 3;
  int col = len / 2;
 
  char a[30], b[10][10];
  for (int l = 0; l < 10; l++)
    {
      for (int k = 0; k < 10; k++)
	{
	  b[l][k] = ' ';
	}
    }
  strcpy (a, s1.c_str ());

  int count = 0, i = 0, j = 0;
  while (j <= col)
    {
      if (j % 2 == 0)
	{
	  while (i <= 2)
	    {
	      b[i][j] = a[count];
	      ++count;
	      ++i;
	    }
	}
      else
	{
	  b[1][j] = a[count];
	  ++count;

	}
      i = 0;
      ++j;



    }
//   for (int j = 0; j < 3; j++)
//     {
//       for (int i = 0; i < 6; i++)
// 	{
// 	  cout << b[j][i];

// 	} cout << "\n";
//     }
    
    for (int i = 0; i < 3; i++)
    {
      for (int j = 0; j < col; j++)
	{
	  cout << b[i][j];

	} cout << "\n";
    }


  return 0;
}
