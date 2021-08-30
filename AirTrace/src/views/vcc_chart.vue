<template>
  <div class="content">
    <remote-js src="/g20/airtrace/api/Resource/echarts.min.js"></remote-js>
    <v-row class="search-modular">
      <v-col cols="4">
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
      <v-col
        cols="2"
        class="flex"
      ></v-col>
      <v-col
        cols="4"
        class="flex"
      >
        <v-flex>
          <span
            class="ml-4 mr-4 mt-2"
            style="float: left"
          >Region</span>
          <v-select
            v-model="region"
            :items="regionList"
            item-text="name"
            item-value="value"
            dense
            disabled
            outlined
            return-object
          ></v-select>
        </v-flex>
      </v-col>
      <!-- <v-col cols="4">
         <v-flex>
          <span
            class="ml-4 mr-4 mt-2"
            style="float: left"
          >Model</span>
          <v-select
            v-model="priceModel"
            :items="modelList"
            item-text="name"
            item-value="value"
            dense
            outlined
          ></v-select>
        </v-flex>
      </v-col>-->
    </v-row>
    <v-row class="line-modular">
      <v-col cols="12">
        <div class="chart-descrip">
          <span>Transition risks refer to the risks to companies in the move
            towards a less polluting, greener economy. This could include the
            response, or lack of response toward policy action and technology
            development. Sectors which are more carbon intensive have a higher
            exposure to transition risks.
          </span>
          <a
            href="/g20/airtrace/page/helpmelearnpage?type=risk"
            target="_blank"
          ><img src="/g20/airtrace/api/Resource/ic_question.png" /></a>
          <h4>The Transition risk explorer shows three main risk factors:</h4>
          <h4>(a) Carbon price and carbon costs for the company</h4>
          <h4>(b) Electricity costs for the company</h4>
          <h4>(c) Revenue impact based on the sector of the company</h4>
        </div>
      </v-col>
    </v-row>

    <div class="content-chart-item">
      <v-row class="line-modular">
        <v-col
          cols="6"
          sm="12"
          md="6"
        >
          <div class="chart-descrip-title">
            <p>(a) Carbon price per tonne of CO2 (US$2020 prices)</p>
          </div>

          <chartcarbon
            class="chart-item"
            :model="model"
            :schema="chartcarbon"
            :options="options"
            :id="carbonPrice.divName"
            :colorList="color"
            :date="date"
            :title="carbonPrice.title"
            :data="carbonPrice.data"
            :typename="carbonPrice.name"
            :itemColor="carbonPrice.color"
          ></chartcarbon>
        </v-col>

        <v-col
          cols="6"
          sm="12"
          md="6"
        >
          <div class="chart-descrip-title">
            <p>{{ reportName[0].title }}</p>
          </div>
          <chartreport
            class="chart-item"
            :model="model"
            :schema="chartreport"
            :options="options"
            :id="reportName[0].divName"
            :colorList="color"
            :date="date"
            :title="reportName[0].title"
            :data="reportName[0].data"
            :typename="reportName[0].name"
            :itemColor="reportName[0].color"
          ></chartreport>
        </v-col>
      </v-row>
      <v-row class="line-modular">
        <v-col cols="24">
          <div class="chart-descrip-bottom">
            <span>
              Scenarios with higher carbon prices imply that the costs of doing
              business increase for the company. The Projected carbon costs for
              the company assumes that the company’s GHG emissions follow the
              same trajectory as the sector average, in the selected country or
              region. Companies with higher GHG emissions incur higher carbon
              costs.
            </span>
          </div>
        </v-col>
      </v-row>
    </div>
    <div class="content-chart-item">
      <v-row class="line-modular">
        <v-col
          cols="6"
          sm="12"
          md="6"
        >
          <div class="chart-descrip-title">
            <p>(b) Electricity price per GJ (US$2020 prices)</p>
          </div>
          <chartcarbon
            class="chart-item"
            :model="model"
            :schema="chartcarbon"
            :options="options"
            :id="electricityPrice.divName"
            :colorList="color"
            :date="date"
            :title="electricityPrice.title"
            :data="electricityPrice.data"
            :typename="electricityPrice.name"
            :itemColor="electricityPrice.color"
          ></chartcarbon>
        </v-col>

        <v-col
          cols="6"
          sm="12"
          md="6"
        >
          <div class="chart-descrip-title">
            <p>{{ reportName[1].title }}</p>
          </div>
          <chartreport
            class="chart-item"
            :model="model"
            :schema="chartreport"
            :options="options"
            :id="reportName[1].divName"
            :colorList="color"
            :date="date"
            :title="reportName[1].title"
            :data="reportName[1].data"
            :typename="reportName[1].name"
            :itemColor="reportName[1].color"
          ></chartreport>
        </v-col>
      </v-row>
      <v-row class="line-modular">
        <v-col cols="24">
          <div class="chart-descrip-bottom">
            <span>
              Different scenarios assume different speed and degree of low
              carbon energy transition for each country. In some countries, the
              energy transition could lead to higher energy prices, such as
              electricity prices. Higher electricity prices lead to increased
              costs of doing business for the company. The Projected electricity
              costs for the company assumes that the company’s GHG emissions
              follow the same trajectory as the sector average, in the selected
              country or region. Companies with higher electricity usage incur
              higher electricity costs.
            </span>
          </div>
        </v-col>
      </v-row>
    </div>

    <div class="content-chart-item">
      <v-row class="line-modular">
        <v-col
          cols="6"
          sm="12"
          md="6"
        >
          <div class="chart-descrip-title">
            <p>(c) Sectoral price trends</p>
          </div>
          <chartreport
            class="chart-item"
            :model="model"
            :schema="chartreport"
            :options="options"
            :id="reportName[2].divName"
            :colorList="color"
            :date="date"
            :title="reportName[2].title"
            :data="reportName[2].data"
            :typename="reportName[2].name"
            :itemColor="reportName[2].color"
          ></chartreport>
        </v-col>

        <v-col
          cols="6"
          sm="12"
          md="6"
        >
          <div class="chart-descrip-title">
            <p>{{ reportName[3].title }}</p>
          </div>
          <chartreport
            class="chart-item"
            :model="model"
            :schema="chartreport"
            :options="options"
            :id="reportName[3].divName"
            :colorList="color"
            :date="date"
            :title="reportName[3].title"
            :data="reportName[3].data"
            :typename="reportName[3].name"
            :itemColor="reportName[3].color"
          ></chartreport>
        </v-col>
      </v-row>
      <v-row class="line-modular">
        <v-col cols="24">
          <div class="chart-descrip-bottom">
            <span>
              Some sectors may see impacts on their revenue streams due to the
              shifts away from higher carbon sectors to lower carbon sectors.
              The Projected revenue stream assumes that the company’s revenue
              stream follows the same trajectory as the sector average, in the
              selected country or region.
            </span>
          </div>
        </v-col>
      </v-row>
    </div>

    <!-- <v-row
      class="line-modular"
      :gutters="10"
    >
      <v-col
        v-for="item in reportName"
        :key="item.divName"
        cols="6"
        sm="12"
        md="6"
      >
        <div class="chart-descrip-title">
          <p>{{ item.title }}</p>
        </div>
        <chartreport
          class="chart-item"
          :model="model"
          :schema="chartreport"
          :options="options"
          :id="item.divName"
          :colorList="color"
          :date="date"
          :title="item.title"
          :data="item.data"
          :typename="item.name"
          :itemColor="item.color"
        ></chartreport>
      </v-col>
    </v-row> -->

    <!-- <v-row gutters>
      <v-col
        v-for="item in otherName"
        :key="item.divName"
        cols="6"
        sm="12"
        md="6"
      >
        <div class="chart-descrip-title">
          <p>{{ item.title }}</p>
        </div>
        <chartprice
          class="chart-item"
          :model="model"
          :schema="chartprice"
          :options="options"
          :id="item.divName"
          :color="color"
          :date="date"
          :title="item.title"
          :data="item.data"
          :typename="item.name"
          :itemColor="item.color"
        ></chartprice>
      </v-col>
    </v-row> -->
  </div>
