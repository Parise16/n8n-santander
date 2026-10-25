# Fonte 1: Visão Geral da Amazon Web Services (AWS Overview Whitepaper)

**Origem:** AWS Whitepapers & Guides  
**URL de Referência:** https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html  
**Tipo de Fonte:** Documento Técnico / Whitepaper Oficial  
**Autoridade:** Amazon Web Services Inc. (Equipe de Arquitetura Global)

---

## 1. O que é Computação em Nuvem?

Computação em nuvem é a entrega sob demanda de poder computacional, armazenamento de banco de dados, aplicativos e outros recursos de TI por meio de uma plataforma de serviços em nuvem pela Internet, com definição de preço de pagamento conforme o uso (pay-as-you-go).

### Seis Vantagens Principais da Computação em Nuvem:
1. **Trocar despesas de capital (CapEx) por despesas variáveis (OpEx):** Em vez de investir pesadamente em datacenters e servidores físicos antes de saber como serão usados, você paga apenas quando consome recursos e conforme o volume consumido.
2. **Beneficiar-se de economias de escala massivas:** A agregação de centenas de milhares de clientes na nuvem permite à AWS alcançar maiores economias de escala, que se traduzem em preços mais baixos de pagamento pelo uso.
3. **Parar de adivinhar a capacidade:** Elimina a necessidade de estimar capacidade de infraestrutura. Em vez de lidar com servidores ociosos ou falta de capacidade, você escala vertical ou horizontalmente conforme a demanda real.
4. **Aumentar a velocidade e a agilidade:** Novos recursos de TI ficam disponíveis com apenas um clique, reduzindo o tempo para disponibilizar recursos aos desenvolvedores de semanas para minutos.
5. **Parar de gastar dinheiro executando e mantendo datacenters:** Foco total em projetos que diferenciam o seu negócio, em vez de infraestrutura pesada (energia, cabeamento, refrigeração, hardware).
6. **Tornar-se global em minutos:** Facilidade de implantar aplicações em várias regiões do mundo com poucos cliques, oferecendo menor latência e melhor experiência aos usuários a um custo mínimo.

---

## 2. Tipos de Computação em Nuvem

### Modelos de Serviço:
- **IaaS (Infrastructure as a Service):** Contém os blocos de construção fundamentais para a TI na nuvem. Oferece acesso a recursos de rede, computadores (virtuais ou em hardware dedicado) e espaço de armazenamento de dados. Oferece o mais alto nível de flexibilidade e controle de gerenciamento sobre seus recursos de TI. *Exemplo AWS: Amazon EC2.*
- **PaaS (Platform as a Service):** Elimina a necessidade da sua organização de gerenciar a infraestrutura subjacente (geralmente hardware e sistemas operacionais) e permite que você se concentre na implantação e no gerenciamento de suas aplicações. *Exemplo AWS: AWS Elastic Beanstalk.*
- **SaaS (Software as a Service):** Fornece um produto completo, executado e gerenciado pelo provedor de serviços. Na maioria dos casos, as pessoas se referem a aplicações de usuário final (como e-mail corporativo). Você não precisa pensar em como o serviço é mantido ou como a infraestrutura subjacente é gerenciada. *Exemplo de mercado: Microsoft 365, Google Workspace, Salesforce.*

### Modelos de Implantação:
- **Cloud (Nuvem Pública):** Toda a infraestrutura do aplicativo é executada na nuvem.
- **Híbrida:** Integração e conexão entre recursos baseados na nuvem e recursos de datacenters locais existentes (on-premises).
- **On-premises (Nuvem Privada):** Implantação de recursos no local, usando tecnologias de virtualização e ferramentas de gerenciamento de recursos próprios.

---

## 3. Infraestrutura Global da AWS

