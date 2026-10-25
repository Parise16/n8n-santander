# Fonte 2: AWS Well-Architected Framework

**Origem:** AWS Architecture Center  
**URL de Referência:** https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html  
**Tipo de Fonte:** Documento Técnico / Framework de Arquitetura Oficial  
**Autoridade:** AWS Well-Architected Team

---

## 1. Visão Geral do Framework

O **AWS Well-Architected Framework** ajuda arquitetos de nuvem a criar infraestruturas seguras, de alta performance, resilientes e eficientes para seus aplicativos e cargas de trabalho. Baseia-se em seis pilares fundamentais e oferece uma abordagem consistente para avaliar arquiteturas e implementar designs escaláveis.

---

## 2. Os Seis Pilares do Well-Architected Framework

### Pilar 1: Excelência Operacional (Operational Excellence)
Foca na execução e monitoramento de sistemas para agregar valor ao negócio e na melhoria contínua de processos e procedimentos de suporte.
- **Princípios de Design:**
  1. Executar operações como código (Infrastructure as Code - IaC com AWS CloudFormation ou Terraform).
  2. Fazer alterações pequenas, frequentes e reversíveis.
  3. Refinar procedimentos operacionais com frequência.
  4. Antecipar falhas e simular eventos de emergência (GameDays).
  5. Aprender com todas as falhas operacionais (Post-mortems sem culpa).

### Pilar 2: Segurança (Security)
Foca na proteção de informações, sistemas e ativos, oferecendo valor empresarial por meio de avaliações de risco e estratégias de mitigação.
- **Princípios de Design:**
  1. Implementar uma base forte de identidade (IAM com menor privilégio e MFA obrigatório).
  2. Habilitar a rastreabilidade (AWS CloudTrail, CloudWatch Logs, AWS Config).
  3. Aplicar segurança em todas as camadas (Defesa em profundidade na borda, VPC, sub-rede, host e aplicação).
  4. Automatizar práticas recomendadas de segurança.
  5. Proteger dados em trânsito (TLS/HTTPS) e em repouso (criptografia nativa com AWS KMS).
  6. Manter as pessoas longe dos dados de produção.
  7. Preparar-se para eventos de segurança (planos de resposta a incidentes).

### Pilar 3: Confiabilidade (Reliability)
Capacidade de uma carga de trabalho executar sua função pretendida de forma correta e consistente quando esperado. Inclui a capacidade de operar e testar a carga de trabalho ao longo de todo o ciclo de vida.
- **Princípios de Design:**
  1. Testar procedimentos de recuperação (Chaos Engineering e simulação de falhas).
  2. Recuperar-se automaticamente de falhas (Auto Scaling, Health Checks e Failover automático Multi-AZ).
  3. Escalar horizontalmente para aumentar a disponibilidade agregada (substituir um único servidor grande por múltiplos nós menores distribuídos).
  4. Parar de adivinhar a capacidade (auto scaling baseado em métricas reais de demanda).
  5. Gerenciar alterações por meio de automação.

### Pilar 4: Eficiência de Performance (Performance Efficiency)
Capacidade de usar recursos de computação de maneira eficiente para atender aos requisitos do sistema e manter essa eficiência à medida que a demanda muda e as tecnologias evoluem.
- **Princípios de Design:**
  1. Democratizar tecnologias avançadas (usar serviços gerenciados e serverless em vez de montar clusters complexos).
  2. Tornar-se global em minutos (implantar em várias regiões e usar CDNs como o CloudFront).
  3. Usar arquiteturas sem servidor (Serverless com AWS Lambda para evitar consumo ocioso).
  4. Fazer experimentos com mais frequência (testar tipos diferentes de instâncias EC2 e tipos de armazenamento).
  5. Ter afinidade mecânica (usar a tecnologia mais adequada ao perfil de processamento, ex: instâncias baseadas em Graviton para economia de energia e custo).

### Pilar 5: Otimização de Custos (Cost Optimization)
Capacidade de executar sistemas para entregar valor ao negócio pelo menor ponto de preço possível.
- **Princípios de Design:**
  1. Praticar o Cloud Financial Management (FinOps).
  2. Adotar um modelo de consumo (pagar apenas pelo que consome).
  3. Medir a eficiência geral (medir a relação entre saída de negócios e custo de nuvem).
  4. Parar de gastar dinheiro com tarefas pesadas indiferenciadas de datacenter.
  5. Analisar e atribuir despesas (uso de Tags de alocação de custos e AWS Cost Explorer).
  6. Modelos de compra: On-Demand, Savings Plans, Instâncias Reservadas (RI) e Spot Instances (com descontos de até 90% para cargas tolerantes a interrupções).

### Pilar 6: Sustentabilidade (Sustainability)
Foca em minimizar os impactos ambientais da execução de cargas de trabalho na nuvem.
- **Princípios de Design:**
  1. Compreender seu impacto ambiental (medir pegada de carbono usando o AWS Customer Carbon Footprint Tool).
  2. Estabelecer metas de sustentabilidade para cada carga de trabalho.
  3. Maximizar a utilização de recursos (evitar superprovisionamento e eliminar recursos ociosos).
  4. Antecipar e adotar novas ofertas de hardware e software mais eficientes (ex: processadores AWS Graviton e AWS Inferentia).
  5. Usar serviços gerenciados para compartilhar recursos com eficiência.
  6. Reduzir a quantidade de dados transferidos e armazenados por meio de compressão e políticas de ciclo de vida (S3 Lifecycle).