</template>

<script>
export default {
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
  name: "Dashboard",

  props: {
    regionList: Array,
    region: String,
  },
  data () {
    return {
      carbonPrice: {
        variable: "Price|Carbon|Demand|Industry",
        divName: "myCarbonprice",
        title: "(a) Carbon price per tonne of CO2 (US$2020 prices)",
        data: [],
      },

      electricityPrice: {
        variable: "",
        divName: "myCarelectricityrice",
        title: "(b) Electricity price per MWh (US$2020 prices)",
        data: [],
      },
      options: "",
      companyName: "ExxonMobil",
      chartprice: {
        component: "chartprice",
        name: "chartprice",
      },
      chartreport: {
        component: "chartreport",
        name: "chartreport",
      },

      chartcarbon: {
        component: "chartcarbon",
        name: "chartcarbon",
      },
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
      scenario: { Name: "", Value: "Below 2℃" },

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
      otherName: [
        {
          color: "#E0301E",
          name: "Oil price",
          variable: "Price|Secondary Energy|Liquids|Oil",
          divName: "myOliPrice",
          title: "Oil price (US$2020/GJ)",
          data: {},
        },
        {
          color: "#EE9C34",
          name: "Gas price",
          variable: "Price|Primary Energy|Gas",
          divName: "myGasPrice",
          title: "Gas price (US$2020/GJ)",
          data: {},
        },
        {
          color: "#E669A2",
          name: "Coal price",
          variable: "Price|Primary Energy|Coal",
          divName: "myCoalPrice",
          title: "Coal price (US$2020/GJ)",
          data: {},
        },
        {
          color: "#7bfefa",
          name: "Electricity price",
          variable: "Price|Secondary Energy|Electricity",
          divName: "myElectricityPrice",
          title: "Electricity price (US$2020/GJ)",
          data: {},
        },
      ],
      reportName: [
        {
          type: "Carbon cost",
          divName: "myCarbonCost",
          title: "Carbon costs (US$2020 prices, million)",
          data: [],
        },
        {
          type: "Electricity cost",
          divName: "myElectricityRevenue",
          title: "Electricity costs (US$2020 prices, million)",
          data: [],
        },
        {
          type: "revenue_price",
          divName: "myRevenuePrice",
          title: "Sectoral price trends",
          data: [],
        },
        {
          type: "revenue",
          divName: "myRevenue",
          title:
            "Projected revenue stream for the company (US$2020 million)",
          data: [],
        },
      ],
      priceModel: "REMIND-MAgPIE 2.1-4.2_downscaled",
      modelList: [
        {
          id: "1",
          name: "GCAM5.3_NGFS_downscaled",
          value: "GCAM5.3_NGFS_downscaled",
        },
        {
          id: "2",
          name: "MESSAGEix-GLOBIOM 1.1_downscaled",
          value: "MESSAGEix-GLOBIOM 1.1_downscaled",
        },
        {
          id: "3",
          name: "REMIND-MAgPIE 2.1-4.2_downscaled",
          value: "REMIND-MAgPIE 2.1-4.2_downscaled",
        },
      ],

      addressData: [],
      modelName: "REMIND-MAgPIE 2.1-4.2_downscaled",
      scenarioCorrect: "Below 2oC",
      climateDriver: null,

      firstAction: false
    };
  },
  methods: {
    async init () {
      // await this.GetModelData();
      await this.getClimateDriver();
      //this.getPriceData();

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
    getClimateDriver () {
      var _this = this;
      if (!_this.firstAction) {
        var requestPara = {
          pageCode: "climate_drivers",
          searchItems: [
            {
              Method: "AND",
              Operator: "Equal",
              Name: "Sector",
              Value: _this.model.Sector[0]["SectorID"],
            },
          ],
          order: {},
          columns: [],
          withSocialStatus: false,
          index: 1,
          size: 10000,
        };
        _this.callApi("GetDocs", requestPara).then((data) => {
          console.log("climateDriver: ", data);
          if (data.statusCode == 200 && data.data.totalCount > 0) {
            _this.climateDriver = data.data.items[0];
            // _this.carbonPrice.variable = _this.climateDriver.CarbonPrice;
            // _this.electricityPrice.variable = _this.climateDriver.ElectricityPrice;
            _this.$set(_this.carbonPrice, 'variable', _this.climateDriver.CarbonPrice);
            _this.$set(_this.electricityPrice, 'variable', _this.climateDriver.ElectricityPrice);
            _this.firstAction = true;
          }
        }).then(() => {
          _this.getInitCarbonPrice();
          _this.getInitElectricityPrice();
          _this.getReportData();

        });
      } else {
        _this.getInitCarbonPrice();
        _this.getInitElectricityPrice();
        _this.getReportData();
      }
    },

    getInitCarbonPrice () {
      var _this = this;
      console.log("carbonPrice: ", _this.carbonPrice);
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
          Value: _this.region.value,
        },
        {
          Method: "AND",
          Operator: "Equal",
          Name: "Variable",
          Value: _this.carbonPrice.variable,
        },
        {
          Method: "AND",
          Operator: "",
          Name: "",
          SubSearchItems: [
            {
              Method: "OR",
              Operator: "Equal",
              Name: "Model",
              Value: "GCAM5.3_NGFS_downscaled",
            },
            {
              Method: "OR",
              Operator: "Equal",
              Name: "Model",
              Value: "MESSAGEix-GLOBIOM 1.1_downscaled",
            },
            {
              Method: "OR",
              Operator: "Equal",
              Name: "Model",
              Value: "REMIND-MAgPIE 2.1-4.2_downscaled",
            },
          ],
        },
      ];
      _this.getFormData("ModelData", searchItem, function (result) {
        if (result) {
          var data = result.items;
          _this.carbonPrice.data = data;
          console.log({ 0: result });
        } else {
          _this.otherName.map((item) => {
            _this.carbonPrice.data = [];
          });
        }
      });
    },
    getInitElectricityPrice () {
      var _this = this;
      console.log("ElectricityPrice: ", _this.electricityPrice);
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
          Value: _this.region.value,
        },
        {
          Method: "AND",
          Operator: "Equal",
          Name: "Variable",
          value: _this.electricityPrice.variable,
        },
        {
          Method: "AND",
          Operator: "",
          Name: "",
          SubSearchItems: [
            {
              Method: "OR",
              Operator: "Equal",
              Name: "Model",
              Value: "GCAM5.3_NGFS_downscaled",
            },
            {
              Method: "OR",
              Operator: "Equal",
              Name: "Model",
              Value: "MESSAGEix-GLOBIOM 1.1_downscaled",
            },
            {
              Method: "OR",
              Operator: "Equal",
              Name: "Model",
              Value: "REMIND-MAgPIE 2.1-4.2_downscaled",
            },
          ],
        },
      ];
      _this.getFormData("ModelData", searchItem, function (result) {
        if (result) {
          var data = result.items;
          _this.electricityPrice.data = data;
          console.log({ 0: result });
        } else {
          _this.otherName.map((item) => {
            _this.electricityPrice.data = [];
          });
        }
      });
    },
    getPriceData () {
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
          Value: _this.region.value,
        },
        {
          Method: "AND",
          Operator: "Equal",
          Name: "Model",
          Value: _this.modelName,
        },
      ];

      var subsearch = [];
      _this.otherName.map((item) => {
        subsearch.push({
          Method: "OR",
          Operator: "Equal",
          Name: "Variable",
          Value: item.variable,
        });
      });
      searchItem.push({
        Method: "AND",
        Operator: "",
        Name: "",
        SubSearchItems: subsearch,
      });
      _this.getFormData("ModelData", searchItem, function (result) {
        if (result) {
          var data = result.items;
          _this.otherName.map((item) => {
            var newitem = data.find(
              (element) => element.Variable == item.variable
            );
            if (newitem != undefined) item.data = newitem;
            else item.data = null;
          });
        } else {
          _this.otherName.map((item) => {
            item.data = null;
          });
        }
      });
    },
    getRegion () {
      var _this = this;
      _this.regionList = [];
      var searchItem = [];

      _this.getFormData("Address", searchItem, function (result) {
        if (result) {
          var data = result.items;
          data.map((item, index) => {
            _this.regionList.push({
              Name: item.Name,
              Value: item.Region,
            });
          });
          if (_this.regionList.length > 0 && "CompanyRegion" in _this.model) {
            var item = data.find((element, index) => {
              return element.Name == _this.model.CompanyRegion[0];
            });
            if (item) {
              _this.region = { name: item.Name, value: item.Region };
            }
            console.log(_this.region);
          } else {
            this.region = "";
          }
        } else {
          _this.regionList = [];
        }
      });
    },
    getReportData () {
      let _this = this;
      var iso3 = "";
      var requestPara = {
        pageCode: "address",
        searchItems: [],
        order: {
          Name: 1,
        },
        columns: [],
        withSocialStatus: false,
        index: 1,
        size: 10000,
      };
      _this.callApi("GetDocs", requestPara).then((data) => {
        let newData = data.data;
        let regionObj = newData.items.filter(function (item) {
          return item.Name == _this.model["CompanyRegion"][0];
        });
        if (regionObj && regionObj.length > 0) {
          iso3 = regionObj[0].Region;
        }
        var requestPara = {
          id: "610a50b09549b40001cfabe4",
          parameter: {
            // Company: this.model["CompanyName"],
            // GHGEmissions: this.model["GHGEmissions"],
            // ElectricityUse: this.model["ElectricityUse"],
            // CountryISO3: iso3,
            LoanAppID: _this.model._id,
            Scenario: _this.scenarioCorrect,
            Region: _this.region.value,
          },
          fileName: "",
        };
        _this.callApi("CallCustomiseAPI", requestPara).then((data) => {
          this.bus.$emit("chartReportLoading");
          if (data.statusCode == 200) {
            var result = JSON.parse(data.data.result);
            if (result.code == 0) {
              _this.reportName.forEach((otheritem) => {
                if (result.data) {
                  var reportdata = result.data.filter(
                    (item) => item.Type == otheritem.type
                  );
                  otheritem.data = reportdata;
                } else {
                  otheritem.data = [];
                }
              });
            } else {
              this.bus.$emit("chartReportNoData");
            }
          } else {
            this.bus.$emit("chartReportNoData");
          }
        });
      });
    },
    getQueryVariable (variable) {
      var query = window.location.search.substring(1);
      var vars = query.split("&");
      for (var i = 0; i < vars.length; i++) {
        var pair = vars[i].split("=");
        if (pair[0] == variable) {
          return pair[1];
        }
      }
      return false;
    },
    GetModelData () {
      var parameter = {
        ListName: "model",
        State: 0,
      };
      this.callApi("GetListItems", parameter).then((data) => {
        console.log("climateDriver: ", data);
        if (data.statusCode == 200 && data.data.length > 0) {
        } else {
        }
      });
    },
  },
  created () { },
  mounted () {
    var _this = this;
    this.companyName = this.model ? this.model["CompanyName"] : "";
    this.bus.$on("refreshTransitionRiskCharts", (name) => {
      this.companyName = name;
      setTimeout(function () {
        _this.getReportData();
      }, 2000);
      this.$nextTick(function () {
        this.bus.$emit("chartInit");
      });
    });

  },
  watch: {
    priceModel (newValue, oldValue) {
      this.getInitCarbonPrice();
      this.getInitElectricityPrice();
    },
    region: {
      handler (new_value, old_value) {
        this.bus.$emit("loadingTransitionRiskCharts");
        this.init();
      },
      deep: true,
    },
    scenario: {
      handler (new_value, old_value) {
        this.scenarioCorrect =
          new_value.Value == "Below 2℃" ? "Below 2oC" : new_value.Value;
        this.bus.$emit("loadingTransitionRiskCharts");
        this.init();
      },
      deep: true,
    },
  },
};
</script>
 
