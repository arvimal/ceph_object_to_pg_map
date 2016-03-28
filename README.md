# pg_id_calc.py
Ceph Object to Placement Group mapper

* This program mimics how Ceph maps an object to a placement group.

* The client side intelligence of Ceph chunks the data to a specific size,
usually 4MB for RGW and RBD. These objects are then hashed to a hexadecimal value,
and then divided by the number of Placement Group. The resulting modulo is appended
to the Pool ID, and that result value is taken as the Placement Group.

* This program takes the hash value, the number of Placement Groups in the pool, and the Pool ID.

* I've not added the intelligence on splitting the file to 4MB (or a configurable size) chunks yet,
and hashing it.
