# Guia de Estudos: Fundamentos de Cloud Computing com AWS

> **Material gerado a partir do Estúdio do Google NotebookLM / Gemini Notebook**  
> **Tema:** Fundamentos de Cloud Computing com AWS  
> **Base de Conhecimento:** Whitepapers Oficiais AWS, Well-Architected Framework, Documentação de Segurança e Videoaulas Técnicas.

---

## 1. Visão Geral e Roteiro de Aprendizagem

Este guia de estudos consolida os tópicos mais importantes para quem está iniciando em computação em nuvem com a Amazon Web Services (AWS) ou se preparando para a certificação **AWS Certified Cloud Practitioner (CLF-C02)**.

### Trilha de Aprendizado Recomendada:
1. **Conceitos de Nuvem:** Definição, CapEx vs OpEx, as 6 vantagens da nuvem.
2. **Modelos de Entrega:** IaaS, PaaS, SaaS e estratégias de implantação (Cloud, Híbrida, On-premises).
3. **Infraestrutura Global AWS:** Regiões, Zonas de Disponibilidade (AZs) e Pontos de Presença (Edge Locations).
4. **Serviços Principais:**
   - Computação: EC2, Lambda, ECS, Elastic Beanstalk.
   - Armazenamento: S3 (classes de armazenamento), EBS, EFS.
   - Redes: VPC, Subnets, Security Groups, NACLs, Internet Gateways.
   - Bancos de Dados: RDS, Aurora, DynamoDB.
5. **Segurança e Conformidade:** Modelo de Responsabilidade Compartilhada, AWS IAM, Menor Privilégio e MFA.
6. **Arquitetura de Excelência:** Os 6 Pilares do AWS Well-Architected Framework.

---

## 2. Resumos Conceituais Rápidos (Flashcards de Revisão)

### Cartão 1: CapEx vs OpEx
- **Pergunta:** O que significa trocar despesas de capital (CapEx) por despesas variáveis (OpEx)?
- **Resposta:** CapEx exige grande investimento financeiro adiantado na compra de hardware físico e datacenters antes do uso. OpEx permite pagar sob demanda apenas pelos recursos computacionais consumidos a cada segundo/hora, ajustando o custo à receita do negócio.

### Cartão 2: Regiões vs Zonas de Disponibilidade
- **Pergunta:** Por que uma Região AWS tem múltiplas Zonas de Disponibilidade?
- **Resposta:** Para proporcionar tolerância a falhas e alta disponibilidade. Cada AZ é um datacenter fisicamente separado (com energia e internet independentes). Se um desastre atingir uma AZ, as outras AZs da mesma região continuam operando normalmente sem interromper o serviço.

### Cartão 3: S3 vs EBS
- **Pergunta:** Qual a diferença prática entre o Amazon S3 e o Amazon EBS?
- **Resposta:** O **Amazon S3** é armazenamento de objetos acessível via HTTP/API, ideal para arquivos não estruturados, imagens, backups e data lakes com durabilidade de 11 noves. O **Amazon EBS** é armazenamento em bloco montado como um disco virtual exclusivo diretamente em uma instância EC2, ideal para sistemas operacionais e bancos de dados transacionais.

### Cartão 4: Modelo de Responsabilidade Compartilhada
- **Pergunta:** Em uma instância Amazon EC2, quem deve atualizar o sistema operacional?
- **Resposta:** O cliente. A AWS cuida da segurança **DA** nuvem (hardware, virtualização, datacenter físico), enquanto o cliente cuida da segurança **NA** nuvem (instalação de patches no SO do EC2, antivírus, regras de firewall e credenciais).

---

## 3. Simulado Prático (Quiz com 10 Questões e Gabarito Comentado)

### Questão 1
Uma startup deseja hospedar uma aplicação web e quer focar apenas no código, sem gerenciar servidores, atualizações do sistema operacional ou balanceamento de carga manual. Qual modelo de computação em nuvem e qual serviço AWS melhor atendem a essa necessidade?
- (A) IaaS - Amazon EC2
- (B) PaaS - AWS Elastic Beanstalk
- (C) SaaS - Amazon WorkSpaces
- (D) On-premises - AWS Outposts

> **Resposta Correta: (B)**  
> **Comentário:** O AWS Elastic Beanstalk é um exemplo clássico de PaaS (Platform as a Service), onde o desenvolvedor apenas faz upload do código e a plataforma cuida do provisionamento, balanceamento de carga, auto scaling e patches do SO.

---

### Questão 2
De acordo com o Modelo de Responsabilidade Compartilhada da AWS, qual das seguintes tarefas é de responsabilidade EXCLUSIVA da AWS?
- (A) Criptografar os dados armazenados em um bucket do Amazon S3.
- (B) Configurar as regras de entrada (Inbound Rules) de um Security Group.
- (C) Descarte seguro e destruição física de discos rígidos defeituosos nos datacenters.
- (D) Habilitar a Autenticação Multifator (MFA) para os usuários do AWS IAM.

> **Resposta Correta: (C)**  
> **Comentário:** A segurança física das instalações e do hardware (incluindo o descarte seguro de mídia de armazenamento) é de responsabilidade da AWS ("Segurança DA nuvem"). Criptografia, regras de firewall e gestão de IAM são de responsabilidade do cliente ("Segurança NA nuvem").

---

### Questão 3
Uma empresa armazena relatórios fiscais obrigatórios que precisam ser mantidos por 7 anos. Esses relatórios são acessados raramente (menos de uma vez por ano) e um tempo de recuperação de algumas horas é aceitável. Qual classe de armazenamento do Amazon S3 oferece o menor custo para esse caso de uso?
- (A) S3 Standard
- (B) S3 Standard-Infrequent Access (S3 Standard-IA)
- (C) S3 One Zone-IA
- (D) S3 Glacier Deep Archive

