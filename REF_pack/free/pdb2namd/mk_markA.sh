#!/bin/bash

cat > tcl <<EOF

mol new pep_250ns.pdb

set sel [atomselect top "chain A and resid 3 and not name C CA N O HN HA CB"]
foreach name [\$sel get name] {
  set sel [atomselect top "chain A and resid 3 and name \$name"]
  \$sel set name \${name}A
}
set sel [atomselect top "all"]
\$sel writepdb pep_250ns_1.pdb
quit
EOF

vmd -dispdev text -e tcl

