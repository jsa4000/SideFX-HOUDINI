# Section Composite

This node will be used for place assets or objects into a section. 

For the placement will be reqired to set some initial inputs and parameters so the composition
will be defined. However, all the operations will be done using procedural paradigm to determine
the current position, patterns, size, etc..

The section composite will be used for each asset of object that will be used to populate the main structure.
Each section composite will get a section which will be used to place the objects and scattered with procedural rules.

Some prior considerations:

- Area, min_size, max_size, min_instances, max_instances, etc. will be used to limit and set some initial characteristic for the
current section_compostite to create.

- The initial section must have the geoemtry where the assets will be scattered through. This will mean this structure will need to generate 
two outputs, one with the scattered objects and another will the geoemetry removing the used part.
The previous operation could be done for the section_generator node, so it will remove the used geometry. However the section_composite
must allow to decide if the scattered assets will use or note the left spaces or the entire thing.

1. Inputs



2. Parameters


3. Machine Learning

For future implementations it will be useful to use Machine Learning techniques to determine the positions of 
the assets and objects. The position will be computed using Generative or Discriminative Neural Networks based
on existing facades. Depending on the trained dated set the result will be different.

The Neural Network must learn characteristics of the architectures and faced of the images and the result must
be positions (TOP-LEFT) with the size (1m, 0.25, etc..), rectangle (TOP, BOTTOM, LEFT, RIGHT), number of repetitions (1,2,3), 
asset to use for each case, etc..

	