# Structure Generator 

The purpose of this generator is to create a procedural structure. The way this will work will depend on the nodes that will be 
attached to this Node. For this purpose additional generators will be created like section generators, composition managers, etc..

This structure will be generated taking into account the scale and height of the building. 
For each section, a minimum height will be defined to compute the number of sections.

Sections could be optional. First and last section are optional, since a building could not have any of those sections. 
Also the separation between the floors is also optional.

1. Inputs
		
1.1 First input (Shape)

The structure Generator will allow the possibility to accept different type of inputs. The input will be used to generate the shape and the form of the building.
	- Shape that will be repeated along an axis. 
	- Polygon Geometry (block) with the overal shape the the building will have
Both inputs, shape and block could be also modified with a ramp so the shilouette.
	
The structure generator will be composed of different sections. 
Examples of sections will be: First Floor, shop facades, Roof, building floors, separation between buildings, special floors, etc... 
	
1.2 Second Input (Generators)
		
The structure could also admit another kind of inputs so they will be used to stamp them along the entire building. This could be stairs, pipes, ivys, etc..
This could be done inside or outside the main loop that will generate the different sections.

1.3 Third Input (neighbours)

This will be the surrounded geometry that will be near this structure. This inputs is optional, and it will be useful to know the sections and
parts of the section that will be hidden or not populated. In order to do this, for each section this node will determine the areas and parts that
won't have anything or there is going to be another thing like stair, pipes, etc..

2. Parameters

- Random Seed
- Type of Input Geomemtry (Shape or Block)
- Lattice (Deform the geometry)

- Min section size
- Top section
- Bottom section
- Height (if not block input geometry)

- Use Input 3 
	True. The node will compute (by inference) the intersection with other geometry to know if that size it's going to be usable or not
			   Also the entrance will be also determined by using the proper side so the geoemtry will face to the correct direction.
	False. The node will allow to randomilly determine these characteristics and also allows to specify by parameters these parameters.

	- Min distance. This will determine the min distance between the buildings, so the section will be empty
	- Orientation. This will determine if the orientation. A bulding could be orientated in different directions...
	   
- Global settings. (experimental)
	Some global setting that will be propaged for all the generatos...
	With this I mean the type of windows, global seed, height of the windows, level of detail, textures, etc..
		   
3. Functionality

Additionally this node will allow the possibility to create additional features that will be used globallty to the building instead being determined
by each section. In order to do this the node will tell to the section generator which parts of the section mustn't be populated. This will be similar
when detection if a part of the section is intersecting with another building.

Could be interesting to create dynamically the number of sections to populate the buildings. However by default the tool will only allow the basic
sections that could be found in a simple building.




