# *MapReduce*
## *Introduction*

MapReduce is a programming model and implementation to enable the parallel processing of huge amounts of data. In a nutshell, it breaks a large dataset into smaller chunks to be processed separately on different worker nodes and automatically gathers the results across the multiple nodes to return a single result. 

As it name suggests, it allows for distributed processing of the map() and reduce() functional operations, which carry out most of the programming logic. 

The steps that we have implemented are the following ones:
* "Map" step: In this step, each worker named Mapper applies the "map()" function to the local data passed by parameter which in this case is a chunk of a very large file. A master node ensures that only one copy of redundant input data is processed. Each mapper sends the result of te "map()" function to a single Reducer.
* "Reduce" step: In this step, the worker named "reducer" receives all the resuls from the mappers and joins them. With this step we obtain the final result.

## *Implementation*





### *Authored by:*

Alejandro López Mellina & Gwenaëlle Mege Barriola
