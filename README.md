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


## Use
To be able to use our distributed code, open a terminal in the Server folder and use the following command:
```
./God 
```
Note that 5 different terminals are now open. 
Introduce in the last one the name of the file that you want to use and the function that you want to execute (it can be 1 for countWord or 2 for wordCount).

## Comments
To see all the implementation comments and the documentation of the code, please open the MapReduce.pdf file.

### *Authored by:*
```
Alejandro López Mellina & Gwenaëlle Mege Barriola
```
