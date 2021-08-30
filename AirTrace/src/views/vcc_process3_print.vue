<template>
  <div>
    <div
      style="display:none"
      class="print-process3"
    >
      <div class="company-info">
        <v-row>
          <v-col cols="6">
            Sector:<span class="company-val-style">{{
              company.Sector[0].SectorID
            }}</span>
          </v-col>

          <v-col cols="6">
            Loan Start Date:<span class="company-val-style">{{
              formatDate(company.StartDate)
            }}</span>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="6">
            Loan End Date:<span class="company-val-style">{{
              formatDate(company.EndDate)
            }}</span>
          </v-col>

          <v-col cols="6">
            Loan Amount (US$m):<span class="company-val-style">{{
              formatter_money(company.LoanValue)
            }}</span>
          </v-col>
        </v-row>
        <v-row>
          <!-- <v-col cols="6">
            Amount (US$m):<span class="company-val-style">{{
              formatter_money(company.LoanValue)
            }}</span>
          </v-col> -->
          <v-col cols="6">
            GHG emissions (tCO2):<span class="company-val-style">{{
              formatter_money(company.GHGEmissions)
            }}</span>
          </v-col>
          <v-col cols="6">
            Electricity Use (MWh):<span class="company-val-style">{{
              formatter_money(company.ElectricityUse)
            }}</span>
          </v-col>
        </v-row>
      </div>
      <v-row
        class="line-modular"
        :gutters="10"
      >
        <v-col
          sm="12"
          cols="12"
          md="12"
        >
          <div class="content-chart-item pd-charts">
            <div class="chart-descrip-title">
              <p>
                Climate-adjusted probability of default over time and under
                different scenarios
              </p>
            </div>
            <div
              style="width:700px"
              class="chart-canvas"
              id="chartCompanyPD1"
            ></div>
          </div>
        </v-col>

      </v-row>
      <v-row
        :gutters="10"
        class="line-modular"
      >
        <v-col cols="12">
          <div class="content-chart-item">
            <v-row class="search-modular content">
              <v-col cols="6">
                <v-flex>
                  <span
                    class="ml-4 mr-4 mt-2"
                    style="float: left"
                  >Scenario</span>
                  <v-select
                    v-model="scenario"
                    :items="scenarioList"
                    item-text="Name"
                    item-value="Value"
                    outlined
                    dense
                    return-object
                  ></v-select>
                </v-flex>
              </v-col>
              <v-col cols="2">
                <!-- <v-flex>
          <span
            class="ml-4 mr-4 mt-2"
            style="float: left"
          >Type</span>
          <v-select
            v-model="type"
            :items="typeList"
            item-text="Name"
            item-value="Value"
            outlined
            dense
            return-object
          ></v-select>
        </v-flex> -->
              </v-col>
              <v-col
                cols="6"
                class="flex"
              >
                <v-flex>
                  <span
                    class="ml-4 mr-4 mt-2"
                    style="float: left;display:none;"
                  >Region</span>
                  <v-select
                    style="display:none;"
                    v-model="region"
                    :items="regionList"
                    item-text="Name"
                    item-value="Value"
                    dense
                    outlined
                    return-object
                  ></v-select>
                </v-flex>
              </v-col>
            </v-row>
            <v-row class="line-modular">
              <v-col
                sm="12"
                cols="6"
                md="6"
                v-for="item in typeName"
                :key="item.divName"
              >
                <div class="content-chart-item">
                  <div class="chart-descrip-title">
                    <p>{{ item.title }}</p>
                  </div>
                  <printchartapply
                    class="chart-item"
                    :model="model"
                    :schema="printchartapply"
                    :options="options"
                    :id="item.divName"
                    :colorList="color"
                    :date="date"
                    :title="item.title"
                    :data="item.data"
                    :typename="item.name"
                    :itemColor="item.color"
                  ></printchartapply>
                  <div class="chart-descrip-bottom">
                    <span>
                      {{ item.desc }}
                    </span>
                  </div>
                </div>
              </v-col>
            </v-row>
          </div>

        </v-col>

      </v-row>
    </div>
  </div>
