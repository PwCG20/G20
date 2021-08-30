<template>
  <div class="process2">
    <div>
      <v-card>
        <v-tabs
          class="title-tab"
          v-model="tab"
          @change="changeTabs"
          color="#E0301E"
          icons-and-text
        >
          <!-- <v-tabs-slider></v-tabs-slider> -->

          <v-tab href="#tab_transition">
            <span>
              <v-icon class="mr-4">pwc-icon pwc-bargraph</v-icon>Transition risk
              explorer
            </span>
          </v-tab>

          <v-tab href="#tab_physical">
            <span>
              <v-icon class="mr-4">pwc-icon pwc-bargraph</v-icon>Physical risk
              explorer
            </span>
          </v-tab>
        </v-tabs>

        <v-tabs-items
          :value="tab"
          style="margin: 0px"
        >
          <v-tab-item
            value="tab_transition"
            eager
          >
            <v-card flat>
              <vccchart
                class="chart-item"
                :model="model"
                :schema="vccchart"
                :options="options"
                :regionList="climateRegionList"
                :region="climateRegion"
              ></vccchart>
            </v-card>
          </v-tab-item>
          <v-tab-item
            value="tab_physical"
            eager
          >
            <v-card flat>
              <v-row class="line-modular">
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
                      style="margin-top: 40px; max-width: 350px"
                      color="#E0301E"
                      :items="climateRegionList"
                      return-object
                      v-model="climateRegion"
                      item-text="name"
                      item-value="value"
                      outlined
                      @change="chooseClimateRegion"
                      dense
                    >
                    </v-select>
                  </v-flex>
                </v-col>
                <v-col cols="4">
                  <v-flex>
                    <span
                      class="ml-4 mr-4 mt-2"
                      style="float: left"
                    >Indicator</span>
                    <v-select
                      style="margin-top: 40px; max-width: 350px"
                      color="#E0301E"
                      :items="climateIndicatorList"
                      return-object
                      v-model="climateIndicator"
                      item-text="name"
                      item-value="value"
                      outlined
                      @change="chooseClimateIndicator"
                      dense
                    >
                    </v-select>
                  </v-flex>
                </v-col>
                <v-col cols="4">
                  <v-flex>
                    <span
                      class="ml-4 mr-4 mt-2"
                      style="float: left"
                    >Scenario</span>
                    <v-select
                      style="margin-top: 40px; max-width: 350px"
                      return-object
                      color="#E0301E"
                      :items="climateScenarioList"
                      v-model="climateScenario"
                      item-text="name"
                      item-value="value"
                      outlined
                      @change="chooseClimateScenario"
                      dense
                    >
                    </v-select>
                  </v-flex>
                </v-col>
              </v-row>
              <v-row
                class="line-modular"
                style="margin-top: 15px"
              >
                <div class="chart-descrip">
                  <span>Physical risks refer to potential impacts of climate change
                    risks on a company. These risks could include extreme
                    weather events, sea level rise and increasing water
                    scarcity.
                  </span>
                  <a
                    href="/g20/airtrace/page/helpmelearnpage"
                    target="_blank"
                  ><img src="/g20/airtrace/api/Resource/ic_question.png" /></a>
                  <h4>
                    The Physical risk explorer shows four main types of extreme events risk indicators relevant to the locations of the company. These are flooding risks (precipitation), tropical cyclones, wildfires and heatwaves. We show projected future trends of these risk indicators and their impacts on different geographical region.
                  </h4>
                  <!-- <h4>
                    (a) Extreme weather risks: flooding risks (precipitation),
                    tropical cyclones, wildfires and heatwaves. We show
                    projected future trends of these risk indicators and their
                    impacts on different geographical region.
                  </h4>
                  <h4>(b) Economic losses due to physical damages.</h4> -->
                </div>
              </v-row>

              <div style="text-align: left; padding-bottom: 10px">
                <v-row class="line-modular">
                  <div class="map-descrip-title">
                    <p>
                      (a) Relative change in
                      {{ climateIndicator ? climateIndicator.name : "" }}
                      in
                      {{ climateRegion ? climateRegion.name : "" }}
                    </p>
                  </div>
                  <div class="chart-descrip">
                    <span>This graph shows how relative changes in
                      {{ climateIndicator ? climateIndicator.name : "" }}
                      (expressed in percent) will play out over time in
                      {{ climateRegion ? climateRegion.name : "" }} at different
                      global warming levels compared to the reference period
                      1986-2006, based on the
                      {{ climateScenario ? climateScenario.name : "" }}
                      scenario.
                    </span>
                  </div>
                </v-row>
              </div>
              <div
                id="climateChangeChart"
                style="width: 100%; height: 400px"
              ></div>

              <div style="text-align: left; padding-top: 20px">
                <v-row class="line-modular">
                  <div class="map-descrip-title">
                    <p>
                      (b) How is
                      {{ climateIndicator ? climateIndicator.name : "" }}
                      affected by {{ tabPosition }}°C of warming?
                    </p>
                  </div>
                  <div class="chart-descrip">
                    <span>
                      This map shows the relative change in
                      {{ climateIndicator ? climateIndicator.name : "" }}
                      (expressed in percent) at {{ tabPosition }}°C of global
                      warming compared to the reference period 1986-2006.
                    </span>
                  </div>
                </v-row>
                <v-row
                  class="line-modular"
                  style="margin-left: 10px; text-align: left"
                >
                  <v-col
                    cols="2"
                    style="line-height: 48px; margin-left: -6px"
                  >Global warming level</v-col>
                  <v-col cols="10">
                    <v-btn-toggle
                      v-model="tabPosition"
                      mandatory
                      @change="chooseTabPosition"
                      borderless
                    >
                      <v-btn value="1.5">
                        <span class="hidden-sm-and-down">1.5°C</span>
                      </v-btn>

                      <v-btn value="2.0">
                        <span class="hidden-sm-and-down">2.0°C</span>
                      </v-btn>

                      <v-btn value="2.5">
                        <span class="hidden-sm-and-down">2.5°C</span>
                      </v-btn>

                      <v-btn value="3.0">
                        <span class="hidden-sm-and-down">3.0°C</span>
                      </v-btn>
                    </v-btn-toggle>
                  </v-col>
                </v-row>
                <div
                  id="mapChart"
                  class="chartsdom"
                ></div>
                <div style="padding-top: 15px; margin-left: 10px">
                  <div>
                    Change in
                    <b>{{ climateIndicator ? climateIndicator.name : "" }}</b>
                    in %
                  </div>
                  <div style="
                      align-items: center;
                      width: 100%;
                      display: flex;
                      padding-top: 10px;
                      color: #73777c;
                      font-size: 13px;
                    ">
                    <span style="text-align: right">below<br /><span>{{ mapBelowValue }}%</span></span>
                    <div style="
                        position: relative;
                        line-height: 0;
                        width: 240px;
                        margin: 0 3px;
                      ">
                      <div
                        id="mapLegend"
                        style="width: 240px; height: 40px"
                      ></div>
                      <div id="mapLegendDetail"></div>
                    </div>
                    <span>above<br /><span>{{ mapAboveValue }}%</span></span>
                  </div>
                </div>
              </div>
            </v-card>
          </v-tab-item>
        </v-tabs-items>
      </v-card>
    </div>
  </div>
