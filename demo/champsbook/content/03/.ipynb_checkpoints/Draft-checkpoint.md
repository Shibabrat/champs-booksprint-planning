---
title: Chapter
author:
- 'Rafael Garcia-Meseguer'
output:
  pdf_document:
    fig_caption: yes
    fig_height: 1
  html_document:
    fig_caption: yes
    fig_height: 1
bibliography: myBib.bib
csl: elsevier-without-titles.csl
---

## Introduction

<font color='red'>(This will be the introduction)</font>

### Equations for the system

Our model potential (see @fig:ModelFig) consists of a one-dimensional double well oscillator that represents the reactive system, coupled to a one-dimensional harmonic oscillator representing the bath. The only coupling between the two oscillators is a Lennard-Jones-like repulsion potential term. Consequently, this model is appropriate only for nonpolar systems; our concern here is the consequence of non-bonded interactions between solvent and solute, not the more commonly studied polar interactions.

![Schematic representation (left) and definitions (right) of the model system used in our study.](SB_model.png)

The Hamiltonian that describes the system is as follows:

$$ H(\mathbf{x})=H(\mathbf{r},\mathbf{p})=\frac{p_1^2}{2\mu_1}+\frac{p_2^2}{2\mu_2}+\sum_{j=1}^{5} c_j r_1^{j-1}+c_6 (c_7-r_2 )^2+\frac{c_8}{(r_2-r_1 )^{12}} $${#eq:modelEq}

where the subscripts 1 and 2 refer to the reactive system and bath oscillators respectively; $r=(r_1,r_2 )$ is the position of the two oscillators and $p=(p_1,p_2 )$ represents the conjugate momenta. The reduced mass of each oscillator is represented by $\mu$, and c are coefficients whose values are listed in @fig:ModelFig. The potential energy can be divided between $\sum_{j=1}^{5} c_j r_1^{j-1}$ as the potential of the reactive system, $V_2=c_6 (c_7-r_2 )^2$ as the potential of the bath and $V_{int}=c_8⁄(r_2-r_1 )^{-12}$ as the interaction between the two; hence $V=V_1+V_1+V_{int}$. The potential of the reactant, shown in @fig:PESFig, is chosen to have a minimum at $r_1=1.0$ and a second one at $r_1=2.0$ , with respective potential energies $V_1=0.0$ and $V_1=-10$. The maximum energy is at $r_1=1.33867$ and $V_1=2.0$. The full potential, shown in @fig:PESFig, has a saddle point at $r_1=1.36561$ and $r_2=2.161769$ at $V=3.47291$. The "reactant" minimum occurs at $r_1 = 0.98779$, $r_2 = 1.80661$, $V = 0.77040$. The "product" minimum occurs at $r_1 = 1.98517$, $r_2 = 2.75642$, $V = -6.66284$.

![(Left)Reactive system's potential energy profile. (Right) Contours of the full potential energy surface. The contours are depicted in the $-7 \leq V \leq 6$ interval.](PES.png){#fig:PESFig width=100%}

## Phase Space Structures

<font color='red'>(Here I will explain that for this problem I'll be focusing on the PODS)</font>

### Periodic Orbit Dividing Surface

<font color='red'>(Explanation of PODS)</font>

One of the reasons for choosing this system was the relative ease on computing the periodic orbits that define the PODSs. These calculations (and all the ones that will follow) were done at an energy of 3.691966889, i.e. slightly above the energy of the saddle point.

In order to understand the properties of the trajectories that depart from the DS we need to sample its points in phase space. The procedure, applicable to a 2 DoF Hamiltonian system, selects points on a 2D surface with fixed total energy (E), where the periodic orbit forms the one dimensional boundary of the DS. The algorithm is as described in [@JCP2016Maug; @ezra2018sampling]:

1. Locate an unstable PO.
2. Project the unstable PO into configuration space, which gives a curve in configuration space.
3. Choose points on the curve $(x_i,y_i)$ for $i=1,...,N$, where N is the desired number of points. The points are spaced uniformly according to distance along the PO.
4. For each point $(x_i,y_i )$ determine $p_{x_{max},i}$ by solving for $p_x$.

    $$ H(x_i,y_i,p_x,0)=\frac{p_x^2}{2\mu_x}+V(x_i,y_i)=E $${#eq:PODSsampEq}

5. Note that solution of this equation requires $E- V(x_i,y_i ) \ge 0$, and there will be two solutions, $\pm p_{x_{max},i}$.
6. For each point $(x_i,y_i)$ choose points $p_{x_j}$ for $j=1,...,K$, with $p_{x_1}=-p_{x_{max},i}$ and $p_{x_K}=p_{x_{max},i}$ and solve the equation $H(x_i,y_i,p_x,p_y)=E$ to obtain $p_y$.

The geometrical structure of the DS sampled in this manner is a one parameter family of circles. The parameter defining the family is given by the distance along the projection of the PO onto the configuration space from Steps 1-3 in the algorithm above, and the momentum-space circles are given by the following equation obtained from the Hamiltonian:

$$ \frac{p_x^2}{2\mu_x}+\frac{p_y^2}{2\mu_y}=E-V(x_i,y_i) $${#eq:DSGeomEq}

#### Effect of the Solvent Mass

<font color='red'>(...)</font>

In @fig:DSCloseFig (top) we can see the projection of the calculated PODSs in configuration space. @fig:DSCloseFig also includes two approximations to the DS explained in the caption and shows how the three of them respond as $\mu_2$ changes. It can be seen that, for low reduced masses, the approximate DSs are close to the PODS. That is because the bath can rapidly adapt to the position of the reactive system. However, as $\mu_2$ increases the PODS starts to curve and to displace from the approximate DSs, moving closer to the product well.

The geometry of this one parameter family of circles depends on the nature of the projection of the PO into configuration space. In this particular case the PO projections are arcs where a configuration space point on the projection of the PO moves back and forth along the arc. This means that the endpoints of the arc are turning points with $p_x=p_y=0$, where the circles defined by eq. \ref{DSGeomEq} shrink to points. This implies that the geometry of the one parameter family of circles defines a 2D sphere (see @fig:DSCloseFig bottom).

![(Top)Close-up of the PES of the full system, near the saddle point region at different reduced masses of the bath. Each of the axis scales were weighted by the square root of its coordinate mass. The dashed red line is the intrinsic reaction coordinate (IRC). The blue line is DS if one assumes that the reaction coordinate is $r_1$. The red line is the DS projection at the saddle point, which is locally orthogonal to the IRC (It does not look orthogonal because of the choice of axis scales). The green line is the projection of the PO that defines the Dividing surface. (Bottom) Schematic representation of the DS's geometrical structure for the different reduced masses. The yellow structure represents the possible momenta depending of the location in the DS.](PODS_DSshape.png){#fig:DSCloseFig width=100%}

<font color='red'>(Discussion)</font>

#### Checking the Valdity

<font color='red'>(...)</font>

From the sampled trajectories we can measure the time taken to reach a determined region (transit time), in this case the PES minimum identified as the product well. Then we can perform the same calculation but with trajectories starting on the DS defined only with $r_1$ (the blue line in @fig:DSCloseFig). The blue line corresponds to the common choice for solution phase reactions of assigning the transition state location to the PES saddle point, and assuming that the reaction coordinate is entirely determined by the solute. @fig:TransitFig is a representation in phase space of the transit times of trajectories that start on the true and approximate dividing surfaces with different initial $p_\perp$, the momentum normal to the dividing surface. The transit times (calculated as the time for $r_1$ to reach a value greater than that for product minimum) show brighter colors in Figure @fig:TransitFig as the transit time increases. The expected results for a DS is that trajectories starting with negative momenta normal to the dividing surface ($p_\perp<0$), i.e. directed to the reactant well, would take longer to reach the product well than those that start with positive momenta. This is clearly the case for the PODS as can be seen in Figure 6, where $p_\perp=0$ (which corresponds to the PO) provides an exact line of demarcation in the transit times. By contrast, the approximate DS shows long and short transit times on both sides of $p_1=0$. It is interesting to note that those areas where the transit times are long for $p_1>0$ or short for $p_1<0$ correspond to recrossing of trajectories, and that the amount of recrossing gets larger as $\mu_2$ increases. Thus, the approximate DS becomes a poorer and poorer choice for the transition state as the mass of the bath oscillator increases.

![A comparison of trajectory transit times from the DS to the product. (Top) Being the PODS (green DS in @fig:DSCloseFig) and (Bottom) the DS conventional definition of the TS (blue DS in @fig:DSCloseFig). The color scale goes from dark colors for short times to brighter colors for long times. The quantity $p_\perp$ is the momentum perpendicular to the dividing surface, with a positive sign being in the direction of the product.](TransitT.png){#fig:TransitFig width=100%}

The brighter colored bands visible on the reactant sides ($p_\perp <0$) in Figure @fig:TransitFig are associated with the many periodic orbits located in the reactant well. Trajectories that approach these POs can spend a long time before finally crossing over to the product well.

### Lagrangian Descriptors

<font color='red'>(...)</font>

#### Method 1

<font color='red'>(...)</font>

#### Method 2

<font color='red'>(...)</font>

## Applications to multiple DoF problems

<font color='red'>(...)</font>

## References

```python

```