> **Resposta Correta: (D)**  
> **Comentário:** O S3 Glacier Deep Archive é a classe de armazenamento de menor custo da AWS, desenhada especificamente para retenção de dados a longo prazo com acesso raríssimo e tempo de recuperação entre 9 e 12 horas.

---

### Questão 4
Qual dos 6 pilares do AWS Well-Architected Framework prioriza a realização de operações como código (IaC), melhoria contínua de processos e aprendizado com todas as falhas operacionais?
- (A) Excelência Operacional
- (B) Confiabilidade
- (C) Eficiência de Performance
- (D) Sustentabilidade

> **Resposta Correta: (A)**  
> **Comentário:** O pilar da Excelência Operacional foca em executar e monitorar sistemas para fornecer valor ao negócio e aprimorar continuamente processos operacionais por meio de automação e aprendizado com incidentes.

---

### Questão 5
Uma aplicação precisa processar imagens enviadas por usuários. Os uploads acontecem esporadicamente ao longo do dia, totalizando cerca de 20 minutos de processamento diário. Qual opção computacional é a mais econômica e eficiente?
- (A) Manter uma instância EC2 t3.large ligada 24 horas por dia.
- (B) Configurar uma função AWS Lambda orientada a eventos de upload no S3.
- (C) Provisionar um cluster fixo do Amazon EKS com nós dedicados.
- (D) Comprar uma Instância Reservada de 3 anos do Amazon EC2.

> **Resposta Correta: (B)**  
> **Comentário:** Como a carga é orientada a eventos e dura apenas 20 minutos no total, o AWS Lambda é ideal (Serverless), pois não cobra tempo ocioso; paga-se estritamente pelos milissegundos de execução do processamento de cada imagem.

---

### Questão 6
O que representa uma Zona de Disponibilidade (Availability Zone - AZ) na infraestrutura global da AWS?
- (A) Uma cidade inteira com dezenas de escritórios comerciais da AWS.
- (B) Um ou mais datacenters discretos com energia, rede e conectividade redundantes dentro de uma Região.
- (C) Um servidor de cache de borda (Edge Location) usado pelo CloudFront.
- (D) Um endereço IP público atribuído a um balanceador de carga.

> **Resposta Correta: (B)**  
> **Comentário:** Cada AZ consiste em um ou mais datacenters físicos independentes e isolados contra enchentes e quedas elétricas, conectados a outras AZs da mesma região por fibra óptica de baixíssima latência.

---

### Questão 7
Qual prática de segurança do AWS IAM é altamente recomendada pelas diretrizes oficiais da AWS para proteger o acesso à conta?
- (A) Compartilhar as credenciais do usuário raiz (root) com os líderes técnicos da equipe.
- (B) Gerar chaves de acesso permanentes (Access Keys) para a conta raiz.
- (C) Adotar o princípio do menor privilégio e exigir MFA (Multi-Factor Authentication).
- (D) Desativar o AWS CloudTrail para economizar custos de registro em log.

> **Resposta Correta: (C)**  
> **Comentário:** As melhores práticas do IAM incluem nunca usar a conta raiz para tarefas rotineiras, habilitar MFA em todas as contas e aplicar o princípio do menor privilégio (concedendo apenas as permissões mínimas necessárias).

---

### Questão 8
Qual componente de rede da AWS atua como um firewall com estado (stateful) controlando o tráfego de entrada e saída no nível de uma instância virtual EC2?
- (A) Network ACL (NACL)
- (B) Security Group
- (C) Internet Gateway
- (D) AWS Route 53

> **Resposta Correta: (B)**  
> **Comentário:** Os Security Groups operam no nível da instância e têm estado (stateful): se o tráfego de entrada for permitido, a resposta de retorno correspondente será automaticamente permitida, independentemente das regras de saída. As Network ACLs operam no nível da sub-rede e não têm estado (stateless).

---

### Questão 9
Como uma arquitetura em nuvem pode aplicar o pilar da Confiabilidade para prevenir paradas totais de serviço decorrentes de falhas em um datacenter?
- (A) Aumentando o tamanho da CPU do servidor único (escalabilidade vertical).
- (B) Implantando instâncias em múltiplas Zonas de Disponibilidade (Multi-AZ) atrás de um Load Balancer.
- (C) Desativando o Auto Scaling para evitar oscilações de instâncias.
- (D) Armazenando todos os dados apenas no disco local efêmero da instância.

> **Resposta Correta: (B)**  
> **Comentário:** A estratégia Multi-AZ combinada com balanceamento de carga garante alta disponibilidade e resiliência: se uma AZ inteira sofrer uma pane, o balanceador redireciona o tráfego instantaneamente para a AZ saudável remanescente.

---

### Questão 10
No pilar de Sustentabilidade do AWS Well-Architected Framework, qual das seguintes ações ajuda a diminuir a pegada de carbono de uma organização na nuvem?
- (A) Manter servidores de teste rodando continuamente nos finais de semana.
- (B) Migrar cargas de trabalho para processadores mais eficientes, como instâncias baseadas em AWS Graviton.
- (C) Evitar a exclusão de arquivos obsoletos ou cópias duplicadas no armazenamento.
- (D) Dobrar o provisionamento de servidores para garantir folga de capacidade.

> **Resposta Correta: (B)**  
> **Comentário:** Os processadores baseados em arquitetura ARM AWS Graviton oferecem até 60% menos consumo de energia para o mesmo desempenho que processadores legados x86, reduzindo diretamente a pegada ambiental da carga de trabalho.
