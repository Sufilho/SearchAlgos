### A* Algoritmo

Para começarmos a implementar nosso algoritmo de busca A*, precisaremos primeiramente de um grafo para podermos representar nosso problema de caminho.

Inicialmente fazemos a construção do grafo iniciando pelo método ´__init__` das classes de Python, passando como parâmetros um _dicionario de grafos_ e se este Grafo é _direcionado_ (por padrão ele será direcionado) ou não. Caso este não seja direcionado, iremos modelar um Grafo não direcionado.

Sobre grafos:

* _Undirected graphs_ have edges that do not have a direction. The edges indicate a two-way relationship, in that each edge can be traversed in both directions. 

* _Directed graphs_ have edges with direction. The edges indicate a one-way relationship, in that each edge can only be traversed in a single direction.

``` python
class Graph:
  def __init__(self, graph_dict=None, directed=True):
    self.graph_dict = graph_dict or {}
    self.directed = directed
    if not directed:
      self.make_undirected()

  def make_undirected(self):
    for x in list(self.graph_dict.keys()):
      for (y, dist) in self.graph_dict[x].items():
        self.graph_dict.setdefault(y, {})[x] = dist

```
