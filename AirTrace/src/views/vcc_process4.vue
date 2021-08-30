
<template>
  <div
    v-if="p3ShowState"
    class="process4-module"
  >
    <div class="company-info  print">
      <v-row>
        <v-col cols="3">
          Sector:<span class="company-val-style">{{
            company.Sector[0].SectorID
          }}</span>
        </v-col>

        <v-col cols="3">
          Loan Start Date:<span class="company-val-style">{{
            formatDate(company.StartDate)
          }}</span>
        </v-col>
        <v-col cols="3">
          Loan End Date:<span class="company-val-style">{{
            formatDate(company.EndDate)
          }}</span>
        </v-col>
        <v-col cols="3">
          Loan Amount (US$m):<span class="company-val-style">{{
            formatter_money(company.LoanValue)
          }}</span>
        </v-col>
        <!-- <v-col cols="3">
          Amount (US$m):<span class="company-val-style">{{
            formatter_money(company.LoanValue)
          }}</span>
        </v-col> -->
        <v-col cols="3">
          GHG emissions (tCO2):<span class="company-val-style">{{
            formatter_money(company.GHGEmissions)
          }}</span>
        </v-col>
        <v-col cols="3">
          Electricity Use (MWh):<span class="company-val-style">{{
            formatter_money(company.ElectricityUse)
          }}</span>
        </v-col>
        <v-col cols="3"> </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
    </div>

    <v-row>
      <v-col cols="12">
        <div class="chart-content print">
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
              @change="addThirdChart"
              dense
              label=""
            >
            </v-select>
          </div>
          <div
            id="chartCompanyResult"
            :style="[styleChart1, styleChart2]"
          ></div>
        </div>
      </v-col>
      <v-col cols="6">
        <div class="chart-content">
          <div class="title">
            Climate-adjusted probability of default over time and under
            different scenarios
          </div>
          <v-row>
            <v-col cols="12">
              <div
                class="condition"
                style="padding-top: 10px"
              >
                <v-checkbox
                  style="margin-right: 30px"
                  v-model="checked"
                  label="Portfolio average"
                  value="Portfolio average"
                >
                </v-checkbox>
                <v-checkbox
                  v-model="checked"
                  label="Sector average"
                  value="Sector average"
                >
                </v-checkbox>
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-col>
              <div
                id="p4ChartCompanyPD"
                :style="[styleChart3, styleChart2]"
              ></div>
            </v-col>
          </v-row>
        </div>
      </v-col>
      <v-col cols="6">
        <div class="chart-content">
          <div class="title">
            Sector average: change in climate-adjusted probability of default (PD)
          </div>
          <v-row>
            <v-col cols="12">
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
                  @change="addThirdChart"
                  dense
                  label=""
                >
                </v-select>
              </div>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12">
              <div
                id="thirdChart"
                class="line-vertical"
                :style="[styleChart3, styleChart2]"
              ></div>
            </v-col>
          </v-row>
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <div class="chart-desc">
          Based on the climate risk assessment of this loan applicant, the
          recommended action is
          <span style="
              background-color: #d04a02;
              color: #fff;
              padding: 0px 5px;
              margin: 0px 5px;
            ">
            {{ suggestAction }}
          </span>
        </div>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="8">
        <span>Hash Code:</span>
        <span>{{ model.PDHashCode }}</span>
      </v-col>
      <v-col cols="4">
        <span>Timestamp: </span>
        <span>{{ model.PDTimestamp }}</span>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        :span="22"
        class="p3-action-style"
      >
        <v-btn
          outlined
          :loading="loading"
          class="p3-status-btn"
          @click="updateClick('Under consideration')"
        >Under consideration</v-btn>
        <v-btn
          outlined
          :loading="loading"
          class="p3-status-btn"
          @click="updateClick('Approved')"
        >Approve</v-btn>
        <v-btn
          outlined
          :loading="loading"
          class="p3-status-btn"
          @click="updateClick('Drawdown')"
        >Drawdown</v-btn>
        <v-btn
          outlined
          class="p3-status-btn"
          @click="print()"
        >Print</v-btn>
      </v-col>

    </v-row>
    <v-row>
      <v-dialog
        v-model="confirmDialog"
        persistent
        max-width="450px"
      >
        <v-card>
          <v-card-text style="padding: 15px 10px 10px 10px">Are you sure to update the loan application status?</v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="green"
              text
              @click="confirmDialog = false"
            >
              Cancel
            </v-btn>
            <v-btn
              color="green"
              text
              @click="updateStatus"
            > OK </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
    <v-row>

    </v-row>
  </div>