</template>
<script>
export default {
  // components: {
  //   remote: {
  //     render(createEle) {
  //       return createEle("script", {
  //         attrs: {
  //           type: "text/javascript",
  //           src: this.src,
  //         },
  //       });
  //     },
  //     props: {
  //       src: {
  //         type: String,
  //         required: true,
  //       },
  //     },
  //   },
  // },
  data () {
    return {
      pageCode: 2,
      vccchart: {
        component: "vccchart",
        name: "vccchart",
      },
      tabsChanged: false,
      regionUrl: this.getResource("chart_icon3.svg"),
      scenarioUrl: this.getResource("chart_icon1.svg"),
      tabUrl: this.getResource("icon_bar.svg"),
      tab: "tab_transition",
      text: "",
      mapBelowValue: "",
      mapAboveValue: "",
      climateRegionList: [
        {
          "id": 0,
          "name": "Australia",
          "value": "AUS"
        },
        {
          "id": 1,
          "name": "Brazil",
          "value": "BRA"
        },
        {
          "id": 2,
          "name": "Canada",
          "value": "CAN"
        },
        {
          "id": 3,
          "name": "China",
          "value": "CHN"
        },
        {
          "id": 5,
          "name": "France",
          "value": "FRA"
        },
        {
          "id": 7,
          "name": "Hong Kong",
          "value": "HKG"
        },
        {
          "id": 8,
          "name": "Hungary",
          "value": "HUN"
        },
        {
          "id": 10,
          "name": "India",
          "value": "IND"
        },
        {
          "id": 9,
          "name": "Indonesia",
          "value": "IDN"
        },
        {
          "id": 11,
          "name": "Italy",
          "value": "ITA"
        },
        {
          "id": 12,
          "name": "Japan",
          "value": "JPN"
        },
        {
          "id": 13,
          "name": "Korea, Republic of",
          "value": "KOR"
        },
        {
          "id": 15,
          "name": "Malaysia",
          "value": "MYS"
        },
        {
          "id": 14,
          "name": "Mexico",
          "value": "MEX"
        },
        {
          "id": 16,
          "name": "Netherlands",
          "value": "NLD"
        },
        {
          "id": 17,
          "name": "New Zealand",
          "value": "NZL"
        },
        {
          "id": 18,
          "name": "Philippines",
          "value": "PHL"
        },
        {
          "id": 19,
          "name": "Russia",
          "value": "RUS"
        },
        {
          "id": 20,
          "name": "Saudi Arabia",
          "value": "SAU"
        },
        {
          "id": 21,
          "name": "Singapore",
          "value": "SGP"
        },
        {
          "id": 26,
          "name": "South Africa",
          "value": "ZAF"
        },
        {
          "id": 4,
          "name": "Spain",
          "value": "ESP"
        },
        {
          "id": 23,
          "name": "Taiwan, Province of China",
          "value": "TWN"
        },
        {
          "id": 22,
          "name": "Thailand",
          "value": "THA"
        },
        {
          "id": 6,
          "name": "United Kingdom",
          "value": "GBR"
        },
        {
          "id": 24,
          "name": "United States",
          "value": "USA"
        },
        {
          "id": 25,
          "name": "Viet Nam",
          "value": "VNM"
        }
      ],
      climateRegion: null,
      climateIndicatorList: [
        {
          id: 0,
          name: "Precipitation",
          value: "prAdjust",
          // baseline: "Baseline 0.01kg m⁻² s⁻¹ \n(reference period \n1986-2006)",
          baseline: "Baseline \n(reference period \n1986-2006)",
        },
        {
          id: 1,
          name: "Annual Expected Damage from Tropical Cyclones",
          value: "ec3",
          baseline: "Baseline \n(reference year 2020)",
        },
        {
          id: 2,
          name: "Fraction of Population annually exposed to Heatwaves",
          value: "peh",
          baseline: "Baseline \n(reference period \n1986-2006)",
        },
        {
          id: 3,
          name: "Fraction of Population annually exposed to Wildfires",
          value: "pew",
          baseline: "Baseline \n(reference period \n1986-2006)",
        },
      ],
      climateIndicator: null,
      climateScenarioList: [
        {
          id: 0,
          name: "Current policies",
          value: "h_cpol",
        },
        {
          id: 1,
          name: "Delayed transition",
          value: "d_delfrag",
        },
        {
          id: 2,
          name: "Net Zero 2050",
          value: "o_1p5c",
        },
      ],
      climateScenario: null,
      dataClimateChange: {},
      dataClimate: {},
      climateGranular: {},
      tabPosition: "1.5",
      companyCoorList: [
        {
          city: "Beijing",
          lon_lat: [39.9, 76.3],
        },
        {
          city: "Shenzen",
          lon_lat: [22, 84],
        },
      ],
      countryOutlineList: {
        HKG: "75a44e0e-fd82-40ff-bf85-c6202ad56e4a",
        CHN: "83dee9a2-dc6b-4836-b04d-b942c1cc15bf",
        USA: "efdb8949-9a3b-4456-92ab-7c073059ef04",
      },
      mapBelowValue: "",
      mapAboveValue: "",
      climateIndicatorColor: {
        prAdjust: {
          below0: "#a88262",
          above0: "#2658a6",
        },
        ec3: {
          below0: "#2967e7",
          above0: "#f04d24",
        },
        pew: {
          below0: "#6a97ec",
          above0: "#f04d24",
        },
        peh: {
          below0: "#6a97ec",
          above0: "#f04d24",
        },
      },
      mapStepInfo: {},
      mapLegendStepDiv: "",
      companyCoordList: [],
    };
  },
  created () {
    // if (val == "tab_2") {}
  },
  methods: {
    // getResourceDemo(name) {
    //     let url = '';
    //     switch (name) {
    //         case "icon-search.svg":
    //             url = require("../assets/g20/icon-search.svg");
    //             break;
    //         case "gettyimages.png":
    //             url = require("../assets/g20/GettyImages.png");
    //             break;
    //     }
    //     return url;
    // },
    // initEchart() {
    //     let _self = this;
    //     let si = setInterval(function () {
    //         if (echarts) {
    //             _self.getClimateChangeChart();
    //             clearInterval(si);
    //         }
    //     }, 1000);
    // },
    changeTabs () {
      // if (this.tab == "tab_transition") {
      //   this.bus.$emit("chartInit");
      // }
      if (this.tab == "tab_physical") {
        if (!this.tabsChanged) {
          this.tabsChanged = true;
          this.onloadchnjsondata();
        }
      }
      var a = document.getElementsByClassName(".v-tab--active")[0];
      if (a) {
        var width = a.offsetWidth;
        document.getElementsByClassName("v-tabs-slider-wrapper")[0].style.width = width + "px";
      }
    },

    importMapBoxJS () {
      var script = document.createElement("script");
      script.id = "mapbox-js-module";
      script.type = "text/javascript";
      script.src = this.getResource("mapbox-gl.js");
      script.async = true;
      script.defer = true;
      document.head.appendChild(script);
    },
    importgeojsondata () {
      var _self = this;
      var geoList = ["chnjsondata.js", "usageo.js", "hkggeo.js"];
      geoList.forEach(function (geojs) {
        var script = document.createElement("script");
        script.id = "json-data-module";
        script.type = "text/javascript";
        if (geojs == "hkggeo.js") {
          script.src = _self.getResource("hkggeo.js");
        } else if (geojs == "usageo.js") {
          script.src = _self.getResource("usageo.js");
        } else {
          script.src = _self.getResource("chnjsondata.js");
        }
        script.async = true;
        script.defer = true;
        // script.onload = this.onloadchnjsondata;
        document.head.appendChild(script);
      });
    },
    onloadchnjsondata () {
      this.getClimateGeo();
      this.getClimateChangeData();
      //this.initEchart();
    },
    chooseRegion () { },
    chooseScenario () { },
    getClimateGeo () {
      var _self = this;
      let filterData = [];
      if (_self.tabPosition) {
        filterData.push({
          name: "warming_level",
          value: _self.tabPosition,
          operator: "Equal",
          method: "And",
          subSearchItems: [],
        });
      }
      if (_self.climateRegion) {
        filterData.push({
          name: "country",
          value: _self.climateRegion.value,
          operator: "Equal",
          method: "And",
          subSearchItems: [],
        });
      }
      if (_self.climateIndicator) {
        filterData.push({
          name: "type_id",
          value: _self.climateIndicator.value,
          operator: "Equal",
          method: "And",
          subSearchItems: [],
        });
      }
      var requestPara = {
        pageCode: "climategeogranular",
        searchItems: filterData,
        order: {},
        columns: [],
        withSocialStatus: false,
        index: _self.pageIndex,
        size: 1,
      };
      _self.callApi("GetDocs", requestPara).then((data) => {
        let newData = data.data;
        if (newData.items.length > 0) {
          _self.climateGranular = newData.items[0];
          _self.dataClimate = JSON.parse(newData.items[0].data);
          _self.getEchart();
        }
      });
    },
    getClimateChangeData () {
      var _self = this;
      let filterData = [];
      if (_self.climateRegion) {
        filterData.push({
          name: "country",
          value: _self.climateRegion.value,
          operator: "Equal",
          method: "And",
          subSearchItems: [],
        });
      }
      if (_self.climateIndicator) {
        filterData.push({
          name: "type_id",
          value: _self.climateIndicator.value,
          operator: "Equal",
          method: "And",
          subSearchItems: [],
        });
      }
      if (_self.climateScenario) {
        filterData.push({
          name: "scenario_id",
          value: _self.climateScenario.value,
          operator: "Equal",
          method: "And",
          subSearchItems: [],
        });
      }
      var requestPara = {
        pageCode: "climategeogranular",
        searchItems: filterData,
        order: {},
        columns: [],
        withSocialStatus: false,
        index: _self.pageIndex,
        size: 1,
      };
      _self.callApi("GetDocs", requestPara).then((data) => {
        let newData = data.data;
        _self.dataClimateChange = newData.items[0];
        _self.getClimateChangeChart();
      });
    },
    getMapGranularStops (min, max, stepInfo, granularColors, gradientColors) {
      var stops = [];
      var sc = stepInfo.length;
      for (var i = 0; i < sc; i++) {
        if (i == 0 && min != stepInfo[0]) {
          stops.push([min, granularColors[0]]);
        }
        stops.push([stepInfo[i], gradientColors[i]]);
        if (i == sc - 1 && max != stepInfo[sc - 1]) {
          stops.push([max, gradientColors[gradientColors.length - 1]]);
        }
      }
      return stops;
    },
    calcMapInfo (min, max) {
      this.mapBelowValue = min;
      this.mapAboveValue = max;

      this.calcLegendStep(min, max);
      var zeroColor = "#e6ebf0";
      var stepsInfo = this.mapStepInfo.stepInfo;
      var stepMinVal = stepsInfo[0];
      var stepMaxVal = stepsInfo[stepsInfo.length - 1];
      //补充空数据的情况处理逻辑
      if (!this.climateIndicator) {
        this.climateIndicator = {
          id: 0,
          name: "Precipitation",
          value: "prAdjust",
          baseline: "Baseline 0.01kg m⁻² s⁻¹ \n(reference period \n1986-2006)",
        };
      }
      var colorInfo = this.climateIndicatorColor[this.climateIndicator.value];
      if (stepsInfo.length == 1) {
        color_range = [zeroColor];
      } else if (stepMinVal >= 0) {
        color_range = [zeroColor, colorInfo.above0];
      } else if (stepMinVal < 0 && stepMaxVal == 0) {
        color_range = [colorInfo.below0, zeroColor];
      } else if (stepMinVal < 0 && stepMaxVal > 0) {
        color_range = [colorInfo.below0, zeroColor, colorInfo.above0];
      } else {
        color_range = [colorInfo.below0, colorInfo.above0];
      }

      var granularColors = color_range;

      var mapGranularStops = [];
      var colorsCount = granularColors.length;
      if (colorsCount == 1) {
        mapGranularStops = [[min, granularColors[0]]];
      } else if (colorsCount == 2) {
        var gc = this.gradientColors(
          granularColors[0],
          granularColors[1],
          stepsInfo.length,
          2.2
        );
        mapGranularStops = this.getMapGranularStops(
          min,
          max,
          stepsInfo,
          granularColors,
          gc
        );
      } else {
        var zeroIdx = stepsInfo.indexOf(0) == -1 ? 0 : stepsInfo.indexOf(0);
        var gc1 = this.gradientColors(
          granularColors[0],
          granularColors[1],
          stepsInfo.length - zeroIdx,
          2.2
        );
        var gc2 = this.gradientColors(
          granularColors[1],
          granularColors[2],
          zeroIdx,
          2.2
        );
        gc1 = gc1.concat(gc2);
        mapGranularStops = this.getMapGranularStops(
          min,
          max,
          stepsInfo,
          granularColors,
          gc1
        );
      }

      return [color_range, mapGranularStops];
    },
    getMapLegendChart (min, max, color_range) {
      var linearGradientInfo = [];
      for (var i = 0; i < color_range.length; i++) {
        var offsetVal = 1;
        if (i == 0) {
          offsetVal = 1;
        } else if (i == color_range.length - 1) {
          offsetVal = 0;
        } else {
          offsetVal = 1 - parseFloat((Math.abs(min) / (max - min)).toFixed(2));
        }
        linearGradientInfo.push({
          offset: offsetVal,
          color: color_range[i],
        });
      }
      var leftSymbolColor = color_range[0];
      var rightSymbolColor = color_range[color_range.length - 1];
      var legendChart = echarts.init(document.getElementById("mapLegend"));
      var barData = [100];
      var l_option = {
        xAxis: {
          show: false,
          type: "value",
          lineStyle: {
            show: false,
          },
          data: barData,
        },
        yAxis: [
          {
            show: false,
            type: "category",
          },
          {
            show: false,
            type: "category",
          },
        ],
        grid: {
          left: -20,
          right: -20,
          top: 0,
          bottom: 0,
        },
        series: [
          {
            type: "bar",
            data: barData,
            barWidth: 15,
            smooth: true,
            yAxisIndex: 0,
            itemStyle: {
              normal: {
                color: new echarts.graphic.LinearGradient(
                  1,
                  0,
                  0,
                  0,
                  linearGradientInfo
                ),
              },
            },
          },
          {
            data: [-6],
            type: "line",
            symbol:
              "path://M702.6721384546835 130.655724878184L321.3278615453163 512 702.6721384546835 893.3442751218158Z",
            symbolSize: 15,
            yAxisIndex: 0,
            itemStyle: {
              color: leftSymbolColor,
            },
          },
          {
            data: [106],
            type: "line",
            symbol:
              "path://M321.32786154 893.34427512L702.67213845 512 321.32786154 130.65572488Z",
            symbolSize: 15,
            yAxisIndex: 0,
            itemStyle: {
              color: rightSymbolColor,
            },
          },
        ],
      };
      legendChart.setOption(l_option);
      this.mapLegendStepDiv = "";
      var stepInfo = this.mapStepInfo.stepInfo;
      var widthVal = 190;
      var sp = 22.5;
      var positionInterval = 0;
      if (stepInfo.length == 1) {
        this.mapLegendStepDiv =
          '<div class="legendTick" style="left: 117.5px;">' +
          stepInfo[0] +
          "</div>";
      } else {
        var ts = (widthVal / (stepInfo.length - 1)).toFixed(4);
        for (var i = 0; i < stepInfo.length; i++) {
          var tp = sp + ts * i;
          var div =
            '<div class="legendTick" style="left: ' +
            tp +
            'px;">' +
            stepInfo[i] +
            "</div>";
          this.mapLegendStepDiv += div;
        }
      }
      document.getElementById("mapLegendDetail").innerHTML =
        this.mapLegendStepDiv;
    },
    getEchart () {
      var _self = this;
      // var fileID = _self.countryOutlineList[_self.climateRegion.value] == null ? _self.countryOutlineList[
      //         "CHN"] :
      //     _self
      //     .countryOutlineList[_self.climateRegion.value];
      // var countryMap = "/securecamera/techsprint/Admin/HomePage/DownloadFile?fileIds=" + fileID;

      var addOutlineFlag = ["CHN", "USA", "HKG"].includes(
        _self.climateRegion.value
      );
      var center = [
        parseFloat(_self.climateGranular.center[0]),
        parseFloat(_self.climateGranular.center[1]),
      ];
      var color_range_values = _self.climateGranular.color_range;
      var min = parseFloat(parseFloat(color_range_values[0]).toFixed(1));
      var max = parseFloat(parseFloat(color_range_values[1]).toFixed(1));
      var mapInfo = _self.calcMapInfo(min, max);
      var color_range = mapInfo[0];
      var paint_stops = mapInfo[1];

      _self.getMapLegendChart(min, max, color_range);

      mapboxgl.accessToken =
        "pk.eyJ1Ijoia2VsaS0xNyIsImEiOiJja3JjdXFpMHczOXFqMm5uM2hxc3E1M2g0In0.Hqe4OfavRrAzHEmkh7W5Hw";
      var map = new mapboxgl.Map({
        container: "mapChart",
        style: "mapbox://styles/mapbox/light-v10",
        center: center,
        zoom: 3,
        scrollZoom: false,
        dragRotate: false,
        pitchWithRotate: false,
        minZoom: 2,
        attributionControl: false,
      });
      map.addControl(
        new mapboxgl.NavigationControl({
          showCompass: false,
        })
      );
      map.on("load", function () {
        if (addOutlineFlag) {
          let geoData = window._chnjsondata; //JSON.parse(newData.items[0].CountryData);
          if (_self.climateRegion.value == "USA") {
            geoData = window._usageodata;
          } else if (_self.climateRegion.value == "HKG") {
            geoData = window._hkggeodata;
          }
          map.addSource("region", {
            type: "geojson",
            data: geoData,
          });

          map.addLayer({
            id: "outline",
            type: "line",
            source: "region",
            layout: {},
            paint: {
              "line-color": "lightblue",
              "line-width": 2,
            },
          });
        }

        map.addSource("climate", {
          type: "geojson",
          data: _self.dataClimate,
        });

        map.addLayer({
          id: "fillID",
          type: "fill",
          source: "climate",
          paint: {
            "fill-color": {
              property: "climate_val",
              stops: paint_stops,
            },
            "fill-opacity": 0.8,
          },
        });
      });

      _self.companyCoordList.forEach(function (addrInfo) {
        var lon_lat = addrInfo["coordinate"];
        if (!Number.isNaN(lon_lat[0]) && !Number.isNaN(lon_lat[1])) {
          const marker = new mapboxgl.Marker({
            /* options */
          });
          const markerDiv = marker.getElement();
          markerDiv.addEventListener("mouseenter", () => marker.togglePopup());
          markerDiv.addEventListener("mouseleave", () => marker.togglePopup());

          marker
            .setLngLat(addrInfo["coordinate"])
            .setPopup(
              new mapboxgl.Popup().setHTML("<span>" + addrInfo.city + "</span>")
            )
            .addTo(map);
        }
      });

      // //如果Resource中支持上传JSON文件，则需要修改为利用getResource接口来获取JSON文件内容
      // var requestPara = {
      //     pageCode: "countryoutlinelist",
      //     searchItems: [{
      //         name: "CountryCode",
      //         value: _self.climateRegion.value,
      //         operator: "Equal",
      //         method: "And",
      //         subSearchItems: [],
      //     }],
      //     order: {},
      //     columns: ["CountryData"],
      //     withSocialStatus: false,
      //     index: _self.pageIndex,
      //     size: 1,
      // };
      // _self.callApi("GetDocs", requestPara).then((data) => {
      //     let newData = data.data;
      //     if (newData.items.length > 0) {
      //         let geoData = JSON.parse(newData.items[0].CountryData);
      //         mapboxgl.accessToken =
      //             "pk.eyJ1Ijoia2VsaS0xNyIsImEiOiJja3JjdXFpMHczOXFqMm5uM2hxc3E1M2g0In0.Hqe4OfavRrAzHEmkh7W5Hw";
      //         var map = new mapboxgl.Map({
      //             container: "mapChart",
      //             style: "mapbox://styles/mapbox/light-v10",
      //             center: center,
      //             zoom: 3,
      //             scrollZoom: false,
      //             dragRotate: false,
      //             pitchWithRotate: false,
      //             minZoom: 2,
      //             attributionControl: false
      //         });
      //         map.addControl(new mapboxgl.NavigationControl({
      //             showCompass: false
      //         }));
      //         map.on("load", function () {
      //             if (addOutlineFlag) {
      //                 map.addSource("region", {
      //                     'type': 'geojson',
      //                     'data': geoData
      //                 });

      //                 map.addLayer({
      //                     id: "outline",
      //                     type: "line",
      //                     source: "region",
      //                     layout: {},
      //                     paint: {
      //                         "line-color": "lightblue",
      //                         "line-width": 2,
      //                     },
      //                 });
      //             }

      //             map.addSource("climate", {
      //                 'type': 'geojson',
      //                 'data': _self.dataClimate
      //             });

      //             map.addLayer({
      //                 id: "fillID",
      //                 type: "fill",
      //                 source: "climate",
      //                 paint: {
      //                     "fill-color": {
      //                         property: "climate_val",
      //                         stops: paint_stops
      //                     },
      //                     "fill-opacity": 0.8,
      //                 },
      //             });
      //         });

      //         _self.companyCoorList.forEach(function (addrInfo) {
      //             new mapboxgl.Marker()
      //                 .setLngLat(center)
      //                 .addTo(map);
      //         });
      //     }
      // });
    },
    getClimateChangeChart () {
      var _self = this;
      var climateDataStr = this.dataClimateChange.data;
      var data = JSON.parse(climateDataStr);
      var upper = data.upper;
      var median = data.median;
      var lower = data.lower;
      var years = data.year;
      var changeChart = echarts.init(
        document.getElementById("climateChangeChart")
      );
      var area_color = "#a6d5e9";
      var indicatorItem = _self.climateIndicatorList.find(
        (ind) => ind.value == _self.climateIndicator.value
      );
      var baselineInfo =
        indicatorItem.baseline + "\n" + this.climateScenario.name;
      var option = {
        title: {
          text: _self.climateIndicator.name + " in %",
          show: true,
          textStyle: {
            color: "#7F7F7F",
            fontWeight: "normal",
            fontSize: 13,
          },
          left: 130,
        },
        tooltip: {
          trigger: "axis",
          axisPointer: {
            type: "cross",
            label: {
              backgroundColor: "#6a7985",
            },
          },
        },
        xAxis: [
          {
            type: "category",
            boundaryGap: false,
            data: years,
            axisTick: {
              show: true,
            },
          },
        ],
        yAxis: [
          {
            type: "value",
          },
        ],
        series: [
          {
            name: "Upper bound",
            type: "line",
            smooth: true,
            symbol: "circle",
            showSymbol: false,
            itemStyle: {
              normal: {
                color: "#34cfe4",
                lineStyle: {
                  color: area_color,
                  width: 0,
                },
              },
            },
            areaStyle: {
              color: area_color,
            },
            data: upper,
          },
          {
            name: "Median",
            type: "line",
            smooth: true,
            symbol: "circle",
            symbolSize: 3,
            itemStyle: {
              normal: {
                color: "#6e43a1",
                lineStyle: {
                  color: "#b0bbd7",
                },
              },
            },
            markLine: {
              silent: true,
              lineStyle: {
                normal: {
                  color: "black",
                },
              },
              symbol: "none",
              data: [
                {
                  yAxis: 0,
                },
              ],
              label: {
                normal: {
                  formatter: baselineInfo,
                  color: "#73777c",
                },
              },
            },
            data: median,
          },
          {
            name: "Lower bound",
            type: "line",
            smooth: true,
            showSymbol: false,
            symbol: "circle",
            itemStyle: {
              normal: {
                color: "#97c9cf",
                lineStyle: {
                  color: area_color,
                  width: 0,
                },
              },
            },
            areaStyle: {
              color: area_color,
            },
            emphasis: {
              focus: "series",
            },
            data: lower,
          },
        ],
      };
      changeChart.setOption(option, true);
    },
    chooseClimateRegion () {
      this.getClimateChangeData();
      this.getClimateGeo();
    },
    chooseClimateIndicator () {
      this.getClimateChangeData();
      this.getClimateGeo();
    },
    chooseClimateScenario () {
      this.getClimateChangeData();
    },
    chooseTabPosition () {
      this.getClimateGeo();
    },
    parseColor (hexStr) {
      return hexStr.length === 4
        ? hexStr
          .substr(1)
          .split("")
          .map(function (s) {
            return 0x11 * parseInt(s, 16);
          })
        : [hexStr.substr(1, 2), hexStr.substr(3, 2), hexStr.substr(5, 2)].map(
          function (s) {
            return parseInt(s, 16);
          }
        );
    },
    getColor (hexStr) {
      return hexStr.length === 4
        ? hexStr
          .substr(1)
          .split("")
          .map(function (s) {
            return 0x11 * parseInt(s, 16);
          })
        : [hexStr.substr(1, 2), hexStr.substr(3, 2), hexStr.substr(5, 2)].map(
          function (s) {
            return parseInt(s, 16);
          }
        );
    },
    pad (s) {
      return s.length === 1 ? "0" + s : s;
    },
    gradientColors (start, end, steps, gamma) {
      var i,
        j,
        ms,
        me,
        output = [],
        so = [];
      gamma = gamma || 1;
      var normalize = function (channel) {
        return Math.pow(channel / 255, gamma);
      };
      start = this.parseColor(start).map(normalize);
      end = this.parseColor(end).map(normalize);
      for (i = 0; i < steps; i++) {
        ms = i / (steps - 1);
        me = 1 - ms;
        for (j = 0; j < 3; j++) {
          so[j] = this.pad(
            Math.round(
              Math.pow(start[j] * me + end[j] * ms, 1 / gamma) * 255
            ).toString(16)
          );
        }
        output.push("#" + so.join(""));
      }
      return output;
    },
    calcLegendStep (min, max, alignToOrigin = true) {
      var _min = parseFloat(min);
      var _max = parseFloat(max);
      if (alignToOrigin && _min > 0) {
        _min = 0;
      }
      if (alignToOrigin && _max < 0) {
        _max = 0;
      }
      var _distance = (_max - _min).toExponential().split("e");
      var _unit = Math.pow(10, _distance[1]);
      if (_distance[0] <= 2.5) {
        _unit *= 0.5;
      } else if (_distance[0] > 6) {
        _unit *= 2;
      }
      if (_unit > 20) {
        _unit = 20;
      }
      if (_min % _unit !== 0) {
        if (_min < 0) {
          _min -= _unit;
        }
        _min -= _min % _unit;
      }
      if (_max % _unit !== 0) {
        if (_max > 0) {
          _max += _unit;
        }
        _max -= _max % _unit;
      }
      var steps = (_max - _min) / _unit;
      var stepInfo = [];
      for (var i = 0; i <= steps; i++) {
        var val = _min + _unit * i;
        if (
          (i == 0 && val == min) ||
          (i == steps && val == max) ||
          (i > 0 && i < steps)
        )
          stepInfo.push(parseFloat(val.toFixed(2)));
      }
      var result = {
        min: _min,
        max: _max,
        unit: _unit,
        stepInfo: stepInfo,
      };
      this.mapStepInfo = result;
    },
    initListData () {
      this.climateRegion = this.climateRegionList[0];
      this.climateIndicator = this.climateIndicatorList[0];
      this.climateScenario = this.climateScenarioList[0];
    },
    initParam () {
      var companyRegion = this.model.CompanyRegion[0];
      this.climateRegion = this.climateRegionList.find(
        (r) => r.name == companyRegion
      );
      // this.climateRegion = this.climateRegionList.find((r) => r.value == "CHN");
      // this.climateRegion = this.climateRegionList[3];
      this.climateIndicator = this.climateIndicatorList[0];
      this.climateScenario = this.climateScenarioList[0];
      this.getCompanyAddrList();
    },
    getCompanyAddrList () {
      if (this.model) {
        var addrList = [];
        var companyObj = this.model;
        var loanCoordList =
          companyObj.LoanCoordinate == null
            ? []
            : companyObj.LoanCoordinate.split(",");
        if (loanCoordList.length > 0) {
          addrList.push({
            region: companyObj.LoanRegion[0],
            city: companyObj.LoanCity[0],
            coordinate: [
              parseFloat(loanCoordList[0]),
              parseFloat(loanCoordList[1]),
            ],
          });
        }
        var cmpCoordList =
          companyObj.CompanyCoordinate == null
            ? []
            : companyObj.CompanyCoordinate.split(",");
        if (cmpCoordList.length > 0) {
          addrList.push({
            region: companyObj.CompanyRegion[0],
            city: companyObj.CompanyCity[0],
            coordinate: [
              parseFloat(cmpCoordList[0]),
              parseFloat(cmpCoordList[1]),
            ],
          });
        }
        var collateralCoordList =
          companyObj.CollateralCoordinate == null
            ? []
            : companyObj.CollateralCoordinate.split(",");
        if (collateralCoordList.length > 0) {
          addrList.push({
            region: companyObj.CollateralRegion[0],
            city: companyObj.CollateralCity[0],
            coordinate: [
              parseFloat(collateralCoordList[0]),
              parseFloat(collateralCoordList[1]),
            ],
          });
        }
        this.companyCoordList = addrList;
      } else {
        console.log("company_obj is null");
      }
    },
  },
  watch: {},
  mounted () {
    let _self = this;
    _self.bus.$on("showPage", (page) => {
      if (page == _self.pageCode) {
        _self.schema.show = true;

        _self.importMapBoxJS();
        _self.initParam();
        _self.importgeojsondata();
        if (_self.tab == "tab_transition") {
          this.$nextTick(function () {
            this.bus.$emit("chartInit");
          });
        }
      } else {
        _self.schema.show = false;
      }

    });
    if (_self.schema.show) {
      _self.importMapBoxJS();
      _self.initParam();
      _self.importgeojsondata();
    }


  },
};
</script>
<style  scoped>
.process2 {
  height: calc(100vh - 159px - 74px) !important;
  max-height: calc(100vh - 159px - 74px) !important;
  /* padding: 0px 20px; */
  overflow-y: auto;
  overflow: auto;
  /* margin: 0 15px 10px 0; */
}

