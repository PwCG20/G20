<template>
  <div class="third-chart">
    <v-row class="scenarioselect">
      <v-col class="third-chart-search" cols="8">
        <label class="third-chart-search-label">Scenario:</label>&nbsp;
        <v-select
          :items="ScenarioArray"
          v-model="ScenarioValue"
          item-text="label"
          item-value="value"
          outlined
          @change="chooseScenario"
          dense
          label=""
        ></v-select>
      </v-col>
      <v-col cols="6"></v-col>
    </v-row>
    <div
      id="thirdChart"
      class="line-vertical"
      style="margin: 0 auto; height: 360px"
      :style="[styleChart]"
    ></div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      ScenarioArray: [
        {
          value: "Below 2℃",
          label: "Below 2℃",
        },
        {
          value: "Current policies",
          label: "Current policies",
        },
        {
          value: "Delayed transition",
          label: "Delayed transition",
        },
      ],
      styleChart: {
        width: "100%",
      },
      pageIndex: 1,
      ScenarioValue: "Below 2℃",
      thirdChartObj: {},
      thirdChartData: {},
      year: [2025, 2030, 2035, 2040, 2045, 2050],
    };
  },
  methods: {
    chooseScenario() {
      this.addThirdChart();
    },
    getInitCompanyPDData() {
      var _self = this;
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
        console.log("getInitCompanyPD", newData);
        if (newData.items.length > 0) {
          let sectors = [];
          let timelineArr = _self.year;
          let below2ocArr = [[], [], [], [], [], [], []];
          let currentpoliciesArr = [[], [], [], [], [], [], []];
          let delayedtransitionArr = [[], [], [], [], [], [], []];

          newData.items.map((item) => {
            if (sectors.indexOf(item["Sector"]) == -1) {
              sectors.push(item["Sector"]);
              let sectorArr = newData.items.filter((item1) => {
                return item1["Sector"] == item["Sector"];
              });
              // sector total loan value
              let totalPrice = sectorArr.reduce((e, p) => e + p.LoanValue, 0);
              let unadjustedPD_b2 = _self.getSectorAveragePD(sectorArr, "Below2oCSector", 2020);
              for (let index = 0; index < timelineArr.length; index++) {
                let year = timelineArr[index];
                let pdVal = _self.getSectorAveragePD(sectorArr, "Below2oCSector", year);

                let belowArr = [
                  // (
                  //   (item["Below2oCSector"][0]["2020"] == undefined
                  //     ? 0
                  //     : item["Below2oCSector"][0]["2020"]) * 100
                  // ).toFixed(2),
                  // (
                  //   (item["Below2oCSector"][0][year] == undefined
                  //     ? 0
                  //     : item["Below2oCSector"][0][year]) * 100
                  // ).toFixed(2),
                  unadjustedPD_b2,
                  pdVal,
                  totalPrice,
                  item["Sector"],
                  year,
                ];
                below2ocArr[index].push(belowArr);
              }

              let unadjustedPD_cp = _self.getSectorAveragePD(sectorArr, "CurrentPoliciesSector", 2020);
              for (let index = 0; index < timelineArr.length; index++) {
                let year = timelineArr[index];
                let pdVal = _self.getSectorAveragePD(sectorArr, "CurrentPoliciesSector", year);
                let currentArr = [
                  unadjustedPD_cp,
                  pdVal,
                  totalPrice,
                  item["Sector"],
                  year,
                ];
                currentpoliciesArr[index].push(currentArr);
              }

              let unadjustedPD_dt = _self.getSectorAveragePD(sectorArr, "DelayedTransitionSector", 2020);
              for (let index = 0; index < timelineArr.length; index++) {
                let year = timelineArr[index];                
                let pdVal = _self.getSectorAveragePD(sectorArr, "DelayedTransitionSector", year);
                let delayedArr = [
                  unadjustedPD_dt,
                  pdVal,
                  totalPrice,
                  item["Sector"],
                  year,
                ];
                delayedtransitionArr[index].push(delayedArr);
              }
            }
          });
          let chartData = {
            secotrs: sectors,
            series: {
              "Below 2℃": below2ocArr,
              "Current policies": currentpoliciesArr,
              "Delayed transition": delayedtransitionArr,
            },
            timeline: timelineArr,
          };
          _self.thirdChartData = chartData;
          _self.addThirdChart();
        } else {
          _self.thirdChartData = {};
        }
      });
    },
    getSectorAveragePD(sectorArr, scenarioKey, year) {
      let count = 0;
      let totalPD = sectorArr.reduce(function (prev, item) {
        var secVals = item[scenarioKey][0];
        var pdVal = parseFloat(secVals[year]);
        if (pdVal != parseFloat(0)) {
          prev += pdVal * 100;
          count += 1;
        }
        return prev;
      }, 0);
      return (count == 0 ? 0 : totalPD / count).toFixed(2)
    },
    formatter_money(val) {
      var num = val.toString().replaceAll(",", "");
      var re = /^[0-9]+.?[0-9]*/;
      var newvalue = "";
      if (num.indexOf(".") > -1) {
        var notsymbolnum = num.substring(0, num.indexOf("."));
        if (re.test(notsymbolnum)) {
          var newNum = parseFloat(notsymbolnum);
          newvalue =
            newNum.toLocaleString() +
            num.substring(num.indexOf("."), num.length);
        }
      } else {
        if (re.test(num)) {
          var newNum = parseFloat(num);
          newvalue = newNum.toLocaleString();
        }
      }
      return newvalue;
    },
    addThirdChart() {
      let _self = this;
      let data = _self.thirdChartData;
      _self.thirdChartObj = echarts.init(document.getElementById("thirdChart"));
      var itemStyle = {
        opacity: 0.8,
      };

      var sizeFunction = function (x) {
        return x / 200;
      };

      var schema = [
        { name: "Sector", index: 0, text: "Sector", unit: "" },
        { name: "LoanValue", index: 1, text: "Loan Value", unit: "US${val}M" },
        {
          name: "Climate adjusted PD",
          index: 2,
          text: "Climate adjusted PD",
          unit: "%",
        },
        { name: "Unadjusted PD", index: 3, text: "Unadjusted PD", unit: "%" },
      ];

      let option = {
        baseOption: {
          fontStyle: "Helvetica Neue",
          timeline: {
            axisType: "category",
            orient: "vertical",
            autoPlay: false,
            inverse: true,
            playInterval: 1000,
            left: null,
            right: 7,
            top: 50,
            bottom: 30,
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
          tooltip: {
            padding: 5,
            borderWidth: 1,
            formatter: function (obj) {
              var value = obj.value;
              console.log(value);
              if (value) {
                return (
                  schema[0].text +
                  "：" +
                  value[3] +
                  "<br>" +
                  schema[1].text +
                  "：" +
                  schema[1].unit.replace(
                    "{val}",
                    _self.formatter_money(value[2])
                  ) +
                  "<br>" +
                  schema[2].text +
                  "：" +
                  value[1] +
                  schema[2].unit +
                  "<br>" +
                  schema[3].text +
                  "：" +
                  value[0] +
                  schema[3].unit +
                  "<br>"
                );
              } else {
                return "";
              }
            },
            textStyle: {
              fontSize: 30,
            },
          },
          grid: {
            top: 85,
            containLabel: true,
            left: "30",
            right: "80",
            bottom: 30,
          },
          xAxis: {
            type: "value",
            name: "Unadjusted sector average PD",
            min: 0,
            splitNumber: 10,
            nameGap: 30,
            nameLocation: "middle",
            nameTextStyle: {
              fontSize: 14,
            },
            splitLine: {
              show: true,
            },
            axisLabel: {
              formatter: "{value} %",
            },
          },
          yAxis: {
            type: "value",
            name: "Climate adjusted sector average PD",
            nameLocation: "middle",
            nameGap: 50,
            min: 0,
            splitNumber: 10,
            nameTextStyle: {
              fontSize: 14,
            },
            splitLine: {
              show: true,
            },
            axisLabel: {
              formatter: "{value} %",
            },
          },
          visualMap: [
            {
              show: false,
              dimension: 3,
              categories: data.secotrs,
              inRange: {
                color: (function () {
                  var colors = [
                    "#EB8C00",
                    "#D93954",
                    "#E0301E",
                    "#FFB600",
                    "#2D2D2D",
                  ];
                  return colors.concat(colors);
                })(),
              },
            },
          ],
          series: [
            {
              type: "scatter",
              itemStyle: itemStyle,
              data: data.series[_self.ScenarioValue][0],
              symbolSize: function (val) {
                return sizeFunction(val[2]);
              },
              markLine: {
                lineStyle: {
                  normal: {
                    type: "solid",
                  },
                },
                data: [
                  [
                    {
                      symbol: "none",
                      xAxis: 0,
                      yAxis: 0,
                    },
                    {
                      symbol: "none",
                      xAxis: 5,
                      yAxis: 5,
                    },
                  ],
                ],
              },
            },
          ],
          animationDurationUpdate: 1000,
          animationEasingUpdate: "quinticInOut",
        },
        options: [],
      };

      for (var n = 0; n < data.timeline.length; n++) {
        option.baseOption.timeline.data.push(data.timeline[n]);
        var xmax = 0;
        var ymax = 0;
        data.series[_self.ScenarioValue][n].map((item) => {
          xmax = parseFloat(item[0]) > xmax ? parseFloat(item[0]) : xmax;
          ymax = parseFloat(item[1]) > ymax ? parseFloat(item[1]) : ymax;
        });
        var newxMax = Math.ceil(xmax) == 0 ? 1 : Math.ceil(xmax);
        var newyMax = Math.ceil(ymax) == 0 ? 1 : Math.ceil(ymax);
        option.options.push({
          title: {
            show: true,
            text: data.timeline[n] + "",
            right: "12%",
            bottom: "20%",
          },
          xAxis: {
            max: newxMax,
            min: 0,
          },
          yAxis: {
            max: newyMax,
            min: 0,
          },
          series: {
            name: data.timeline[n],
            type: "scatter",
            itemStyle: itemStyle,
            data: data.series[_self.ScenarioValue][n],
            markLine: {
              lineStyle: {
                normal: {
                  type: "solid",
                },
              },
              data: [
                [
                  {
                    symbol: "none",
                    xAxis: 0,
                    yAxis: 0,
                  },
                  {
                    symbol: "none",
                    xAxis: newxMax,
                    yAxis: newyMax,
                  },
                ],
              ],
            },
            symbolSize: function (val) {
              return sizeFunction(val[2]);
            },
          },
        });
      }

      _self.thirdChartObj.setOption(option);
    },
    resize() {
      let _self = this;
      var width = document.body.clientWidth;
      _self.styleChart = width - 30 + "px";

      this.$nextTick(() => {
        _self.thirdChartObj.resize();
      });
    },
  },
  mounted() {
    let _self = this;
    let si = setInterval(function () {
      if (echarts) {
        _self.getInitCompanyPDData();
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
.third-chart {
  padding: 0px 5px;
  position: relative;
}
.third-chart-search {
  display: flex;
}
.scenarioselect {
  position: absolute;
  left: 15px;
  top: 10px;
  z-index: 20;
}
.third-chart-search-label {
  padding-top: 4px;
}
.scenarioselect .v-input__slot {
  min-height: 24px !important;
}
.scenarioselect .v-text-field input {
  padding: 0;
}
</style>