<template>
  <div class="loan-main">
    <div class="dialog-content-left">
      <div class="content-info">
        Progress <i class="mdi mdi-close cursor-pointer"></i>
      </div>
      <div class="content-left-step">
        <div>
          <div class="single-step">
            <div
              class="step-info"
              :class="{ 'step-info-active': currentPage == 1 }"
            >
              Fill in loan info
            </div>
            <div class="step-num-wrap">
              <div class="step-num">
                <i
                  v-show="currentPage > 1"
                  class="mdi pwc_circlecheckmarkicon"
                ></i>
                <span
                  class="step-num-span"
                  :class="{ 'step-num-active': currentPage == 1 }"
                  >1</span
                >
              </div>
              <div class="after-line"></div>
            </div>
          </div>
        </div>
        <div>
          <div class="single-step">
            <div
              class="step-info"
              :class="{ 'step-info-active': currentPage == 2 }"
            >
              Climate risks dashboard
            </div>
            <div class="step-num-wrap">
              <div class="step-num">
                <i
                  v-show="currentPage > 2"
                  class="mdi pwc_circlecheckmarkicon"
                ></i>
                <span
                  class="step-num-span"
                  :class="{ 'step-num-active': currentPage == 2 }"
                  >2</span
                >
              </div>
              <div class="after-line"></div>
            </div>
          </div>
        </div>
        <div>
          <div class="single-step">
            <div
              class="step-info"
              :class="{ 'step-info-active': currentPage == 3 }"
            >
              Financial impact
            </div>
            <div class="step-num-wrap">
              <div class="step-num">
                <i
                  v-show="currentPage > 3"
                  class="mdi pwc_circlecheckmarkicon"
                ></i>
                <span
                  class="step-num-span"
                  :class="{ 'step-num-active': currentPage == 3 }"
                  >3</span
                >
              </div>
              <div class="after-line"></div>
            </div>
          </div>
        </div>
        <div>
          <div class="single-step">
            <div
              class="step-info"
              :class="{ 'step-info-active': currentPage == 4 }"
            >
              Climate risk assessment
            </div>
            <div class="step-num-wrap">
              <div class="step-num">
                <i
                  v-show="currentPage > 4"
                  class="mdi pwc_circlecheckmarkicon"
                ></i>
                <span
                  class="step-num-span"
                  :class="{ 'step-num-active': currentPage == 4 }"
                  >4</span
                >
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {
      currentPage: 1,
    };
  },
  mounted() {
    let _self = this;
    _self.bus.$on("watchCurrentPageStatus", (curPageStatus) => {
      _self.currentPage = curPageStatus;
    });
  },
};
</script>
<style>
.loan-main {
  padding-top: 64px;
  background-color: #fff;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  min-width: 290px;
  height: calc(100vh - 40px);
  width: 100%;
}

.loan-main .dialog-content-left {
  width: 15%;
  min-width: 210px;
  max-width: 280px;
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  background-color: #f5f5f5;
}

.loan-main .dialog-content-left .content-info {
  box-sizing: border-box;
  background-color: #d04a02;
  padding: 20px 25px;
  font-size: 24px;
  font-weight: 100;
  color: #fff;
  text-align: left;
  font-family: ITC Charter Com;
  line-height: 36px;
  text-align: center;
}

.loan-main .dialog-content-left .content-info i {
  display: none;
}

.loan-main .dialog-content-left .content-left-step {
  padding: 30px 20px;
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: flex-end;
}

.loan-main .dialog-content-left .content-left-step .single-step {
  display: flex;
  align-items: flex-start;
  justify-content: flex-end;
}

.loan-main .dialog-content-left .content-left-step .single-step .step-info {
  font-size: 16px;
  text-align: right;
}

.loan-main
  .dialog-content-left
  .content-left-step
  .single-step
  .step-info-active {
  font-weight: 700;
}

.loan-main
  .dialog-content-left
  .content-left-step
  .single-step
  .step-num-wrap
  i {
  color: #d04a02;
  font-size: 34px;
}

.loan-main
  .dialog-content-left
  .content-left-step
  .single-step
  .step-num-wrap
  .step-num {
  margin-left: 15px;
  position: relative;
  width: 25px;
  height: 25px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.loan-main
  .dialog-content-left
  .content-left-step
  .single-step
  .step-num-wrap
  .step-num-span {
  display: inline-block;
  width: 25px;
  height: 25px;
  border-radius: 50%;
  border-color: #d04a02;
  background-color: #fedacc;
  color: #d04a02;
  font-size: 16px;
  flex: 0 0 auto;
  text-align: center;
  line-height: 25px;
}

.loan-main
  .dialog-content-left
  .content-left-step
  .single-step
  .step-num-wrap
  .step-num-active {
  border-color: #d04a02;
  background-color: #d04a02;
  color: #fff;
}

.loan-main
  .dialog-content-left
  .content-left-step
  .single-step
  .step-num-wrap
  .after-line {
  width: 100%;
  height: 55px;
  border-right: 1px solid #d04a02;
  transform: translateX(-12px);
}
</style>