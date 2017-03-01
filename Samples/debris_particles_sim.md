

This simulation use particles and key-animation to direct the simulation and the forces applied.

This imulation used rigid pody solver and finite solver. So this can be applied to a simulation where you want both debris to be simulated.

The force uses the velocity to direct the wind, so the final effect it seems a breath that propagates through the ground in time. This wind advect the particles and at some point the particles stop and fall to the ground using the gravity.



PArticles

This Solver will accumulate the groups at frame step. Since it's a linear workflow the attributes amd groups will be overwritten by the new ones. In order to be able to accumulate the values it's needed to use the Solver SOP.

The particles will have velocity, forces and torque. These attributes will be used later for the simulation and the advection part.

![](https://github.com/jsa4000/SideFX-HOUDINI/blob/master/Samples/Images/debris_particles_sim-particlesSOP.jpg)


![](/Images/debris_particles_sim_particlesSOP].jpg)

![](/Images/debris_particles_sim_particlesSOP].jpg)