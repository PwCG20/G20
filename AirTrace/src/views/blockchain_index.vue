
<template>
  <div class="blockchain-module">
    <remote-js src="/g20/airtrace/api/Resource/echarts.min.js"></remote-js>
    <div
      class="layout"
      id="blockchain-loading"
      :style='{display:display}'
    >
      <div class="blockchain-loading1">
        <div>
          <div class="layout-loading">
            <h1>
              <span id="loading-span">Connecting to blockchain...</span>
            </h1>
          </div>
          <div class="layout-loading">
            <div class="progress-bar"></div>
          </div>
        </div>

      </div>
    </div>

    <div class="blockchain-title">
      <span>{{
            company.CompanyName
          }}</span>
    </div>

    <div class="blockchain-info">
      <v-row>
        <v-col cols="12">
          <div class="title-info">
            Loan application info
          </div>
        </v-col>
      </v-row>
      <v-row>
        <!-- <v-col cols="4">
          CompanyName:<span class="company-val-style">{{
            company.CompanyName
          }}</span>
        </v-col> -->
        <v-col cols="4">
          Sector:<span class="company-val-style">{{
            company.Sector[0].SectorID
          }}</span>
        </v-col>
        <v-col cols="4">
          Company credit score:<span class="company-val-style">{{
            company.CreditScore
          }}</span>
        </v-col>

        <v-col cols="4">
          Company region:<span class="company-val-style">{{
            company.CompanyRegion[0]
          }}</span>
        </v-col>
        <v-col cols="4">
          Company city:<span class="company-val-style">{{
            company.CompanyCity[0]
          }}</span>
        </v-col>
        <v-col cols="4">
          Company address:<span class="company-val-style">{{
            company.CompanyAddress
          }}</span>
        </v-col>

        <v-col cols="4">
          Proposed loan start date:<span class="company-val-style">{{
            formatDate(company.StartDate)
          }}</span>
        </v-col>
        <v-col cols="4">
          Proposed loan end date:<span class="company-val-style">{{
            formatDate(company.EndDate)
          }}</span>
        </v-col>
        <v-col cols="4">
          Loan value (US$m):<span class="company-number-style">{{
            formatter_money(company.LoanValue)
          }}</span>
        </v-col>

        <v-col cols="4">
          Loan region:<span class="company-val-style">{{
            company.LoanRegion[0]
          }}</span>
        </v-col>
        <v-col cols="4">
          Loan city:<span class="company-val-style">{{
            company.LoanCity[0]
          }}</span>
        </v-col>
        <v-col cols="4">
          Loan address:<span class="company-val-style">{{
            company.LoanAddress
          }}</span>
        </v-col>

        <v-col cols="4">
          Loan collateral asset type:<span class="company-val-style">{{
            company.CollateralAssetType
          }}</span>
        </v-col>
        <v-col cols="4">
          Loan collateral asset value:<span class="company-val-style">{{
            company.CollateralAssetValue
          }}</span>
        </v-col>

        <v-col cols="4">
          Collateral region:<span class="company-val-style">{{
            company.CollateralRegion[0]
          }}</span>
        </v-col>
        <v-col cols="4">
          Collateral city:<span class="company-val-style">{{
            company.CollateralCity[0]
          }}</span>
        </v-col>
        <v-col cols="4">
          Collateral address:<span class="company-val-style">{{
            company.CollateralAddress
          }}</span>
        </v-col>
        <v-col cols="4">
          Revenue (US$m):<span class="company-number-style">{{
            formatter_money(company.Revenue)
          }}</span>
        </v-col>
        <v-col cols="4">
          EBIT (US$m):<span class="company-number-style">{{
            formatter_money(company.EBIT)
          }}</span>
        </v-col>
        <v-col cols="4">
          Total Assets (US$m):<span class="company-number-style">{{
            formatter_money(company.TotalAssets)
          }}</span>
        </v-col>
        <v-col cols="4">
          Total Liabilities (US$m):<span class="company-number-style">{{
            formatter_money(company.TotalLiabilities)
          }}</span>
        </v-col>

        <v-col cols="4">
          Net asset value (US$m):<span class="company-number-style">{{
            formatter_money(company.NetAssetValue)
          }}</span>
        </v-col>
        <v-col cols="4">
          Net Income (US$m):<span class="company-number-style">{{
            formatter_money(company.NetIncome)
          }}</span>
        </v-col>
        <v-col cols="4">
          GHG emissions (Scope 1 and Scope 2):<span class="company-number-style">{{
            formatter_money(company.GHGEmissions)
          }}</span>
        </v-col>
        <v-col cols="4">
          TElectricity Use (MWh)​:<span class="company-number-style">{{
            formatter_money(company.ElectricityUse)
          }}</span>
        </v-col>

        <v-col cols="4">
          Current Assets (US$m):<span class="company-number-style">{{
            formatter_money(company.CurrentAssets)
          }}</span>
        </v-col>
        <v-col cols="4">
          Current Liabilities (US$m):<span class="company-number-style">{{
            formatter_money(company.CurrentLiabilities)
          }}</span>
        </v-col>
        <v-col cols="3"> </v-col>
        <v-col cols="3"> </v-col>
      </v-row>
    </div>

    <div
      class="report-info"
      v-show="isChartShow"
    >

      <div class="blockchain-chart-item">
        <v-row>
          <v-col cols="12">
            <div class="title-info">
              Loan climate risk assessment
            </div>
          </v-col>
          <v-col
            sm="12"
            cols="12"
            md="12"
          >
            <div class="chart-descrip-title">
              <!-- <p>
              Climate-adjusted probability of default over time and under
              different scenarios
            </p> -->
            </div>
            <div
              class="chart-canvas"
              id="chartCompanyPD"
            ></div>
          </v-col>
        </v-row>
      </div>

    </div>

  </div>
