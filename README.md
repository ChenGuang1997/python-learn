# python-learn
python-learn,python学习笔记&amp;资料
flowchart TD
    %% 1. 用户层
    User[用户/运维人员] --> Grafana_Web[Grafana 前端界面]

    %% 2. 接入层（K8s 网络）
    subgraph K8s 接入层
        Ingress[Ingress Controller\n(Nginx/Traefik)] --> Grafana_SVC[Grafana Service\n(ClusterIP)]
        Promtail_DS[Promtail DaemonSet\n(每节点1个Pod)] --> Loki_Distributor_SVC[Loki Distributor Service\n(ClusterIP)]
    end

    %% 3. 核心服务层（Loki 集群 + Grafana）
    subgraph 核心服务层
        %% Grafana 组件（高可用）
        Grafana_SVC --> Grafana[Grafana Deployment\n(2副本, 配置存储ConfigMap)]
        Grafana --> Loki_Query_Frontend_SVC[Loki Query Frontend Service\n(ClusterIP)]

        %% Loki 集群组件（高可用拆分）
        Loki_Distributor_SVC --> Loki_Distributor[Loki Distributor\n(3副本, 负载均衡接收日志)]
        Loki_Distributor --> Loki_Ingester_SVC[Loki Ingester Service\n(Headless Service)]
        
        Loki_Ingester_SVC --> Loki_Ingester[Loki Ingester\n(3副本 StatefulSet\n分片+副本存储日志)]
        Loki_Ingester --> MinIO_SVC[MinIO Service\n(ClusterIP)]  %% 持久化日志到 MinIO
        
        Loki_Query_Frontend_SVC --> Loki_Query_Frontend[Loki Query Frontend\n(2副本, 查询优化+缓存)]
        Loki_Query_Frontend --> Loki_Querier_SVC[Loki Querier Service\n(ClusterIP)]
        
        Loki_Querier_SVC --> Loki_Querier[Loki Querier\n(3副本, 处理查询请求)]
        Loki_Querier --> Loki_Ingester_SVC  %% 优先查 Ingester 缓存
        Loki_Querier --> MinIO_SVC  %% 查 MinIO 持久化日志
        
        Loki_TableManager[Loki Table Manager\n(1副本, 数据生命周期管理)] --> MinIO_SVC  %% 管理 MinIO 分片/过期
    end

    %% 4. 存储层（MinIO 分布式存储）
    subgraph 存储层
        MinIO_SVC --> MinIO[MinIO 分布式集群\n(4节点 StatefulSet\nErasure Code 冗余)]
        MinIO --> MinIO_PVC[MinIO 数据卷\n(PVC, 对接存储类\n如 Ceph/Rook)]
        MinIO --> Loki_Chunk_Bucket[Loki Chunk Bucket\n(存储日志块)]
        MinIO --> Loki_Index_Bucket[Loki Index Bucket\n(存储日志索引)]
    end

    %% 5. 日志收集层（Promtail + 数据源）
    subgraph 日志数据源
        K8s_Pods[K8s 业务 Pod\n(容器日志)] --> Promtail_DS
        Node_Logs[节点系统日志\n(/var/log)] --> Promtail_DS
        App_Logs[宿主机应用日志\n(挂载到Pod)] --> Promtail_DS
    end

    %% 6. 监控与运维层（生产必备）
    subgraph 监控运维层
        Prometheus[Prometheus 监控\n(采集 Loki/MinIO/Grafana 指标)] --> Loki_Ingester
        Prometheus --> MinIO
        Prometheus --> Grafana
        Prometheus --> AlertManager[AlertManager\n(日志异常告警)]
        Secret[K8s Secret\n(MinIO密钥/Loki认证)] --> Loki_Ingester & MinIO & Grafana
        ConfigMap[K8s ConfigMap\n(Loki/Promtail配置)] --> Loki_Distributor & Promtail_DS
    end

    %% 数据流向标注
    style Promtail_DS fill:#f9d,stroke:#333
    style Loki_Ingester fill:#9cf,stroke:#333
    style MinIO fill:#9f9,stroke:#333
    style Grafana fill:#ff9,stroke:#333
