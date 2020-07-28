#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _ca_a1g_reg();
extern void _ca_a1h_reg();
extern void _ca_a1i_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," ca_a1g.mod");
fprintf(stderr," ca_a1h.mod");
fprintf(stderr," ca_a1i.mod");
fprintf(stderr, "\n");
    }
_ca_a1g_reg();
_ca_a1h_reg();
_ca_a1i_reg();
}
