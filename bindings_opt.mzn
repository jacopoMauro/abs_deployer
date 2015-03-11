include "table.mzn";
include "alldifferent.mzn";

set of int: locations;
set of int: bindings;
set of int: types;

array[bindings] of locations: prov_port_locations;
array[bindings] of locations: req_port_locations;
array[bindings] of types: prov_port_types;
array[bindings] of types: req_port_types;

array[bindings] of var bindings: bind_req;
array[bindings] of var locations: bind_prov_location;
array[bindings] of var locations: bind_req_location;
array[bindings] of var types: bind_types;

array[bindings,1..3] of int: prov_data = array2d(bindings,1..3,
  [ if i=1 then j else if i=2 then prov_port_types[j] else prov_port_locations[j] endif endif | j in bindings, i in 1..3]);
array[bindings,1..3] of int: req_data = array2d(bindings,1..3,
  [ if i=1 then j else if i=2 then req_port_types[j] else req_port_locations[j] endif endif | j in bindings, i in 1..3]);

constraint alldifferent(bind_req);

constraint forall(i in bindings) (
   table( [i, bind_types[i], bind_prov_location[i]], prov_data));

constraint forall(i in bindings) (
   table( [bind_req[i], bind_types[i], bind_req_location[i]], req_data));


array[bindings] of var 0..1: local_bindings;
constraint forall(i in bindings) (
  bind_prov_location[i] !=  bind_req_location[i] <-> local_bindings[i] == 0);

var int: metric = sum(local_bindings);
solve maximize metric;

output [ if j = 1 then show(bind_req[i]) else show(" ") endif | i in bindings, j in 1..2 ];
% ++ [ "\n", show(metric) ];