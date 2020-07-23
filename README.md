<h1> Problema do Fluxo Máximo </h1> 
<b>Descrição:</b> Relatório solicitado pelo professor Teobaldo Leite Bulhõeos Junior, da disciplina de Pesquisa Operacional, do curso de Engenharia de Computação.

<h2>Sumário</h2>
<ol>
	<li><a href="https://github.com/GiovanniBru/PFM#introdu%C3%A7%C3%A3o">Introdução</a></li>
	<li><a href="https://github.com/GiovanniBru/PFM#defini%C3%A7%C3%A3o-do-problema">Definição do Problema</a></li>
	<li><a href="https://github.com/GiovanniBru/PFM#modelagem">Modelagem</a></li>
	<li><a href="https://github.com/GiovanniBru/PFM#instru%C3%A7%C3%B5es">Instruções</a></li>
	<li><a href="https://github.com/GiovanniBru/PFM#conclus%C3%A3o">Conclusão</a></li>
	<li><a href="https://github.com/GiovanniBru/PFM#refer%C3%AAncias">Referências</a></li>
</ol>

<h2>Introdução</h2> 
O trabalho consiste em implementar a modelagem do Problema do Fluxo Máximo (PFM). O PFM é um dos problemas mais clássicos e importantes do Problema do Fluxo de Custo Mínimo (PFCM). A implementação foi realizada na linguagem de programação Python, com auxílio do pacote de programação linear OR-Tools, disponibilizado pelo Google, e a biblioteca igraph para visualização e impressão dos grafos.

<h2>Definição do Problema</h2> 
<p> O Problema do Fluxo Máximo (PFM) é um dos modelos de otimização de rede que trata de maximizar o fluxo que passa pelos arcos de um nó de origem (oferta) até um nó de destino (demanda/escoadouro). Nesse trajeto, do nó de origem até o destino, o fluxo passa por nós intermediários chamados de nós transshipment. O fluxo através de um arco é permitido apenas na direção indicada pela seta, e a quantidade máxima de fluxo é determinada pela capacidade daquele arco.</p>
<p> O objetivo do PFM é maximizar a quantidade total de fluxo da origem para o escoadouro de forma que não fique sobrando, ou seja, não seja desperdiçado nada nos nós de transshipment. Portanto, a quantidade que sai da origem tem que ser igual a quantidade que chega no escoadouro, respeitando a capacidade de fluxo de cada arco. </p>
<p> Algumas aplicações típicas do PFM são:</p>
<ol>
  <li> Maximizar o fluxo através da rede de distribuição de uma empresa partindo de suas fábricas para chegar aos clientes;</li>
  <li> Maximizar o fluxo de petróleo através de um sistema de tubulação;</li>
  <li> Maximizar o fluxo de veículos através de uma rede de transporte.</li>
</ol>
<p> Pelo fato de o problema do fluxo máximo poder ser formulado como um problema de programação linear, ele pode ser resolvido pelo método simplex, de forma que qualquer um dos pacotes de software de programação linear possa ser usado </p>
<p> Em geral, o PFM pode ser modelado da seguinte forma: </p> 
<ul>
  <li> N − Conjunto de vértices </li>
  <li> A − Conjunto de arestas </li>
  <li> Xij - Quantidade de Fluxo existente na aresta i → j </li>
  <li> uij - Capacidade máxima da aresta i → j;
</ul>
<p><b> Objetivo:</b> </p>
<img src = "https://github.com/GiovanniBru/PFM/blob/master/imagens/FO.PNG">
<p><b> Restrições:</b> </p>
<img src = "https://github.com/GiovanniBru/PFM/blob/master/imagens/restricoes.PNG">
 <p> Podemos ver abaixo um exemplo do PFM em uma companhia de saneamento que transporta água potável por meio de uma malha de aquedutos. A companhia busca determinar o fluxo máximo de água (em m³/s) que pode ser transportado na rede da Figura 1. A rede tem como nó de origem (O) uma estação no Norte de Minas e como nó de destino (T) um consumidor final localizado na região central do estado de São Paulo. Os valores nos arcos representam as capacidades máximas em cada arco (em m³/s).</p>
 <img src = "https://github.com/GiovanniBru/PFM/blob/master/imagens/figura1.PNG">
 <p> Para resolver esse problema, primeiro definimos as variáveis de decisão do modelo:</p>
 <p><b> Xij = fluxo de água no arco (i,j), ∀ i,j </b> </p>
<p> Assim, temos 8 variáveis de decisão, cada uma representando um arco, como por exemplo Xoa que é o fluxo da estação de origem até a estação A.</p>
<p> A função objetivo busca maximizar o fluxo total de saída da estação de origem O, ou maximizar o fluxo total de chegada na estação final T: </p>
<ul>
  <li> max z = Xoa + Xob </li>
  <li> max z = Xct + Xdt </li>
