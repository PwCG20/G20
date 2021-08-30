<template>
  <div>
    <div
      id="secondChart"
      class="line-vertical"
      style="height: 350px; margin: 0 auto"
      :style="[styleChart]"
    ></div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      pageIndex: 1,
      styleChart: {
        width: "100%",
      },
      middleChart: {},
    };
  },
  methods: {
    importJS () {
      var script = document.createElement("script");
      script.id = "mapbox-js-module";
      script.type = "text/javascript";
      script.src = this.getResource("echarts.min.js");
      script.async = true;
      script.defer = true;
      document.head.appendChild(script);
    },
    addSecondChart () {
      let _self = this;
      var requestPara = {
        pageCode: "companypddata",
        searchItems: [],
        order: {},
        columns: [],
        withSocialStatus: false,
        index: _self.pageIndex,
        size: 99999,
      };
      _self.callApi("GetDocs", requestPara).then((data) => {
        let newData = data.data;
        _self.companyResultList = newData.items;
        _self.initSecondChar();
      });
    },
    initSecondChar () {
      let _self = this;
      var temp = 0;


      var list = _self.companyResultList.sort((a, b) => {
        return parseFloat(a.UnAdjustedPD.toString()) - parseFloat(b.UnAdjustedPD.toString());
      });
      var xAsixList = list.map((data) =>
        data.Company.toString()
      );
      var yAsixList = list.map((data) =>
        (parseFloat(data.UnAdjustedPD.toString()) * 100).toFixed(2)
      );

      let myChart = echarts.init(document.getElementById("secondChart"));
      _self.middleChart = myChart;
      var option = {
        color: [
          "#EB8C00"
        ],
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "shadow",
          },
          textStyle: {
            fontSize: 30,
          },
          formatter: function (param) {
            var value = param[0].value;
            if (value == null || value == undefined) {
              value = 0;
            }
            return param[0].axisValue + ":" + parseFloat(value).toFixed(2) + "%";
          },
        },
        toolbox: {
          show: true,
        },
        grid: {
          left: "15%",
          bottom: "33%",
          right: "3%",
        },
        xAxis: {
          type: "category",
          data: xAsixList,
          axisLabel: {
            interval: 0,
            rotate: 35,

          },
        },

        yAxis: {
          type: "value",
          axisLabel: {
            formatter: function (param) {
              return parseFloat(param).toFixed(1) + "%";
            },
          },
        },
        series: [
          {
            type: "bar",
            data: yAsixList,
          },
        ],
      };
      myChart.setOption(option, true);
    },
    resize () {
      let _self = this;
      var width = document.body.clientWidth;
      _self.styleChart = width - 30 + "px";

      this.$nextTick(() => {
        _self.middleChart.resize();
      });
    },
  },
  beforeMount () {
    this.importJS();
  },
  mounted () {
    let _self = this;
    let si = setInterval(function () {
      if (echarts) {
        _self.addSecondChart();
        clearInterval(si);
        console.log("clearInterval");
      }
      console.log("setInterval");
    }, 1000);
    /*window.onresize = () => {
      _self.resize();
    };*/
  },
};
</script>
<style>
</style>