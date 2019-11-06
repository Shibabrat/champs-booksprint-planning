The index of a saddle point {#the-index-of-a-saddle-point .unnumbered}
===========================

We consider a $n$ degree-of-freedom Hamiltonian of the following form:

$$H(q, p) = \sum_{i=1}^{n} \frac{p_i^2}{2} + V(q), \quad (q,p) \in \mathbb{R}^n \times \mathbb{R}^n,
\label{ham_int}$$

where $q \in \mathbb{R}^n$ denote the configuration space variables and
$p \in \mathbb{R}^n$ denote the corresponding conjugate momentum
variables. This Hamiltonian function gives rise to the corresponding
Hamilton’s differential equations (or just ‘’Hamilton’s equations’’)
having the following form:

$$\begin{aligned}
\dot{q}_i & = & p_i, \nonumber \\
\dot{p}_i & = & -\frac{\partial V}{\partial q_i} (q), \quad i=1. \ldots , n.
\label{hameq_int}\end{aligned}$$

These are a set of $2n$ first order differential equations defined on
the phase space $\mathbb{R}^n \times \mathbb{R}^n$.

A critical point of the potential energy function is a point
$\bar{q} \in \mathbb{R}^n$ satisfying the following equations:

$$\frac{\partial V}{\partial q_i} (\bar{q}) =0, \quad i=1, \ldots n.$$

Once a critical point of the potential energy function is located, we
want to ‘’classify’’ it. This is done by examining the second derivative
of the potential energy function evaluated at the critical point. The
second derivative matrix is referred to as the [*Hessian matrix*]{}, and
it is given by:

$$\frac{\partial^2 V}{\partial q_i \partial q_j} (\bar{q}) =0, \quad i,j=1, \ldots n,
\label{hessian}$$

which is a $n \times n$ symmetric matrix. Hence has $n$ real
eigenvalues, which we denote by:

$$\sigma_k, \quad k=1, \ldots, n.
\label{eiv_Hess}$$

However, returning to dynamics as given by Hamilton’s equations , the
point $(\bar{q}, 0)$ is an equilibrium point of Hamilton’s equations,
i.e. when this point is substituted into the right-hand-side of we
obtain
$(\dot{q}_1, \ldots, \dot{q}_n, \dot{p}_1, \ldots, \dot{p}_n) = (0, \ldots, 0, 0, \ldots, 0)$,
i.e. the point $(\bar{q}, 0)$ does not change in time.

Next, we want to determine the nature of the stability of this
equilibrium point. Linearized stability is determined by computing the
Jacobian of the right hand side of , which we will denote by $M$,
evaluating it at the equilibrium point $(\bar{q}, 0)$, and determining
its eigenvalues. The following calculation is from
[@ezra2004impenetrable]. The Jacobian of the Hamiltonian vector field
evaluated at $(\bar{q}, 0)$ is given by:

$$M = 
\left(
\begin{array}{cc}
0_{n\times n} &  \rm{id}_{n \times n} \\
-\frac{\partial^2 V}{\partial q_i \partial q_j} (\bar{q}) & 0_{n\times n} 
\end{array}
\right),$$

which is a $2n \times 2n$ matrix. The eigenvalues of $M$, denoted by
$\lambda$, are given by the solutions of the following characteristic
equation:

$${\rm det} \, \left( M - \lambda \, {\rm id}_{2n \times 2n} \right) =0,
\label{eivM}$$

where ${\rm id}_{2n \times 2n}$ denoted the $2n \times 2n$ identity
matrix. Writing in detail (i.e. using the explicit expression for the
Jacobian of ) gives:

$${\rm det} \, 
\left(
\begin{array}{cc}
-\lambda \, \rm{id}_{n \times n} & \rm{id}_{n \times n} \\
 -\frac{\partial^2 V}{\partial q_i \partial q_j} (\bar{q}) & -\lambda \rm{id}_{n \times n}
 \end{array}
 \right) =  {\rm det} \,  \left(\lambda^2 \, \rm{id}_{n \times n}  + \frac{\partial^2 V}{\partial q_i \partial q_j} (\bar{q})  \right) =0.$$

We can conclude from this calculation that the eigenvalues of the
$n \times n$ symmetric matrix
$\frac{\partial^2 V}{\partial q_i \partial q_j} (\bar{q})$ are
$-\lambda^2$, where $\lambda$ are the eigenvalues of the $n \times n$
matrix $M$. Hence, the eigenvalues of $M$ occur in pairs, denoted by
$\lambda_k, \, \lambda_{k+n}, \, k=1, \ldots n$, which have the form:

$$\lambda_k, \, \lambda_{k+n} = \pm \sqrt{-\sigma_k},  \quad k=1, \ldots, n,$$

where $\sigma_k$ are the eigenvalues of the Hessian of the potential
energy evaluated at the critical point $\bar{q}$ as denoted in . Hence,
we see that the existence of equilibrium points of Hamilton’s equations
of ‘’saddle-like stability’’ implies that there must be [*at least*]{}
one negative eigenvalue of . In fact, we have the following
classification of the linearized stability of saddle-type equilibrium
points of Hamilton’s equations in terms of the critical points of the
potential energy surface.

Index 1 saddle.

:   One eigenvalue of is positive, the rest are negative[^1]. In the
    mathematics literature, these are often referred to as
    ‘’saddle-center-$\cdots$-center equilibria, with the number of
    center-$\cdots$-center terms equal to the number of pairs of pure
    imaginary eigenvalues.

Index 2 saddle.

:   Two eigenvalues of are positive, the rest are negative

    and in general,

Index k saddle.

:   $k$ eigenvalues of are positive, the rest are negative ($k \le n$).

[^1]: We will assume that none of the eigenvalues of are zero. Zero
    eigenvalues give rise to special cases that must be dealt with
    separately.

```python

```