</template>
<script> 
export default {
  name: "blockchain",
  components: {
    "remote-js": {
      render (createElement) {
        return createElement("script", {
          attrs: { type: "text/javascript", src: this.src },
        });
      },
      props: {
        src: { type: String, required: true },
      },
    },
  },
  data () {
    return {
      companyName: "RS Real estate Ltd",
      date: [2020, 2025, 2030, 2035, 2040, 2045, 2050],
      year: [2025, 2030, 2035, 2040, 2045, 2050],
      company: {
        "_id": "",
        "CompanyName": "",
        "Sector": [
          {
            "SectorID": "",
            "_id": ""
          }
        ],
        "CreditScore": "",
        "CompanyRegion": [
          ""
        ],
        "CompanyISO3": "",
        "CompanyCity": [
          ""
        ],
        "CompanyAddress": "",
        "CompanyCoordinate": "",
        "StartDate": "",
        "EndDate": "",
        "LoanValue": "",
        "CloseDate": "",
        "LoanRegion": [
          ""
        ],
        "LoanISO3": "",
        "LoanCity": [
          ""
        ],
        "LoanAddress": "",
        "LoanCoordinate": "",
        "CollateralAssetType": "",
        "CollateralAssetValue": "",
        "CollateralRegion": [
          ""
        ],
        "CollateralISO3": "",
        "CollateralCity": [
          ""
        ],
        "CollateralAddress": "",
        "CollateralCoordinate": "",
        "Revenue": "",
        "EBIT": "",
        "TotalAssets": "",
        "TotalLiabilities": "",
        "NetAssetValue": "",
        "NetIncome": "",
        "GHGEmissions": "",
        "CurrentAssets": "",
        "CurrentLiabilities": "",
        "Stage": "",
        "Owner": "",
        "RiskAssessment": 0,
        "PD": "",
      },
      companyId: "",
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
      isChartShow: false,
      sectorColor: [],
      chart: {},
    };
  },
  methods: {
    formatDate (time) {
      if (time == "")
        return "";
      var d = new Date(time);
      return d.getFullYear() + "-" + (d.getMonth() + 1) + "-" + d.getDate();
      // return moment(time).format("YYYY-MM-DD");
    },
    getInitCompany () {
      var _this = this;
      if (_this.companyId == "") {
        return;
      }

      var filterData = [];
      filterData.push({
        name: "_id",
        value: _this.companyId,
        operator: "Equal",
        method: "And",
        subSearchItems: [],
      });
      var requestPara = {
        pageCode: "loanappblockchain",
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
          console.log('blockchain_company:', _this.company);
          if ("PDHashCode" in _this.company && _this.company.PDHashCode != "") {
            _this.isChartShow = true;
            setTimeout(function () {
              _this.setCompanyPD();
            }, 1000);
          }
        } else {
          _this.company =
          {
            "_id": "",
            "CompanyName": "",
            "Sector": [
              {
                "SectorID": "",
                "_id": ""
              }
            ],
            "CreditScore": "",
            "CompanyRegion": [
              ""
            ],
            "CompanyISO3": "",
            "CompanyCity": [
              ""
            ],
            "CompanyAddress": "",
            "CompanyCoordinate": "",
            "StartDate": "",
            "EndDate": "",
            "LoanValue": "",
            "CloseDate": "",
            "LoanRegion": [
              ""
            ],
            "LoanISO3": "",
            "LoanCity": [
              ""
            ],
            "LoanAddress": "",
            "LoanCoordinate": "",
            "CollateralAssetType": "",
            "CollateralAssetValue": "",
            "CollateralRegion": [
              ""
            ],
            "CollateralISO3": "",
            "CollateralCity": [
              ""
            ],
            "CollateralAddress": "",
            "CollateralCoordinate": "",
            "Revenue": "",
            "EBIT": "",
            "TotalAssets": "",
            "TotalLiabilities": "",
            "NetAssetValue": "",
            "NetIncome": "",
            "GHGEmissions": "",
            "CurrentAssets": "",
            "CurrentLiabilities": "",
            "Stage": "",
            "Owner": "",
            "RiskAssessment": 0,
            "PD": "",
          };
        }
      });
    },
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
        setTimeout(function () {
          _this.setCompanyPD();
        }, 1000);
      });
    },
    setCompanyPD () {
      var _this = this;
      var seriesList = [];

      if (document.getElementById("chartCompanyPD") == undefined || echarts == null) {
        setTimeout(function () {
          _this.setCompanyPD();
        }, 2000);
        return;
      }
      var myChart = echarts.init(document.getElementById("chartCompanyPD"));
      _this.chart = myChart;
      myChart.showLoading({
        text: "loading...",
      });

      var item = _this.company;
      var Below2oCClimate = [];
      var CurrentPolicies = [];
      var DelayedTransition = [];
      var below2oC = "Below2oCClimate" in item ? item["Below2oCClimate"][0] : {
        "2020": 0.03690274478131217,
        "2025": 0.12589630141643282,
        "2030": 0.2036769232608786,
        "2035": 0.263889797164313,
        "2040": 0.28595063452826086,
        "2045": 0.2917025007542095,
        "2050": 0.29302147057607997
      };
      var currentPolicies = "CurrentPoliciesClimate" in item ? item["CurrentPoliciesClimate"][0] : {
        "2020": 0.03690274478131217,
        "2025": 0.061468961203638796,
        "2030": 0.06112604064246714,
        "2035": 0.07082058066813078,
        "2040": 0.08427818365398293,
        "2045": 0.09260858994865187,
        "2050": 0.08888663504782453
      };
      var delayedTransition = "DelayedTransitionClimate" in item ? item["DelayedTransitionClimate"][0] : {
        "2020": 0.03690274478131217,
        "2025": 0.0,
        "2030": 0.0,
        "2035": 0.0,
        "2040": 0.0,
        "2045": 0.0,
        "2050": 0.0
      };
      var legendList = [];
      _this.date.map((item) => { 
        Below2oCClimate.push(below2oC[item] == undefined ? "" : (parseFloat(below2oC[item]) == 0 ? "" : (below2oC[item] * 100).toFixed(2)));
        CurrentPolicies.push(currentPolicies[item] == undefined ? "" : (parseFloat(currentPolicies[item]) == 0 ? "" : (currentPolicies[item] * 100).toFixed(2)));
        DelayedTransition.push(delayedTransition[item] == undefined ? "" : (delayedTransition[item] == 0 ? "" : (delayedTransition[item] * 100).toFixed(2)));
     
      });
      seriesList.push(
        {
          symbol: "none",
          name: "Below 2oC - DelayedTransitionSector",
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
          name: "Current policies - DelayedTransitionSector",
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
          name: "Delayed transition - DelayedTransitionSector",
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
      legendList.push("Below 2oC - DelayedTransitionSector");
      legendList.push("Current policies - DelayedTransitionSector");
      legendList.push("Delayed transition - DelayedTransitionSector");

      var loanvalue = _this.company["LoanValue"];
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
          right: "3%",
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
    getQueryString (name) {
      var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
      var r = window.location.search.substr(1).match(reg);
      if (r != null) return unescape(r[2]); return "";
    },
    getQueryVariable (variable) {
      var query = window.location.search.substring(1);
      var vars = query.split("&");
      for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] == variable) { return pair[1]; }
      }
      return (false);
    },
    formatter_money (val) {
      if (val == "" || val == undefined)
        return;
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
    resize () {
    },
    init () {

    },
  },
  mounted () {
    var _this = this;
    var letters = document.getElementById('loading-span');
    this.companyId = this.getQueryVariable("id");
    letters.innerText = "Connecting to blockchain...";
    setTimeout(() => {
      letters.innerText = "Loading data from blockchain...";
      this.getInitCompany();
    }, 2000);
    setTimeout(() => {
      letters.innerText = "Successfully";
    }, 4000);
    setTimeout(() => {
      document.getElementById("blockchain-loading").style.display = "none";
    }, 4500);
    window.addEventListener("resize", () => {
      if (_this.chart != undefined)
        _this.chart.resize();
    });
  },
  computed: {

  },
  watch: {

  },
};
</script>
<style>
.blockchain-title {
  color: #000;
  font-size: 25px;
  padding-left: 20px;
  margin: 20px 150px;
  background-color: #fff;
  padding: 25px;
}
.title-info {
  font-size: 26px;
  color: #d04a02;
}
.company-val-style {
  padding-left: 10px;
}

