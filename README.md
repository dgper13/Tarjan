# Tarjan
Identifying the subnetworks of a product distribution network using [Tarjan's strongly connected components algorithm](https://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm).

## Usage
### `python main.py tests/test01.txt`

### Input

`N` - number of points of distribution

`M` - number of connections in the network

`origin destination` - products can be transported from `origin` to `destination`


### Output

`R` - number of subnetworks

`L` - number of connections between subnetworks

`origin destination`