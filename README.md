<h1> Problema do Fluxo Máximo </h1> 
<b>Descrição:</b> Relatório solicitado pelo professor Teobaldo Leite Bulhõeos Junior, da disciplina de Pesquisa Operacional, do curso de Engenharia de Computação.

<h2>Sumário</h2>
<ol>
	<li><a href="">Introdução</a></li>
	<li><a href="">Definição do Problema</a></li>
	<li><a href="">Modelagem</a></li>
	<li><a href="">Instruções</a></li>
	<li><a href="">Conclusão</a></li>
	<li><a href="">Referências</a></li>
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
<img src = "">
<p><b> Restrições:</b> </p>
<img src = "">
 <p> Podemos ver abaixo um exemplo do PFM em uma companhia de saneamento que transporta água potável por meio de uma malha de aquedutos. A companhia busca determinar o fluxo máximo de água (em m³/s) que pode ser transportado na rede da Figura 1. A rede tem como nó de origem (O) uma estação no Norte de Minas e como nó de destino (T) um consumidor final localizado na região central do estado de São Paulo. Os valores nos arcos representam as capacidades máximas em cada arco (em m³/s).</p>
 <img src = "">
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

