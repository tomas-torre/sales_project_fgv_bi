# Projeto de Business Intelligence – Enterprise X  
Trabalho Final – Curso de BI (FGV)  
Autor: **Tomás Fernandes Torre**  

## Contexto  
Este projeto foi desenvolvido como trabalho final do curso de Business Intelligence da FGV. O estudo de caso aborda a **Enterprise X**, uma empresa fictícia de distribuição de erva-mate na América do Sul, que buscava implementar uma cultura **data driven** para profissionalizar sua gestão e alinhar estratégias comerciais entre suas matrizes no Brasil, Argentina, Paraguai, Uruguai e Bolívia.  

O objetivo central foi criar uma **plataforma de BI integrada** para a alta gestão, com dashboards e indicadores de desempenho que suportassem a tomada de decisão estratégica baseada em dados.  

---

## Documentação
O que você encontrará na documentação (modelo obrigatório da FGV): 

| Seção                        | Descrição                                                                 |
|-------------------------------|---------------------------------------------------------------------------|
| **Introdução**               | Contexto da empresa fictícia, motivação para o BI e desafios identificados |
| **Objetivos**                | Objetivo estratégico e objetivos específicos do projeto de BI              |
| **Data Driven Canvas**       | Metas, fórmulas, atores envolvidos e ações estratégicas                   |
| **Wireframe dos Dashboards** | Protótipos iniciais com filtros, métricas e visualizações                  |
| **Dashboard Final**          | Layout adaptado para desktop, tablet e celular                             |
| **Cronograma de Atividades** | Cálculo de horas por etapa (Banco, ETL, DAX, Layout, etc.)                 |
| **Mapeamento do Legado**     | Fontes antigas: CRM e sistema financeiro                                   |
| **Mapeamento das Origens**   | Fontes atuais: CRM/ERP via API + PostgreSQL                                |
| **Metadados**                | Estrutura das tabelas `f_sales`, `d_products`, `d_salesman`                |
| **Indicadores**              | Cálculos principais: Faturamento, Ticket Médio, Variação no Tempo, etc.    |
| **Regras Customizadas**      | Classificação de vendedores (*good/treat*)                                |
| **Conclusão**                | Benefícios do BI e próximos passos sugeridos                              |
| **Referências**              | Artigos acadêmicos e livro da FGV   
---

## Metodologia e Modelagem  
O fluxo de desenvolvimento do projeto seguiu as seguintes etapas:  

1. **Geração de Bases de Dados**  
   - Criação de bases simuladas no Excel.  
   - Estruturação de dados de vendas, produtos e vendedores.  

2. **Carga e Armazenamento**  
   - Inserção dos dados no banco **PostgreSQL** via **scripts em Python**.  
   - Criação de schemas e tabelas para suportar análises históricas e atuais.  

3. **Tratamento e ETL**  
   - Conexão entre Power BI e PostgreSQL via conector nativo.  
   - Aplicação de transformações em **SQL Queries** e **Power Query**.  

4. **Modelagem no Power BI**  
   - Criação de relacionamentos entre tabelas fato e dimensão.  
   - Desenvolvimento de medidas em **DAX** para cálculo de métricas de negócio.  

5. **Documentação**  
   - Projeto documentado no modelo acadêmico obrigatório disponibilizado pela FGV.  

---

## Cálculos e Métricas Implementadas  
As principais medidas desenvolvidas em DAX foram:  

- **Faturamento** = Σ Vendas  
- **Quantidade Produzida** = Σ Quantidade  
- **Ticket Médio** = Σ Vendas / Σ Quantidade  
- **Quantidade em Kg Vendidos** = Σ (Vendas / Preço/kg)  
- **Variação Percentual no Tempo** = (Vendas Período Atual / Vendas Período Anterior) – 1  

Além disso, foi criada uma **regra de desempenho de vendedores**, comparando vendas médias individuais com a média global, para classificação automática em *“good”* ou *“treat”*.  

---

## Dashboards e Entregas  
O projeto entregou diferentes painéis interativos no Power BI, acessíveis via **desktop, tablet e celular**:  

- **Visão Geral de Vendas (Sales Overview)**  
  - Faturamento total e por matriz.  
  - Evolução temporal de vendas.  
  - Variação percentual entre períodos.  

- **Visão por Produto**  
  - Distribuição de vendas por tipo, classe e preço/kg.  
  - Identificação de produtos de alto e baixo giro.  

- **Visão por Vendedor**  
  - Ranking de vendedores.  
  - Comparação de desempenho individual com a média global.  

- **Filtros e Drill-Downs**  
  - Ano/mês, matriz, unidade, tipo de produto, gerente e vendedor.  

---

## Conclusão  
Com este projeto de BI, a **Enterprise X** passou a ter uma plataforma unificada para análise de vendas, produtos e vendedores. Os dashboards permitem:  

- Monitoramento em tempo real dos indicadores.  
- Identificação rápida de desvios e oportunidades.  
- Ações corretivas e estratégicas mais ágeis.  
- Maior alinhamento entre as matrizes e gestores.  

Assim, o BI se torna um **instrumento essencial para decisões mais assertivas e crescimento sustentável da empresa**.  

---

## **Referências bibliográficas:** 

CHECHI, L.A.; SCHULTZ, G. A produção de erva-mate: um estudo da dinâmica produtiva nos Estados do Sul do Brasil. Enciclopédia Biosfera, Goiás, v. 13, n. 23, 2016. DOI: 10.18677/Enciclopedia_Biosfera_2016_002 Disponível em: https://lume.ufrgs.br/handle/10183/275043. Acesso em:05 ago. 2025.

GULLÓN, Beatriz et al. Yerba mate waste: a sustainable resource of antioxidant compounds.Industrial Crops And Products, [S.L.], v. 113, p. 398-405, mar. 2018. Elsevier BV. http://dx.doi.org/10.1016/j.indcrop.2018.01.064. Disponível em: https://www.sciencedirect.com/science/article/abs/pii/S0926669018300773?via%3Dihub#preview-section-cited-by. Acesso em: 05 ago. 2025.

OLIVEIRA, R.; RONDINA, J. M. Business Intelligence: ferramentas e métodos. Rio de Janeiro: FGV, 2023.  