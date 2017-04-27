# Building Generator

1. List of building types

A list of structural structure types and forms of architecture.

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
		

		
3.2 Section Generator (1 Input)

	The section will be part of the Structure generator. This will be used for the structure generator to add the different elements into each section.
	In order to do this, this node needs to know the Structure generator that will be connected to. To simplify this task a button called Find has been used
	to locate the first generator that it's connected. This is because we can have a Merge ortransform node in between so the could be not connected directly.
	
	Each generator will be used for a specified section type defined in the structure. This means the number of sections generator need the be the same as the sections id.
	
	Since, the section generator could be behave different depending on the current section, this must be overwritten or specialized depending on the needs.


3.3 Section Composite (2 Inputs)
	
	
	
3.4 Assets and Objects Generators
	
	
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

 