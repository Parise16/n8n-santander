# Glossário Técnico: Fundamentos de Cloud Computing e AWS

Este glossário reúne as definições canônicas dos principais termos, conceitos e siglas abordados no Segundo Cérebro de Fundamentos de Cloud Computing com AWS.

---

### A
- **Amazon Aurora:** Mecanismo de banco de dados relacional compatível com MySQL e PostgreSQL desenvolvido para a nuvem pela AWS, oferecendo até 5x a velocidade do MySQL padrão e 3x do PostgreSQL padrão.
- **Amazon CloudFront:** Serviço de rede de entrega de conteúdo (CDN) de alta performance que distribui dados, vídeos e APIs com baixa latência usando Pontos de Presença (Edge Locations) distribuídos no mundo todo.
- **Amazon EC2 (Elastic Compute Cloud):** Serviço Web que fornece capacidade computacional segura e redimensionável na nuvem na forma de Máquinas Virtuais (instâncias).
- **Amazon S3 (Simple Storage Service):** Serviço de armazenamento de objetos baseado na nuvem com durabilidade de 99,999999999% (11 noves) projetado para armazenar qualquer quantidade de dados em qualquer formato.
- **Availability Zone (AZ):** Um ou mais datacenters discretos com energia, rede e conectividade redundantes dentro de uma mesma Região AWS, interconectados por fibra óptica de baixíssima latência.

---

### C
- **CapEx (Capital Expenditure):** Despesas de capital inicial investidas em ativos físicos tangíveis, como servidores de datacenter, no-breaks e racks.
- **CloudTrail (AWS CloudTrail):** Serviço que registra todas as chamadas de API efetuadas na conta da AWS, fornecendo histórico de governança, conformidade e auditoria de segurança.
- **CloudWatch (Amazon CloudWatch):** Serviço de monitoramento e observabilidade em tempo real de recursos e aplicativos em nuvem da AWS.

---

### D
- **DynamoDB (Amazon DynamoDB):** Banco de dados NoSQL totalmente gerenciado de chave-valor e documentos que oferece desempenho rápido e previsível com escalabilidade transparente em milissegundos de um único dígito.

---

### E
- **EBS (Amazon Elastic Block Store):** Discos virtuais em bloco de alto desempenho montados em instâncias Amazon EC2 para hospedar sistemas operacionais e bancos de dados transacionais.
- **EFS (Amazon Elastic File System):** Sistema de arquivos elástico NFS totalmente gerenciado e sem servidor para uso com serviços de computação em nuvem AWS e recursos locais.
- **Elastic Load Balancing (ELB):** Distribui automaticamente o tráfego de entrada em múltiplos destinos (como instâncias EC2, contêineres e endereços IP) em uma ou mais Zonas de Disponibilidade.

---

### I
- **IaaS (Infrastructure as a Service):** Modelo de nuvem que fornece os blocos de infraestrutura fundamentais (computação virtualizada, armazenamento e redes), dando ao cliente controle total sobre o SO e softwares instalados.
- **IAM (AWS Identity and Access Management):** Serviço que controla com precisão quem está autenticado (logado) e autorizado (possui permissões) para utilizar os recursos na nuvem.

---

### M
- **Multi-AZ:** Padrão arquitetural que replica dados e implanta componentes de infraestrutura em múltiplas Zonas de Disponibilidade para garantir alta disponibilidade e tolerância a falhas.
- **MFA (Multi-Factor Authentication):** Camada adicional de segurança que exige um código temporário de um dispositivo físico ou aplicativo além de senha para acessar contas de nuvem.

---

### O
- **OpEx (Operational Expenditure):** Despesas operacionais recorrentes do dia a dia, onde os custos de TI variam proporcionalmente ao consumo real de recursos computacionais.

---

### P
- **PaaS (Platform as a Service):** Modelo de computação em nuvem onde a plataforma gerencia o hardware subjacente e o sistema operacional, permitindo que a equipe foque apenas na escrita e deploy do código.

---

### R
- **Region (Região AWS):** Localidade física no mundo onde a AWS possui clusters de datacenters organizados em múltiplas Zonas de Disponibilidade isoladas.
- **RDS (Amazon Relational Database Service):** Serviço gerenciado que facilita a configuração, operação e escalabilidade de bancos relacionais comuns (PostgreSQL, MySQL, MariaDB, Oracle e SQL Server).
- **Responsabilidade Compartilhada:** Modelo que divide a governança de segurança em "Segurança DA Nuvem" (sob tutela da AWS) e "Segurança NA Nuvem" (sob controle do cliente).

---

### S
- **SaaS (Software as a Service):** Aplicação de usuário final completamente operada e mantida pelo fornecedor de software sobre a nuvem.
- **Serverless (Sem Servidor):** Modelo de execução em que o provedor de nuvem provisiona e escala automaticamente a infraestrutura, cobrando apenas pelo tempo exato de execução de funções (ex: AWS Lambda).
- **Security Group:** Firewall virtual com estado (stateful) associado a interfaces de rede de instâncias virtuais para controlar tráfego autorizado de entrada e saída.

---

### V
- **VPC (Amazon Virtual Private Cloud):** Rede virtual isolada logicamente dentro da conta AWS de um cliente, onde recursos de computação são executados com endereçamento IP privado e regras de roteamento personalizadas.

---

### W
- **Well-Architected Framework:** Conjunto de 6 pilares e boas práticas desenvolvidos pela AWS para orientar a criação de sistemas confiáveis, seguros, eficientes e econômicos na nuvem.
