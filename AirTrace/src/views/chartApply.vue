<template>
  <div>
    <div
      :id="id"
      class="line-vertical"
    ></div>
  </div>
</template>
<style>
.line-vertical {
  width: (100vw - 20px);

  height: 460px;
}
</style>

<script>
export default {
  props: {
    id: String,
    data: Array,
    title: String,
    date: Array,
    colorList: Array,
    itemColor: String,
    typename: String,
  },
  data () {
    return {
      chart: Object,
      colorArr: {}
    };
  },
  methods: {
    init () {

      var _this = this;
      _this.colorArr["GCAM5.3_NGFS_downscaled"] = "#51689b";
      _this.colorArr["MESSAGEix-GLOBIOM 1.1_downscaled"] = "#ce5c5c";
      _this.colorArr["REMIND-MAgPIE 2.1-4.2_downscaled"] = "#fbc357";

      var myChart = echarts.init(document.getElementById(_this.id));
      _this.chart = myChart;
      myChart.showLoading({
        text: 'Processing...',
        color: '#ffb600',
        textColor: '#ffb600',
        fontSize: 28,
        textStyle: {
          fontSize: 28,
        },
        maskColor: 'rgba(255, 255, 255, 0.8)',
      });
    },
    loadData () {
      var _this = this;
      var myChart = _this.chart;
      var option = {
        animationDuration: 5000,
        addDataAnimation: true,
        animationDuration: 2000,
        animationEasing: "ExponentialOut",
        legend: {
          data: [],
          show: false,
        },
        xAxis: {
          type: "category",
          data: _this.date,
          axisPointer: {
            value: "Tue",
            snap: true,
            lineStyle: {
              color: "#DDDDDD",
              width: 2,
            },
            label: {
              show: true,
              formatter: function (params) {
                return params.value == 0 ? "" : params.value;
              },
              backgroundColor: "#DDDDDD",
            },
            handle: {
              show: false,
              color: "#C5f100",
            },
          },
          splitLine: {
            show: false,
          },
        },
        yAxis: {
          type: "value",
        },
        tooltip: {
          order: "valueDesc",
          trigger: "axis",
          backgroundColor: "rgba(50, 50, 50, 0.7)",
          position: function (point, params, dom, rect, size) {
            var x = point[0];
            var y = point[1];
            var viewWidth = size.viewSize[0];
            var viewHeight = size.viewSize[1];
            var boxWidth = size.contentSize[0];
            var boxHeight = size.contentSize[1];
            var posX = 0;
            var posY = 0;

            if (x < boxWidth) {
              posX = 10;
            } else {
              posX = x - boxWidth;
            }

            if (y < boxHeight) {
              posY = 10;
            } else {
              posY = y - boxHeight;
            }
            return [posX, posY];
          },
          textStyle: {
            color: "#fff",
          },
          formatter: function (params) {
            var html = "";
            if (params.length != 0) {
              var getName = params[0].name;
              html += getName + "<br/>";
              for (let i = 0; i < params.length; i++) {
                if (
                  params[i].value != null &&
                  params[i].value != 0 &&
                  params[i].value != ""
                ) {
                  html += params[i].marker;
                  html +=
                    params[i].seriesName + ":" + params[i].value + "<br/>";
                }
              }
            }
            return html;
          },
        },
        grid: {
          left: "10%",
          right: "4%",
          bottom: "8%",
          containLabel: true,
        },
        series: [],
      };

      var model = [];
      var seriesList = [];


      if (_this.data.length > 0) {
        if (typeof _this.data[0] == "number") {
          option.yAxis.min = 0;
          option.yAxis.max = 0.8;
          option.title = {
            left: "center",
            top: "center",
            text: "No Data",
            effect: "whirling",
            effectOption: {
              backgroundColor: "rgba(50,50,50,0.5)",
            },
            textStyle: {
              fontSize: 28,
              fontWeight: "bold",
            },
          };
        } else {
          _this.data.map((item, index) => {
            var dataReport = [];
            _this.date.forEach(function (value) {
              if (item.Data[value] == 0) {
                dataReport.push("");
              } else dataReport.push(parseFloat(item.Data[value]).toFixed(2));
            });
            var resultarr = [...new Set(dataReport)];
            if (resultarr.length == 1 && resultarr[0] == "") {
              return;
            }
            var newcolor = _this.colorArr[item.Model];
            seriesList.push({
              connectNulls: true,
              name: item.Model,
              type: "line",
              data: dataReport,
              smooth: true,
              endLabel: {
                show: false,
                formatter: function (params) {
                  return parseFloat(params.value).toFixed(2);
                },
              },
              labelLayout: {
                moveOverlap: "shiftY",
              },
              emphasis: {
                focus: "series",
              },
              showSymbol: true,
              hoverAnimation: true,
              symbol: "circle",
              symbolSize: 6,
              itemStyle: {
                normal: {
                  color: newcolor,
                  lineStyle: {
                    width: 3,
                    color: newcolor,
                  },
                },
              },
            });
          });

        }
      } else {
        option.yAxis.min = 0;
        option.yAxis.max = 0.8;
        option.title = {
          left: "center",
          top: "center",
          text: "No Data",
          effect: "whirling",
          effectOption: {
            backgroundColor: "rgba(50,50,50,0.5)",
          },
          textStyle: {
            fontSize: 28,
            fontWeight: "bold",
          },
        };
      }

      option.legend.data = model;

      if (seriesList.length < 1) {
        option.yAxis.min = 0;
        option.yAxis.max = 3000;
      } else {
        option.series = seriesList;
      }
      myChart.clear();
      option && myChart.setOption(option, true);

      myChart.hideLoading();
    },
  },
  mounted () {
    this.init();

    this.bus.$on("chartReportNoData", () => {
      this.loadData();
    });

    window.addEventListener("resize", () => {
      if (this.chart != undefined) this.chart.resize();
    });
  },
  watch: {
    data: {
      handler (new_value, old_value) {
        this.init();
        this.loadData();
      },
      deep: true,
    },
  },
};
</script>
