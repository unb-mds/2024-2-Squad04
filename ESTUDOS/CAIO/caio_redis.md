# 🔴 Redis
###### Uma tecnologia complicada... 
***

### Links:
- https://redis.io/docs/latest/get-started/
- https://medium.com/@vndpal/why-you-should-use-redis-cache-2e48bdd2c0be
- https://aws.amazon.com/pt/caching/
- https://runcloud.io/blog/redis-alternatives
<br>

### O que é:
Redis primeiramente é um cache, um armazenamento que pode ser usado como:
- in-memory data store
- vector database
- document database
- streaming engine
- message broker

Redis é um acrônimo para “Remote Dictionary Server”. Às vezes referido como servidor de estrutura de dados, o cache do Redis é extremamente rápido, possibilita dados de diferentes formatos, persistente e com expiração automática.

### Para quê Caching?
Na área de computação, um cache é uma camada de armazenamento físico de dados de alta velocidade que guarda um subconjunto de dados, geralmente temporário por natureza, para que futuras solicitações referentes a esses dados sejam atendidas de modo mais rápido do que é possível fazer ao acessar o local de armazenamento principal de dados.

**Aplicações**: os caches podem ser aplicados e utilizados entre várias camadas de tecnologia, como sistemas operacionais, camadas de redes, incluindo Redes de entrega de conteúdo (CDN) e DNS, além de aplicativos web e bancos de dados. Você pode usar o cache para reduzir significativamente a latência e melhorar as IOPS para muitas cargas de trabalho de aplicativos de leitura intensa, como portais de perguntas e respostas, jogos, compartilhamento de mídia e redes sociais. As informações armazenadas em cache podem incluir os resultados de consultas de banco de dados, cálculos computacionalmente intensivos, solicitações/respostas de APIs e artefatos da web, como arquivos HTML, JavaScript e imagem. As cargas de trabalho com alto consumo computacional que trabalham com conjuntos de dados, como mecanismos de recomendação e simulações computacionais de alta performance, também se beneficiam de uma camada de dados de memória atuando como um cache. Nesses aplicativos, conjuntos de dados muito grandes devem ser acessados em tempo real em clusters de máquinas que podem abranger centenas de nós. Devido à velocidade do hardware subjacente, manipular esses dados em um armazenamento baseado em disco é um gargalo significativo para esses aplicativos.

**Padrões de projeto**: em um ambiente computacional distribuído, uma camada de armazenamento em cache dedicada permite que sistemas e aplicativos sejam executados de forma independente do cache com seus próprios ciclos de vida, sem o risco de afetar o cache. O cache serve como uma camada central que pode ser acessada a partir de sistemas diferentes com seu próprio ciclo de vida e topologia arquitetônica. Isso é especialmente relevante em um sistema em que nós de aplicativo podem ser dimensionados dinamicamente na direção horizontal ou vertical. Se o cache residir no mesmo nó que o aplicativo ou os sistemas que o utilizam, o dimensionamento poderá afetar a integridade do cache. Além disso, quando caches locais são usados, eles só beneficiam o aplicativo local que consome os dados. Em um ambiente de armazenamento em cache distribuído, os dados podem abranger vários servidores de cache e ser armazenados em um local central para o benefício de todos os consumidores desses dados.

### Outras tecnologias de Cache:
1. Valkey
2. Dragonfly DB
3. Memcached
4. Hazelcast
5. Key DB
6. MongoDB
7. RethinkDB
8. Amazon MemoryDB
9. SAP HANA