A AWS possui uma infraestrutura global altamente redundante e confiável:
- **Regiões (Regions):** Localizações geográficas físicas no mundo onde a AWS agrupa múltiplos datacenters. Cada região é totalmente isolada das demais para garantir tolerância máxima a falhas e conformidade com soberania de dados (ex: `us-east-1` no Norte da Virgínia, `sa-east-1` em São Paulo).
- **Zonas de Disponibilidade (Availability Zones - AZs):** Cada Região da AWS é composta por múltiplas Zonas de Disponibilidade isoladas e separadas fisicamente (geralmente 3 ou mais por região). Cada AZ é composta por um ou mais datacenters discretos com energia, refrigeração e conectividade de rede redundantes. As AZs de uma região são conectadas por redes de fibra óptica de altíssima velocidade e latência ultrabaixa (< 1-2 ms).
- **Pontos de Presença (Edge Locations):** Redes de datacenters distribuídos globalmente usados pelo Amazon CloudFront (CDN) e AWS Route 53 (DNS) para entregar conteúdo com baixa latência para usuários finais em qualquer continente.

---

## 4. Serviços Centrais da AWS

### A. Computação (Compute):
- **Amazon EC2 (Elastic Compute Cloud):** Fornece capacidade de computação redimensionável na nuvem por meio de Máquinas Virtuais (instâncias). O usuário escolhe CPU, memória, armazenamento, sistema operacional (Linux, Windows) e gerencia configurações e atualizações.
- **AWS Lambda (Serverless Compute):** Permite executar código sem provisionar ou gerenciar servidores. Paga-se apenas pelo tempo de computação consumido em milissegundos. Execução orientada a eventos.
- **Amazon ECS (Elastic Container Service) e Amazon EKS (Elastic Kubernetes Service):** Orquestradores de contêineres Docker de alta performance e suporte nativo ao ecossistema Kubernetes.
- **AWS Elastic Beanstalk:** Serviço PaaS para implantação rápida e gerenciamento de aplicações web em Java, .NET, PHP, Node.js, Python, Ruby, Go e Docker, automatizando provisionamento, balanceamento de carga e auto-scaling.

### B. Armazenamento (Storage):
- **Amazon S3 (Simple Storage Service):** Armazenamento de objetos com escalabilidade líder do setor, disponibilidade e durabilidade de 99,999999999% (11 9's). Ideal para arquivos, imagens, backups, data lakes e hospedagem de sites estáticos.
  - *Classes de Armazenamento:*
    - **S3 Standard:** Para dados acessados com frequência (baixa latência e alto throughput).
    - **S3 Intelligent-Tiering:** Move objetos automaticamente entre níveis de acesso frequente, infrequente e arquivo para economizar custos sem impacto operacional.
    - **S3 Standard-IA (Infrequent Access):** Para dados acessados com menor frequência, mas que exigem acesso rápido quando solicitados (menor custo de GB/mês, taxa de recuperação).
    - **S3 One Zone-IA:** Armazenamento de menor custo para dados infrequentes armazenados em uma única AZ.
    - **S3 Glacier Flexible Retrieval / Deep Archive:** Arquivamento frio de longo prazo (retenção regulatória), com custos de frações de centavos por gigabyte.
- **Amazon EBS (Elastic Block Store):** Volumes de armazenamento em bloco de alta performance persistentes para uso exclusivo com instâncias EC2 (equivalente ao disco rígido/SSD do servidor).
- **Amazon EFS (Elastic File System):** Sistema de arquivos NFS totalmente gerenciado e elástico, montável simultaneamente em centenas de instâncias EC2 e funções Lambda.

### C. Redes (Networking):
- **Amazon VPC (Virtual Private Cloud):** Permite provisionar uma seção isolada e logicamente dedicada da nuvem AWS, onde você define seu próprio espaço de endereçamento IP (CIDR), subnets públicas e privadas, tabelas de roteamento e gateways de rede.
- **Security Groups e Network ACLs:** Firewall virtual com estado (Security Groups, a nível de instância) e sem estado (NACLs, a nível de sub-rede) para controlar o tráfego de entrada e saída.
- **Elastic Load Balancing (ALB / NLB):** Distribui automaticamente o tráfego de aplicativos de entrada entre vários destinos, como instâncias EC2, contêineres e endereços IP.
