<template>
  <div>
    <div style="float: right; padding-bottom: 30px">
      <v-btn
        outlined
        :loading="loading"
        class="bc-upload-btn"
        @click="uploadClick()"
        >Upload to block chain</v-btn
      >
    </div>
    <!-- <loading id="bc_loading" v-show="showLoading"></loading> -->
  </div>
</template>

<script>
export default {
  props: {
    uploadType: String,
  },
  data() {
    return {
      //   loading: {
      //     component: "loading",
      //     name: "loading",
      //   },
      showLoading: false,
    };
  },
  methods: {
    uploadClick() {
      if(!(this.model.CompanyName && this.model.CompanyRegion && this.model.LoanValue && this.model.TotalAssets)){
          return
      }
      this.showLoading = true;
      var timestamp = new Date().getTime();
      var hc = this.genHashCode(timestamp);
      this.upload_blockchain(hc, timestamp);
    },
    genHashCode(str) {
      var hash = 0;
      var len = str.length;
      for (var i = 0; i < len; i++) {
        var character = str.charCodeAt(i);
        hash = (hash << 5) - hash + character;
        // hash = hash & hash; // Convert to 32bit integer
        hash |= 0;
      }
      return hash;
    },
    upload_blockchain(hashCode, timestamp) {     
      let _self = this;
      let dataParam = {
        _id: _self.model._id,
        CompanyHashCode: hashCode,
        CompanyTimestamp: timestamp,
      };
      var hcId = "CompanyHashCode";
      var tsId = "CompanyTimestamp";
      if (this.uploadType == "PD") {
        dataParam = {
          _id: _self.model._id,
          PDHashCode: hashCode,
          Timestamp: timestamp,
        };
        hcId = "PDHashCode";
        tsId = "PDTimestamp";
      }
      let newdata = {
        autoCreate: true,
        message: "Create By G20 API",
        data: dataParam,
        pageCode: "loanapplication",
        docId: _self.model._id,
      };
      _self.callApi("UpdateDoc", newdata).then((data) => {
        _self.model.CompanyHashCode = hashCode;
        _self.model.CompanyTimestamp = timestamp;
        var hcDiv = document.getElementById(hcId);
        var tsDiv = document.getElementById(tsId);
        if (hcDiv) {
          hcDiv.innerText = hashCode;
        }
        if (tsDiv) {
          tsDiv.innerText = timestamp;
        }
        this.showLoading = false;
      });
    },
  },
  created() {},
};
</script>
<style>
.bc-upload-btn {
  margin-right: 10px;
  background-color: #d04a02;
  color: #fff !important;
  font-size: 18px !important;
}
</style>