</ul>
<p> As restrições do modelo são: </p>
<p> <b>1.</b> O fluxo de entrada em T é igual ao fluxo de saída em O: </p> 
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xct + Xdt = Xoa + Xob </p>
<p> <b>2.</b> Existe uma conservação de fluxo de saída e entrada em cada nó de transshipment, pois não pode restar nada nesses nós: </p> 
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xoa = Xac + Xad </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xob = Xbc + Xbd </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xac + Xbc = Xct </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xad + Xbd = Xdt </p>
<p> <b>3.</b> A capacidade máxima em cada arco: </p> 
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xoa ≤ 50 m³/s </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xob ≤ 60 m³/s </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xac ≤ 40 m³/s </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xad ≤ 60 m³/s </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xbc ≤ 80 m³/s </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xbd ≤ 60 m³/s </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xct ≤ 50 m³/s </p>
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xdt ≤ 70 m³/s </p>
<p> <b>4.</b> Restrição de não negatividade: </p> 
<p> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Xoa, Xob, Xac, Xad, Xbc, Xbd, Xct, Xdt ≥ 0 </p>
<p> Resolvendo esse PFM por meio de qualquer solver como simplex, ou por meio do código desenvolvido pelo trabalho, foi encontrado a <b>solução ótima de Z = 110 m³/s.</b> </p>

<h2>Modelagem</h2> 
<p> Foi requisitado que construíssemos um problema que resolva o PFM modelado como Problema de Fluxo de Custo Mínimo (PFCM). Para realizar a transformação do PFM no formato do PFCM foram necessárias três alterações:</p>
<p> 1. Custo do arco (Cij) com valor igual a zero para todos os arcos existentes de modo a refletir a ausência de custos no PFM.</p>
<p> 2. Selecionar um limite superior (F) seguro sobre o fluxo viável máximo da rede, para servir de parâmetro aos nós de suprimento e demanda. </p>
<p> 3. Criar um arco de ligação entre o nó de suprimento (origem) e o nó de demanda (escoadouro), com o custo unitário grande (M). </p>
<p> Em razão de criarmos esse custo unitário positivo para o arco de ligação e atribuirmos o custo unitário zero para todos os demais, o PFCM enviará o fluxo
viável máximo através dos arcos de transshipment, o que faz alcançar o objetivo do PFM. Na Figura 2 podemos observar uma rede do Seervada Park, como exemplo, antes da aplicação dessas transformações, e na Figura 3 observamos a mesma após as transformações.</p>
<img src = "https://github.com/GiovanniBru/PFM/blob/master/imagens/figura2.PNG">
<img src = "https://github.com/GiovanniBru/PFM/blob/master/imagens/figura3.PNG">

<h2>Instruções</h2> 
<p> O código foi desenvolvido na linguagem Python, usando o ambiente Spyder do Anaconda 3. A versão do Python utilizada foi a 3.7. O algoritmo se encontra no arquivo “PFM.py” anexado e para rodá-lo é necessário fazer as seguintes importações no Prompt do Anaconda, ou no terminal do Sistema Operacional:</p>
<ul>
  <li> $ sudo apt-get install python3 </li>
  <li> $ sudo apt-get install python3-pip</li>
  <li> $ pip install --upgrade --user ortools</li>
  <li> $ pip install python-igraph</li>
  <li> $ pip install pycairo </li>
</ul>
<p> Caso esteja no linux, é necessário instalar o python 3 e pip usando as duas primeiras chamadas de função no terminal.</p>
<p> A terceira importação é referente ao pacote de programação linear OR-Tools, disponível pelo Google, cuja referência está anexada no sétimo tópico ‘Bibliografia’. As outras importações são referentes aos pacotes necessários para visualização do grafo.</p>
<h2>Conclusão</h2> 
<p>O objetivo do trabalho foi alcançado, em ordem o algoritmo lê: o número de vértices, número de arcos, índice da origem, índice do escoadouro, e os dados de cada arco (direção e custo). A saída do algoritmo exibe na tela a solução ótima do PFM e também os grafos utilizados e seus fluxos.</p>
<p> Nas figuras abaixo temos dois exemplos de execução do algoritmo. </p>
<img src = "https://github.com/GiovanniBru/PFM/blob/master/imagens/figura4.PNG">
<img src = "https://github.com/GiovanniBru/PFM/blob/master/imagens/figura5.PNG">
<h2>Referências</h2> 
<ul>
	<li>HILLIER, Frederick S; LIEBERMAN, Gerald J.; GRIESI, Ariovaldo. Introdução à pesquisa operacional. 9.ed. Porto Alegre: AMGH,, 2013. 1005p. ISBN: 9788580551181.</li>
	<li> <a href="https://developers.google.com/optimization/reference/python/linear_solver/pywraplp"> Referência do pacote de programação linear OR-Tools </a> </li>
	<li> <a href="https://igraph.org/"> Referência do pacote igraph </a> </li>
	<li> <a href="https://developers.google.com/optimization/lp/glop"> Referência Glop Linear Solver </a> </li>
</ul>