<style scoped>
html body {
  font-family: 'Arial, sans-serif';
}
.content {
  margin: 0 15px 10px 0;
}

.content-chart-item {
  border: 1px solid #dcdcdc;
  margin: 5px 10px;
}
.search-modular {
  align-items: center;
  margin-top: 40px;
}

.chart-descrip > span,
.chart-descrip-bottom > span {
  font-size: 16px;
  line-height: 32px;
}

.chart-descrip > h4 {
  font-size: 16px;
  line-height: 32px;
  font-weight: 400;
  color: #000;
}

.chart-descrip,
.chart-descrip-bottom {
  background-color: #f2f2f2;
  margin: 3px -3px;
  padding: 5px 15px;
}

.chart-descrip-bottom {
  margin: 3px 5px 15px 5px;
  width: calc(100% - 10px);
  border-bottom: 1px solid #dedede;
}

.chart-descrip-title {
  text-align: center;
  display: flex;
  justify-content: center;
  vertical-align: middle;
}

.chart-descrip-title > p {
  text-align: center;
  font-size: 18px;
  font-weight: 700;
  line-height: 40px;
  padding-top: 15px;
}

.nochart-text {
  text-align: center;
  margin-top: 200px;
  font-weight: bold;
}
.chart-item {
  height: 460px;
  width: calc(100% - 15px);
}
.line-vertical {
  width: calc(100% - 10px) !important;
}
</style>
