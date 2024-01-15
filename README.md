# Obj To Nodebox

A script/mod for converting .obj files to minetest nodeboxes

## Usage

Run the python script `convert.py` with the argument being the path to your .obj file. An optional second argument is a float scalar for the output, since often minetest treats the scale of models differently from nodes.

For example, run ```convert.py models/sample.obj [0.5]```

This will output into the terminal a lua table which can be copied into a mod for use as a nodebox.