---
name: capricornio-visualizacoes
description: Criar dashboards e visualizações 3D no navegador para produtos da Capricórnio, com indicadores rastreáveis e mapeamento prévio de acesso a fontes.
---

# Dashboards e 3D

Leia `AGENTS.md`. Antes de conectar fontes, mapeie responsável, solicitação, concessão, manutenção e revogação de acesso, além das permissões necessárias. A solução corporativa própria de DataViz continua em avaliação; este template não declara uma plataforma aprovada.

## Dashboard

- Defina decisão apoiada, público, fonte, fórmula, granularidade, unidade, período e frequência de atualização de cada indicador. Não invente métricas ou metas da empresa.
- Use Python/SQL para preparar e validar agregações; JavaScript e Tailwind para a interface. Escolha biblioteca de gráficos apenas quando necessária, justificando a dependência.
- Mostre origem, atualização, filtros e unidade. Distinga zero, dado ausente e acesso negado. Não use dados sintéticos como evidência de desempenho real.
- Valide totais, duplicidades, denominadores, datas e comparações. Garanta leitura por teclado e alternativa textual/tabela para informação essencial do gráfico.
- Autorização deve filtrar os dados no servidor. Exportação e compartilhamento respeitam as mesmas permissões da consulta.

## Visualização 3D

- Escolha **Three.js ou Babylon.js** conforme interação, desempenho e complexidade; registre a justificativa em `docs/decisoes.md`. Não instale as duas por padrão.
- Confirme unidades, escala, sistema de coordenadas e origem/autorização dos modelos. Não envie ativos industriais confidenciais a serviços externos sem autorização.
- Carregue ativos sob demanda, descarte recursos da GPU quando não usados e teste desempenho em equipamentos representativos. Ofereça estado de carregamento, falha e alternativa para dispositivos sem suporte.

Entregue critérios verificáveis de precisão e usabilidade, fontes dos indicadores ou ativos e a lista de acessos pendentes.
