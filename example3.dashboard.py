from grafanalib.core import (
    Dashboard, Graph,
    OPS_FORMAT, Row,
    single_y_axis, Target, TimeRange, YAxes, YAxis
)
from numpy import DataSource


dashboard = Dashboard(
    title="Python generated dashboard",
    rows=[
        Row(panels=[
          Graph(
              title="Prometheus http requests",
              dataSource="prometheus",
              targets=[
                  Target(
                    datasource='prometheus',
                    expr='rate(prometheus_http_response_size_bytes_bucket[5m])',
                    legendFormat="{{ handler }}",
                    refId='A',
                  ),
              ],
              yAxes=single_y_axis(format=OPS_FORMAT),
          ),
        ]),
    ],
).auto_panel_ids()