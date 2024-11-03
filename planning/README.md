
# Key Questions

− How does auto-tuning work in AutoPas?
− What are the strengths and weaknesses of auto-tuning?
− How do other simulators e.g. GROMACS incorporate auto-tuning or algorithm selection in their
code?

Gromacs:

<https://mailman-1.sys.kth.se/pipermail/gromacs.org_gmx-users/2015-June/098608.html>
> A colleague of mine and I have recently discovered that gromacs 4.6.4 and
> 5.0.4 give very different results in the simulation of a biomimetic polymer
> using an AMBER-based force field.  She found that gromacs 5 mdrun is
> dynamically changing nstlist from 10 to 20 or 40 depending on the
> simulation, as documented below.  Is it possible that this is causing the
> favored conformation of the polymer to change? Is there a way in GMX 5 to
> prevent this dynamic updating from happening?

Uses either Verlet Lists: O(n), in form of pair list: All pairs of atoms within a certain distance

+ Parameter nstlist: Number of steps between updates of the neighbor list.
  Can be tuned by gmx mdrun

+ Parameter rlist: Cut-off for the short-range neighbor list.

+ Uses clusters of particles (4,8) for stream computing SSE, AVX, CUDA

+ Relies on auto-parallellization for clusters, especially on new hardware and compilers

+ Uses: <https://www.sciencedirect.com/science/article/pii/S0010465513001975> to achive good SIMD performance. Adjusting the cluster size allows controlling over various SIMD architectures.

+ Prior to SIMD. Inner loop unrolling was used by compilers to increase performance.
+ Nowadays heavy caching is required, as CPUs are much faster than memory.

Algorithm: Load cluster of M particles, and calculate M^2 interactions. Then move to next cluster.

```c
Algorithm ClusteredSIMDVerlet(particles, M, N):
    // M = particles per SIMD cluster
    // N = particles per neighbor group

    // Phase 1: Clustering
    clusters = DivideIntoMParticleClusters(particles)
    
    // Phase 2: Build neighbor lists for clusters
    for each cluster C:
        C.neighbors = FindNeighboringClusters(C)
    
    // Phase 3: SIMD Force Computation
    for each cluster C:
        load_M_particles_SIMD(C)                    // Load M particles once
        for each neighbor_cluster in C.neighbors:
            for N_particles in neighbor_cluster:     // Process N at a time
                compute_M_x_N_interactions_SIMD()    // M x N interactions per load
        store_results()
```

The kernel implementations reach about 50 % of the peak flop rate on all
supported hardware, which is very high for MD.  This comes at the cost of calculating about twice as many interactions as required; not all particle pairs in all
cluster pairs will be within the cut-off at each time step

<!-- file:///C:/Users/Manue/Downloads/978-3-319-15976-8.pdf -->
<https://www.softxjournal.com/action/showPdf?pii=S2352-7110%2815%2900005-9>

Uses OpenMP + MPI for parallelization

# LAMMPS

Verlet Lists
periodacily sorts owned atoms, to improve cache locality
OpenMP

Pillars:

+ Tuning in autopas
+ Efficiveness of retunes
+ Early stopping
+ Comparison to other simulators
