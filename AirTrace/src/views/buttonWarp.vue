
<template>
  <div class="content-footer">
    <div class="progress-wrap">
      <div class="default-progress">
        <div class="real-progress"></div>
      </div>
      <div class="progress-info">1/2</div>
    </div>
    <div class="button-wrap">
      <div
        v-show="currentPage == 1 || currentPage == 4"
        @click="uploadBlockChainClick()"
        class="default-button default-button-next uploadBC-btn"
      >
        Upload to Blockchain
      </div>
      <div
        v-show="currentPage != 1"
        @click="prevClick()"
        class="default-button mar-10"
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="11.746"
          height="19.845"
          viewBox="0 0 11.746 19.845"
          class="button-previous-icon"
        >
          <defs></defs>
          <path
            d="M.162.149a.865.865,0,0,1,.974,0L11.746,9.9,1.137,19.745a.7.7,0,0,1-.433.1.87.87,0,0,1-.541-.1.7.7,0,0,1,0-.9L9.8,9.9.162,1.044a.7.7,0,0,1,0-.9"
            class="a"
          ></path>
        </svg>
        Previous
      </div>
      <div
        v-show="currentPage != 4"
        @click="nextClick()"
        class="default-button default-button-next"
      >
        Next
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="11.746"
          height="19.845"
          viewBox="0 0 11.746 19.845"
          class="button-next-icon"
        >
          <defs></defs>
          <path
            d="M.162.149a.865.865,0,0,1,.974,0L11.746,9.9,1.137,19.745a.7.7,0,0,1-.433.1.87.87,0,0,1-.541-.1.7.7,0,0,1,0-.9L9.8,9.9.162,1.044a.7.7,0,0,1,0-.9"
            class="a"
          ></path>
        </svg>
      </div>
      <div
        v-show="currentPage == 4"
        @click="homeClick()"
        class="default-button default-button-next"
      >
        Home
      </div>
    </div>
  </div>
