# sina
Social and Information Network Analysis subject - Graph and Network Analytics


## NetworkX
 
[NetworkX Documentation](https://networkx.github.io/documentation/networkx-1.10/tutorial/tutorial.html)

## Clustering coefficient for a vertix

Is the proportion of linkes between the verticies within its neighbourhood divided by the number of links that could possibly exist between them. 

if k is the number of verticies in the neighbourhood
then number of links (edges) that could possibly exist is k(k-1)/2

```
--> C = number of links in neibhourhood / (k(k-1)/2)
```

![graph](images/01-test-clustering-coeff.png)

``` 
nx.clustering(G)


nx.clustering(G)
{1: 0.14285714285714285,
 2: 0.4,
 3: 0.6666666666666666,
 0: 0,
 4: 1.0,
 5: 0,
 6: 1.0,
 7: 0.6666666666666666,
 8: 0.6666666666666666,
 9: 0}

 ```

 for node 1: 
 
    number of neighbours = 7
    possible links in neighbourhood = 7 * 6 /2 = 21 
    links in neighbourhood = 3 

    => clustering coeeff for node 1 = 3/21 = 0.14286
