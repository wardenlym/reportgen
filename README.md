本周工作：
16H Prometheus文档学习和api测试等
8H  python prometheus_client进行简单的指标查询测试。
16H 用grafana创建报表用dashboard和调整图表绘制等。

实现过程：
1. 检查现有metric，找到对应指标，如果有必要需要增加Prometheus中的采集指标
2. 预先制作grafana图表，测试通过api能否取到指定周期的数据
3. 写python脚本，该脚本通过整合需要的数据，形成一份单页的数据报表

报表需要体现的metric:
# 本周期
last_week:
topk pod/workload usage - cpu/mem/disk/bandwith by namespace (占用资源最多的业务)
utilization ratio - pod/cpu/mem (集群资源的使用率)
topk svc request - by namespace (被访问最多业务)
critical alerting (如果有高级别的告警)

# 上周期环比变化
week_earlier_incr/decr:
pod_num/deployment/cpu/mem/disk/bandwith (关键性资源与上周环比增长/下降的量和比例)
svc request - by namespace (服务调用量环比变化)

预计需要2-3周左右。
