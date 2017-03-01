## Debris Simulation with Particles Advection

This simulation use **particles** and **key-frame animation** to direct the simulation and the forces applied to it.

This simulation uses **Static Solver** (NULL), **Rigid Body Solver** and **Finite Solver**. 

The simulation uses **Field Force** and **Gravity**. For the field force I will use the velocity to direct the _Attribute force_ (instead using the default force).
The final effect will seem like a wind that propagates through the environment in time, like a Storm or a Breath. Initially, the **field force** will advent the particles, however at some frame the particles stop and fall to the ground using the **Gravity force** instead.

### Ground

![](https://github.com/jsa4000/SideFX-HOUDINI/blob/master/Samples/Images/debris_particles_sim-GroundSOP.jpg)

### Debris Rigid SOP

![](https://github.com/jsa4000/SideFX-HOUDINI/blob/master/Samples/Images/debris_particles_sim-RigidSOP.jpg)

### Debris Finite SOP

![](https://github.com/jsa4000/SideFX-HOUDINI/blob/master/Samples/Images/debris_particles_sim-FiniteSOP.jpg)

###Particles

This Solver will accumulate the groups at frame step. Since it's a linear Workflow the attributes and groups will be overwritten by the new ones. In order to be able to accumulate the values it's needed to use the Solver SOP.
![](https://github.com/jsa4000/SideFX-HOUDINI/blob/master/Samples/Images/debris_particles_sim-particlesSOP.jpg)

The particles will have velocity, forces and torque. These attributes will be used later for the simulation and the advection part.

![](https://github.com/jsa4000/SideFX-HOUDINI/blob/master/Samples/Images/debris_particles_sim-particlesPOP.jpg)



### Simulation

The overall simulation will be composed

![](https://github.com/jsa4000/SideFX-HOUDINI/blob/master/Samples/Images/debris_particles_sim-SimDOP.jpg)

1. Set the Ground Collision
![](https://github.com/jsa4000/SideFX-HOUDINI/blob/master/Samples/Images/debris_particles_sim-RIGIDColDOP.jpg)


![](https://github.com/jsa4000/SideFX-HOUDINI/blob/master/Samples/Images/debris_particles_sim-FINITEvsBulltetDOP.jpg)



2. Set the Field Force (v)
![](https://github.com/jsa4000/SideFX-HOUDINI/blob/master/Samples/Images/debris_particles_sim-FieldForceDOP.jpg)

3 Set the GRavity Force






