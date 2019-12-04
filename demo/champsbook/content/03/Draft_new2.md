---
author:
- 'Rafael Garcia-Meseguer'
bibliography: myBib.bib
csl: elsevier-without-titles.csl
pagetitle: Rafa's Chapter
---
# Chapter

## Introduction

It is well known that for chemical reactions finding the location of the Dividing Surface (DS) is key most rate constant calculation throught the application of Transition State Theory (TST). This Dividing Surface divides the space into reactants and products regions and has the property that any trajectory reaching it from one of this regions will not reach it again before entering the local minima in the other one.

TST is a classical theory developed by Wigner, Eyring, Gwynne Evans and Polanyi;{% cite Wigner1932 Eyring1935 Polanyi1935 Eyring1941 --file myBib %} that calculates the rate of the reaction as the equilibrium flux of reactive trajectories through the DS. The development of TST has been discussed extensively[@TruhlarVTST1980;@PechukasTST1981;@TruhlarVTST2017]

Finding this dividing surface for polyatomic reactions in solution is not an easy task as the dynamic relation between the solvent and the solute is not fully understood. It is not impossible, however, to obtain a good approximation to this DS which will not comply with the no-recrossing condition.

## Equations for the system

Our model potential (see [fig:1](#ModelFig)) consists of a one-dimensional double well oscillator that represents the reactive system, coupled to a one-dimensional harmonic oscillator representing the bath. The only coupling between the two oscillators is a Lennard-Jones-like repulsion potential term. Consequently, this model is appropriate only for nonpolar systems; our concern here is the consequence of non-bonded interactions between solvent and solute, not the more commonly studied polar interactions.

![Schematic representation (left) and definitions (right) of the model system used in our study.](Figures\SB_model.png)
<a id="ModelFig"></a>

The Hamiltonian that describes the system is as follows:

\begin{equation}
H(\mathbf{x})=H(\mathbf{r},\mathbf{p})=\frac{p_1^2}{2\mu_1}+\frac{p_2^2}{2\mu_2}+\sum_{j=1}^{5} c_j r_1^{j-1}+c_6 (c_7-r_2 )^2+\frac{c_8}{(r_2-r_1 )^{12}}
\label{modelEq}
\end{equation}

where the subscripts 1 and 2 refer to the reactive system and bath oscillators respectively; $r=(r_1,r_2 )$ is the position of the two oscillators and $p=(p_1,p_2 )$ represents the conjugate momenta. The reduced mass of each oscillator is represented by $\mu$, and c are coefficients whose values are listed in [fig:1](#ModelFig). The potential energy can be divided between $\sum_{j=1}^{5} c_j r_1^{j-1}$ as the potential of the reactive system, $V_2=c_6 (c_7-r_2 )^2$ as the potential of the bath and $V_{int}=c_8/(r_2-r_1 )^{-12}$ as the interaction between the two; hence $V=V_1+V_1+V_{int}$. The potential of the reactant, shown in [fig:2](#PESFig), is chosen to have a minimum at $r_1=1.0$ and a second one at $r_1=2.0$ , with respective potential energies $V_1=0.0$ and $V_1=-10$. The maximum energy is at $r_1=1.33867$ and $V_1=2.0$. The full potential, shown in [fig:2](#PESFig), has a saddle point at $r_1=1.36561$ and $r_2=2.161769$ at $V=3.47291$. The "reactant" minimum occurs at $r_1 = 0.98779$, $r_2 = 1.80661$, $V = 0.77040$. The "product" minimum occurs at $r_1 = 1.98517$, $r_2 = 2.75642$, $V = -6.66284$.

![(Left)Reactive system's potential energy profile. (Right) Contours of the full potential energy surface. The contours are depicted in the $-7 \leq V \leq 6$ interval.](Figures\PES.png)
<a id="PESFig"></a>

## Phase Space Structures

<font color='red'>(Here I will explain that for this problem I'll be focusing on the PODS)</font>

<font color='red'>(Explanation of PODS)</font>

One of the reasons for choosing this system was the relative ease on computing the periodic orbits that define the PODSs. These calculations (and all the ones that will follow) were done at an energy of $3.691966889$, i.e. slightly above the energy of the saddle point.

In order to understand the properties of the trajectories that depart from the DS we need to sample its points in phase space. The procedure, applicable to a 2 DoF Hamiltonian system, selects points on a 2D surface with fixed total energy (E), where the periodic orbit forms the one dimensional boundary of the DS. The algorithm is as described in {% cite JCP2016Maug ezra2018sampling --file myBib %}:

1. Locate an unstable PO.
2. Project the unstable PO into configuration space, which gives a curve in configuration space.
3. Choose points on the curve $(x_i,y_i)$ for $i=1,...,N$, where N is the desired number of points. The points are spaced uniformly according to distance along the PO.
4. For each point $(x_i,y_i )$ determine $p_{x_{max},i}$ by solving for $p_x$.

    \begin{equation}
    H(x_i,y_i,p_x,0)=\frac{p_x^2}{2\mu_x}+V(x_i,y_i)=E
    \label{PODSsampEq}
    \end{equation}

5. Note that solution of this equation requires $E- V(x_i,y_i ) \ge 0$, and there will be two solutions, $\pm p_{x_{max},i}$.
6. For each point $(x_i,y_i)$ choose points $p_{x_j}$ for $j=1,...,K$, with $p_{x_1}=-p_{x_{max},i}$ and $p_{x_K}=p_{x_{max},i}$ and solve the equation $H(x_i,y_i,p_x,p_y)=E$ to obtain $p_y$.

The geometrical structure of the DS sampled in this manner is a one parameter family of circles. The parameter defining the family is given by the distance along the projection of the PO onto the configuration space from Steps 1-3 in the algorithm above, and the momentum-space circles are given by the following equation obtained from the Hamiltonian:

\begin{equation}
\frac{p_x^2}{2\mu_x}+\frac{p_y^2}{2\mu_y}=E-V(x_i,y_i)
\label{DSGeomEq}
\end{equation}

#### Effect of the Solvent Mass

<font color='red'>(...)</font>

In [fig:3](#DSCloseFig) (top) we can see the projection of the calculated PODSs in configuration space. [fig:3](#DSCloseFig) also includes two approximations to the DS explained in the caption and shows how the three of them respond as $\mu_2$ changes. It can be seen that, for low reduced masses, the approximate DSs are close to the PODS. That is because the bath can rapidly adapt to the position of the reactive system. However, as $\mu_2$ increases the PODS starts to curve and to displace from the approximate DSs, moving closer to the product well.

The geometry of this one parameter family of circles depends on the nature of the projection of the PO into configuration space. In this particular case the PO projections are arcs where a configuration space point on the projection of the PO moves back and forth along the arc. This means that the endpoints of the arc are turning points with $p_x=p_y=0$, where the circles defined by eq. \ref{DSGeomEq} shrink to points. This implies that the geometry of the one parameter family of circles defines a 2D sphere (see [fig:3](#DSCloseFig) bottom).

![(Top)Close-up of the PES of the full system, near the saddle point region at different reduced masses of the bath. Each of the axis scales were weighted by the square root of its coordinate mass. The dashed red line is the intrinsic reaction coordinate (IRC). The blue line is DS if one assumes that the reaction coordinate is $r_1$. The red line is the DS projection at the saddle point, which is locally orthogonal to the IRC (It does not look orthogonal because of the choice of axis scales). The green line is the projection of the PO that defines the Dividing surface. (Bottom) Schematic representation of the DS's geometrical structure for the different reduced masses. The yellow structure represents the possible momenta depending of the location in the DS.](Figures\PODS_DSshape.png)
<a id="DSCloseFig"></a>

<font color='red'>(Discussion)</font>

#### Checking the Valdity

<font color='red'>(...)</font>

From the sampled trajectories we can measure the time taken to reach a determined region (transit time), in this case the PES minimum identified as the product well. Then we can perform the same calculation but with trajectories starting on the DS defined only with $r_1$ (the blue line in [fig:3](#DSCloseFig)). The blue line corresponds to the common choice for solution phase reactions of assigning the transition state location to the PES saddle point, and assuming that the reaction coordinate is entirely determined by the solute. [fig:4](#TransitFig) is a representation in phase space of the transit times of trajectories that start on the true and approximate dividing surfaces with different initial $p_\perp$, the momentum normal to the dividing surface. The transit times (calculated as the time for $r_1$ to reach a value greater than that for product minimum) show brighter colors in Figure [fig:4](#TransitFig) as the transit time increases. The expected results for a DS is that trajectories starting with negative momenta normal to the dividing surface ($p_\perp<0$), i.e. directed to the reactant well, would take longer to reach the product well than those that start with positive momenta. This is clearly the case for the PODS as can be seen in Figure 6, where $p_\perp=0$ (which corresponds to the PO) provides an exact line of demarcation in the transit times. By contrast, the approximate DS shows long and short transit times on both sides of $p_1=0$. It is interesting to note that those areas where the transit times are long for $p_1>0$ or short for $p_1<0$ correspond to recrossing of trajectories, and that the amount of recrossing gets larger as $\mu_2$ increases. Thus, the approximate DS becomes a poorer and poorer choice for the transition state as the mass of the bath oscillator increases.

![A comparison of trajectory transit times from the DS to the product. (Top) Being the PODS (green DS in [fig:3](#DSCloseFig)) and (Bottom) the DS conventional definition of the TS (blue DS in [fig:3](#DSCloseFig)). The color scale goes from dark colors for short times to brighter colors for long times. The quantity $p_\perp$ is the momentum perpendicular to the dividing surface, with a positive sign being in the direction of the product.](Figures\TransitT.png)
<a id="TransitFig"></a>

The brighter colored bands visible on the reactant sides ($p_\perp <0$) in Figure [fig:4](#TransitFig) are associated with the many periodic orbits located in the reactant well. Trajectories that approach these POs can spend a long time before finally crossing over to the product well.

### Lagrangian Descriptors

#### Method 1

The LD is calculated on a chosen initial time and conditions $(t_0, \mathbf{x_0})$ and measured for fixed forward and backward integration time $\tau$. This calculation is repeated for several initial conditions obtaining a grid of points in phase space. The general expression of the LD is:

\begin{equation}
M\left(\mathbf{x_0},t_0\right)_\tau = \int_{t-\tau}^{t+\tau} \mathcal{F}\left(\mathbf{x_0}(t)\right) dt
\label{LDEq}
\end{equation}

where $\mathcal{F}\left(\mathbf{x_0}(t)\right)$ is a positively bounded scalar representing a geometrical or physical property of a trajectory with initial conditions $\mathbf{x_0}$ and initial time $t_0$; that is integrated over the time interval $[t_0-\tau, t_0+\tau]$. Because we are interested in the DS, and we know that the action is a minimum on its vicinity we will be using an action-like value of the form:

\begin{equation}
\mathcal{F}\left(\mathbf{x_0}(t)\right) = \sum_{i=1}^{N}\left(p_i \frac{dx_i}{dt}\right)^{1/2}
\label{actionLikeEQ}
\end{equation}

where N is the number of DoF, $p_i$ and $x_i$ are respectively the momenta and position of the DoF $i$. It is interesting to note that, by finding the modulus of each term separately, we could examine their effect on the LD independently, although that issue is not explored in the present paper. In this case the LD will be:

\begin{equation}
M\left(\mathbf{x_0},t_0\right)_\tau = \int_{t-\tau}^{t+\tau} \sum_{i=1}^{N}\left(p_i \frac{dx_i}{dt}\right)^{1/2} = \int_{t-\tau}^{t+\tau} \sum_{i=1}^{N}\left(v_i^2 m_i\right)^{1/2} dt
\label{LDEq2}
\end{equation}

The application of LD to higher DoF is already being studied in depth.{% cite NaikSWigginsPysRevE2019 naik2019finding --file myBib %} However, these studies revolve around systems with a known Hamiltonian, which is not the case for many chemical processes. Also, the control of every DoF to create the required initial conditions becomes unbearable as soon as you convert the system into a full atomistic model. Therefore, if we want to calculate the LD for complex chemical systems we need a different approach that is described in the following section.
As in our previous study the mass of the reactive system ($\mu_1$) is set to a value of 1 and the reduced mass of the bath ($\mu_2$) will be given values of 0.1, 1 or 10. But in this case we will be using the LD methodology to locate the DS and the $\tau$ value will be 1 for $\mu_2=0.1, 1$ and 2 for $\mu_2=10$.

The images shown in [fig:5](#LDFirst) where obtained by the above mentioned grid methodology. In those figures, for each point in the plot, the momenta of the bath DoF was equal to 0. The location of the saddle point (blue line) and the PO associated to it (red line) were included in the plots to better understanding of the information obtained. Of significant relevance are the plots obtained for the position and momenta of the reactive DoF (a plots in [fig:5](#LDFirst)). In those plots we can see how the invariant manifolds converge at the PO that encloses the DS forming a crossing point that indicates its location.

![LD plots for the different reduced masses of the bath for (a) the position and momenta of the reactive DoF and (b) the position of both DoF, each with a close up of on the saddle point area. The blue straigth line in the first line of plots indicates the position of the saddle point and the red line in the close ups represents the PO enclosing the DS.](Figures\LDFirst.png)
<a id="LDFirst"></a>

It is important to note that this plots represent a section of the full phase space in which all the kinetic energy is in the reactive DoF. Thus, all we can expect to see from the PODS is the intersection with this section. Of course this is not a big problem, as it is very easy to change the value of the momenta of the bath at which the LD is calculated.

#### Method 2

The main idea of this method comes from a solution that has been applied in almost every studied chemical reaction. This is, the reduction of the system to a 1 or 2 DoF problem using a Reaction Coordinate (RC). However, as in those chemical studies, the equations of motion are not reduced to a single coordinate but instead the RC is used as a measure of the location of the system at each timestep.

The method was developed with the following assumptions about the problem to be studied:

- The system's Hamiltonian is unknown.
- The system is represented as an atomistic model with Cartesian coordinates.
- We can combine the Cartesian coordinates into one or two collective variables that accurately represent the process we want to model.

Also, the following assumptions are not required but will make the computations much easier:

- The system will have a saddle point from which we will have a rough estimate of where is it.
- The DS is relatively close to that saddle point.
- It is a closed system.

As mentioned previously the definition of the initial conditions of the system can be a major problem when dealing with atoms that have three Cartesian coordinates and velocities each. However, as we want to focus our study in the reactivity of the system, the trajectories in which we are interested have something in common. They all cross a surface orthogonal to the IRC[ref] at the saddle point in their journey. So starting at that point is much easier to assign different initial velocities as a way of exploring part of the phase space.

This part of phase space, is what we will call the reactive phase space which, and by exploring it we can discriminate those phase space structures that have no direct influence in the reactive process.

The general description of the methodology is the following:

1. We define 1 or 2 RC that will measure the evolution of the system.
2. We establish a set of initial conditions for our RC in the configurational space as our initial point.
3. From this point, we integrate several trajectories with different momenta of a time length longer than $\tau$, both forward and backward in time.
4. For each trajectory of length $T$ we can calculate the LD with a value of $\tau$ for at least a number $(T-2\tau)/dt$ of *initial conditions* that have enough trajectory length before and after them.

The amount of trajectories and their length will strongly depend on the problem and the time it takes to the trajectory to explore the reactive phase space. But, in principle will follow the rule of the longer the better.

In this method, the evolution of the trajectory defines the initial conditions and not the user. Thus, avoiding the problem of defining many initial conditions. Also, although here we talk about having a single point as initial condition there is no reason for not including a second or several points in configurational space as initial conditions. This will be most useful when the DS is far from our initial condition as we will see in the System bath model.

We could suppose that the 2DoF from the described system are instead 2 collective coordinates obtained from a system of multiples DoF. We then proceed to calculate the LD as described in our second method, first to check if we could replicate the results from the previous method and then to analyze the extra information we are generating with it.

In [fig:6](#LDSecondSec) we can see how the plots are very similar to those obtained in [fig:5](#LDFirst). The main difference appears as we increase the mass of the bath where this effect reduces the ergodicity of the system. Even in those cases, there are similarities between plots in the places visited by the trajectories.

![Equivalent plots from [fig:5](#LDFirst) obtained with the second methodology](Figures\LDSecondSection.png)
<a id="LDSecondSec"></a>

But this is just a small amount of information that we have obtained from the calculations. The full set of values that this method produces can be projected into a single plot. Obviously these projections have so many dynamical structures depicted in them that it is very difficult to see anything. But with a bit of *cleaning* we can obtain a nice picture of the dynamical structure of the system. The plots shown in [fig:7](#LDProject) where obtained by projecting in configurational space all the values obtained from the calculations. However, for each value proyected in the same point only the minimum value was represented. This is because the value of the LD is expected to be a minimum in the vicinity of the PODS. These plots show a clear picture of the behaviour of the trajectories after crossing the DS but also they have a clear definition of the projection of the PODS in configurational space.

![(a) LD plots for the different reduced masses of the bath in configurational space and (b) their respective close up. The value of LD was obtained by selecting the minimum value between all the values that share the same point in configurational space. The red line in the close ups represents the PO enclosing the DS. ](Figures\LDSecondProjection.png)
<a id="LDProject"></a>

Moreover, if take a slice of the plots in [fig:7](#LDProject) we can visualize the effect of the DS in the value of the LD (see [fig:8](#LDSlice)). This is quite obvious in [fig:7](#LDProject) but it will be very useful in multiples degrees of freedom where there will be much more noise.

![Slice at bath position of 2.2 of the LD values along the reactive coordinate.](Figures\LDSecondSlice.png)
<a id="LDSlice"></a>

We have shown that the DS can be easily identified by the calculation of LD, not only with the grid methodology, but also with our version of the method. It is expected that for multidimensional problems the results will not be as clear and sharp as with this simple model. After all, we are including a significant amount of DoF that will introduce a lot of noise in the calculations. However, if we can identify the DS signal in the LD calculation, then we can begin to understand the dynamical properties that make the system behave as it does, like in the former case, the coupling between the bath and the reactive system.

## References

{% bibliography --file myBib --cited %}