<template>
  <div class="chart-content">
    <div class="title">
      Applicant’s climate adjusted PD relative to portfolio
    </div>
    <div
      class="condition"
      style="padding-top: 10px"
    >
      <span style="
          padding-right: 10px;
          margin-top: 8px;
          font-size: 16px;
          line-height: 30px;
        ">Scenario:
      </span>
      <v-select
        style="max-width: 200px"
        color="#E0301E"
        :items="ScenarioArray"
        v-model="ScenarioValue"
        item-text="label"
        item-value="value"
        outlined
        @change="changeScenarion"
        dense
        label=""
      >
      </v-select>
    </div>
    <div
      id="chartCompanyResult"
      style="height: 460px; margin: 20px auto"
    ></div>
  </div>
</template>

<script>
export default {
  props: {
    year: Array,
    ScenarioArray: Array,
    ScenarioValue: String,
    sectorColor: Array,
    adjustedPDData: Object,
    companyName: String,
  },
  data () {
    return {
      chart: Object,
    };
  },
  methods: {
    load () {
      var myChart = echarts.init(document.getElementById("chartCompanyResult"));
      _this.mychart = myChart;
    },
    changeScenarion () {
      this.bus.$emit("adjuestChangeScenario", this.ScenarioValue);
    },
    loadData () {
      var _this = this;
      var myChart = _this.mychart;
      myChart.showLoading({
        text: "loading...",
      });
      var option = {
        baseOption: {
          timeline: {
            axisType: "category",
            orient: "vertical",
            autoPlay: false,
            inverse: true,
            playInterval: 3000,
            left: null,
            right: 10,
            top: 20,
            bottom: 50,
            width: 55,
            height: null,
            symbol: "none",
            checkpointStyle: {
              borderWidth: 2,
            },
            controlStyle: {
              showNextBtn: false,
              showPrevBtn: false,
            },
            data: [],
          },
          title: [
            {
              textAlign: "center",
              left: "160",
              top: "10%",
              textStyle: {
                color: "rgba(0,0,0,0.3)",
                fontSize: 40,
              },
            },
          ],

          tooltip: {
            trigger: "axis",
            axisPointer: {
              type: "shadow",
            },
            formatter: function (param) {
              var value = param[0].value;
              return param[0].axisValue + ":" + value.toFixed(2) + "%";
            },
          },
          grid: {
            top: "3%",
            left: "100",
            right: "5%",
            bottom: "30%",
          },
          dataset: {
            source: [],
          },
          xAxis: {
            type: "category",
            data: [],
            itemStyle: {},
            boundaryGap: true,
            axisLabel: {
              interval: 0,
              rotate: 60,
              color: function (param) {
                console.log({ name: param });
                if (param == _this.companyName) {
                  return "#0089eb";
                } else return "#000";
              },
            },
          },
          yAxis: {
            type: "value",
            axisLabel: {
              formatter: function (param) {
                return parseFloat(param).toFixed(1);
              },
            },
          },
          series: [
            {
              encode: {
                x: 1,
                y: 0,
              },
              type: "bar",
              data: [],
              animation: false,
              barCategoryGap: "40%",
              barGap: "-100%",
              itemStyle: {
                normal: {
                  label: {
                    show: true,
                    position: "top",
                    textStyle: {
                      color: "#0089eb",
                      fontSize: 15,
                    },
                    formatter: function (params) {
                      if (params.name == _this.companyName) {
                        return params.value.toFixed(2) + "%";
                      } else return "";
                    },
                  },
                  color: function (param) {
                    if (param.name == _this.companyName) {
                      return "#0089eb";
                    } else {
                      return _this.sectorColor[param.data.sector];
                    }
                    /* return _this.randomHexColor();*/
                  },
                },
              },
              animationDuration: 0,
              animationDurationUpdate: 4000,
              animationEasing: "linear",
              animationEasingUpdate: "linear",
              graphic: {
                elements: [
                  {
                    type: "text",
                    right: 160,
                    bottom: 60,
                    style: {
                      text: "2025",
                      font: "bolder 80px monospace",
                      fill: "rgba(100, 100, 100, 0.25)",
                    },
                    z: 100000,
                  },
                ],
              },
            },
          ],
        },
        options: [],
      };

      var data = _this.adjustedPDData[_this.ScenarioValue];
      var item = JSON.parse(data);
      var seriesList = [];

      option.baseOption.timeline.data = _this.year;

      _this.year.map((k) => {
        seriesList.push({
          title: {
            text: k,
          },
          series: [
            {
              data: item[k].sort((a, b) => {
                return a.value - b.value;
              }),
            },
          ],
          xAxis: {
            type: "category",
            data: item[k]
              .sort((a, b) => {
                return a.value - b.value;
              })
              .map((item) => {
                return [item.company];
              }),
            itemStyle: {},
            boundaryGap: true,
            axisLabel: {
              interval: 0,
              rotate: 60,
              color: function (param) {
                if (param == _this.companyName) {
                  return "#0089eb";
                } else return "#000";
              },
            },
          },
          animationDuration: 5000,
          animationEasing: "cubicInOut",
        });
      });

      option.options = seriesList;
      myChart.clear();
      myChart.hideLoading();
      myChart.setOption(option, true);


    },
  },
  mounted () {
    this.load();
    this.bus.$on("thirdChangeScenario", (parmas) => {
      this.ScenarioValue = parmas;
      this.loadData();
    });
  },
  watch: {
    adjustedPDData: {
      handler () {
        this.loadData();
      },
      deep: true,
    },
    ScenarioValue () {
      this.loadData();
    },
  },
};
</script>
