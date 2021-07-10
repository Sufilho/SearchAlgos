class Graph:
  def __init__(self, graph_dict=None, directed=True):
    self.graph_dict = graph_dict or {}
    self.directed = directed
    if not directed:
      self.make_undirected()

  # Essa func criará um grafo nao dirigido
  def make_undirected(self):
    for x in list(self.graph_dict.keys()):
      for (y, dist) in self.graph_dict[x].items():
        self.graph_dict.setdefault(y, {})[x] = dist

  # Cria uma conexao de um Nó para o outro com um determinda distância
  # caso seja um grafo nao dirigido, esta irá adicionar a conexão inversa.
  def connect(self, node_A, node_B, distance=1):
    # Determina o valor padrão da distância de A para B
    self.graph_dict.setdefault(node_A, {})[node_B] = distance
    # Caso seja não digirido vai fazer o inverso também
    if not self.directed:
      self.graph_dict.setdefault(node_B, {})[node_A] = distance
  
  # Retorna as conexões dos nodes
  def get(self, node_A, node_B=None):
    conections = self.graph_dict.setdefault(node_A, {})
    if node_B is None:
      return conections
    else:
      return conections.get(node_B)

  # Retornar a lista completa de nodes do grafo
  def nodes(self):
    # cria um set com todos as chaves no dicionario do grafo
    set1 = set([k for k in self.graph_dict.keys()])
    # cria um set com todos os valores nos values do dicionario para cada item de cada valor
    set2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
    # realiza a uniao entre os 2 sets    
    nodes = set1.union(set2)
    # retorna os nodes em formato de lista
    return list(nodes)

class Node:

  # Construindo a classe Node
  def __init__(self, name:str, parent:str):
    self.name = name
    self.parent = parent
    self.g = 0 # Custo para o ponto de partida
    self.h = 0 # Custo para o objetivo final
    self.f = 0 # Custo total

  # Fazendo comparação de Nodes
  def __eq__(self, other_node):
    return self.name == other_node.name

  # Sequenciar os nodes
  def __lt__(self, other_node):
    return self.f < other_node.f

  # Printar node
  def __repr__(self):
    return (f'{self.name}, {self.f}')


# definindo o search algo
def astar_search(graph, data, start, end):

  # criando as stacks de nos abertos e fechados
  open = []
  closed = []

  # iniciando o Node inicial e final

  start_node = Node(start, None)

  goal_node = Node(end, None)

  # adicionar o Node inicial para a pilha de abertos
  open.append(start_node)

  while len(open) > 0:
    # ordenar a lista para pegar o nó com o menor self.f primeiro

    open.sort()

    # node com o menor custo
    current_node = open.pop(0)

    # agora podemos passar esse node para a lista dos nodes fechados
    closed.append(current_node)

    # fazer a checagem se o goal_node é igual ao current_node, que é a condicial final para chegarmos no goal
    if current_node == goal_node:
      # definimos o caminho levado até chegar no goal
      path = []
      
      # quando chegar no goal, ele vai fazer a iteração até chegar no nó de start
      # adicionando todos os nodes no caminho.
      while current_node != start_node:
        path.append(current_node.name + ': ' + str(current_node.g))
        current_node = current_node.parent
      
      path.append(start_node.name + ': ' + str(start_node.g))

      # como estamos vindo do final pro começo, vamos reverter o path, para ficar na sequencia direta do node_start
      return path[::-1]

    # se o current_node nao for o goal_node, iremos verificar os nodes vizinhos
    # neighbors será um dicionario    
    neighbors = graph.get(current_node.name)

    # iterar neighbors
    for key, value in neighbors.items():
      # criar um node para o neighbor
      neighbor = Node(key, current_node)

      # verifica se o node neighbor definido já foi avaliado e transferido pra pilha closed
      if(neighbor in closed):
        continue

      # realizar o calculo completo do path até o momento

      neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
      neighbor.h = data.get(neighbor.name)
      neighbor.f = neighbor.g + neighbor.h

      # checar se o neighbor está na lista open e se este tem um valor f (total) menor
      if(add_to_open(open, neighbor) == True):
        open.append(neighbor)
  # caso nenhum path seja formado, retornará None
  return None

# checa se pode adicionar o node neighbor pra stack open
# caso exista um node igual ao neighbor ocorrerá a comparação do valor f destes
# se o f de neighbor for maior q o do node no open, o neighbor nao será adicionado na stack open
def add_to_open(open, neighbor):
  for node in open:
    if (neighbor == node and neighbor.f > node.f):
      return False
  return True

def main():
  
  # criar o grafo a ser trabalhado
  graph = Graph()

  # Criar conexões entre os Nodes (valores aleatórios)
  graph.connect('A', 'B', 20)
  graph.connect('B', 'C', 10)
  graph.connect('A', 'C', 32)

  # criar medições para serem utilizadas no grafo
  # são os valores que o algoritmo irá comparar pra ver se tomou a melhor decisão
  data = {}
  data['A'] = 0
  data['B'] = 9
  data['C'] = 27

  # formando o caminho do node de inicio para o node de objetivo
  path = astar_search(graph, data, 'A', 'C')
  print(path)

if __name__ == "__main__": main()