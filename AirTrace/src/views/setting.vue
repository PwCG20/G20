<template>
  <div class="st-wrapper">
    <div
      id="help-banner"
      :style="{
        background:
          'url(' +
          getResource('help_banner.png') +
          ') center center no-repeat !important',
      }"
    >
      <div class="help-box-width">
        <span>Settings</span>
      </div>
    </div>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-container>
        <v-row>
          <v-col cols="12" md="12">
            <div>
              <span class="st-type-title"
                >Setting the thresholds for the risk assessment
              </span>
            </div>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="12">
            <div>
              <span class="st-type-title-desc"
                >Probability of default thresholds: </span
              ><span style="padding-left: 5px; font-size: 15px"
                >Please adjust the thresholds of tolerance to the change in
                probability of default as a result of climate-related risks, or
                use the default setting.
              </span>
            </div>
          </v-col>
        </v-row>
        <v-row style="text-align: center">
          <v-col cols="2"
            ><span class="st-threshold-tbl-title">Threshold</span></v-col
          >
          <v-col cols="4"></v-col>
          <v-col cols="2"
            ><span class="st-threshold-tbl-title">Change in PD</span></v-col
          >
          <v-col cols="4"
            ><span class="st-threshold-tbl-title"
              >Recommended actions to loan assessors</span
            ></v-col
          >
        </v-row>
        <v-row style="text-align: center">
          <v-col>
            <v-row class="st-row">
              <v-col cols="2">
                <div>Low</div>
              </v-col>
              <v-col cols="4">
                <v-slider
                  class="st-slider"
                  max="100"
                  min="0"
                  :step="threshlodStep"
                  :color="lineColor"
                  :thumb-color="thumbColor"
                  thumb-label
                  v-model="settingData.PDThresholdsFrom"
                >
                  <template v-slot:prepend>
                    <v-icon :color="lineColor" @click="decrement('low')">
                      mdi-minus
                    </v-icon>
                    <span style="padding-left: 10px">0</span>
                  </template>
                  <template v-slot:append>
                    <span>100</span>
                    <v-icon
                      style="padding-left: 10px"
                      :color="lineColor"
                      @click="increment('low')"
                    >
                      mdi-plus
                    </v-icon>
                  </template>
                </v-slider>
              </v-col>
              <v-col cols="2">
                <span>&lt; {{ settingData.PDThresholdsFrom }}%</span>
              </v-col>
              <v-col cols="4">
                <!-- <span>No action required</span> -->
                <v-text-field
                  v-model="settingData.PDThresholdsActionLow"
                  label=""
                  clearable
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row class="st-row">
              <v-col cols="2">
                <div>Medium</div>
              </v-col>
              <v-col cols="4">
                <v-slider
                  class="st-slider"
                  max="100"
                  :min="settingData.PDThresholdsFrom"
                  :step="threshlodStep"
                  :color="lineColor"
                  :thumb-color="thumbColor"
                  thumb-label
                  v-model="settingData.PDThresholdsTo"
                >
                  <template v-slot:prepend>
                    <v-icon :color="lineColor" @click="decrement('medium')">
                      mdi-minus
                    </v-icon>
                    <span style="padding-left: 10px">{{
                      settingData.PDThresholdsFrom
                    }}</span>
                  </template>
                  <template v-slot:append>
                    <span>100</span>
                    <v-icon
                      style="padding-left: 10px"
                      :color="lineColor"
                      @click="increment('medium')"
                    >
                      mdi-plus
                    </v-icon>
                  </template>
                </v-slider>
              </v-col>
              <v-col cols="2">
                <span
                  >{{ settingData.PDThresholdsFrom }}% -
                  {{ settingData.PDThresholdsTo }}%
                </span>
              </v-col>
              <v-col cols="4">
                <!-- <span>Refer to safeguards on climate risks</span> -->
                <v-text-field
                  v-model="settingData.PDThresholdsActionMedium"
                  label=""
                  clearable
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row class="st-row">
              <v-col cols="2">
                <div>High</div>
              </v-col>
              <v-col cols="4">
                <v-slider
                  class="st-slider"
                  max="100"
                  min="0"
                  :step="threshlodStep"
                  :color="lineColor"
                  thumb-color="grey"
                  thumb-label
                  v-model="settingData.PDThresholdsTo"
                  readonly
                >
                  <template v-slot:prepend>
                    <span>0</span>
                  </template>
                  <template v-slot:append>
                    <span>100</span>
                  </template>
                </v-slider>
              </v-col>
              <v-col cols="2">
                <span>&gt; {{ settingData.PDThresholdsTo }}% </span>
              </v-col>
              <v-col cols="4">
                <!-- <span>Refer to Risk Committee</span> -->
                <v-text-field
                  v-model="settingData.PDThresholdsActionHigh"
                  label=""
                  clearable
                ></v-text-field>
              </v-col>
            </v-row>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12" md="12">
            <div>
              <span class="st-type-title"
                >Monitoring of portfolio carbon intensity and decarbonisation
                targets
              </span>
            </div>
          </v-col>
        </v-row>
        <v-row style="padding-left: 20px">
          <v-col cols="12" md="2">
            <div class="st-select">Metric to monitor</div>
          </v-col>
          <v-col cols="12" md="10">
            <v-select
              v-model="settingData.Metric"
              :items="monitorList"
              item-text="Name"
              item-value="Value"
              persistent-hint
              outlined
              dense
            ></v-select>
          </v-col>
        </v-row>
        <v-row style="padding-left: 20px">
          <v-col cols="12" md="12">
            <div>Target carbon intensity of portfolio</div>
            <v-col>
              <v-row class="st-row-carbon">
                <v-col cols="5" style="text-align: left">Base Year:</v-col>
                <v-col cols="5" style="text-align: center">
                  <v-slider   
                    class="st-slider-carbon"                 
                    max="2025"
                    min="2000"
                    :step="yearStep"
                    :color="lineColor"
                    :thumb-color="thumbColor"
                    thumb-label
                    v-model="settingData.CarbonIntensityBaseYear"
                  >
                    <template v-slot:prepend>
                      <v-icon
                        :color="lineColor"
                        @click="decrement('base_year')"
                      >
                        mdi-minus
                      </v-icon>
                      <span style="padding-left: 10px">2000</span>
                    </template>
                    <template v-slot:append>
                      <span>2025</span>
                      <v-icon
                        style="padding-left: 10px"
                        :color="lineColor"
                        @click="increment('base_year')"
                      >
                        mdi-plus
                      </v-icon>
                    </template>
                  </v-slider>
                </v-col>
                <v-col cols="2" style="text-align: left">{{
                  settingData.CarbonIntensityBaseYear
                }}</v-col>
              </v-row>
              <v-row class="st-row-carbon">
                <v-col cols="5" style="text-align: left">Target Year: </v-col>
                <v-col cols="5" style="text-align: center">
                  <v-slider   
                    class="st-slider-carbon"                 
                    max="2050"
                    min="2025"
                    :step="yearStep"
                    :color="lineColor"
                    :thumb-color="thumbColor"
                    thumb-label
                    v-model="settingData.CarbonIntensityTargetYear"
                  >
                    <template v-slot:prepend>
                      <v-icon
                        :color="lineColor"
                        @click="decrement('target_year')"
                      >
                        mdi-minus
                      </v-icon>
                      <span style="padding-left: 10px">2025</span>
                    </template>
                    <template v-slot:append>
                      <span>2050</span>
                      <v-icon
                        style="padding-left: 10px"
                        :color="lineColor"
                        @click="increment('target_year')"
                      >
                        mdi-plus
                      </v-icon>
                    </template>
                  </v-slider>
                </v-col>
                <v-col cols="2" style="text-align: left">{{
                  settingData.CarbonIntensityTargetYear
                }}</v-col>
              </v-row>
              <v-row class="st-row-carbon">
                <v-col cols="5" style="text-align: left">Carbon reduction required from base year to target year: </v-col>
                <v-col cols="5" style="text-align: center">
                  <v-slider   
                    class="st-slider-carbon"                 
                    max="100"
                    min="0"
                    :step="threshlodStep"
                    :color="lineColor"
                    :thumb-color="thumbColor"
                    thumb-label
                    v-model="settingData.CarbonReduction"
                  >
                    <template v-slot:prepend>
                      <v-icon
                        :color="lineColor"
                        @click="decrement('carbon_reduction')"
                      >
                        mdi-minus
                      </v-icon>
                      <span style="padding-left: 10px">0</span>
                    </template>
                    <template v-slot:append>
                      <span>100</span>
                      <v-icon
                        style="padding-left: 10px"
                        :color="lineColor"
                        @click="increment('carbon_reduction')"
                      >
                        mdi-plus
                      </v-icon>
                    </template>
                  </v-slider>
                </v-col>
                <v-col cols="2" style="text-align: left">{{
                  settingData.CarbonReduction
                }}%</v-col>
              </v-row>
            </v-col>
          </v-col>
          <!-- <v-col cols="12" md="10">
            <v-select
              v-model="settingData.TargetType"
              :items="targetTypeList"
              item-text="Name"
              item-value="Value"
              outlined
              dense
            ></v-select>
          </v-col> -->
        </v-row>
        <v-row>
          <v-col>
            <v-btn outlined :loading="loading" class="st-save-btn" @click="save"
              >Save</v-btn
            >
            <v-btn
              outlined
              :loading="loading"
              class="st-save-btn"
              style="padding-left: 10px"
              @click="reset"
              >Restore to Default Setting</v-btn
            >
          </v-col>
        </v-row>
        <v-dialog v-model="alertShow" persistent max-width="250px">
          <v-card>
            <v-card-text style="padding: 15px 10px 10px 10px"
              >Save successfully!</v-card-text
            >
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn text @click="alertShow = false">Close</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-container>
    </v-form>
  </div>