.company-number-style {
  padding-left: 10px;
  color: #d04a02 !important;
}

.condition > .v-input--selection-controls {
  margin-top: 0 !important;
  padding-top: 0px !important;
}

.blockchain-module {
  height: calc(100vh - 40px) !important;
  padding: 0px 20px;
  overflow-y: auto;
  overflow: auto;
  font-family: 'Helvetica Neue' !important;
  background-color: #f2f2f2;
}

.blockchain-module .chart-content {
  margin-right: 25px;
  margin-top: 30px;
  box-shadow: 0 5px 20px 5px rgb(0 0 0 / 5%) !important;
  height: 617px;
  border-radius: 5px;
  background-color: #fff;
}
.blockchain-module .condition span {
  font-size: 18px !important;
}

.blockchain-module .condition {
  display: flex;
  text-align: center;
  height: 40px;
  justify-content: center;
  font-size: 18px;
}

.blockchain-module .condition .v-input--is-label-active .v-input__slot label {
  color: #7d7d7d !important;
}

.blockchain-module .blockchain-info span {
  font-size: 19px !important;
  color: #7d7d7d;
}

.blockchain-module .blockchain-info,
.report-info {
  font-size: 18px;
  box-shadow: 0 5px 20px 5px rgb(0 0 0 / 5%) !important;
  background-color: #fff;
  margin: 20px 150px;
  padding: 5px 25px;
  min-width: 900px;
}

