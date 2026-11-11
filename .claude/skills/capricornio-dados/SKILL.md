---
name: capricornio-dados
description: Modelar dados e implementar SQL, migrações e análises em produtos da Capricórnio, incluindo preparação para Neon e acesso industrial autorizado a ClickHouse.
---

# Dados e SQL

Leia `AGENTS.md` e a matriz de decisões em `docs/stack-e-governanca.md`.

- Confirme fonte, responsável, finalidade, granularidade, chave, unidades, fuso e classificação dos dados antes de modelar. Documente ausências e divergências; preserve os originais e não preencha lacunas por invenção.
- Use PostgreSQL/SQL compatível com Neon para protótipos. Plano, contratação e acessos estão pendentes. Até a liberação, prepare modelo, consultas e migrações sem conectar a serviços reais. Se precisar executar SQL localmente, combine uma instância PostgreSQL de desenvolvimento isolada, com dados sintéticos; ela não substitui a diretriz corporativa.
- Quando Neon for liberado, isole banco e credenciais por protótipo e ambiente; conceda acesso individual e mínimo necessário. `DATABASE_URL` é segredo exclusivo do backend. Use TLS conforme as instruções oficiais de conexão e nunca reduza a verificação para contornar falhas.
- Para ClickHouse industrial, obtenha acesso com os administradores e confirme tabelas, permissões, limites e janela de consulta. Não copie a base industrial para o protótipo por conveniência.
- Use um driver Python apropriado e consultas parametrizadas; entradas não podem virar SQL por concatenação. Para nomes de tabela/coluna dinâmicos, use identificadores seguros e lista permitida. Limite volume e tempo de execução.
- Crie migrações SQL versionadas quando a funcionalidade exigir persistência. Descreva impacto, estratégia de backup/recuperação e validação em ambiente isolado. Nunca execute alterações destrutivas ou migrações em bases reais sem autorização específica.
- Para análises, valide duplicidades, chaves, nulos, denominadores, totais, percentuais, períodos e diferenças de unidades. Separe correlação de causalidade. Informe a origem e a data da extração, sem expor registros confidenciais na resposta.

Entregue modelo/consulta, premissas, verificações realizadas e acessos ainda necessários. A migração futura para a plataforma corporativa deve permanecer possível; evite dependência desnecessária de recursos exclusivos de um provedor.
