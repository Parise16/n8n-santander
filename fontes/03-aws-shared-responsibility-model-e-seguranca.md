# Fonte 3: Modelo de Responsabilidade Compartilhada e Segurança AWS

**Origem:** AWS Security & Compliance Center  
**URL de Referência:** https://aws.amazon.com/compliance/shared-responsibility-model/  
**Tipo de Fonte:** Documento Oficial de Governança, Compliance e Segurança  
**Autoridade:** AWS Information Security & Identity Architecture

---

## 1. O Modelo de Responsabilidade Compartilhada (Shared Responsibility Model)

A segurança e a conformidade na AWS são uma responsabilidade compartilhada entre a AWS e o cliente. Esse modelo compartilhado alivia a carga operacional do cliente, uma vez que a AWS opera, gerencia e controla os componentes do sistema operacional do host e da camada de virtualização até a segurança física das instalações onde o serviço opera.

A diferenciação fundamental é:

> **"A AWS é responsável pela Segurança DA Nuvem (Security OF the Cloud)."**  
> **"O Cliente é responsável pela Segurança NA Nuvem (Security IN the Cloud)."**

---

### A. Responsabilidade da AWS (Segurança DA Nuvem):
A AWS é responsável por proteger a infraestrutura global que executa todos os serviços oferecidos na AWS Cloud. Esta infraestrutura é composta por:
- **Hardware físico e instalações:** Proteção física dos datacenters, controle de acesso biométrico, monitoramento por câmeras, redundância de fornecimento de energia (UPS/geradores) e climatização.
- **Software de infraestrutura:** A camada de virtualização (hipervisor, como o AWS Nitro System), firmware e software proprietário de rede da AWS.
- **Rede física e isolamento:** Cabeamento submarino e terrestre, roteadores de borda e separação de tráfego entre contas de clientes.
- **Serviços gerenciados de alto nível:** Em serviços como Amazon S3, AWS Lambda, Amazon DynamoDB e Amazon RDS, a AWS também gerencia a aplicação de patches no sistema operacional subjacente, atualizações do motor de banco de dados e resiliência de hardware.

---

### B. Responsabilidade do Cliente (Segurança NA Nuvem):
A responsabilidade do cliente é determinada pelo serviço da nuvem que ele seleciona. Isso determina a quantidade de trabalho de configuração que o cliente deve realizar como parte de suas responsabilidades de segurança.
- **Dados do Cliente:** O cliente é o proprietário exclusivo dos seus dados. É responsável pela classificação dos dados, mecanismos de criptografia (em trânsito e em repouso) e integridade dos arquivos.
- **Gerenciamento de Identidade e Acesso (IAM):** Criação de usuários, grupos, papéis (roles), aplicação de políticas de menor privilégio e obrigatoriedade de autenticação multifator (MFA).
- **Configuração de Redes e Firewalls:** Configuração de VPCs, subnets, rotas, Security Groups e Network ACLs para restringir portas e IPs autorizados.
- **Sistema Operacional e Patches (em serviços IaaS como Amazon EC2):** O cliente é inteiramente responsável pela instalação do sistema operacional na VM, aplicação regular de patches de segurança e updates, configuração de antivírus, firewall de host e gerenciamento de usuários locais.

---

## 2. Comparativo da Responsabilidade por Categoria de Serviço

| Camada / Componente | IaaS (Ex: Amazon EC2) | PaaS / DB Gerenciado (Ex: Amazon RDS) | Serverless / SaaS (Ex: AWS Lambda / S3) |
| :--- | :--- | :--- | :--- |
| **Dados do Cliente** | Responsabilidade do Cliente | Responsabilidade do Cliente | Responsabilidade do Cliente |
| **Políticas de IAM e Acesso** | Responsabilidade do Cliente | Responsabilidade do Cliente | Responsabilidade do Cliente |
| **Firewall de Aplicação / Portas** | Responsabilidade do Cliente (SG/NACL) | Responsabilidade do Cliente (SG) | Gerenciado pela AWS / Configurado pelo Cliente |
| **Patches do Sistema Operacional** | **Responsabilidade do Cliente** | **Responsabilidade da AWS** | **Responsabilidade da AWS** |
| **Configuração do Software da VM** | **Responsabilidade do Cliente** | **Responsabilidade da AWS** | **Responsabilidade da AWS** |
| **Virtualização e Hipervisor** | Responsabilidade da AWS | Responsabilidade da AWS | Responsabilidade da AWS |
| **Hardware e Datacenter Físico** | Responsabilidade da AWS | Responsabilidade da AWS | Responsabilidade da AWS |

---

## 3. Práticas Recomendadas de AWS IAM (Identity and Access Management)

1. **Bloquear a conta raiz (Root User):** Utilizar as credenciais da conta raiz apenas para criar o primeiro usuário administrativo e tarefas estritamente necessárias de conta. Nunca criar chaves de acesso (Access Keys) para a conta raiz e exigir MFA físico ou virtual.
2. **Princípio do Menor Privilégio (Least Privilege):** Conceder apenas as permissões estritamente necessárias para desempenhar a função, nada mais.
3. **Usar IAM Roles para Recursos AWS:** Nunca codificar chaves de acesso estáticas (Access Key ID e Secret Access Key) em instâncias EC2, funções Lambda ou arquivos de código. Utilizar IAM Roles temporárias para fornecer credenciais rotativas automaticamente.
4. **Auditoria Contínua:** Utilizar o AWS CloudTrail para auditar todas as chamadas de API efetuadas na conta, monitorando acessos anômalos ou tentativas não autorizadas.
