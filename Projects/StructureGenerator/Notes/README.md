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

- The idea is to build a System that allows the creation of an structure. This structure could be created by many different components by using nodes. This componentes could be assets, procedural geometry, imported models (statics), etc..

3. Basic Nodes

NOTES:  Always try to maintain Scale for all geoemetry created.
		The idea is to build an structure that could be reused for any pouprpose.
		Global Seed so the sections and some of its characteristics will be maintained along the construction. (type of windows, style, architecture, etc...)
			
	
3.1 Structure Generator (2 Inputs)

3.1.1 First input

	The structure Generator will allow the possibility to accept different inputs that will be used to generate the shape and the form of the building.
		- Shape that will be repeated along an axis. 
		- Polygon Geometry (block) with the overal shape the the building will have
	Both inputs, shape and block could be also modified with a ramp so the shilouette.
		
	The structure generator will be composed of different sections. 
	Examples of sections will be: First Floor, shop facades, Roof, building floors, separation between buildings, special floors, etc... 
		
3.1.2 Second Input	
		
	The structure could also admit another kind of inputs so they will be used to stamp them along the entire building. This could be stairs, pipes, ivys, etc..
		
		
.3.2 Section Generator(2 Inputs)

		
	