</template>

<script>
export default {
  name: "",
  components: {},
  props: {},
  data() {
    return {
      valid: true,
      threshold: "",
      monitor: "",
      monitorList: [
        {
          id: 1,
          Name: "Weighted Average Carbon Intensity of portfolio",
          Value: "WACI",
          Desc: "WACI unit: loan applicants’ carbon-to-revenue x US$ loan value / total portfolio US $ loan value [option to change base currency and units (thousands/millions)]",
        },
        {
          id: 2,
          Name: "Carbon-to-Revenue",
          Value: "C/R",
          Desc: "C/R: tCO2 of loan applicants’ emissions / US$ loan applicants’ revenue [option to change base units (thousands/millions)]",
        },
        {
          id: 3,
          Name: "Carbon-to-Value",
          Value: "C/V",
          Desc: "C/V: tCO2 of loan applicants’ emissions / total portfolio US$ loan value [option to change base units (thousands/millions)]",
        },
      ],
      targetType: "",
      targetTypeList: [
        {
          id: 1,
          Name: "Carbon intensity unit: WACI or Carbon-to-Value",
          Value: "Carbon intensity unit: WACI or Carbon-to-Value",
        },
        { id: 2, Name: "Base year", Value: "Base year" },
        { id: 3, Name: "Target year", Value: "Target year" },
        {
          id: 4,
          Name: "Carbon intensity reduction target from base year to target year",
          Value:
            "Carbon intensity reduction target from base year to target year",
        },
      ],
      settingData: {
        Metric: "C/V",
        PDThresholdsFrom: "0.5",
        PDThresholdsTo: "2",
        PDThresholdsActionLow: "No action required",
        PDThresholdsActionMedium: "Refer to safeguards on climate risks",
        PDThresholdsActionHigh: "Refer to Risk Committee",
        CarbonIntensityBaseYear: "2021",
        CarbonIntensityTargetYear: "2030",
        CarbonReduction: "50",
      },
      threshlodStep: 0.01,
      yearStep: 1,
      lineColor: "#4dacf1",
      thumbColor: "#feb791",
      alertShow: false,
    };
  },
  watch: {},
  computed: {},
  methods: {
    initParam() {},
    getSetting() {
      let _self = this;
      var requestPara = {
        pageCode: "settings",
        searchItems: [],
        order: {},
        columns: [],
        withSocialStatus: false,
        index: 1,
        size: 1,
      };
      _self.callApi("GetDocs", requestPara).then((data) => {
        console.log("setting: ", data);
        _self.settingData = data.data.items[0];
        // _self.pdThresholdsFrom = _self.settingData.PDThresholdsFrom;
        // _self.pdThresholdsTo = _self.settingData.PDThresholdsTo;
      });
    },
    decrement(tType) {
      // debugger
      switch (tType) {
        case "low":
          this.settingData.PDThresholdsFrom -= this.threshlodStep;
          break;
        case "medium":
          this.settingData.PDThresholdsFrom -= this.threshlodStep;
          break;
        case "base_year":
          this.settingData.CarbonIntensityBaseYear -= this.yearStep;
          break;
        case "target_year":
          this.settingData.CarbonIntensityTargetYear -= this.yearStep;
          break;
        case "carbon_reduction":
          this.settingData.CarbonReduction -= this.threshlodStep;
          break;
      }
    },
    increment(tType) {
      switch (tType) {
        case "low":
          this.settingData.PDThresholdsFrom += this.threshlodStep;
          break;
        case "medium":
          this.settingData.PDThresholdsFrom += this.threshlodStep;
          break;
        case "base_year":
          this.settingData.CarbonIntensityBaseYear += this.yearStep;
          break;
        case "target_year":
          this.settingData.CarbonIntensityTargetYear += this.yearStep;
          break;
        case "carbon_reduction":
          this.settingData.CarbonReduction += this.threshlodStep;
          break;
      }
    },
    save() {
      this.updateSetting();
    },
    reset() {
      this.settingData.PDThresholdsFrom = 0.5;
      this.settingData.PDThresholdsTo = 2.0;
      this.settingData.PDThresholdsActionLow = "No action required";
      this.settingData.PDThresholdsActionMedium = "Refer to safeguards on climate risks";
      this.settingData.PDThresholdsActionHigh = "Refer to Risk Committee";
      this.updateSetting();
    },
    updateSetting() {
      var _self = this;
      let newdata = {
        autoCreate: true,
        message: "Create By G20 API",
        data: _self.settingData,
        pageCode: "settings",
        docId: _self.settingData._id,
      };
      _self.callApi("UpdateDoc", newdata).then((data) => {
        console.log("update_setting_data", data);
        // debugger;
        if (data.statusCode == 200) {
          _self.alertShow = true;
        }
      });
    },
  },
  created() {
    this.getSetting();
  },
  mounted() {},
};
</script>
<style>
#help-banner {
  position: relative;
  height: 260px;
}
.help-box-width {
  margin: 0 auto;
  width: calc(100% - 200px);
}
#help-banner span {
  padding: 15px 25px;
  width: 180px;
  background-color: #ffb600;
  position: absolute;
  top: 45px;
  font-size: 30px;
  font-weight: bold;
  text-align: center;
}
.st-type-title {
  font-size: 20px !important;
  font-weight: bold;
}

.st-type-title-desc {
  font-size: 18px !important;
  font-weight: bold;
  padding-left: 20px;
}
.st-wrapper {
  font-size: 16px;
  font-family: "Helvetica Neue" !important;
}
.st-save-btn {
  float: right;
  background-color: #d04a02;
  color: #fff !important;
  font-size: 18px !important;
}
.st-row {
  line-height: 70px;
}
.st-row-carbon {
  line-height: 40px;
}
.st-select {
  line-height: 50px;
}
.st-threshold-tbl-title {
  font-weight: bold;
  font-size: 15px;
}
.st-slider {
  width: 380px;
  padding-top: 20px;
  /* float: left; */
}
.st-slider-carbon {
  width: 380px;
  padding-top: 5px;
}
.st-slider span {
  line-height: 24px;
}
</style>