<template>
  <div>

    <div
      :id="id"
      class="line-vertical"
    ></div>
  </div>
</template>
<style>
</style>
<script>     
export default {
  props: {
    id: String,
    data: Object,
    title: String,
    date: Array,
    colorList: Array,
    itemColor: String,
    typename: String
  },

  data () {
    return {
      chart: Object,
      styleChart: {
        width: '100%',
      },
    }
  },
  methods: {
    init () {
      var _this = this;
      var myChart = echarts.init(document.getElementById(_this.id));
      _this.chart = myChart;

      myChart.showLoading({
        text: '正在加载...'
      });

      var option = {
        animation: true,
        animationDuration: 5000,
        addDataAnimation: true,
        color: ['#E0301E'],
        tooltip: {
          trigger: 'axis',
          backgroundColor: "rgba(50, 50, 50, 0.7)",
          axisPointer: {
            symbolSize: 9,
            type: 'cross',
            label: {
              backgroundColor: _this.itemColor
            }
          },
          textStyle: {
            color: '#fff',
          },
          formatter: function (params) {
            var html = '';
            if (params.length != 0) {
              var getName = params[0].name;
              html += getName + '<br/>';
              for (let i = 0; i < params.length; i++) {
                if (params[i].value != null && params[i].value != 0 &&
                  params[i].value != '') {
                  html += params[i].marker;
                  html += params[i].seriesName + ':' + params[i].value + '<br/>';
                }
              }
            }
            return html;
          }
        },
        xAxis: [{
          type: 'category',
          boundaryGap: false,
          data: _this.date,
        }],
        yAxis: [{
          type: 'value'
        }],
        grid: {
          left: '5%',
          bottom: '12%',
          containLabel: true
        },
        series: [{
          connectNulls: true,
          name: _this.typename,
          type: 'line',
          stack: '总量',
          smooth: true,
          data: [],
          lineStyle: {
            width: 0
          },
          showSymbol: true,
          hoverAnimation: true,
          cursor: 'pointer',
          rippleEffect: {
            period: 1.5,
            scale: 6,
            brushType: 'stroke',
          },
          symbol: 'circle',
          symbolSize: 6,
          itemStyle: {
            normal: {
              color: _this.itemColor,
              lineStyle: {
                color: _this.itemColor,
                width: 2
              },
            },
          },
          areaStyle: {
            opacity: 0.8,
            color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
              offset: 1,
              color: '#fff'
            }, {
              offset: 0,
              color: _this.itemColor
            }])
          },
          emphasis: {
            focus: 'series'
          },
        },]
      };
      if (_this.data != null) {

        var item = _this.data;
        var dataGasPrice = [];
        _this.date.forEach(i => {
          if (item[i] == 0)
            dataGasPrice.push('');
          else
            dataGasPrice.push(item[i]);
        });
        option.series[0].data = dataGasPrice;
      }
      else {
        option.series[0].data = [];
        option.title = {
          left: "center",
          top: "center",
          text: 'No Data',
          effect: 'whirling',
          effectOption: {
            backgroundColor: "rgba(50,50,50,0.5)",
          },
          textStyle: {
            fontSize: 28,
            fontWeight: 'bold'
          }
        }
      }

      myChart.clear();

      option && myChart.setOption(option, true);
      myChart.hideLoading();

    }
  },
  mounted () {
    this.init();
    this.bus.$on("chartInit", () => {
       
      this.$nextTick(function () {
        this.chart.resize();
      }) 
    });
    window.addEventListener('resize', () => {
      if (this.chart != undefined)
        this.chart.resize();
    });
  },
  created () {

  },
  watch: {
    data: {
      handler (new_value, old_value) {
        this.init();
        this.chart.resize();
      },
      deep: true
    }
  }
}
</script>
