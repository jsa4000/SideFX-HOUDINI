# Building Generator

1. List of building types

- A list of structural structure types and forms of architecture.

    - Agricultural buildings
    - Commercial buildings
    - Residential buildings
    - Medical buildings
    - Educational buildings
    - Government buildings
    - Industrial buildings
    - Military buildings
    - Parking structures and storage
    - Religious buildings
    - Transport buildings
    - Non-buildings
    - Infrastructure
    - Power Providers
    - Others

Following a link to the Wikipedia:
> https://en.wikipedia.org/wiki/List_of_building_types


2. Idea and Motivations

The idea is to build a procedural system that allows the creation of structures, like buildings, factories, towers, etc... 
The structures are created by using many different components and generators. 
The idea is to include different components and assets that can change the look and composition of the elements inside each structure.  
This components could be assets, procedural geometry (sweep, revolve, arrays,), imported models (statics), extrusions, etc..

3. Basic Nodes

	NOTES:  
	
	Always try to maintain Scale for all elements.
	Try to use a standard way of work for settings up the assets into the correct axis, orientation and position.
	The idea is to build an structure that could be reused for any pourpose and arquitectural type.
	Use a Global Seed so the sections and some of its characteristics will be maintained along its construction. (e.j. type of windows, style, architecture, etc...)
	
3.1 Structure Generator (3 Inputs)

	This structure will be generated taking into account the scale and height of the building. 
	For each section, a minimun height will be defined to compute the number of sections.
	
	Sections could be optional. First and last section are optional, since a building could not have any of those sections. 
	Also the separation between the floors is also optional.
		
3.1.1 First input (Shape)

	The structure Generator will allow the possibility to accept different type of inputs. The input will be used to generate the shape and the form of the building.
		- Shape that will be repeated along an axis. 
		- Polygon Geometry (block) with the overal shape the the building will have
	Both inputs, shape and block could be also modified with a ramp so the shilouette.
		
	The structure generator will be composed of different sections. 
	Examples of sections will be: First Floor, shop facades, Roof, building floors, separation between buildings, special floors, etc... 
		
3.1.2 Second Input (Generators)
		
	The structure could also admit another kind of inputs so they will be used to stamp them along the entire building. This could be stairs, pipes, ivys, etc..
	This could be done inside or outside the main loop that will generate the different sections.

3.1.3 Third Input (neighbours)

	This will be the surrounded geometry that will be near this structure. This inputs is optional, and it will be useful to know the sections and
	parts of the section that will be hidden or not populated. In order to do this, for each section this node will determine the areas and parts that
	won't have anything or there is going to be another thing like stair, pipes, etc..

3.1.4 Parameters

	1. Random Seed
	2. Type of Input Geomemtry (Shape or Block)
	3. Lattice (Deform the geometry)
	
	4. Min section size
	5. Top section
	6. Bottom section
	7. Height (if not block input geometry)
	
	4. Use Input 3 
		4.1 True. The node will compute (by inference) the intersection with other geometry to know if that size it's going to be usable or not
				   Also the entrance will be also determined by using the proper side so the geoemtry will face to the correct direction.
		4.2 False. The node will allow to randomilly determine these characteristics and also allows to specify by parameters these parameters.

		- Min distance. This will determine the min distance between the buildings, so the section will be empty
		- Orientation. This will determine if the orientation. A bulding could be orientated in different directions...
		   
	5. Global settings. (experimental)
		Some global setting that will be propaged for all the generatos...
		With this I mean the type of windows, global seed, height of the windows, level of detail, textures, etc..
		   
3.1.5 Functionality

	Additionally this node will allow the possibility to create additional features that will be used globallty to the building instead being determined
	by each section. In order to do this the node will tell to the section generator which parts of the section mustn't be populated. This will be similar
	when detection if a part of the section is intersecting with another building.

	Could be interesting to create dinamically the number of sections to populate the buildings. However by default the tool will only allow the basic
	sections that could be found in a simple building.
	
		
3.2 Section Generator (1 Input)

	The section will be part of the Structure generator. This will be used for the structure generator to add the different elements into each section.
	In order to do this, this node needs to know the Structure generator that will be connected to. To simplify this task a button called Find has been used
	to locate the first generator that it's connected. This is because we can have a Merge ortransform node in between so the could be not connected directly.
	
	Each generator will be used for a specified section type defined in the structure. This means the number of sections generator need the be the same as the sections id.
	
	Since, the section generator could be behave different depending on the current section, this must be overwritten or specialized depending on the needs.


3.3 Composition Manager (2 Inputs)

	
		
	
4. Future Proposals

4.1 Machine Learning. 

	For future proposal the integration of machine learning models like Neural Networks to create procedural assets based on already existing knowledge.
	The machine learning feature will use an existing supervised model, already trained, which decide how, when and where to place each element.
	
	This will be done using Python for the training process and the explotation process.

4.2 Real Satellite Data (GIS)

	The idea is to recreate a real city by using Geographic Information System (GIS). 
	This information will be created like layers into the system with the streets, roads, green areas, residencial areas, lakes, etc..
	Also, this information will be useful to get the shape and distribution of the areas and buildings inside a city.
	
4.3 City Polulation

	The idea with this asset is to be able to integrate this asset into the creation of an entire city. 
	This proposal is similar to the previous one, however this asset will populate the city with additional details such as trees, cars, people, traffic lights, 

 