</template>
<script>
export default {
  name: "print-print-process3",
  data () {
    return {
      pageCode: 3,
      page3Show: false,
      isRefresh: false,
      companyName: "",
      company: {},
      printchartapply: {
        component: "printchartapply",
        name: "printchartapply",
      },
      color: [
        "#51689b",
        "#ce5c5c",
        "#fbc357",
        "#8fbf8f",
        "#659d84",
        "#005aab",
        "#979797",
        "#0d0b0c",
      ],
      date: [2020, 2025, 2030, 2035, 2040, 2045, 2050],
      scenarioList: [
        {
          id: "Below 2℃",
          Name: "Below 2℃",
          Value: "Below 2℃",
        },
        {
          id: "Delayed transition",
          Name: "Delayed transition",
          Value: "Delayed transition",
        },
        {
          id: "Divergent Net Zero",
          Name: "Divergent Net Zero",
          Value: "Divergent Net Zero",
        },
        {
          id: "Nationally Determined Contributions (NDCs)",
          Name: "Nationally Determined Contributions (NDCs)",
          Value: "Nationally Determined Contributions (NDCs)",
        },
        {
          id: "Net Zero 2050",
          Name: "Net Zero 2050",
          Value: "Net Zero 2050",
        },
        {
          id: "Current policies",
          Name: "Current policies",
          Value: "Current policies",
        },
      ],
      scenarioCorrect: "Below 2oC",
      scenario: { Name: "Below 2℃", Value: "Below 2℃" },
      region: { Name: "World", Value: "World" },
      typeName: [
        {
          type: "net_income",
          divName: "myNet_income1",
          title: "Net Income",
          data: [],
          desc: "Change in revenue from varying demand with low-carbon market sentiment will lead to change in net sales. Change in cost of production including electricity cost and carbon cost will cause change in COGS. Both drive the change of net income in income statement.",
        },
        // {
        //   type: "current_liabilities",
        //   divName: "myCurrent_liabilities",
        //   title: "Impact on Current Liabilities",
        //   data: [],
        //   desc: 'To compensate loss caused by the impact of reduced revenue and increased cost of production, more loans will be borrowed or more equity capital will be raised, which drive the change of liabilities in balance sheet.'
        // },
        {
          type: "total_liabilities",
          divName: "myTotal_liabilities1",
          // title: "Impact to Total Liabilities",
          title: "Total Liabilities",
          data: [],
          desc: "Return on assets is the key financial measurement on the profitability and business performance of a company - the higher ROA, the higher profitability and better performance, hence lower PD.",
        },

        {
          type: "leverage",
          divName: "myLeverage1",
          title: "Leverage Ratio",
          data: [],
          desc: "Leverage ratio is one of key financial measurements that assesses the ability of a company to pay back its financial obligations. The higher leverage ratio, the higher liabilities relative to its assets, hence higher PD.",
        },
        {
          type: "liquidity",
          divName: "myLiquidity1",
          title: "Liquidity Ratio",
          data: [],
          desc: "Liquidity ratio measure a company's ability to pay debt obligations and its margin of safety. But too high or too low liquidity ratio is not good. If a company has a very high current ratio compared to its peer group, it indicates that management may not be using its assets efficiently.",
        },
      ],
      regionList: [
        {
          "id": 0,
          "Name": "Australia",
          "Value": "AUS"
        },
        {
          "id": 1,
          "Name": "Brazil",
          "Value": "BRA"
        },
        {
          "id": 2,
          "Name": "Canada",
          "Value": "CAN"
        },
        {
          "id": 3,
          "Name": "China",
          "Value": "CHN"
        },
        {
          "id": 5,
          "Name": "France",
          "Value": "FRA"
        },
        {
          "id": 7,
          "Name": "Hong Kong",
          "Value": "HKG"
        },
        {
          "id": 8,
          "Name": "Hungary",
          "Value": "HUN"
        },
        {
          "id": 10,
          "Name": "India",
          "Value": "IND"
        },
        {
          "id": 9,
          "Name": "Indonesia",
          "Value": "IDN"
        },
        {
          "id": 11,
          "Name": "Italy",
          "Value": "ITA"
        },
        {
          "id": 12,
          "Name": "Japan",
          "Value": "JPN"
        },
        {
          "id": 13,
          "Name": "Korea, Republic of",
          "Value": "KOR"
        },
        {
          "id": 15,
          "Name": "Malaysia",
          "Value": "MYS"
        },
        {
          "id": 14,
          "Name": "Mexico",
          "Value": "MEX"
        },
        {
          "id": 16,
          "Name": "Netherlands",
          "Value": "NLD"
        },
        {
          "id": 17,
          "Name": "New Zealand",
          "Value": "NZL"
        },
        {
          "id": 18,
          "Name": "Philippines",
          "Value": "PHL"
        },
        {
          "id": 19,
          "Name": "Russia",
          "Value": "RUS"
        },
        {
          "id": 20,
          "Name": "Saudi Arabia",
          "Value": "SAU"
        },
        {
          "id": 21,
          "Name": "Singapore",
          "Value": "SGP"
        },
        {
          "id": 26,
          "Name": "South Africa",
          "Value": "ZAF"
        },
        {
          "id": 4,
          "Name": "Spain",
          "Value": "ESP"
        },
        {
          "id": 23,
          "Name": "Taiwan, Province of China",
          "Value": "TWN"
        },
        {
          "id": 22,
          "Name": "Thailand",
          "Value": "THA"
        },
        {
          "id": 6,
          "Name": "United Kingdom",
          "Value": "GBR"
        },
        {
          "id": 24,
          "Name": "United States",
          "Value": "USA"
        },
        {
          "id": 25,
          "Name": "Viet Nam",
          "Value": "VNM"
        }
      ],
      type: "",
      mychartList: {},
      intervalCompany: null,
    };
  },
  methods: {
    getFormData (formName, searchItem, callback) {
      var _this = this;
      var requestPara = {
        pageCode: formName,
        searchItems: searchItem,
        order: {},
        columns: [],
        withSocialStatus: false,
        index: 1,
        size: 10000,
      };
      _this.callApi("GetDocs", requestPara).then((data) => {
        if (data.statusCode == 200 && data.data.totalCount > 0) {
          return callback(data.data);
        } else {
          return callback(false);
        }
      });
    },
    getInitApplyData () {
      let _this = this;

      var searchItem = [
        {
          Method: "AND",
          Operator: "Equal",
          Name: "Scenario",
          Value: _this.scenarioCorrect,
        },
        {
          Method: "AND",
          Operator: "Equal",
          Name: "Region",
          Value: _this.region.Value,
        },
        {
          Method: "AND",
          Operator: "Equal",
          Name: "Company",
          Value: this.model["CompanyName"],
        },
      ];
      var subsearch = [];
      _this.typeName.map((item) => {
        subsearch.push({
          Method: "OR",
          Operator: "Equal",
          Name: "Type",
          Value: item.type,
        });
      });
      searchItem.push({
        Method: "AND",
        Operator: "",
        Name: "",
        SubSearchItems: subsearch,
      });

      _this.getFormData("reportData", searchItem, function (result) {
        if (result) {
          var data = result.items;
          console.log({ data: data });
          _this.typeName.map((item) => {
            var newitem = data.filter((element) => {
              return element.Type == item.type;
            });
            if (newitem != undefined) item.data = newitem;
            else item.data = [Math.ceil(Math.random() * 1000000)];
          });
        } else {
          _this.typeName.map((item) => {
            item.data = [Math.ceil(Math.random() * 1000000)];
          });
        }
      });
    },
    getCompanyPdData () {
      var _this = this;
      var searchItem = [
        {
          Method: "AND",
          Operator: "Equal",
          Name: "Company",
          Value: this.model["CompanyName"],
        },
      ];
      _this.getFormData("companypddata", searchItem, function (result) {
        if (result) {
          _this.companyPDData = result.items[0];
        } else {
          _this.companyPDData = [];
        }
        _this.setCompanyPD();
      });
    },
    formatDate (time) {
      var d = new Date(time);
      return d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate();
      // return moment(time).format("YYYY-MM-DD");
    },
    getInitCompany () {
      var _this = this;
      if (_this.companyName == "") {
        return;
      }

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
        if (newData.items.length > 0) {
          _this.company = newData.items[0];
        } else {
          _this.company = {};
        }
      });
    },

    setCompanyPD () {
      var _this = this;
      var seriesList = [];

      if (document.getElementById("chartCompanyPD1") == undefined) {
        setTimeout(function () {
          _this.setCompanyPD();
        }, 2000);
        return;
      }

      var myChart = echarts.init(document.getElementById("chartCompanyPD1"));
      _this.mychartList["chartCompanyPD1"] = myChart;
      myChart.showLoading({
        text: "loading...",
      });

      var item = _this.companyPDData;
      var Below2oCClimate = [];
      var CurrentPolicies = [];
      var DelayedTransition = [];
      var below2oC = "Below2oCClimate" in item ? item["Below2oCClimate"][0] : {};
      var currentPolicies = "CurrentPoliciesClimate" in item ? item["CurrentPoliciesClimate"][0] : {};
      var delayedTransition = "DelayedTransitionClimate" in item ? item["DelayedTransitionClimate"][0] : {};
      var legendList = [];
      _this.date.map((item) => {
        Below2oCClimate.push(below2oC[item] == undefined ? "" : (parseFloat(below2oC[item]) == 0 ? "" : (below2oC[item] * 100).toFixed(2)));
        CurrentPolicies.push(currentPolicies[item] == undefined ? "" : (parseFloat(currentPolicies[item]) == 0 ? "" : (currentPolicies[item] * 100).toFixed(2)));
        DelayedTransition.push(delayedTransition[item] == undefined ? "" : (delayedTransition[item] == 0 ? "" : (delayedTransition[item] * 100).toFixed(2)));
      });
      seriesList.push(
        {
          connectNulls: true,
          symbol: "none",
          name: "Below 2℃",
          data: Below2oCClimate,
          type: "line",
          itemStyle: {
            normal: {
              color: _this.color[0],
              lineStyle: {
                color: _this.color[0],
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
              color: _this.color[1],
              lineStyle: {
                color: _this.color[1],
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
              color: _this.color[2],
              lineStyle: {
                color: _this.color[2],
              },
            },
          },
        }
      );
      legendList.push("Below 2℃");
      legendList.push("Current policies");
      legendList.push("Delayed transition");

      var loanvalue = item["LoanValue"] == undefined ? _this.company.LoanValue : item["LoanValue"];
      var symbol = {
        symbolSize: loanvalue / 150,
        data: [[0, Below2oCClimate[0]]],
        type: "scatter",
        color: "#ffb600",
        itemStyle: {
          normal: {
            borderColor: "#ffb600",
            borderWidth: 3,

          },
        },
      };
      seriesList.push(symbol);
      var xAxis = [];

      var option = {
        legend: {
          x: 'right',
          orient: 'vertical',
          data: legendList,
        },
        tooltip: {
          trigger: "axis",
          formatter: function (params) {
            var html = "";
            params.map((item) => {
              if (item.componentSubType == "scatter") {
                html += `<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:${item.color};"></span>Loan Value  : ${loanvalue}<br/>`;
              } else {
                html += `<span style="display:inline-block;margin-right:5px;border-radius:10px;width:10px;height:10px;background-color:${item.color};"></span>${item.seriesName}  : ${item.value}% <br/>`;
              }
            });
            return html;
          },
        },
        grid: {
          left: "8%",
          bottom: 50,
          right: "100",
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
  },
  mounted () {
    let _this = this;
    _this.bus.$on("showPage", (page) => {
      _this.page3Show = false;
      if (page == _this.pageCode) {
        _this.page3Show = true;
        _this.region = _this.regionList.find((item) => {
          return item.Name == _this.model.CompanyRegion[0];
        });
        _this.companyName = _this.model
          ? _this.model["CompanyName"].trimLeft().trimEnd()
          : "";
        _this.getInitApplyData();
        _this.getInitCompany();
        _this.getCompanyPdData();
        var chartlist = Object.values(_this.mychartList);
        if (chartlist.length > 0) {
          chartlist.forEach((item) => {
            item.resize();
          });
        }
      }
    });
    window.addEventListener("resize", () => {
      if (_this.mychartList["chartCompanyPD1"] != undefined)
        _this.mychartList["chartCompanyPD1"].resize();
    });
  },
  computed: {},
  created () { },
  watch: {
    region: {
      handler (new_value, old_value) {
        var _this = this;
        _this.getInitApplyData();
        _this.getInitCompany();
      },
      deep: true,
    },
    scenario: {
      handler (new_value, old_value) {
        var _this = this;
        this.scenarioCorrect =
          new_value.Value == "Below 2℃" ? "Below 2oC" : new_value.Value;
        _this.getInitApplyData();
        _this.getInitCompany();
      },
      deep: true,
    },
  },
};
</script>

<style scoped>
.print-process3 {
  height: calc(100vh - 159px - 74px) !important;
  overflow-y: auto;
  overflow: auto;
  padding: 0 12px;
}

.line-modular {
  margin-left: 0;
}

.process3 .company-info {
  font-size: 18px;
  margin: 10px 20px 5px 20px;
  box-shadow: 1px 1px 5px rgb(0 0 0 / 20%);
  padding-top: 15px;
  padding-left: 15px;
  background-color: #f2f2f2;
}
.print-process3 .pd-charts {
  height: 674px;
}

.company-val-style {
  padding-left: 10px;
}

.print-process3 .content-chart-item {
  border: 1px solid #dcdcdc;
  margin: 5px -3px 5px 7px;
}
.print-process3 .company-info span {
  font-size: 19px !important;
  color: #d04a02;
}

.print-process3 .chart-canvas {
  height: 600px;
  width: calc((100vw - 546px));
  margin-left: 10px;
}

.print-process3 .content {
  width: 660px;
}
</style>
 