.process2 .echart-container .search-icon {
  padding-left: 30px;
  height: 100px;
  line-height: 140px;
  display: flex;
  float: left;
}

.chartsdom {
  width: calc(100%) - 20 !important;
  height: 600px;
  padding-bottom: 30px;
  margin-left: 15px;
  margin-right: 15px;
}

.chart-descrip > span,
.chart-descrip-bottom > span {
  font-size: 16px;
}

.chart-descrip > h4 {
  font-size: 16px;
  color: #000;
}

.chart-descrip,
.chart-descrip-bottom {
  background-color: #f2f2f2;
  margin: 3px 10px;
  padding: 5px 15px;
  width: 100%;
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

.map-descrip-title {
  display: flex;
  justify-content: left;
  vertical-align: middle;
  margin-left: 10px;
}

.map-descrip-title > p {
  text-align: center;
  font-size: 18px;
  font-weight: 700;
  line-height: 40px;
  padding-top: 15px;
  margin-left: 10px;
}

.chart-descrip-title > p {
  text-align: center;
  font-size: 18px;
  font-weight: 700;
  line-height: 40px;
  padding-top: 15px;
}

.left {
  margin: 0 10px;
}

.mapboxgl-ctrl-bottom-left {
  display: none;
}

.mapboxgl-ctrl-bottom-right {
  display: none;
}

.legendTick {
  position: absolute;
  transform: translateX(-50%);
  font-size: 0.75rem;
  color: #73777c;
  top: 40px;
}

.line:hover {
  opacity: 1;
}

.line-modular {
  width: calc(100% - 10px) !important;
}

.newinfo {
  font-size: 14px;
  padding-left: 5px;
  padding-right: 5px;
  color: #fff;
}

.nochart-text {
  text-align: center;
  margin-top: 200px;
  font-weight: bold;
}

.theme--light.v-tabs-items {
  box-shadow: none !important;
}
.v-tabs.title-tab span {
  font-size: 1rem !important;
}

.title-tab .v-tab--active i.v-icon {
  color: #d04a02;
}

.title-tab .v-tabs-slider-wrapper {
  min-width: 335px !important;
  height: 3px !important;
}

.title-tab a.v-tab {
  width: 335px;
}
</style>