</template>
<script> 
export default {
  inject: {
    vcForm: {
      default: {
        validate () { },
        setButtonType () { },
      },
    },
  },
  data () {
    return {
      currentPage: 1,
      alreadySave: false,
      addressData: [],
      orignalModel: null,
      orignalGHGEmissions: "",
      orignalElectricityUse: "",
      orignalSector: "",
      orignalLoanValue: "",
      orignalRegion: "",
      saveModel: {},
    };
  },
  methods: {
    prevClick () {
      this.currentPage = this.currentPage > 1 ? this.currentPage - 1 : 1;
      this.showPageLoading();
      this.SyncCurrentPageStatus();
    },
    nextClick () {
      if (!this.vcForm.validate()) {
        return;
      }
      this.showPageLoading();
      var calcTransitionRisk = false;
      var calcPDChart = false;
      //check whether to re-calc transition risk chart
      if (
        this.orignalModel["GHGEmissions"] != this.model["GHGEmissions"] ||
        this.orignalModel["ElectricityUse"] != this.model["ElectricityUse"] ||
        this.orignalModel["LoanValue"] != this.model["LoanValue"] ||
        this.orignalModel["CollateralAssetValue"] != this.model["CollateralAssetValue"] ||
        this.orignalModel["Revenue"] != this.model["Revenue"] ||
        this.orignalModel["EBIT"] != this.model["EBIT"] ||
        this.orignalModel["TotalAssets"] != this.model["TotalAssets"] ||
        this.orignalModel["TotalLiabilities"] != this.model["TotalLiabilities"] ||
        this.orignalModel["NetAssetValue"] != this.model["NetAssetValue"] ||
        this.orignalModel["NetIncome"] != this.model["NetIncome"] ||
        this.orignalModel["CurrentAssets"] != this.model["CurrentAssets"] ||
        this.orignalModel["CurrentLiabilities"] != this.model["CurrentLiabilities"] ||
        this.orignalModel["GHGEmissions"] != this.model["GHGEmissions"] ||
        this.orignalModel["ElectricityUse"] != this.model["ElectricityUse"] ||
        (this.orignalModel["Sector"] != null &&
          this.orignalModel["Sector"][0] != this.model["Sector"][0])
      ) {
        calcTransitionRisk = true;
      }
      //check whether to re-calc PD chart
      if (
        this.orignalModel["GHGEmissions"] != this.model["GHGEmissions"] ||
        (this.orignalModel["Sector"] != null &&
          this.orignalModel["Sector"][0] != this.model["Sector"][0]) ||
        this.orignalModel["LoanValue"] != this.model["LoanValue"]
      ) {
        calcPDChart = true;
      }

      if (this.currentPage == 1) {
        this.customSave();
        if (calcTransitionRisk) {
          this.callCustomApi_cleantransitionriskreport();
          this.callCustomApi_transitionrisk();
        }
        if (calcPDChart) {
          this.callCustomApi_process();
        }
      } else if (this.currentPage == 2) {
      }
      this.currentPage = this.currentPage < 4 ? this.currentPage + 1 : 4;
      this.SyncCurrentPageStatus();
    },
    showPageLoading () {
      var loadingDiv = document.getElementById("loading");
      if (loadingDiv) {
        loadingDiv.style.display = "block";
      }
      setTimeout(() => {
        loadingDiv.style.display = "none";

      }, 2000);
    },
    loadAddress () {
      let _self = this;
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
      _self.callApi("GetDocs", requestPara).then((data) => {
        let newData = data.data;
        _self.addressData = newData.items;
      });
    },
    getLoadISO3 (region) {
      var _self = this;
      var arr = [];
      if (_self.addressData.length > 0) {
        arr = _self.addressData;
      } else {
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
        _self.callApi("GetDocs", requestPara).then((data) => {
          let newData = data.data;
          _self.addressData = newData.items;
          arr = _self.addressData;
        });
      }
      var regionItem = arr.find((item) => {
        return item.Name == region;
      });
      if (regionItem == undefined) return "";
      return "Region" in regionItem ? regionItem.Region : "";
    },
    homeClick () {
      window.location.href = "/g20/AirTrace/";
    },
    showRightForm () {
      if (this.currentPage == 1 || this.currentPage > 4) {
        document
          .getElementsByClassName("right-form-content-module")[0]
          .removeAttribute("style");
      } else {
        document
          .getElementsByClassName("right-form-content-module")[0]
          .setAttribute("style", "display:none");
      }
    },
    SyncCurrentPageStatus () {
      this.bus.$emit("showPage", this.currentPage);
      this.showRightForm();
      this.bus.$emit("watchCurrentPageStatus", this.currentPage);
    },
    callCustomApi_process () {
      let _self = this;
      var requestPara = {
        id: "610a51549549b40001cfabee",
        parameter: {
          LoanAppID: _self.model._id,
          Company: _self.model["CompanyName"],
          Sector: _self.model["Sector"][0]["SectorID"],
          CountryISO3: _self.model["CompanyISO3"],
          LoanValue: _self.model["LoanValue"].replaceAll(",", ""),
          GHGEmission: _self.model["GHGEmissions"].replaceAll(",", ""),
        },
        fileName: "",
      };
      _self.callApi("CallCustomiseAPI", requestPara).then((data) => {
        let newData = data.data;
      });
    },
    callCustomApi_transitionrisk () {
      let _self = this;
      var requestPara = {
        id: "610a50b09549b40001cfabe4",
        parameter: {
          LoanAppID: _self.model._id,
          Scenario: "Below 2oC",
          Region: _self.model.CompanyISO3,
        },
        fileName: "",
      };
      _self.callApi("CallCustomiseAPI", requestPara).then((data) => {
        let newData = data.data;
      });
    },
    callCustomApi_cleantransitionriskreport () {
      let _self = this;
      var requestPara = {
        id: "611215917855e50001427fc6",
        parameter: {
          Company: _self.model["CompanyName"],
        },
        fileName: "",
      };
      _self.callApi("CallCustomiseAPI", requestPara).then((data) => {
        let newData = data.data;
      });
    },
    deleteDraftField () {
      let _self = this;
      delete _self.model.pageleftcomponent;
      delete _self.model.buttonwrap;
      delete _self.model.undefined;
      delete _self.model.vcc_process2;
      delete _self.model.vcc_process3;
      delete _self.model.vcc_companyname;
      delete _self.model.vcc_applicationinfo;
      Object.keys(_self.model).map((m) => {
        if (m.indexOf("Ng_") != -1 && m != "Ng_ConcurrencyStamp") {
          delete _self.model[m];
        }
      });
    },
    updateDraftField () {
      let _self = this;
      Object.keys(_self.saveModel).map((m) => {
        if (m.indexOf("bck_") != -1 && m != "Ng_ConcurrencyStamp") {
          _self.saveModel[m.replace("bck_", "")] = _self.saveModel[
            m.replace("bck_", "")
          ].replaceAll(",", "");
          delete _self.saveModel[m];
        }
      });
    },
    getCoordinate (region, city) {
      let _self = this;
      let coordinate = "";
      let regionObj = _self.addressData.filter(function (item) {
        return item.Name == region;
      });
      if (regionObj && regionObj.length > 0) {
        let cityArr = regionObj[0].Items;
        let cityObj = cityArr.filter(function (item) {
          var jsonitem = JSON.parse(item);
          return jsonitem.Name == city;
        });
        coordinate = cityObj ? JSON.parse(cityObj).Coordinate.join(",") : "";
      }
      return coordinate;
    },
    customSave () {
      let _self = this;
      _self.deleteDraftField();
      if (!_self.model["Stage"]) {
        _self.model["Stage"] = "Draft";
      }
      _self.model["CompanyISO3"] = _self.getLoadISO3(
        _self.model["CompanyRegion"]
      );
      _self.model["Owner"] = _self.$store.state.userInfo.staffName || "";
      if (!_self.model["RiskAssessment"]) {
        _self.model["RiskAssessment"] = 0;
      }
      if (!_self.model["PD"]) {
        _self.model["PD"] = "";
      }
      _self.model["CompanyCoordinate"] = _self.getCoordinate(
        _self.model["CompanyRegion"],
        _self.model["CompanyCity"]
      );
      _self.model["LoanCoordinate"] = _self.getCoordinate(
        _self.model["LoanRegion"],
        _self.model["LoanCity"]
      );

      _self.model["LoanISO3"] = _self.getLoadISO3(_self.model["LoanRegion"]);
      _self.model["CollateralCoordinate"] = _self.getCoordinate(
        _self.model["CollateralRegion"],
        _self.model["CollateralCity"]
      );

      _self.model["CollateralISO3"] = _self.getLoadISO3(
        _self.model["CollateralRegion"]
      );
      _self.refreshMap();

      _self.saveModel = JSON.parse(JSON.stringify(_self.model));
      _self.updateDraftField();
      let newdata = {
        autoCreate: true,
        message: "Create By G20 API",
        data: _self.saveModel,
        pageCode: "loanapplication",
        docId: _self.model._id,
      };
      _self.callApi("UpdateDoc", newdata).then((data) => {
        _self.alreadySave = true;
        //update cached company data
        _self.orignalModel = JSON.parse(JSON.stringify(_self.model));
      });
    },
    showLoading (showFlag) {
      var loadingDiv = document.getElementById("upload-loading");
      if (loadingDiv) {
        window.updateLoading();
        loadingDiv.style.display = showFlag ? "block" : "none";

      }
    },
    uploadBlockChainClick () {
      // this.showLoading = true;
      this.showLoading(true);
      this.customSave();
      var timestamp = new Date().getTime();
      // var objStr = JSON.stringify(this.saveModel);
      var hc = this.genHashCode();
      console.log("hash_code:", hc);
      this.saveblockchain(hc, timestamp);
    },
    genHashCode () {
      var ar = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
      ];
      var hs = [];
      var hl = Number(64);
      var al = ar.length;
      for (var i = 0; i < hl; i++) {
        hs.push(ar[Math.floor(Math.random() * al)]);
      }

      return hs.join("");
    },
    saveblockchain (hashCode, timestamp) {
      let _self = this;
      let dataParam = {
        _id: _self.model._id,
        CompanyHashCode: hashCode,
        CompanyTimestamp: timestamp,
      };
      if (_self.currentPage == 4) {
        dataParam = {
          _id: _self.model._id,
          PDHashCode: hashCode,
          PDTimestamp: timestamp,
        };
      }
      let newdata = {
        autoCreate: true,
        message: "Create By G20 API",
        data: dataParam,
        pageCode: "loanapplication",
        docId: _self.model._id,
      };
      _self.callApi("UpdateDoc", newdata).then((data) => {
        if (_self.currentPage == 1) {
          _self.model.CompanyHashCode = hashCode;
          _self.model.CompanyTimestamp = timestamp;
          _self.saveModel.CompanyHashCode = hashCode;
          _self.saveModel.CompanyTimestamp = timestamp;
        } else {
          _self.model.PDHashCode = hashCode;
          _self.model.PDTimestamp = timestamp;
          _self.saveModel.PDHashCode = hashCode;
          _self.saveModel.PDTimestamp = timestamp;
        }
      });

      if (_self.currentPage == 1) {
        _self.updateLoanAppBC(_self.saveModel);
      } else {
        _self.saveClimatePD2BlockChain();
      }
    },
    saveClimatePD2BlockChain () {
      let _self = this;
      var requestPara = {
        pageCode: "companypdData",
        searchItems: [
          {
            Method: "AND",
            Operator: "Equal",
            Name: "Company",
            Value: _self.model.CompanyName,
          },
        ],
        order: {},
        columns: [],
        withSocialStatus: false,
        index: 1,
        size: 1,
      };
      _self.callApi("GetDocs", requestPara).then((data) => {
        console.log("companypdData: ", data);
        var pddata = data.data.items[0];
        var postData = {
          _id: _self.model._id,
          Below2oCClimate: pddata.Below2oCClimate,
          CurrentPoliciesClimate: pddata.CurrentPoliciesClimate,
          DelayedTransitionClimate: pddata.DelayedTransitionClimate,
        };
        _self.updateLoanAppBC(postData);
      });
    },
    updateLoanAppBC (postData) {
      let _self = this;
      //save to block chain
      let bcdata = {
        autoCreate: true,
        message: "Create By G20 API",
        data: postData,
        pageCode: "loanappblockchain",
        docId: _self.model._id,
      };
      _self.callApi("UpdateDoc", bcdata).then((data) => {
        console.log("save to block chain: ", data);

      }).then(() => {
        setTimeout(() => {
          _self.showLoading(false);

        }, 4000);
      });
    },
    refreshMap () {
      //check whether the addresses are changed.
      if (
        this.orignalModel["CollateralCoordinate"] !=
        this.model["CollateralCoordinate"] ||
        this.orignalModel["CompanyCoordinate"] !=
        this.model["CompanyCoordinate"] ||
        this.orignalModel["LoanCoordinate"] != this.model["LoanCoordinate"]
      ) {
        this.bus.$emit("refreshMap");
      }
    },
    updateDoc () {
      _self.deleteDraftField();
      model["Status"] = "Draft";
      model["Owner"] = $store.state.userInfo.staffName;
      model["RiskAssessment"] = 0;
      _self.saveModel = JSON.parse(JSON.stringify(_self.model));
      _self.updateDraftField();
      let newdata = {
        autoCreate: true,
        message: "Create By G20 API",
        data: this.saveModel,
        pageCode: "companymanagement",
        docId: this.model._id,
      };
      this.callApi("UpdateDoc", newdata).then((data) => { });
    },
  },
  mounted () {
    let _self = this;
    _self.loadAddress();
    _self.orignalModel = JSON.parse(JSON.stringify(_self.model));
  },
};
</script>
<style>
.layout {
  padding-left: 0 !important;
}
.content-footer {
  margin-right: 20px;
  border-top: 1px solid #dedede;
  padding: 20px 0;
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.content-footer .progress-wrap {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  display: none;
}

.content-footer .progress-wrap .default-progress {
  position: relative;
  height: 5px;
  margin-right: 5px;
  width: calc(80% - 30px);
  background-color: #dedede;
}

.content-footer .progress-wrap .default-progress .real-progress {
  position: absolute;
  top: 0;
  left: 0;
  background-color: #d04a02;
  width: 20px;
  height: 5px;
}

.content-footer .progress-info {
  font-size: 14px;
}

.content-footer .button-wrap {
  padding-top: 8px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.content-footer {
  border-top: 0;
  /* border-bottom: 1px solid #dedede; */
  padding-top: 0;
  padding-bottom: 15px;
  order: 1;
}

.content-footer .button-wrap {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.button-wrap .default-button {
  background: #fff;
  min-width: 130px;
  height: 46px;
  padding: 12px 15px;
  color: #464646;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: 1px solid #707070;
  font-size: 16px;
  cursor: pointer;
}

.project-survey-container .back-button {
  padding: 12px 25px;
}

.button-wrap .default-button-next {
  color: #fff;
  background: #d04a02;
  border-color: #d04a02;
  padding: 12px 25px;
}

.uploadBC-btn {
  /* color: #fff;
  background: #d04a02;
  border-color: #d04a02;
  padding: 12px 25px; */
  float: left;
  margin-right: 20px;
}

.button-wrap .button-previous-icon {
  width: 10px;
  height: 19px;
  transform: rotate(180deg);
}

.button-wrap .button-previous-icon .a {
  fill: #7d7d7d;
  fill-rule: evenodd;
}

.button-wrap .button-next-icon {
  width: 10px;
  height: 19px;
}

.button-wrap .button-next-icon .a {
  fill: #fff;
  fill-rule: evenodd;
}

.button-wrap .loading-btn {
  font-size: 18px;
  -webkit-animation: turn-data-v-0b2f0ffe 1s linear infinite;
  animation: turn-data-v-0b2f0ffe 1s linear infinite;
}
</style>