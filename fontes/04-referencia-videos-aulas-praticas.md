# Fonte 4: Síntese de Aulas Práticas e Treinamentos em Vídeo

**Origem:** Cursos Oficiais de Certificação AWS Cloud Practitioner e Arquitetura de Nuvem  
**Vídeos de Referência:**
1. *AWS Certified Cloud Practitioner Training Course* - AWS Developers / FreeCodeCamp  
   **URL:** https://www.youtube.com/watch?v=SOTamWNgDKc  
2. *AWS Essentials - Entendendo a Nuvem na Prática* - AWS Tech Talks Brasil  
   **URL:** https://www.youtube.com/watch?v=3hLmDS179YE  
**Tipo de Fonte:** Videoaulas / Transcrições Técnicas e Demonstrações Práticas  
**Autoridade:** Especialistas e Instrutores Credenciados AWS

---

## 1. Síntese Didática: A analogia do Imóvel para Modelos de Nuvem

Nas aulas práticas, os instrutores utilizam uma analogia amplamente consagrada para facilitar o entendimento dos modelos de serviço em nuvem:

- **On-premises (Datacenter Tradicional):** É equivalente a construir sua própria casa do zero. Você compra o terreno, faz a fundação, sobe as paredes, cuida do encanamento, da rede elétrica, da pintura e de toda a segurança física. Se o telhado quebrar ou faltar energia, o conserto é 100% por sua conta.
- **IaaS (Infrastructure as a Service - Ex: Amazon EC2):** É equivalente a alugar um apartamento sem mobília. O condomínio/proprietário cuida da segurança da portaria, das paredes estruturais, do elevador e da infraestrutura de água e luz. No entanto, mobiliar o apartamento, pintar o interior, instalar os eletrodomésticos e cuidar da chave da porta é sua responsabilidade.
- **PaaS (Platform as a Service - Ex: AWS Elastic Beanstalk):** É como alugar um apartamento mobiliado e com serviços de quarto. Você só precisa levar suas roupas e pertences pessoais (seu código e sua lógica de negócio). A manutenção da mobília e das instalações fica a cargo da administração.
- **SaaS (Software as a Service - Ex: Google Workspace / Salesforce):** É como se hospedar em um quarto de hotel de luxo. Você apenas chega e usufrui do serviço. Não precisa se preocupar com quem troca as lâmpadas, como a cama é arrumada ou quem gerencia a limpeza.

---

## 2. Decisão de Arquitetura Prática: EC2 vs Serverless (AWS Lambda)

Nas discussões de projetos e laboratórios práticos, a decisão entre computação tradicional (EC2) e computação serverless (Lambda) segue critérios objetivos:

### Quando usar Amazon EC2:
- Cargas de trabalho de longa duração ou execução contínua (ex: servidores web legados, sistemas monolíticos rodando 24x7).
- Aplicações que necessitam de controle total do sistema operacional, bibliotecas nativas específicas do kernel ou portas de rede customizadas.
- Processamento com requisitos extremos de hardware fixo (GPU dedicada para Deep Learning, centenas de gigabytes de RAM contínua).
- Cargas previsíveis onde Instâncias Reservadas ou Savings Plans oferecem menor custo por hora de CPU.

### Quando usar AWS Lambda (Serverless):
- Cargas de trabalho orientadas a eventos (event-driven), como disparos por upload de arquivos no S3, mensagens no SQS ou alterações no DynamoDB.
- APIs REST com tráfego flutuante, sazonal ou intermitente (onde pagar por servidores ociosos seria um desperdício financeiro).
- Tarefas de automação, cron jobs, transformações de dados em lote ou webhooks.
- Aplicações que se beneficiam de escalabilidade horizontal instantânea (de 0 a milhares de requisições por segundo) sem gerenciar clusters.

---

## 3. Práticas Recomendadas para Alta Disponibilidade (Multi-AZ)

Nas videoaulas sobre Confiabilidade, o instrutor reforça a "Regra de Ouro da AWS":

> *"Tudo falha o tempo todo (Everything fails all the time)"* — Werner Vogels (CTO da Amazon).

Por essa razão, uma arquitetura profissional nunca deve depender de um único servidor ou de uma única Zona de Disponibilidade:
1. Distribuir instâncias EC2 em pelo menos duas Zonas de Disponibilidade (Multi-AZ) diferentes dentro da mesma Região.
2. Utilizar um Application Load Balancer (ALB) na camada pública para distribuir o tráfego e fazer health checks automáticos.
3. Configurar Auto Scaling Groups para substituir instâncias degradadas e absorver picos de tráfego.
4. Para o banco de dados (ex: Amazon RDS), ativar a funcionalidade **Multi-AZ Replication**, que mantém uma réplica síncrona em espera em outra AZ com failover automático em menos de 60 segundos caso a instância primária falhe.
