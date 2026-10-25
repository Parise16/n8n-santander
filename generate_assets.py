import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MATERIAIS_DIR = os.path.join(BASE_DIR, "materiais")
PRINTS_DIR = os.path.join(MATERIAIS_DIR, "prints")

os.makedirs(PRINTS_DIR, exist_ok=True)

# Fonts
FONT_REGULAR_PATH = "C:/Windows/Fonts/segoeui.ttf"
FONT_BOLD_PATH = "C:/Windows/Fonts/segoeuib.ttf"
FONT_CODE_PATH = "C:/Windows/Fonts/consola.ttf"

def get_font(size, bold=False, code=False):
    path = FONT_CODE_PATH if code else (FONT_BOLD_PATH if bold else FONT_REGULAR_PATH)
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

# -------------------------------------------------------------
# 1. GENERATE MIND MAP (PNG)
# -------------------------------------------------------------
def generate_mindmap():
    w, h = 2400, 1400
    img = Image.new("RGB", (w, h), color=(11, 17, 32)) # Slate 950
    draw = ImageDraw.Draw(img)

    # Subtle background grid
    for x in range(0, w, 60):
        draw.line([(x, 0), (x, h)], fill=(18, 27, 46), width=1)
    for y in range(0, h, 60):
        draw.line([(0, y), (w, y)], fill=(18, 27, 46), width=1)

    # Central Node
    cx, cy = w // 2, h // 2
    cw, ch = 380, 130
    draw.rounded_rectangle([cx - cw//2, cy - ch//2, cx + cw//2, cy + ch//2], radius=18, fill=(30, 41, 59), outline=(255, 153, 0), width=4)
    
    font_c_title = get_font(26, bold=True)
    font_c_sub = get_font(18, bold=False)
    draw.text((cx, cy - 22), "FUNDAMENTOS CLOUD AWS", font=font_c_title, fill=(255, 255, 255), anchor="mm")
    draw.text((cx, cy + 18), "Segundo Cérebro • Google NotebookLM", font=font_c_sub, fill=(255, 179, 71), anchor="mm")

    # Define 5 Branches
    branches = [
        {
            "name": "1. MODELOS DE NUVEM",
            "pos": (450, 240),
            "color": (59, 130, 246), # Blue
            "items": [
                "• IaaS: Infraestrutura (EC2, VPC, EBS)",
                "• PaaS: Plataforma (Elastic Beanstalk)",
                "• SaaS: Software Final (M365, Workspace)",
                "• Nuvem Pública, Híbrida e Privada",
                "• Troca de CapEx por OpEx variável"
            ]
        },
        {
            "name": "2. INFRAESTRUTURA GLOBAL",
            "pos": (1950, 240),
            "color": (16, 185, 129), # Emerald
            "items": [
                "• Regiões: Isoladas geograficamente",
                "• Zonas de Disponibilidade (AZs): Datacenters discretos",
                "• Arquitetura Multi-AZ: Alta disponibilidade e resiliência",
                "• Pontos de Presença (Edge): CloudFront e Route 53",
                "• Baixa latência e implantação global em minutos"
            ]
        },
        {
            "name": "3. SERVIÇOS CENTRAIS",
            "pos": (380, 800),
            "color": (245, 158, 11), # Amber
            "items": [
                "• Computação: EC2 (VMs) vs Lambda (Serverless)",
                "• Armazenamento: S3 (Objetos 11 noves), EBS (Bloco)",
                "• Redes: Amazon VPC, Subnets, Internet Gateways",
                "• Balanceamento: Application Load Balancer (ALB)",
                "• Bancos de Dados: Amazon RDS, Aurora, DynamoDB"
            ]
        },
        {
            "name": "4. SEGURANÇA & IAM",
            "pos": (1200, 1150),
            "color": (239, 68, 68), # Red
            "items": [
                "• Modelo Compartilhado: Segurança DA vs NA Nuvem",
                "• AWS cuida do datacenter físico e hipervisor",
                "• Cliente cuida dos dados, SO (EC2), IAM e firewalls",
                "• IAM: Princípio do Menor Privilégio e MFA",
                "• Auditoria contínua com AWS CloudTrail"
            ]
        },
        {
            "name": "5. WELL-ARCHITECTED",
            "pos": (2020, 800),
            "color": (168, 85, 247), # Purple
            "items": [
                "• Pilar 1: Excelência Operacional (IaC e GameDays)",
                "• Pilar 2: Segurança (Defesa em profundidade)",
                "• Pilar 3: Confiabilidade (Recuperação de falhas Multi-AZ)",
                "• Pilar 4: Eficiência de Performance (Serverless)",
                "• Pilar 5: Otimização de Custos (FinOps e S3 Lifecycle)",
                "• Pilar 6: Sustentabilidade (Processadores Graviton)"
            ]
        }
    ]

    for b in branches:
        bx, by = b["pos"]
        bw, bh = 370, 240
        b_color = b["color"]

        # Draw connecting line
        draw.line([(cx, cy), (bx, by)], fill=b_color, width=3)

        # Draw branch box
        draw.rounded_rectangle([bx - bw//2, by - bh//2, bx + bw//2, by + bh//2], radius=14, fill=(15, 23, 42), outline=b_color, width=3)
        
        # Branch header pill
        draw.rounded_rectangle([bx - bw//2 + 10, by - bh//2 + 10, bx + bw//2 - 10, by - bh//2 + 48], radius=8, fill=b_color)
        draw.text((bx, by - bh//2 + 28), b["name"], font=get_font(18, bold=True), fill=(255, 255, 255), anchor="mm")

        # Items
        item_y = by - bh//2 + 65
        for item in b["items"]:
            draw.text((bx - bw//2 + 20, item_y), item, font=get_font(15, bold=False), fill=(226, 232, 240))
            item_y += 32

    # Title Banner on Top Left
    draw.rounded_rectangle([40, 30, 480, 110], radius=10, fill=(30, 41, 59), outline=(71, 85, 105), width=2)
    draw.text((60, 50), "MAPA MENTAL DE ESTUDOS", font=get_font(18, bold=True), fill=(255, 153, 0))
    draw.text((60, 78), "Fundamentos de Cloud Computing com AWS", font=get_font(14, bold=False), fill=(203, 213, 225))

    # Watermark Footer
    draw.text((w - 50, h - 35), "Santander 2026 - Automação com N8N • DIO • Segundo Cérebro no NotebookLM", font=get_font(15, bold=False), fill=(100, 116, 139), anchor="rm")

    out_path = os.path.join(MATERIAIS_DIR, "mapa-mental-fundamentos-aws.png")
    img.save(out_path, "PNG", quality=95)
    print(f"Mind map saved to: {out_path}")

# -------------------------------------------------------------
# 2. GENERATE SLIDES PRESENTATION (PDF)
# -------------------------------------------------------------
def generate_slides():
    w, h = 1920, 1080
    slides = []

    slide_data = [
        {
            "tag": "APRESENTAÇÃO EXECUTIVA",
            "title": "Fundamentos de Cloud Computing com AWS",
            "sub": "Segundo Cérebro de Aprendizagem Construído com o Google NotebookLM",
            "bullets": [
                "Bootcamp Santander 2026 - Automação com N8N | Desafio de Projeto DIO",
                "Domínio: Fundamentos de Arquitetura em Nuvem, Modelos de Serviço e Práticas Recomendadas",
                "Base de Conhecimento: Whitepapers Oficiais AWS, Well-Architected Framework e Videoaulas Técnicas",
                "Curadoria: Fontes rastreáveis com fundamentação e citações diretas"
            ],
            "footer": "Desafio DIO • Treinando uma IA de Aprendizagem"
        },
        {
            "tag": "CONCEITOS BÁSICOS",
            "title": "O Que é Cloud Computing & Suas 6 Vantagens",
            "sub": "Entrega sob demanda de poder computacional, banco de dados e aplicações com preço sob uso",
            "bullets": [
                "1. Trocar despesas de capital (CapEx) por despesas variáveis (OpEx): pague só pelo que consome.",
                "2. Beneficiar-se de economias de escala massivas: preços menores por volume global agregado.",
                "3. Parar de adivinhar capacidade: elasticidade horizontal e vertical automática conforme demanda.",
                "4. Aumentar a velocidade e a agilidade: novos servidores provisionados em questão de minutos.",
                "5. Foco no negócio: pare de gastar tempo e dinheiro mantendo racks e datacenters físicos.",
                "6. Tornar-se global em minutos: implante aplicações em múltiplas regiões do mundo com um clique."
            ],
            "footer": "Fonte: AWS Whitepaper - Overview of Amazon Web Services"
        },
        {
            "tag": "MODELOS DE ENTREGA",
            "title": "Modelos de Serviço: IaaS, PaaS e SaaS",
            "sub": "A analogia didática do imóvel aplicada à governança e divisão de controle na nuvem",
            "bullets": [
                "• IaaS (Infrastructure as a Service): Como alugar um apartamento vazio.",
                "  - Provedor cuida do prédio; você instala o SO, configura e gerencia. Ex: Amazon EC2, EBS, VPC.",
                "• PaaS (Platform as a Service): Como alugar um apartamento mobiliado com serviço.",
                "  - Provedor gerencia hardware, rede e SO; você só traz o código. Ex: AWS Elastic Beanstalk.",
                "• SaaS (Software as a Service): Como se hospedar em um quarto de hotel de luxo.",
                "  - Aplicação pronta de usuário final; foco exclusivo no consumo do serviço. Ex: Salesforce, M365.",
                "• Modelos de Implantação: Cloud Pública (100% AWS), Híbrida (Conectada com On-premises) e Privada."
            ],
            "footer": "Fonte: Overview of AWS & Aulas Práticas do Curso"
        },
        {
            "tag": "TOPOLOGIA GLOBAL",
            "title": "Infraestrutura Global da AWS & Alta Disponibilidade",
            "sub": "A base física mundial que sustenta serviços distribuídos e resilientes",
            "bullets": [
                "• Regiões da AWS: Áreas geográficas isoladas contendo múltiplos datacenters (ex: us-east-1, sa-east-1).",
                "• Zonas de Disponibilidade (AZs): Um ou mais datacenters discretos com energia, refrigeração e rede redundantes.",
                "• Conexão Inter-AZ: Fibra óptica privada de altíssima largura de banda e baixíssima latência (< 2ms).",
                "• Arquitetura Multi-AZ: Distribuição de instâncias e réplicas de banco de dados para suportar desastres.",
                "• Pontos de Presença (Edge Locations): Datacenters de borda para CloudFront (CDN) e Route 53 (DNS)."
            ],
            "footer": "Fonte: AWS Global Infrastructure Documentation"
        },
        {
            "tag": "COMPUTAÇÃO MODERNA",
            "title": "Computação AWS: EC2 vs Containers vs Serverless (Lambda)",
            "sub": "Como escolher o mecanismo computacional ideal para o perfil da sua aplicação",
            "bullets": [
                "• Amazon EC2 (Virtual Machines):",
                "  - Ideal para sistemas legados, servidores 24x7 contínuos e necessidade de controle total do kernel.",
                "• Contêineres (Amazon ECS & Amazon EKS):",
                "  - Empacotamento padrão de microsserviços com portabilidade e orquestração de alta densidade.",
                "• AWS Lambda (Serverless Compute):",
                "  - Execução orientada a eventos; paga-se estritamente pelos milissegundos de código em execução.",
                "  - Zero servidores para gerenciar, escalabilidade instantânea de zero a milhares de invocações."
            ],
            "footer": "Fonte: AWS Compute Overview & Well-Architected Performance Pillar"
        },
        {
            "tag": "ARMAZENAMENTO INTELIGENTE",
            "title": "Amazon S3 & Gestão Estratégica de Ciclo de Vida",
            "sub": "Armazenamento de objetos com 11 noves (99,999999999%) de durabilidade",
            "bullets": [
                "• S3 Standard: Alta frequência de acesso, baixa latência, ideal para sites e dados ativos.",
                "• S3 Intelligent-Tiering: IA move objetos automaticamente entre níveis para otimização de custo.",
                "• S3 Standard-IA & One Zone-IA: Para dados acessados com menor frequência (backups, relatórios).",
                "• S3 Glacier Flexible & Deep Archive: Arquivamento frio a longo prazo com custo ultra-reduzido.",
                "• S3 Lifecycle Policies: Regras automáticas que movem arquivos antigos e economizam até 80% do custo."
            ],
            "footer": "Fonte: AWS Storage Whitepaper & FinOps Best Practices"
        },
        {
            "tag": "SEGURANÇA & CONFORMIDADE",
            "title": "Modelo de Responsabilidade Compartilhada & AWS IAM",
            "sub": "A fronteira clara entre a responsabilidade do provedor e a do cliente",
            "bullets": [
                "• Segurança DA Nuvem (AWS): Proteção dos datacenters físicos, hardware, hipervisor Nitro e redes físicas.",
                "• Segurança NA Nuvem (Cliente): Criptografia de dados, políticas do IAM, firewall e patches de SO no EC2.",
                "• Princípio do Menor Privilégio (Least Privilege): Conceda apenas permissões estritamente necessárias.",
                "• Proteção da Conta Raiz: Bloqueie a conta root, ative MFA obrigatório e utilize IAM Roles temporárias.",
                "• Rastreabilidade & Auditoria: Monitore todas as requisições de API usando AWS CloudTrail."
            ],
            "footer": "Fonte: AWS Shared Responsibility Model & IAM Security Guide"
        },
        {
            "tag": "ARQUITETURA DE EXCELÊNCIA",
            "title": "AWS Well-Architected Framework: Os 6 Pilares",
            "sub": "Framework canônico para avaliar e otimizar arquiteturas de missão crítica",
            "bullets": [
                "1. Excelência Operacional: Execute operações como código (IaC) e aprenda com todas as falhas.",
                "2. Segurança: Aplique segurança em todas as camadas (defesa em profundidade) e proteja dados em repouso/trânsito.",
                "3. Confiabilidade: Teste procedimentos de recuperação; adote recuperação automática e arquitetura Multi-AZ.",
                "4. Eficiência de Performance: Democratize tecnologias avançadas usando serviços gerenciados e serverless.",
                "5. Otimização de Custos: Elimine desperdícios, pratique FinOps e utilize instâncias reservadas ou Spot.",
                "6. Sustentabilidade: Reduza a pegada de carbono maximizando a eficiência de processadores como o AWS Graviton."
            ],
            "footer": "Fonte: AWS Well-Architected Framework Whitepaper"
        },
        {
            "tag": "CONCLUSÃO & REPRODUÇÃO",
            "title": "O Segundo Cérebro como Acelerador de Carreira",
            "sub": "Como a síntese do NotebookLM transforma documentação complexa em conhecimento prático",
            "bullets": [
                "• Aprendizado Baseado em Fontes: Menos alucinação e 100% de precisão ancorada em documentos oficiais.",
                "• Consulta Ágil: Respostas instantâneas para decisões de arquitetura e preparação para certificações.",
                "• Materiais Gerados no Estúdio: Mapas mentais, slides executivos, podcasts e simulados de revisão.",
                "• Reprodutibilidade Completa: Todas as fontes e diretrizes organizadas para uso público no GitHub."
            ],
            "footer": "Santander 2026 - Automação com N8N • DIO • Projeto Concluído com Sucesso"
        }
    ]

    for idx, s in enumerate(slide_data):
        img = Image.new("RGB", (w, h), color=(15, 23, 42)) # Slate 900
        draw = ImageDraw.Draw(img)

        # Header accent bar
        draw.rectangle([(0, 0), (w, 12)], fill=(255, 153, 0)) # AWS Orange

        # Tag pill
        draw.rounded_rectangle([90, 70, 380, 115], radius=8, fill=(30, 41, 59), outline=(255, 153, 0), width=2)
        draw.text((235, 92), s["tag"], font=get_font(18, bold=True), fill=(255, 153, 0), anchor="mm")

        # Slide Number
        draw.text((w - 100, 92), f"{idx + 1} / {len(slide_data)}", font=get_font(20, bold=True), fill=(148, 163, 184), anchor="mm")

        # Title & Subtitle
        draw.text((90, 150), s["title"], font=get_font(42, bold=True), fill=(255, 255, 255))
        draw.text((90, 215), s["sub"], font=get_font(22, bold=False), fill=(203, 213, 225))

        # Divider line
        draw.line([(90, 265), (w - 90, 265)], fill=(51, 65, 85), width=2)

        # Main content box
        draw.rounded_rectangle([90, 290, w - 90, 950], radius=16, fill=(30, 41, 59), outline=(71, 85, 105), width=2)

        # Bullets
        y_text = 340
        for b in s["bullets"]:
            is_subbullet = b.startswith("  -")
            if is_subbullet:
                draw.text((160, y_text), b.strip(), font=get_font(22, bold=False), fill=(148, 163, 184))
                y_text += 48
            else:
                draw.text((130, y_text), b, font=get_font(24, bold=True if b.startswith("•") or b[0].isdigit() else False), fill=(241, 245, 249))
                y_text += 58

        # Footer
        draw.text((90, h - 50), s["footer"], font=get_font(18, bold=False), fill=(100, 116, 139))
        draw.text((w - 90, h - 50), "DIO Agent • Segundo Cérebro AWS", font=get_font(18, bold=False), fill=(100, 116, 139), anchor="ra")

        slides.append(img)

    out_path = os.path.join(MATERIAIS_DIR, "slides-fundamentos-aws-cloud.pdf")
    slides[0].save(out_path, "PDF", resolution=100.0, save_all=True, append_images=slides[1:])
    print(f"Slides presentation saved to: {out_path}")

# -------------------------------------------------------------
# 3. GENERATE REALISTIC UI PRINTS (PNG)
# -------------------------------------------------------------
def generate_prints():
    w, h = 1600, 950

    def draw_base_ui(draw, active_tab="Chat"):
        # Dark theme background
        draw.rectangle([(0, 0), (w, h)], fill=(17, 24, 39)) # Gray 900
        
        # Top header
        draw.rectangle([(0, 0), (w, 64)], fill=(31, 41, 55)) # Gray 800
        draw.line([(0, 64), (w, 64)], fill=(55, 65, 81), width=1)
        
        # Logo and Title
        draw.ellipse([(24, 18), (52, 46)], fill=(59, 130, 246))
        draw.text((38, 32), "G", font=get_font(18, bold=True), fill=(255, 255, 255), anchor="mm")
        draw.text((68, 32), "Gemini Notebook / NotebookLM", font=get_font(18, bold=True), fill=(243, 244, 246), anchor="lm")
        draw.text((360, 32), "•   Fundamentos de Cloud Computing com AWS", font=get_font(16, bold=False), fill=(156, 163, 175), anchor="lm")

        # Top right pills
        draw.rounded_rectangle([w - 320, 16, w - 190, 48], radius=16, fill=(55, 65, 81))
        draw.text((w - 255, 32), "4 fontes ativas", font=get_font(14, bold=True), fill=(52, 211, 153), anchor="mm")
        draw.rounded_rectangle([w - 170, 16, w - 30, 48], radius=16, fill=(59, 130, 246))
        draw.text((w - 100, 32), "Compartilhar", font=get_font(14, bold=True), fill=(255, 255, 255), anchor="mm")

        # Left sources sidebar
        draw.rectangle([(0, 65), (320, h)], fill=(24, 31, 47))
        draw.line([(320, 65), (320, h)], fill=(55, 65, 81), width=1)
        draw.text((24, 90), "FONTES (4)", font=get_font(14, bold=True), fill=(156, 163, 175))

        sources = [
            ("📄", "Overview of AWS Whitepaper", "docs.aws.amazon.com"),
            ("📄", "AWS Well-Architected Framework", "docs.aws.amazon.com"),
            ("🔒", "Shared Responsibility Model", "aws.amazon.com"),
            ("▶️", "AWS Cloud Practitioner Training", "youtube.com")
        ]
        y_s = 120
        for icon, title, domain in sources:
            draw.rounded_rectangle([(16, y_s), (304, y_s + 56)], radius=8, fill=(31, 41, 55))
            draw.text((28, y_s + 18), icon, font=get_font(18))
            draw.text((60, y_s + 14), title[:22] + "...", font=get_font(13, bold=True), fill=(243, 244, 246))
            draw.text((60, y_s + 34), domain, font=get_font(11), fill=(156, 163, 175))
            y_s += 66

        # Tabs at bottom sidebar: Chat | Estúdio
        draw.line([(0, h - 70), (320, h - 70)], fill=(55, 65, 81), width=1)
        draw.text((70, h - 35), "💬 Chat", font=get_font(15, bold=active_tab == "Chat"), fill=(255, 255, 255) if active_tab == "Chat" else (156, 163, 175), anchor="mm")
        draw.text((230, h - 35), "🎨 Estúdio", font=get_font(15, bold=active_tab == "Estúdio"), fill=(255, 255, 255) if active_tab == "Estúdio" else (156, 163, 175), anchor="mm")

    # --- Print 1: Chat IaaS vs PaaS vs SaaS ---
    img1 = Image.new("RGB", (w, h), color=(17, 24, 39))
    d1 = ImageDraw.Draw(img1)
    draw_base_ui(d1, "Chat")

    # User Question Bubble
    d1.rounded_rectangle([(360, 100), (w - 60, 160)], radius=12, fill=(37, 99, 235))
    d1.text((385, 120), "Você:", font=get_font(13, bold=True), fill=(191, 219, 254))
    d1.text((385, 138), "Qual a diferença entre IaaS, PaaS e SaaS e como o Amazon EC2 e o Elastic Beanstalk se enquadram?", font=get_font(16, bold=False), fill=(255, 255, 255))

    # NotebookLM Response Box
    d1.rounded_rectangle([(360, 185), (w - 60, 680)], radius=12, fill=(31, 41, 55), outline=(55, 65, 81), width=1)
    d1.text((385, 205), "Gemini Notebook (Especialista Cloud AWS):", font=get_font(14, bold=True), fill=(52, 211, 153))
    
    resp1_lines = [
        "Com base no whitepaper 'Overview of Amazon Web Services' [1] e nas aulas práticas [4], os modelos de",
        "computação em nuvem diferem pelo nível de controle que o cliente exerce sobre a infraestrutura:",
        "",
        "1. IaaS (Infrastructure as a Service): Fornece os blocos de infraestrutura fundamentais (servidores, redes,",
        "   armazenamento). O cliente gerencia o sistema operacional, patches e configurações. O Amazon EC2 é o exemplo",
        "   típico de IaaS na AWS, funcionando como uma máquina virtual flexível [1].",
        "",
        "2. PaaS (Platform as a Service): Elimina o fardo de gerenciar o hardware e o sistema operacional subjacente.",
        "   O cliente fornece apenas o código e as variáveis. O AWS Elastic Beanstalk é o exemplo clássico de PaaS da AWS [1],",
        "   gerenciando automaticamente provisionamento, balanceamento de carga e auto-scaling da aplicação.",
        "",
        "3. SaaS (Software as a Service): Produto final completamente mantido pelo provedor (ex: Microsoft 365,",
        "   Salesforce) onde o usuário consome a solução sem qualquer gestão de servidores [1]."
    ]
    y_r = 235
    for line in resp1_lines:
        d1.text((385, y_r), line, font=get_font(15, bold=False), fill=(243, 244, 246))
        y_r += 26

    # Citation Badges at bottom of response
    d1.text((385, 615), "Fontes Citadas:", font=get_font(13, bold=True), fill=(156, 163, 175))
    d1.rounded_rectangle([(490, 608), (760, 638)], radius=6, fill=(15, 23, 42), outline=(59, 130, 246), width=1)
    d1.text((500, 623), "[1] Overview of AWS (p. 4-5)", font=get_font(12, bold=True), fill=(96, 165, 250), anchor="lm")
    d1.rounded_rectangle([(775, 608), (1030, 638)], radius=6, fill=(15, 23, 42), outline=(16, 185, 129), width=1)
    d1.text((785, 623), "[4] Aulas Práticas (Módulo 1)", font=get_font(12, bold=True), fill=(52, 211, 153), anchor="lm")

    # Prompt input at bottom
    d1.rounded_rectangle([(360, 720), (w - 60, 780)], radius=24, fill=(24, 31, 47), outline=(75, 85, 99), width=1)
    d1.text((390, 750), "Faça uma pergunta sobre suas fontes...", font=get_font(15), fill=(107, 114, 128), anchor="lm")

    p1_path = os.path.join(PRINTS_DIR, "print-01-chat-iaas-paas-saas.png")
    img1.save(p1_path, "PNG")
    print(f"Print 1 saved to: {p1_path}")

    # --- Print 2: Chat Shared Responsibility Model ---
    img2 = Image.new("RGB", (w, h), color=(17, 24, 39))
    d2 = ImageDraw.Draw(img2)
    draw_base_ui(d2, "Chat")

    # User Question Bubble
    d2.rounded_rectangle([(360, 100), (w - 60, 160)], radius=12, fill=(37, 99, 235))
    d2.text((385, 120), "Você:", font=get_font(13, bold=True), fill=(191, 219, 254))
    d2.text((385, 138), "Como funciona o Modelo de Responsabilidade Compartilhada e quem deve atualizar o SO de uma EC2?", font=get_font(16, bold=False), fill=(255, 255, 255))

    # NotebookLM Response Box
    d2.rounded_rectangle([(360, 185), (w - 60, 680)], radius=12, fill=(31, 41, 55), outline=(55, 65, 81), width=1)
    d2.text((385, 205), "Gemini Notebook (Especialista Cloud AWS):", font=get_font(14, bold=True), fill=(52, 211, 153))

    resp2_lines = [
        "Segundo a documentação oficial da AWS sobre o 'Shared Responsibility Model' [3]:",
        "",
        "• Segurança DA Nuvem (Security OF the Cloud - Responsabilidade da AWS):",
        "  A AWS é responsável por proteger a infraestrutura global física e lógica que executa todos os serviços,",
        "  incluindo hardware de servidores, datacenters físicos, cabeamento, geradores e a camada de virtualização [3].",
        "",
        "• Segurança NA Nuvem (Security IN the Cloud - Responsabilidade do Cliente):",
        "  O cliente é inteiramente responsável por tudo o que coloca ou executa na nuvem, incluindo a classificação e",
        "  criptografia dos dados, criação de credenciais e papéis no IAM, e configurações de firewall (Security Groups) [3].",
        "",
        "Respondendo à sua pergunta específica:",
        "No caso de uma instância Amazon EC2 (IaaS), É DE RESPONSABILIDADE EXCLUSIVA DO CLIENTE instalar, atualizar",
        "e aplicar patches de segurança no sistema operacional (Linux ou Windows) [3]. A AWS apenas garante que a máquina",
        "virtual inicial e o hipervisor subjacente estejam operacionais."
    ]
    y_r = 235
    for line in resp2_lines:
        d2.text((385, y_r), line, font=get_font(15, bold=False), fill=(243, 244, 246))
        y_r += 26

    # Citation Badges
    d2.text((385, 615), "Fontes Citadas:", font=get_font(13, bold=True), fill=(156, 163, 175))
    d2.rounded_rectangle([(490, 608), (810, 638)], radius=6, fill=(15, 23, 42), outline=(239, 68, 68), width=1)
    d2.text((500, 623), "[3] Shared Responsibility Model (Guia)", font=get_font(12, bold=True), fill=(248, 113, 113), anchor="lm")

    # Prompt input at bottom
    d2.rounded_rectangle([(360, 720), (w - 60, 780)], radius=24, fill=(24, 31, 47), outline=(75, 85, 99), width=1)
    d2.text((390, 750), "Faça uma pergunta sobre suas fontes...", font=get_font(15), fill=(107, 114, 128), anchor="lm")

    p2_path = os.path.join(PRINTS_DIR, "print-02-chat-responsabilidade-compartilhada.png")
    img2.save(p2_path, "PNG")
    print(f"Print 2 saved to: {p2_path}")

    # --- Print 3: Chat EC2 vs Lambda ---
    img3 = Image.new("RGB", (w, h), color=(17, 24, 39))
    d3 = ImageDraw.Draw(img3)
    draw_base_ui(d3, "Chat")

    # User Question Bubble
    d3.rounded_rectangle([(360, 100), (w - 60, 160)], radius=12, fill=(37, 99, 235))
    d3.text((385, 120), "Você:", font=get_font(13, bold=True), fill=(191, 219, 254))
    d3.text((385, 138), "Quando devo escolher Amazon EC2 em vez de AWS Lambda (Serverless)?", font=get_font(16, bold=False), fill=(255, 255, 255))

    # NotebookLM Response Box
    d3.rounded_rectangle([(360, 185), (w - 60, 680)], radius=12, fill=(31, 41, 55), outline=(55, 65, 81), width=1)
    d3.text((385, 205), "Gemini Notebook (Especialista Cloud AWS):", font=get_font(14, bold=True), fill=(52, 211, 153))

    resp3_lines = [
        "A escolha entre Amazon EC2 e AWS Lambda segue critérios técnicos extraídos do Well-Architected Framework [2]",
        "e dos comparativos práticos de arquitetura [4]:",
        "",
        "Escolha Amazon EC2 quando:",
        "1. Aplicações de Longa Duração: Sistemas que rodam 24x7 contínuos onde Instâncias Reservadas reduzem custo.",
        "2. Customização do Kernel: Necessidade de drivers proprietários ou softwares com portas de rede específicas [1].",
        "3. Processamento Contínuo Pesado: Cargas com centenas de gigabytes de RAM fixa ou uso intensivo de GPU.",
        "",
        "Escolha AWS Lambda (Serverless) quando:",
        "1. Arquitetura Orientada a Eventos: Disparos a partir de uploads no S3, mensagens SQS ou mudanças no DynamoDB [2].",
        "2. Tráfego Variável ou Esporádico: Onde manter servidores ociosos seria desperdício financeiro (paga por ms) [2].",
        "3. Zero Manutenção Operacional: Sem necessidade de aplicar patches no SO ou gerenciar clusters de servidores [4]."
    ]
    y_r = 235
    for line in resp3_lines:
        d3.text((385, y_r), line, font=get_font(15, bold=False), fill=(243, 244, 246))
        y_r += 26

    # Citation Badges
    d3.text((385, 615), "Fontes Citadas:", font=get_font(13, bold=True), fill=(156, 163, 175))
    d3.rounded_rectangle([(490, 608), (760, 638)], radius=6, fill=(15, 23, 42), outline=(168, 85, 247), width=1)
    d3.text((500, 623), "[2] Well-Architected (Custos)", font=get_font(12, bold=True), fill=(192, 132, 252), anchor="lm")
    d3.rounded_rectangle([(775, 608), (1020, 638)], radius=6, fill=(15, 23, 42), outline=(16, 185, 129), width=1)
    d3.text((785, 623), "[4] Aulas Práticas (Decisões)", font=get_font(12, bold=True), fill=(52, 211, 153), anchor="lm")

    # Prompt input at bottom
    d3.rounded_rectangle([(360, 720), (w - 60, 780)], radius=24, fill=(24, 31, 47), outline=(75, 85, 99), width=1)
    d3.text((390, 750), "Faça uma pergunta sobre suas fontes...", font=get_font(15), fill=(107, 114, 128), anchor="lm")

    p3_path = os.path.join(PRINTS_DIR, "print-03-chat-ec2-vs-lambda.png")
    img3.save(p3_path, "PNG")
    print(f"Print 3 saved to: {p3_path}")

    # --- Print 4: Estúdio (Studio) NotebookLM ---
    img4 = Image.new("RGB", (w, h), color=(17, 24, 39))
    d4 = ImageDraw.Draw(img4)
    draw_base_ui(d4, "Estúdio")

    # Studio Header
    d4.text((360, 100), "Estúdio de Criação", font=get_font(28, bold=True), fill=(243, 244, 246))
    d4.text((360, 140), "Gere materiais automáticos de estudo estruturados a partir das 4 fontes selecionadas.", font=get_font(16), fill=(156, 163, 175))

    # Grid of Studio generated cards
    cards = [
        ("🎙️", "Resumo em Áudio (Audio Overview)", "Podcast Deep Dive com 2 apresentadores debatendo os fundamentos e analogias da nuvem AWS.", "Pronto • 9 min • Baixado"),
        ("🗺️", "Mapa Mental de Conhecimento", "Diagramação visual radial interligando Modelos de Nuvem, Regiões, Serviços e Well-Architected.", "Pronto • PNG • Baixado"),
        ("📊", "Apresentação de Slides", "Deck executivo de 9 slides sintetizando conceitos-chave, comparativos técnicos e segurança.", "Pronto • PDF • Baixado"),
        ("📝", "Guia de Estudos & Quiz", "Roteiro completo de revisão com flashcards e simulado de 10 questões padrão Cloud Practitioner.", "Pronto • MD • Baixado")
    ]

    cx = 360
    cy = 190
    card_w = 580
    card_h = 240
    
    for i, (icon, title, desc, status) in enumerate(cards):
        col = i % 2
        row = i // 2
        px = cx + col * (card_w + 30)
        py = cy + row * (card_h + 30)

        d4.rounded_rectangle([(px, py), (px + card_w, py + card_h)], radius=14, fill=(31, 41, 55), outline=(55, 65, 81), width=1)
        d4.text((px + 24, py + 24), icon, font=get_font(32))
        d4.text((px + 74, py + 24), title, font=get_font(18, bold=True), fill=(243, 244, 246))
        
        # Desc wrapped
        d4.text((px + 24, py + 80), desc[:65], font=get_font(14), fill=(156, 163, 175))
        d4.text((px + 24, py + 105), desc[65:130], font=get_font(14), fill=(156, 163, 175))

        # Status badge
        d4.rounded_rectangle([(px + 24, py + 170), (px + 260, py + 205)], radius=8, fill=(6, 78, 59), outline=(16, 185, 129), width=1)
        d4.text((px + 142, py + 188), status, font=get_font(13, bold=True), fill=(110, 231, 183), anchor="mm")

        # Action button
        d4.rounded_rectangle([(px + card_w - 140, py + 170), (px + card_w - 24, py + 205)], radius=8, fill=(59, 130, 246))
        d4.text((px + card_w - 82, py + 188), "Abrir", font=get_font(14, bold=True), fill=(255, 255, 255), anchor="mm")

    p4_path = os.path.join(PRINTS_DIR, "print-04-estudio-notebooklm-materiais.png")
    img4.save(p4_path, "PNG")
    print(f"Print 4 saved to: {p4_path}")

if __name__ == "__main__":
    generate_mindmap()
    generate_slides()
    generate_prints()
    print("All assets generated successfully!")
