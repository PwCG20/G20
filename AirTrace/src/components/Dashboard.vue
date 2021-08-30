
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
      <v-col cols="2"></v-col>
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
            item-text="Name"
            item-value="Value"
            dense
            outlined
            return-object
          ></v-select>
        </v-flex>
      </v-col>

      <!--  <h3>Model</h3>
              <el-select v-model="model" placeholder="">
                <el-option v-for="item in modelList" :label="item.Name" :value="item.Name">
                </el-option>
              </el-select> -->
    </v-row>
    <v-row class="line-modular">
      <v-col cols='12'>
        <div class="chart-descrip">
          <span>Transition risks refer to the risks to companies in the move towards a less
            polluting, greener
            economy. This could include the response, or lack of response toward policy
            action and technology
            development. Sectors which are more carbon intensive have a higher exposure to
            transition risks.
          </span>
          <a
            href="/g20/airtrace/page/helpmelearnpage"
            target="_blank"
          ><img src="/g20/airtrace/api/Resource/ic_question.png" /></a>
          <h4>
            The Transition risk explorer shows three main risk factors: </h4>
          <h4>(a) Carbon price and carbon costs for the company</h4>
          <h4>(b) Revenue impact based on the sector of the company</h4>
        </div>
      </v-col>
    </v-row>
    <v-row class="line-modular">
      <v-col cols="7">
        <div class="chart-descrip-title">
          <p>(a) Carbon price per tonne of CO2 (US$2010 prices) </p>
        </div>
        
          <chartcarbon
            class="chart-item"
            :model="model"
            :schema="chartcarbon"
            :options="options"
            :id='carbonPrice.divName'
            :colorList='color'
            :date='date'
            :title='carbonPrice.title'
            :data='carbonPrice.data'
            :typename='carbonPrice.name'
            :itemColor='carbonPrice.color'
          ></chartcarbon>
        </v-lazy>

      </v-col>

      <v-col cols="5">
        <div class="chart-formula">
          <div class="chart-descrip-title">
            <p>(a)Projected carbon costs for the company (US$2010 prices) </p>
          </div>
          <div class="nochart-text">
            Chart (a2) Carbon costs = Emissions Growth Rate x [Company's Emissions] x Carbon price

          </div>
        </div>
        <div>
        </div>
      </v-col>
    </v-row>
    <v-row class="line-modular">
      <v-col cols="24">
        <div class="chart-descrip-bottom">
          <span>
            Scenarios with higher carbon prices imply that the costs of doing business
            increase for the company.
            The
            Projected carbon costs for the company assumes that the company’s GHG emissions
            follow the same
            trajectory as the sector average, in the selected country or region. Companies
            with higher GHG
            emissions
            incur higher carbon costs.
          </span>
        </div>
      </v-col>
    </v-row>

    <v-row class="line-modular">
      <v-col cols='12'>
        <div class="chart-descrip">
          <span>Transition risks refer to the risks to companies in the move towards a less polluting, greener economy.
            This could include the response, or lack of response toward policy action and technology development.
            Sectors which are more carbon intensive have a higher exposure to transition risks.

          </span>
          <a
            href="./helpmelearnpage"
            target="_blank"
          ><i class="mdi pwc_helpquestionicon"></i></a>
          <h4>
            The Transition risk explorer shows three main risk factors: </h4>
          <h4>(a) Carbon price and carbon costs for the company</h4>
          <h4>(b) Revenue impact based on the sector of the company</h4>
        </div>
      </v-col>
    </v-row>
    <v-row class="line-modular">
      <v-col cols="7">
        <div class="chart-descrip-title">
          <p>(b) Electricity price per MWh (US$2010 prices) </p>
        </div>
        <chartcarbon
          class="chart-item"
          :model="model"
          :schema="chartcarbon"
          :options="options"
          :id='electricityPrice.divName'
          :colorList='color'
          :date='date'
          :title='electricityPrice.title'
          :data='electricityPrice.data'
          :typename='electricityPrice.name'
          :itemColor='electricityPrice.color'
        ></chartcarbon>
      </v-col>

      <v-col cols="5">
        <div class="chart-formula">
          <div class="chart-descrip-title">
            <p>(b) Projected electricity costs for the company (US$2010 prices) </p>
          </div>
          <div class="nochart-text">
            Chart (b) Revenue impact = Demand Growth Rate x [Company's Revenue] x Price
          </div>
        </div>
        <div>
        </div>
      </v-col>
    </v-row>
    <v-row class="line-modular">
      <v-col cols="24">
        <div class="chart-descrip-bottom">
          <span>
            Different scenarios assume different speed and degree of low carbon energy transition for each country.
            In some countries, the energy transition could lead to higher energy prices, such as electricity prices.
            Higher electricity prices lead to increased costs of doing business for the company.
            The Projected electricity costs for the company assumes that the company’s GHG emissions follow the same trajectory as the sector average,
            in the selected country or region. Companies with higher electricity usage incur higher electricity costs.

          </span>
        </div>
      </v-col>
    </v-row>
    <v-row
      class="line-modular"
      :gutters="10"
    >
      <v-col
        v-for="item in reportName"
        :key="item.divName"
        cols="6"
        sm="12"
        md='6'
      >
        <div class="chart-descrip-title">
          <p> {{item.title}}</p>
        </div>
        <chartreport
          class="chart-item"
          :model="model"
          :schema="chartreport"
          :options="options"
          :id='item.divName'
          :colorList='color'
          :date='date'
          :title='item.title'
          :data='item.data'
          :typename='item.name'
          :itemColor='item.color'
        ></chartreport>

      </v-col>
    </v-row>

    <v-row gutters>
      <v-col
        v-for="item in otherName"
        :key="item.divName"
        cols="6"
        sm="12"
        md='6'
      >
        <div class="chart-descrip-title">
          <p> {{item.title}}</p>
        </div>
        <chartprice
          class="chart-item"
          :model="model"
          :schema="chartprice"
          :options="options"
          :id='item.divName'
          :color='color'
          :date='date'
          :title='item.title'
          :data='item.data'
          :typename='item.name'
          :itemColor='item.color'
        ></chartprice>

      </v-col>
    </v-row>
  </div>
</template>

<script> 
export default {
  components: {
    'remote-js': {
      render (createElement) {
        return createElement('script', { attrs: { type: 'text/javascript', src: this.src } });
      },
      props: {
        src: { type: String, required: true },
      },
    },
  },
  name: 'Dashboard',

  props: {
  },
  data () {
    return {
      carbonPrice: {
        "type": "Carbon price",
        "divName": "myCarbonprice",
        "title": "(a) Carbon price per tonne of CO2 (US$2010 prices)",
        'data': []
      },

      electricityPrice: {
        "type": "Electricity price",
        "divName": "myCarelectricityrice",
        "title": "(b) Electricity price per MWh (US$2010 prices)",
        'data': []
      },
      options: '',
      companyName: 'ExxonMobil',
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
      scenarioList: [{
        id: 'Below 2℃',
        Name: "Below 2℃",
        Value: 'Below 2℃'
      },
      {
        id: "Delayed transition",
        Name: "Delayed transition",
        Value: 'Delayed transition'
      },
      {
        id: "Divergent Net Zero",
        Name: "Divergent Net Zero",
        Value: "Divergent Net Zero"
      },
      {
        id: "Nationally Determined Contributions (NDCs)",
        Name: "Nationally Determined Contributions (NDCs)",
        Value: "Nationally Determined Contributions (NDCs)"
      },
      {
        id: "Net Zero 2050",
        Name: "Net Zero 2050",
        Value: "Net Zero 2050"
      },
      {
        id: "Current Policies",
        Name: "Current Policies",
        Value: "Current Policies"
      },

      ],
      scenario: { Name: 'Below 2℃', Value: 'Below 2℃' },
      regionList: [{
        id: 0,
        Name: 'World',
        Value: 'World'
      },
      {
        id: 1,
        Name: 'China',
        Value: 'CHN'
      },
      {
        id: 2,
        Name: 'Hong Kong',
        Value: "HKG"
      },
      {
        id: 3,
        Name: 'United States',
        Value: "USA"
      },
      {
        id: 4,
        Name: 'European Union',
        Value: 'EU'
      },
      {
        id: 5,
        Name: 'Canada',
        Value: "CAN"
      },
      {
        id: 6,
        Name: 'Mexico',
        Value: "MEX"
      },
      ],
      color: ["#51689b", "#ce5c5c", "#fbc357", "#8fbf8f", "#659d84", "#005aab", "#979797", "#0d0b0c"],
      date: [2010, 2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050],
      otherName: [{
        "color": "#E0301E",
        "name": "Oil price",
        "divName": "myOliPrice",
        "title": "Oil price (US$2010/GJ)",
        data: {}
      }, {
        "color": "#EE9C34",
        "name": "Gas price",
        "divName": "myGasPrice",
        "title": "Gas price (US$2010/GJ)",
        data: {}
      }, {
        "color": "#E669A2",
        "name": "Coal price",
        "divName": "myCoalPrice",
        "title": "Coal price (US$2010/GJ)",
        data: {}
      }, {
        "color": "#7bfefa",
        "name": "Electricity price",
        "divName": "myElectricityPrice",
        "title": "Electricity price (US$2010/GJ)",
        data: {}
      }],
      reportName: [{
        "type": "Carbon cost",
        "divName": "myCarbonCost",
        "title": "Carbon cost (US$2010/t CO2)",
        'data': []
      }, {
        "type": "Electricity revenue",
        "divName": "myElectricityRevenue",
        "title": "Electricity revenue (US$2010/t CO2)",
        'data': []
      }],
      region: { Name: 'World', Value: 'World' },
      modelList: [{
        id: 0,
        Name: "GCAM5.3_NGFS_downscaled"
      }, {
        id: 1,
        Name: "MESSAGEix-GLOBIOM 1.1_downscaled"
      }, {
        id: 2,
        Name: "REMIND-MAgPIE 2.1-4.2_downscaled"
      }, {
        id: 3,
        Name: "REMIND-MAgPIE 2.1-4.2"
      }, {
        id: 4,
        Name: "GCAM5.3_NGFS"
      }, {
        id: 5,
        Name: "MESSAGEix-GLOBIOM 1.1"
      }, {
        id: 6,
        Name: "REMIND-MAgPIE 2.1-4.2 IntegratedPhysicalDamages (95th)"
      }, {
        id: 7,
        Name: "REMIND-MAgPIE 2.1-4.2 IntegratedPhysicalDamages (median)"
      },],
      modelName: 'REMIND-MAgPIE 2.1-4.2',
      scenarioCorrect: 'Below 2??C',
    }
  },
  methods: {
    init () {
      this.getInitCarbonPrice();
      this.getInitElectricityDemand();
      this.getPriceData();
      this.getReportData();

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
        }
        else {
          return callback(false);
        }
      });
    },
    getInitCarbonPrice () {
      var _this = this;


      var searchItem = [{
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Scenario",
        "Value": _this.scenarioCorrect
      }, {
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Region",
        "Value": _this.region.Value
      }, {
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Variable",
        "Value": _this.carbonPrice.type
      }];
      _this.getFormData('ModelData', searchItem, function (result) {
        if (result) {
          var data = result.items;
          _this.carbonPrice.data = data;
          console.log({ 0: result });
        }
        else {
          _this.otherName.map(item => {
            _this.carbonPrice.data = [];
          })
        }
      });

    },
    getInitElectricityDemand () {
      var _this = this;
      var searchItem = [{
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Scenario",
        "Value": _this.scenarioCorrect
      }, {
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Region",
        "Value": _this.region.Value
      }, {
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Variable",
        "Value": "Electricity demand"
      }];
      _this.getFormData('ModelData', searchItem, function (result) {
        if (result) {
          var data = result.items;
          _this.electricityPrice.data = data;
          console.log({ 0: result });
        }
        else {
          _this.otherName.map(item => {
            _this.electricityPrice.data = [];
          })
        }
      });
    },
    getPriceData () {
      let _this = this;

      var searchItem = [{
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Scenario",
        "Value": _this.scenarioCorrect
      }, {
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Region",
        "Value": _this.region.Value
      },
      {
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Model",
        "Value": _this.modelName
      }
      ];


      var subsearch = [];
      _this.otherName.map(item => {
        subsearch.push({
          "Method": "OR",
          "Operator": "Equal",
          "Name": "Variable",
          "Value": item.name
        })
      });
      searchItem.push({
        "Method": "AND",
        "Operator": "",
        "Name": "",
        SubSearchItems: subsearch
      });
      _this.getFormData('ModelData', searchItem, function (result) {
        if (result) {
          var data = result.items;
          _this.otherName.map(item => {
            var newitem = data.find(element => element.Variable == item.name);
            if (newitem != undefined)
              item.data = newitem;
            else
              item.data = null;
          })
        }
        else {
          _this.otherName.map(item => {
            item.data = null;
          })
        }
      });
    },
    getReportData () {
      var _this = this;
      var item = {
        EntityName: _this.queryReport,
        Columns: [],
        SearchItem: [],
        Index: 0,
        Size: 100000000
      };
      var searchItem = [{
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Scenario",
        "Value": _this.scenarioCorrect
      }, {
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Region",
        "Value": _this.region.Value
      },
      {
        "Method": "AND",
        "Operator": "Equal",
        "Name": "Company",
        "Value": _this.companyName
      }
      ];

      var subsearch = [];
      _this.reportName.map(item => {
        subsearch.push({
          "Method": "OR",
          "Operator": "Equal",
          "Name": "Type",
          "Value": item.type
        })
      });
      searchItem.push({
        "Method": "AND",
        "Operator": "",
        "Name": "",
        SubSearchItems: subsearch
      });
      item.SearchItem = searchItem;
      _this.getFormData('reportdata', searchItem, function (result) {
        if (result) {
          var data = result.items;
          _this.reportName.map(item => {
            var newitem = data.filter(element => element.Type == item.type);
            if (newitem != undefined) {
              item.data = newitem;
              console.log(item.data);
            }

            else
              item.data = [];
          })
        }
        else {
          _this.reportName.map(item => {
            item.data = [];
          })
        }
      })
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
      return (false);
    },

  },
  mounted () {
    this.companyName = this.model ? this.model["CompanyName"] : ''; 
    this.init();
    this.bus.$on("refreshTransitionRiskCharts", (name) => {//有数据更新时候，重新查询数据，更新chart
      this.companyName =name;
      this.init();
      this.$nextTick(function () {
        this.bus.$emit('chartInit');
      })
    });
  },
  watch: {
    region: {
      handler (new_value, old_value) {
        this.init();
      },
      deep: true
    },
    scenario: {
      handler (new_value, old_value) {
        this.scenarioCorrect = new_value.Value == "Below 2℃" ? 'Below 2??C' : new_value.Value;
        this.init();
      },
      deep: true
    }
  }
}
</script>
 
<style scoped>
html body {
  font-family: 'Arial, sans-serif';
}
.content {
  margin: 0 15px 10px 0;
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
  margin: 3px 10px;
  padding: 5px 15px;
}

.chart-descrip-bottom {
  margin: 3px 10px 15px 10px;
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