.blockchain-module .info {
  padding: 0px 0 10px 20px;
}

.blockchain-module .title {
  padding-top: 15px;
  font-size: 18px !important;
  /* font-family: 'Helvetica Neue' !important; */
  text-align: center;
  font-weight: bold;
  /* line-height: 60px; */
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

.blockchain-module .chart-canvas {
  height: 460px;
  width: calc((100vw - 346px));
  margin: 0 auto;
}

.report-info {
  margin-top: 30px;
}

#blockchain-loading {
  display: block;
}

.blockchain-loading1 {
  -moz-opacity: 1;
  filter: alpha(opacity=100);
  position: fixed;
  left: 0;
  top: 0;
  width: calc(100vw);
  height: 100%;
  background-color: rgba(255, 255, 255, 1);
  z-index: 10000;
  display: flex;
  align-items: center;
  justify-content: center;
}

.layout-loading {
  width: 100%;
  flex-flow: column;
}

a,
img {
  border: 0;
}

h1 {
  font: 1.5rem Roboto, sans-serif;
  font-weight: 900;
  padding-bottom: 1rem;
}

h1 span {
  animation: load-text 1s infinite cubic-bezier(0.1, 0.15, 0.9, 1);
  display: inline-block;
}

.progress-bar {
  background-color: #eaeaea;
  width: 300px;
  height: 25px;
  box-shadow: 1px 0px 2px rgba(0, 0, 0, 0.25), 0px 1px 2px rgba(0, 0, 0, 0.25);
  border-radius: 10px;
  position: relative;
}

.progress-bar:after {
  content: '';
  background-color: green;
  position: absolute;
  border-radius: 10px;
  width: 100%;
  height: 100%;
  top: 0px;
  left: 0px;
  animation: load 10s infinite linear;
}

@keyframes load {
  0% {
    width: 5%;
    background-color: #e0301e;
  }

  25% {
    background-color: #d04a02;
  }

  50% {
    background-color: #ffb600;
  }

  75% {
    background-color: #86db4f;
  }

  90% {
    background-color: #175d2d;
    width: 100%;
  }
}

@keyframes load-text {
  0% {
    transform: translateY(0px);
  }

  25% {
    transform: translateY(5px);
  }

  50% {
    transform: translateY(0px);
  }

  75% {
    transform: translateY(-5px);
  }

  100% {
    transform: translateY(0px);
  }
}
</style>