</template>
<script>
export default {
  name: "process4",
  data () {
    return {
      isActive: false,
      showProcessThird: false,
      isRefresh: false,
      pageIndex: 1,
      checked: [],
      checkedLoan: [],
      companyName: "RS Real estate Ltd",
      sector: "",
      loanValue: "",
      GHGEmissions: "",
      companyPDData: {},
      date: [2020, 2025, 2030, 2035, 2040, 2045, 2050],
      year: [2025, 2030, 2035, 2040, 2045, 2050],
      from: {},
      company: {},
      color: [
        "#EB8C00",
        "#2D2D2D",
        "#D93954",
        "#E0301E",
        "#FFB600",
        "#714300",
        "#0089eb",
        "#4eb523",
        "#9013fe",
      ],

      colorArray: [
        "#51689b",
        "#ce5c5c",
        "#fbc357",
        "#8fbf8f",
        "#714300",
        "#0089eb",
        "#4eb523",
        "#9013fe",
      ],
      sectorColor: [],
      styleChart1: {
        width: "calc(100vw - 410px)",
      },
      styleChart2: {
        height: "460px",
        margin: "20px auto",
      },
      styleChart3: {
        width: "540px",
      },
      mychartList: {},

      thirdChartData: {},
      ScenarioValue: "Below 2℃",
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
      adjustedPDData: {
        "Below 2℃": {},
        "Current policies": {},
        "Delayed transition": {},
      },
      status: false,
      actionStatus: "",
      confirmDialog: false,
      p3ShowState: false,
      pageCode: 4,
      settingData: null,
      suggestAction: "Refer to safeguards on climate risks",
    };
  },
  methods: {
    print () {
      window.print();
    },
    formatDate (time) {
      var d = new Date(time);
      return d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate();
      // return moment(time).format("YYYY-MM-DD");
    },
    randomHexColor () {
      var hex = Math.floor(Math.random() * 16777216).toString(16);
      while (hex.length < 6) {
        hex = "0" + hex;
      }
      if (hex == "#d04a02") {
        return _this.randomHexColor();
      }
      return "#" + hex;
    },

    processThirdChartData (newData) {
      let _this = this;
      if (newData.items.length > 0) {
        let sectors = [];
        let timelineArr = _this.year;
        let below2ocArr = [[], [], [], [], [], [], []];
        let currentpoliciesArr = [[], [], [], [], [], [], []];
        let delayedtransitionArr = [[], [], [], [], [], [], []];
        newData.items.map((item) => {
          if (sectors.indexOf(item["Sector"]) == -1) {
            sectors.push(item["Sector"]);
            let sectorArr = newData.items.filter((item1) => {
              return item1["Sector"] == item["Sector"];
            });
            let totalPrice = sectorArr.reduce((e, p) => e + p.LoanValue, 0);
            let unadjustedPD_b2 = _this.getSectorAveragePD(
              sectorArr,
              "Below2oCSector",
              2020
            );
            for (let index = 0; index < timelineArr.length; index++) {
              let year = timelineArr[index];
              let pdVal = _this.getSectorAveragePD(
                sectorArr,
                "Below2oCSector",
                year
              );
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

            let unadjustedPD_cp = _this.getSectorAveragePD(
              sectorArr,
              "CurrentPoliciesSector",
              2020
            );
            for (let index = 0; index < timelineArr.length; index++) {
              let year = timelineArr[index];
              let pdVal = _this.getSectorAveragePD(
                sectorArr,
                "CurrentPoliciesSector",
                year
              );
              let currentArr = [
                unadjustedPD_cp,
                pdVal,
                totalPrice,
                item["Sector"],
                year,
              ];
              currentpoliciesArr[index].push(currentArr);
            }

            let unadjustedPD_dt = _this.getSectorAveragePD(
              sectorArr,
              "DelayedTransitionSector",
              2020
            );
            for (let index = 0; index < timelineArr.length; index++) {
              let year = timelineArr[index];
              let pdVal = _this.getSectorAveragePD(
                sectorArr,
                "DelayedTransitionSector",
                year
              );
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
        _this.thirdChartData = chartData;
        _this.addThirdChart();
      } else {
        _this.thirdChartData = {};
      }
    },
    formatter_money (val) {
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
    addThirdChart () {
      var _this = this;
      var data = _this.thirdChartData;
      if (document.getElementById("thirdChart") == undefined) {
        setTimeout(() => {
          _this.addThirdChart();
        }, 3000);
        return;
      }
      var myChart = echarts.init(document.getElementById("thirdChart"));
      _this.mychartList["thirdChart"] = myChart;
      var itemStyle = {
        opacity: 0.8,
        normal: {
          color: function (param) {
            console.log(param.data[3]);
            return _this.sectorColor[param.data[3]];
          },
        },
      };

      var sizeFunction = function (x) {
        return x / 200;
      };

      var schema = [
        {
          name: "Sector",
          index: 0,
          text: "Sector",
          unit: "",
        },
        {
          name: "LoanValue",
          index: 1,
          text: "Loan Value",
          unit: "US${val}M",
        },
        {
          name: "Climate adjusted PD",
          index: 2,
          text: "Climate adjusted PD",
          unit: "%",
        },
        {
          name: "Unadjusted PD",
          index: 3,
          text: "Unadjusted PD",
          unit: "%",
        },
      ];

      let option = {
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
              text: data.timeline[0],
              textAlign: "center",
              right: "8%",
              bottom: "20%",
              textStyle: {
                fontSize: 40,
              },
            },
          ],
          tooltip: {
            padding: 5,
            borderWidth: 1,
            formatter: function (obj) {
              var value = obj.value;
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
                    _this.formatter_money(value[2])
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
          },
          grid: {
            top: 20,
            containLabel: true,
            left: 60,
            right: "100",
            bottom: 50,
          },
          xAxis: {
            type: "value",
            name: "Unadjusted sector average PD",
            max: 5,
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
            max: 5,
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
              data: data.series[_this.ScenarioValue][0],
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
          animationDurationUpdate: 3000,
          animationEasingUpdate: "quinticInOut",
        },
        options: [],
      };

      for (var n = 0; n < data.timeline.length; n++) {
        option.baseOption.timeline.data.push(data.timeline[n]);
        var xmax = 0;
        var ymax = 0;
        data.series[_this.ScenarioValue][n].map((item) => {
          xmax = parseFloat(item[0]) > xmax ? parseFloat(item[0]) : xmax;
          ymax = parseFloat(item[1]) > ymax ? parseFloat(item[1]) : ymax;
        });
        var newxMax = Math.ceil(xmax) == 0 ? 1 : Math.ceil(xmax);
        var newyMax = Math.ceil(ymax) == 0 ? 1 : Math.ceil(ymax);
        option.options.push({
          title: {
            show: true,
            text: data.timeline[n] + "",
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
            data: data.series[_this.ScenarioValue][n],
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
          animationDurationUpdate: 3000,
          animationEasingUpdate: "quinticInOut",
        });
      }
      /*console.log(option);
      myChart.clear();
      option && */
      myChart.setOption(option, true);
    },

    getInitCompany () {
      //此方法优化为
      var _this = this;
      var filterData = [];
      filterData.push({
        name: "CompanyName",
        value: _this.companyName,
        operator: "Equal",
        method: "And",
        subSearchItems: [],
      });
      var requestPara = {
        pageCode: "loanapplication",
        searchItems: filterData,
        order: {},
        columns: [],
        withSocialStatus: false,
        index: _this.pageIndex,
        size: 1,
      };
      _this.callApi("GetDocs", requestPara).then((data) => {
        let newData = data.data;
        console.log("getInitCompany", newData);
        if (newData.items.length > 0) {
          _this.company = newData.items[0];
        }
      });
    },
    getData (url, searchItem, callback) {
      axios
        .post(url, searchItem)
        .then(function (resp) {
          if ((resp.data.StatusCode != 200) | (resp.data.Data.total == 0)) {
            callback(false);
          } else {
            callback(resp.data);
          }
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    setCompanyPD () {
      var _this = this;
      var seriesList = [];
      console.log(document.getElementById("p4ChartCompanyPD"));
      if (document.getElementById("p4ChartCompanyPD") == undefined) {
        setTimeout(() => {
          _this.setCompanyPD();
        }, 3000);
        return;
      }
      var myChart = echarts.init(document.getElementById("p4ChartCompanyPD"));
      _this.mychartList["p4ChartCompanyPD"] = myChart;
      myChart.showLoading({
        text: "loading...",
      });

      var item = _this.companyPDData;

      var Below2oCClimate = [];
      var CurrentPolicies = [];
      var DelayedTransition = [];
      var below2oC =
        "Below2oCClimate" in item ? item["Below2oCClimate"][0] : {};
      var currentPolicies =
        "CurrentPoliciesClimate" in item
          ? item["CurrentPoliciesClimate"][0]
          : {};
      var delayedTransition =
        "DelayedTransitionClimate" in item
          ? item["DelayedTransitionClimate"][0]
          : {};
      var legendList = [];

      // get climate-adjusted pd for assesment
      // var minPD = 0;
      var minPD = parseFloat(below2oC["2030"]) * 100;
      var currentPoliciesPD = parseFloat(currentPolicies["2030"]) * 100;
      var delayedTransitionPD = parseFloat(delayedTransition["2030"]) * 100;
      if ((currentPoliciesPD > 0) & (currentPoliciesPD < minPD)) {
        minPD = currentPoliciesPD;
      }
      if ((delayedTransitionPD > 0) & (delayedTransitionPD < minPD)) {
        minPD = currentPoliciesPD;
      }
      if (minPD == 0) {
        minPD = parseFloat(below2oC["2020"]) * 100;
      }
      _this.getSussgestAction(minPD);

      _this.date.map((item) => {
        Below2oCClimate.push(below2oC[item] == undefined ? "" : (parseFloat(below2oC[item]) == 0 ? "" : (below2oC[item] * 100).toFixed(2)));
        CurrentPolicies.push(currentPolicies[item] == undefined ? "" : (parseFloat(currentPolicies[item]) == 0 ? "" : (currentPolicies[item] * 100).toFixed(2)));
        DelayedTransition.push(delayedTransition[item] == undefined ? "" : (delayedTransition[item] == 0 ? "" : (delayedTransition[item] * 100).toFixed(2)));

      });
      seriesList.push(
        {
          symbol: "none",
          name: "Below 2℃",
          data: Below2oCClimate,
          type: "line",
          itemStyle: {
            normal: {
              color: _this.colorArray[0],
              lineStyle: {
                color: _this.colorArray[0],
              },
            },
          },
        },
        {
          symbol: "none",
          name: "Current policies",
          data: CurrentPolicies,
          type: "line",
          itemStyle: {
            normal: {
              color: _this.colorArray[1],
              lineStyle: {
                color: _this.colorArray[1],
              },
            },
          },
        },
        {
          symbol: "none",
          name: "Delayed transition",
          data: DelayedTransition,
          type: "line",
          itemStyle: {
            normal: {
              color: _this.colorArray[2],
              lineStyle: {
                color: _this.colorArray[2],
              },
            },
          },
        }
      );
      legendList.push("Below 2℃");
      legendList.push("Current policies");
      legendList.push("Delayed transition");
      if (_this.checked.length > 0) {
        _this.checked.map((name) => {
          var Below2oCClimate = [];
          var CurrentPolicies = [];
          var DelayedTransition = [];
          if (name == "Portfolio average") {
            var below2oC = item["Below2oCPortfolio"][0];
            var currentPolicies = item["CurrentPoliciesPortfolio"][0];
            var delayedTransition = item["DelayedTransitionPortfolio"][0];
            _this.date.map((item) => {
              Below2oCClimate.push(below2oC[item] == undefined ? "" : (parseFloat(below2oC[item]) == 0 ? "" : (below2oC[item] * 100).toFixed(2)));
              CurrentPolicies.push(currentPolicies[item] == undefined ? "" : (parseFloat(currentPolicies[item]) == 0 ? "" : (currentPolicies[item] * 100).toFixed(2)));
              DelayedTransition.push(delayedTransition[item] == undefined ? "" : (delayedTransition[item] == 0 ? "" : (delayedTransition[item] * 100).toFixed(2)));

            });
            seriesList.push(
              {
                symbol: "none",
                name: "Below 2℃ - Portfolio average",
                data: Below2oCClimate,
                type: "line",
                itemStyle: {
                  normal: {
                    color: _this.colorArray[3],
                    lineStyle: {
                      color: _this.colorArray[3],
                    },
                  },
                },
              },
              {
                symbol: "none",
                name: "Current policies - Portfolio average",
                data: CurrentPolicies,
                type: "line",
                itemStyle: {
                  normal: {
                    color: _this.colorArray[4],
                    lineStyle: {
                      color: _this.colorArray[4],
                    },
                  },
                },
              },
              {
                symbol: "none",
                name: "Delayed transition - Portfolio average",
                data: DelayedTransition,
                type: "line",
                itemStyle: {
                  normal: {
                    color: _this.colorArray[5],
                    lineStyle: {
                      color: _this.colorArray[5],
                    },
                  },
                },
              }
            );
            legendList.push("Below 2℃ - Portfolio average");
            legendList.push("Current policies - Portfolio average");
            legendList.push("Delayed transition - Portfolio average");
          } else if (name == "Sector average") {
            var below2oC = item["Below2oCSector"][0];
            var currentPolicies = item["CurrentPoliciesSector"][0];
            var delayedTransition = item["DelayedTransitionSector"][0];

            _this.date.map((item) => {
              Below2oCClimate.push(below2oC[item] == undefined ? "" : (parseFloat(below2oC[item]) == 0 ? "" : (below2oC[item] * 100).toFixed(2)));
              CurrentPolicies.push(currentPolicies[item] == undefined ? "" : (parseFloat(currentPolicies[item]) == 0 ? "" : (currentPolicies[item] * 100).toFixed(2)));
              DelayedTransition.push(delayedTransition[item] == undefined ? "" : (delayedTransition[item] == 0 ? "" : (delayedTransition[item] * 100).toFixed(2)));
            });
            seriesList.push(
              {
                name: "Below 2℃ - Sector average",
                data: Below2oCClimate,
                symbol: "none",
                type: "line",
                itemStyle: {
                  normal: {
                    color: _this.colorArray[6],
                    lineStyle: {
                      color: _this.colorArray[6],
                    },
                  },
                },
              },
              {
                symbol: "none",
                name: "Current policies - Sector average",
                data: CurrentPolicies,
                type: "line",
                itemStyle: {
                  normal: {
                    color: _this.colorArray[7],
                    lineStyle: {
                      color: _this.colorArray[7],
                    },
                  },
                },
              },
              {
                symbol: "none",
                name: "Delayed transition - Sector average",
                data: DelayedTransition,
                type: "line",
                itemStyle: {
                  normal: {
                    color: _this.colorArray[8],
                    lineStyle: {
                      color: _this.colorArray[8],
                    },
                  },
                },
              }
            );
            legendList.push("Below 2℃ - Sector average");
            legendList.push("Current policies - Sector average");
            legendList.push("Delayed transition - Sector average");
          }
        });
      }

      var loanvalue =
        item["LoanValue"] == undefined
          ? _this.company.LoanValue
          : item["LoanValue"];
      var symbol = {
        symbolSize: loanvalue / 150,
        data: [[0, Below2oCClimate[0]]],
        type: "scatter",
        itemStyle: {
          normal: {
            borderColor: "#f58f23",
            borderWidth: 3,
          },
        },
      };
      seriesList.push(symbol);
      var xAxis = [];

      var option = {
        /*legend: {
                      x: 'right',
                      orient: 'vertical',
                      data: legendList, 
                    },*/
        tooltip: {
          trigger: "axis",
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
          backgroundColor: "rgba(50,50,50,0.7)",
          formatter: function (params) {
            var html = "";
            params.map((item) => {
              if (item.componentSubType == "scatter") {

                html += `<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:${item.color};"></span>Loan Value  : ${loanvalue}<br/>`;
              } else {
                if (item.value != null &&
                  item.value != 0 &&
                  item.value != "")
                  html += `<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:${item.color};"></span>${item.seriesName}  : ${item.value}% <br/>`;
              }
            });
            return html;

          },
        },
        grid: {
          left: "8%",
          bottom: 50,
          right: "5%",
        },
        xAxis: {
          type: "category",
          data: _this.date,
        },
        yAxis: {
          type: "value",
          axisLabel: {
            formatter: function (param) {
              return parseFloat(param).toFixed(1) + "%";
            },
          },
        },
        series: seriesList,
      };

      myChart.clear();
      option && myChart.setOption(option, true);
      myChart.hideLoading();
    },
    getSetting () {
      let _this = this;
      var requestPara = {
        pageCode: "settings",
        searchItems: [],
        order: {},
        columns: [],
        withSocialStatus: false,
        index: 1,
        size: 1,
      };
      _this.callApi("GetDocs", requestPara).then((data) => {
        console.log("setting: ", data);
        _this.settingData = data.data.items[0];
        // _this.pdThresholdsFrom = _this.settingData.PDThresholdsFrom;
        // _this.pdThresholdsTo = _this.settingData.PDThresholdsTo;
      });
    },
    getSussgestAction (pdVal) {
      console.log("final_pd: ", pdVal);
      var riskAssessment = 0;
      if (this.settingData) {
        var pdFrom = parseFloat(this.settingData.PDThresholdsFrom);
        var pdTo = parseFloat(this.settingData.PDThresholdsTo);
        if (pdVal < pdFrom) {
          this.suggestAction = this.settingData.PDThresholdsActionLow;
        } else if (pdFrom <= pdVal && pdVal <= pdTo) {
          riskAssessment = 1;
          this.suggestAction = this.settingData.PDThresholdsActionMedium;
        } else {
          riskAssessment = 2;
          this.suggestAction = this.settingData.PDThresholdsActionHigh;
        }
      }
      this.save_pd(pdVal, riskAssessment);
    },
    save_pd (pdVal, riskAssessment) {
      let _this = this;
      let newdata = {
        autoCreate: true,
        message: "Create By G20 API",
        data: {
          _id: _this.model._id,
          PD: pdVal,
          RiskAssessment: riskAssessment,
        },
        pageCode: "loanapplication",
        docId: _this.model._id,
      };
      _this.callApi("UpdateDoc", newdata).then((data) => {
        _this.model.PD = pdVal;
        _this.model.RiskAssessment = riskAssessment;
      });
    },
    resize () {
      var _this = this;
      var width = document.body.clientWidth;
      _this.styleChart1 = width - 30 + "px";
      _this.styleChart3 = (width - 50) / 2 + "px";

      var chartlist = Object.values(_this.mychartList);
      this.$nextTick(() => {
        chartlist.forEach((item) => {
          item.resize();
        });
      });
    },
    init () {
      let _this = this;
      _this.getSetting();
      _this.sectorColor["Real estate"] = "#EB8C00";
      _this.sectorColor["Oil and Gas"] = "#2D2D2D";
      _this.sectorColor["Electricity generation"] = "#D93954";
      _this.sectorColor["Cement"] = "#E0301E";
      _this.sectorColor["Commercial services"] = "#FFB600";
      _this.sectorColor["Mining of Coal and Lignite"] = "#714300";

      _this.companyName = _this.model
        ? _this.model["CompanyName"].trimLeft().trimEnd()
        : "";
      _this.getInitCompany();
      _this.getInitCompanyPDData();
      window.onresize = () => {
        _this.resize();
      };
    },
    getInitCompanyPDData () {
      var _this = this;
      var requestPara = {
        pageCode: "companypddata",
        searchItems: [],
        order: {},
        columns: [],
        withSocialStatus: false,
        index: _this.pageIndex,
        size: 99999,
      };
      _this.callApi("GetDocs", requestPara).then((data) => {
        let newData = data.data;
        if (newData.items.length > 0) {
          var arrBelow = {},
            arrCurrent = {},
            arrDelayed = {};
          newData.items.map((item) => {
            if (item["Company"] == _this.companyName) {
              _this.companyPDData = item;
            }
            if (item["Company"] != "Panda Kevin") {
              var below2oC = item["Below2oCClimate"][0];
              var currentPolicies = item["CurrentPoliciesClimate"][0];
              var delayedTransition = item["DelayedTransitionClimate"][0];
              _this.year.map((year) => {
                if (arrBelow[year] == undefined) {
                  arrBelow[year] = new Array();
                }
                if (arrCurrent[year] == undefined) {
                  arrCurrent[year] = new Array();
                }
                if (arrDelayed[year] == undefined) {
                  arrDelayed[year] = new Array();
                }
                arrBelow[year].push({
                  value: below2oC[year] * 100,
                  company: item["Company"],
                  sector: item["Sector"],
                });
                arrCurrent[year].push({
                  value: currentPolicies[year] * 100,
                  company: item["Company"],
                  sector: item["Sector"],
                });
                arrDelayed[year].push({
                  value: delayedTransition[year] * 100,
                  company: item["Company"],
                  sector: item["Sector"],
                });
              });
            }
          });
          _this.adjustedPDData["Below 2℃"] = JSON.stringify(arrBelow);
          _this.adjustedPDData["Current policies"] = JSON.stringify(arrCurrent);
          _this.adjustedPDData["Delayed transition"] =
            JSON.stringify(arrDelayed);
          _this.setCompanyPDData();
        }
        _this.processThirdChartData(newData);
        setTimeout(_this.setCompanyPD(), 500);
      });
    },
    setCompanyPDData () {
      var _this = this;
      if (document.getElementById("chartCompanyResult") == undefined) {
        setTimeout(() => {
          _this.setCompanyPDData();
        }, 3000);
        return;
      }
      var myChart = echarts.init(document.getElementById("chartCompanyResult"));
      _this.mychartList["chartCompanyResult"] = myChart;

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
              top: "20",
              left: "150",
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
              if (value == null || value == undefined) {
                value = 0;
              }
              return param[0].axisValue + ":" + value.toFixed(2) + "%";
            },
          },
          grid: {
            top: "20",
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
              color: function (param, index) {
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
                return parseFloat(param).toFixed(1) + "%";
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
              color: function (param, index) {
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
      myChart.setOption(option, true);

      myChart.hideLoading();
    },

    updateClick (status) {
      this.confirmDialog = true;
      this.actionStatus = status;
    },

    getSectorAveragePD (sectorArr, scenarioKey, year) {
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
      return (count == 0 ? 0 : totalPD / count).toFixed(2);
    },

    ///重新计算
    updateStatus () {
      var _this = this;
      let newdata = {
        autoCreate: false,
        message: "Update By G20 API",
        data: { Stage: this.actionStatus },
        pageCode: "loanapplication",
        docId: _this.model._id,
      };
      _this.callApi("UpdateDoc", newdata).then((data) => {
        console.log("updateStatus: " + status, data);
        // let newData = data.data;
        window.location.href = "/g20/AirTrace/";
      });
      _this.confirmDialog = false;
    },
  },
  mounted () {
    let _this = this;
    window.addEventListener("resize", () => {
      var chartlist = Object.values(_this.mychartList);
      this.$nextTick(() => {
        chartlist.forEach((item) => {
          item.resize();
        });
      });
    });

    _this.bus.$on("showPage", (page) => {
      _this.p3ShowState = false;
      if (page == _this.pageCode) {
        _this.p3ShowState = true;
        _this.isRefresh = true;

        var chartlist = Object.values(_this.mychartList);
        if (chartlist.length > 0) {
          chartlist.forEach((item) => {
            item.resize();
          });
        }
      }
    });
  },
  computed: {
    length () {
      return this.checked.length;
    },
    lengthLoan () {
      return this.checkedLoan.length;
    },
  },
  watch: {
    p3ShowState (new_value, old_value) {
      if (new_value) {
        var _this = this;
        this.$nextTick(function () {
          _this.init();
        });
      }
    },
    data: {
      handler (new_value, old_value) {
        if (this.isRefresh) {
          this.loadData();
        }
      },
      deep: true,
    },
    length (newValue, oldValue) {
      if (this.isRefresh) {
        this.setCompanyPD();
      }
    },
    ScenarioValue (val, oldval) {
      if (this.isRefresh) {
        this.setCompanyPDData();
      }
    },
  },
};
</script>
<style>
.company-val-style {
  padding-left: 10px;
}

.condition > .v-input--selection-controls {
  margin-top: 0 !important;
  padding-top: 0px !important;
}

.process4-module {
  height: calc(100vh - 159px - 74px) !important;
  padding: 0px 20px;
  margin-left: 10px;
  overflow-y: auto;
  overflow: auto;
  /* font-family: 'Helvetica Neue' !important; */
}

.process4-module .chart-content {
  margin-right: 25px;
  margin-top: 30px;
  box-shadow: 0px 0px 5px rgb(0 0 0 / 30%);
  height: 617px;
  border-radius: 5px;
  background-color: #f2f2f2;
}
.process4-module .condition span {
  font-size: 18px !important;
}

.process4-module .condition {
  display: flex;
  text-align: center;
  height: 40px;
  justify-content: center;
  font-size: 18px;
}

.process4-module .condition .v-input--is-label-active .v-input__slot label {
  color: #d04a02 !important;
}

.process4-module .company-info span {
  font-size: 19px !important;
  color: #d04a02;
}

.process4-module .company-info {
  font-size: 18px;
  margin-right: 25px;
  margin-top: 10px;
  margin-bottom: -10px;
  padding-left: 20px;
  box-shadow: 0px 0px 15px rgb(0 0 0 / 30%);
  padding-top: 15px;
  background-color: #f2f2f2;
}

.process4-module .info {
  padding: 0px 0 10px 20px;
}

.process4-module .title {
  padding-top: 15px;
  font-size: 18px !important;
  /* font-family: 'Helvetica Neue' !important; */
  text-align: center;
  font-weight: bold;
  /* line-height: 60px; */
}

.process4-module .chart-desc {
  margin-right: 25px;
  margin-top: 30px;
  padding-left: 20px;
  padding-right: 10px;
  box-shadow: 0px 0px 15px rgb(0 0 0 / 30%);
  height: 60px;
  border-radius: 5px;
  background-color: #f2f2f2;
  display: flex;
  text-align: center;
  align-items: center;
  font-size: 20px;
}

.process4-module .chart-desc > .v-btn {
  margin-left: 15px !important;
  background-color: #d04a02 !important;
  color: #fff !important;
}

.p3-action-style {
  margin: 15px;
  /* float: right !important; */
  text-align: right;
}

.p3-status-btn {
  margin-right: 10px;
  background-color: #d04a02;
  color: #fff !important;
  font-size: 18px !important;
}

.p3-company-fs {
  font-size: 18px;
}
</style>