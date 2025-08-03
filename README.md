# Observabilidade

Apresentação sobre os fundamentos e práticas de observabilidade em sistemas modernos, com foco nos três pilares principais: Logs, Métricas e Traces. Inclui demonstrações práticas com ELK Stack, Prometheus + Grafana + Loki, e OpenTelemetry + Sentry.

## Autor

**Ramon Lacava Gutierrez Gonçales**

---

## Agenda

1. O que é Observabilidade?
2. Os 3 Pilares:
   - Logs
   - Métricas
   - Traces
3. Prática:
   - Elasticsearch, Logstash, Kibana (ELK)
   - Prometheus, Grafana, Loki
   - OpenTelemetry, Sentry
4. Referências

---

## O que é Observabilidade?

> “Observabilidade é o quão bem os estados internos de um sistema podem ser inferidos a partir do conhecimento de suas saídas externas.”  
> — Rudolf E. Kálmán (1960), Teoria de Controle

### Por que é importante?

- Identificar erros ocultos
- Reproduzir cenários com precisão
- Entender a jornada de qualquer usuário
- Diagnosticar problemas inéditos
- Isolar falhas complexas rapidamente

---

## Os Três Pilares

### 1. Logs

Eventos textuais detalhados sobre o sistema.

#### Boas práticas:
- Utilizar níveis: `ERROR`, `WARNING`, `INFO`, `DEBUG`
- Incluir contexto: user_id, IP, dispositivo, navegador, etc.
- Logar requisições HTTP com request e response (se possível)
- Evitar redundância (base64, arquivos inteiros, etc.)
- Definir política de expiração

---

### 2. Métricas

Valores numéricos que representam o estado do sistema.

#### Exemplos:
- Tempo de resposta da API
- Nº de usuários ativos
- Uso de CPU/RAM
- Transações por segundo

#### Anatomia de uma métrica:
- **Nome/Identificador**
- **Valor**
- **Timestamp**
- **Dimensões** (ex: `user_id`, `page`)

#### Boas práticas:
- Dashboards com métricas técnicas e de negócio
- Monitoramento de filas, falhas e desempenho

---

### 3. Traces

Rastreamento completo de requisições ao longo do sistema.

#### Anatomia de um trace:
- **Trace ID**: Identifica o processo completo
- **Span ID**: Representa uma unidade de execução
- **Parent ID**: Relacionamento hierárquico entre spans
- **Timestamp e Duration**: Marcam tempo de execução

---

## Demonstrações Práticas

### ELK Stack
- Coleta e visualização de logs com Elasticsearch, Logstash e Kibana

### Prometheus, Loki e Grafana
- Monitoramento de métricas e logs com dashboards em tempo real

### OpenTelemetry + Sentry
- Rastreio distribuído e gestão de erros com contexto

---

## Referências Importantes

- Documentações oficiais:  
  - [OpenTelemetry](https://opentelemetry.io)  
  - [Grafana](https://grafana.com)  
  - [Prometheus](https://prometheus.io)  
  - [ELK Stack](https://www.elastic.co/what-is/elk-stack)  
  - [Sentry](https://sentry.io)

---

## Conclusão

Observabilidade vai além de apenas coletar logs. Ela é essencial para diagnóstico eficiente, melhoria contínua e garantir uma boa experiência para os usuários. Adotar práticas corretas de logs, métricas e traces é fundamental para a saúde dos sistemas modernos.

