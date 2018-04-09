# *MapReduce*
## *Introduction*

MapReduce is a programming model and implementation to enable the parallel processing of huge amounts of data. In a nutshell, it breaks a large dataset into smaller chunks to be processed separately on different worker nodes and automatically gathers the results across the multiple nodes to return a single result. 

As it name suggests, it allows for distributed processing of the map() and reduce() functional operations, which carry out most of the programming logic. 

Functions implemented:
> A `WordCount` function to count how many times a word appears in a large file.
> A `CountWord` function to count the total number of words of a large file.

The main objectives of this project are:
* To learn the implementation of basic Distributed Systems.
* Calculate the speed up between a secuential WordCount/CountWord with its distributed implementation.

The steps used for the distributed implementation are the following ones:
* "Map" step: In this step, each worker named Mapper applies the "map()" function to the local data that is in the file which name is passed by parameter which in this case is a chunk of a very large file. A master node ensures that only one copy of redundant input data is processed. Each mapper sends the result of te "map()" function to a single Reducer.
* "Reduce" step: In this step, the worker named "reducer" receives all the resuls from the mappers and joins them. With this step we obtain the final result.


## *Implementation*
First of all, for the secuential version


For the distributed version, we have created a file named 'God'. It invokes five different terminals:
* The first one creates an Apache Server.
* Three of them have each one a different Mapper.   
* One of them is the Server.

Each mapper is in a different terminal to be able to parallelize their execution. The function of these is to wait until the Server sends them the information to execute. Once they have all the information they'll execute the Then, they will execute the WordCount or CountWord functions for a chunk of code 


## *Results*


### *Authored by:*
```
Alejandro López Mellina & Gwenaëlle Mege Barriola
```
