<style>
* {
  margin: 0;
  padding: 0;
}
html,
body {
  background-color: #f2f2f2;
  font-family: Helvetica;
}
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
  width: 400px !important;
  background-color: #ffb600;
  position: absolute;
  top: 45px;
  font-size: 30px;
  font-weight: bold;
}
.main-container {
  margin-top: 60px;
}
.el-menu-item.is-active {
  background-color: #d04a02;
}
.el-menu-item,
.el-submenu__title {
  padding: 12px 0;
  line-height: normal;
  height: 70px;
  font-size: 18px;
}
.el-menu-item [class^='el-icon-'] {
  margin-top: 10px;
  float: right;
}
.el-card,
.el-message {
  border-radius: 0;
}
.el-card__header {
  margin: 0 10px;
}
.el-card__header h2 {
  font-size: 26px;
  margin: 17px 0 20px 0;
}
.el-card__header p {
  margin-bottom: 40px;
  font-size: 18px;
}
.timeline {
  position: relative;
  float: left;
  margin-top: 12px;
}
.timeBg {
  width: 30px;
  height: 30px;
  line-height: 30px;
  text-align: center;
  color: #fff;
  position: absolute;
}
.vertical-line {
  width: 1px;
  height: 845px;
  border-left: 1px dashed #d04a02;
  margin-left: 50px;
  margin-top: 20px;
}
.time1 {
  left: 36px;
  top: 18px;
}
.time2 {
  left: 36px;
  top: 360px;
}
.time3 {
  left: 36px;
  top: 850px;
}
.help-text {
  float: left;
  margin-left: 36px;
  width: 85%;
}
.help-text h3 {
  font-size: 20px;
  color: #d04a02;
  margin-bottom: 22px;
  margin-top: 30px;
}
.help-text p {
  line-height: 40px;
  font-size: 16px;
  color: #111111;
}
.float-left {
  float: left;
}
.float-right {
  float: right;
}
.margin-bottom-40 {
  margin-bottom: 40px;
}
.margin-top-50 {
  margin-top: 50px;
}
.help-container .el-card {
  padding-bottom: 100px;
  margin-bottom: 50px;
  position: relative;
}
.nextBtn {
  position: absolute;
  font-size: 18px;
  color: #464646;
  bottom: 20px;
  right: 35px;
  cursor: pointer;
}
.nextBtn span,
.lastBtn span {
  color: #d04a02;
}
.nextBtn img,
.lastBtn img {
  vertical-align: middle;
}
.lastBtn img {
  transform: rotateZ(180deg);
}
.lastBtn {
  position: absolute;
  font-size: 18px;
  color: #464646;
  bottom: 20px;
  left: 55px;
  cursor: pointer;
}
.header-line {
  padding: 20px 0 35px 35px;
  border-bottom: 1px solid #ddd;
}
.header-line h2 {
  font-size: 28px;
  margin-bottom: 20px;
}
.header-line p {
  font-size: 20px;
}
.v-tabs--vertical > .v-tabs-bar .v-tab {
  padding: 0 0 18px 20px;
  height: 80px;
  text-align: left;
  font-family: 'PwC Helvetica Neue';
  white-space: pre-line;
  line-height: 1.5rem;
}
.theme--light.v-tabs > .v-tabs-bar {
  box-shadow: 0 2px 15px #ddd;
}
.theme--light.v-tabs-items {
  background-color: #fff;
  box-shadow: 0 0 15px #ddd;
  margin-left: 20px;
  padding-bottom: 100px;
}
.v-window .v-window__container {
  position: unset !important;
}
.v-application .light-green.lighten-5 {
  background-color: #fff !important;
  border-color: #fff !important;
}
.leftMenu .v-slide-group__wrapper {
  padding: 26px 10px 0 0px;
}
</style>
        <template>
  <div id="app">
    <div class="help-container">
      <div
        id="help-banner"
        :style="{
              background:
                'url(' +
                getResource('gettyimages.png') +
                ') center center no-repeat !important',
            }"
      >
        <div class="help-box-width">
          <span>Help Me Learn</span>
        </div>
      </div>
      <div class="help-box-width main-container">
        <v-card>
          <v-tabs
            vertical
            class="leftMenu"
          >
            <!-- <v-tab>
                  How to use this tool for assessing <br />
                  climate risk to a new loan?
                  <v-icon right> mdi-chevron-right </v-icon>
                </v-tab>
                <v-tab>
                  What is climate risks and why do I <br />
                  need to assess them?
                  <v-icon right> mdi-chevron-right </v-icon>
                </v-tab>
                <v-tab>
                  What are the assumptions behind <br />
                  this tool?
                  <v-icon right> mdi-chevron-right </v-icon>
                </v-tab> -->
            <v-tab
              class="light-green lighten-5"
              v-for="(i,index) in tables"
              :key="index"
              :id="i.id"
            >
              {{ i.title }}
              <v-icon right> mdi-chevron-right </v-icon>
            </v-tab>
            <v-tab-item>
              <v-card flat>
                <v-card-text>
                  <div class="box-card">
                    <div
                      slot="header"
                      class="clearfix header-line"
                    >
                      <h2>
                        How to use this tool for assessing climate risk to a new
                        loan?
                      </h2>
                      <p>
                        The Climate Smart tool identifies the potential impact
                        of climate-related risks to the loan applicant’s
                        probability of default (PD)
                      </p>
                    </div>
                    <div>
                      <div class="timeline">
                        <div
                          class="time1 timeBg"
                          :style="{
                                background:
                                  'url(' +
                                  getResource('circle_bg.svg') +
                                  ') center center no-repeat !important',
                              }"
                        >
                          01
                        </div>
                        <div
                          class="time2 timeBg"
                          :style="{
                                background:
                                  'url(' +
                                  getResource('circle_bg.svg') +
                                  ') center center no-repeat !important',
                              }"
                        >
                          02
                        </div>
                        <div
                          class="time3 timeBg"
                          :style="{
                                background:
                                  'url(' +
                                  getResource('circle_bg.svg') +
                                  ') center center no-repeat !important',
                              }"
                        >
                          03
                        </div>
                        <div class="vertical-line"></div>
                      </div>
                      <div class="help-text">
                        <div class="float-left">
                          <h3>Enter loan applicant’s information and value</h3>
                          <p>
                            You can enter the loan applicant’s information,
                            including
                          </p>
                          <p>(a) The sector and location of the company</p>
                          <p>
                            (b) Where relevant, the sector and location of the
                            project or activity being financed
                          </p>
                          <p>
                            (c) Information about the loan, including loan
                            value, tenure and collateral information
                          </p>
                        </div>
                        <div
                          class="float-right"
                          style="margin-top: 20px"
                        >
                          <img
                            width="205"
                            height="230"
                            :src="getResource('page1.png')"
                            alt=""
                          />
                        </div>
                      </div>
                      <div class="help-text margin-top-50">
                        <div class="float-left">
                          <h3>
                            Explore potential types of physical and transition
                            risks to the loan applicant
                          </h3>
                          <p class="margin-bottom-40">
                            Based on the loan applicant’s information, the
                            Climate Smart tool will illustrate the <br />
                            potential impacts of climate-related physical and
                            transition risks to the loan <br />
                            applicant.
                          </p>
                          <p class="margin-bottom-40">
                            The results help you understand the key drivers of
                            climate-related risks for this <br />
                            applicant.
                          </p>
                          <p>
                            You can explore the results by different scenarios
                            and by different time horizons. <br />
                            The results are derived from an ensemble of models,
                            reflecting potential <br />
                            uncertainties or disagreement between the expert
                            projections.
                          </p>
                        </div>
                        <div class="float-right margin-top-50">
                          <img
                            width="205"
                            height="400"
                            :src="getResource('page2.png')"
                            alt=""
                          />
                        </div>
                      </div>
                      <div class="help-text margin-top-50">
                        <div class="float-left">
                          <h3>
                            Evaluate next steps based on climate-adjusted PD and
                            LGD
                          </h3>
                          <p>
                            The tool estimates the change in probability of
                            default (PD) as a result of the
                          </p>
                          <p>
                            physical and transition climate-related risks.
                          </p>
                        </div>
                        <div
                          class="float-right"
                          style="margin-top: 30px"
                        >
                          <img
                            width="220"
                            height="400"
                            :src="getResource('page4.png')"
                            alt=""
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                </v-card-text>
              </v-card>
              <div
                class="nextBtn"
                @click="handleOpen(2)"
              >
                Next:
                <span>What is climate risks and why do I need to assess them?</span>
                <img
                  :src="getResource('right_circle.svg')"
                  alt=""
                />
              </div>
            </v-tab-item>
            <v-tab-item>
              <v-card flat>
                <v-card-text>
                  <div class="box-card">
                    <div
                      slot="header"
                      class="clearfix header-line"
                    >
                      <h2>
                        What is climate risks and why do I need to assess them?
                      </h2>
                      <p>
                        By factoring in potential climate risks into our lending
                        decisions, we can both protect our risks and support a
                        low carbon transition.
                      </p>
                    </div>
                    <div>
                      <div class="help-text">
                        <h3>Why do I need to assess climate risks?</h3>
                        <p class="margin-bottom-40">
                          Climate change has become a defining challenge of the
                          21st century, and there is international consensus
                          that its effects can be disastrous for human society.
                        </p>
                        <p class="margin-bottom-40">
                          As a response from the finance sector to these
                          challenges, the Task Force for Climate-Related
                          Financial Disclosure, chaired by UN special envoy on
                          climate change Michael Bloomberg, published its
                          recommendations for disclosure of climate-related
                          risks and opportunities in June 2017. The industry-led
                          initiative aims to increase transparency around the
                          assessment and management of climate-related risks and
                          opportunities. The TCFD encouraged central banks and
                          financial institutions to conduct forward-looking,
                          scenario-based assessments of the risks and
                          opportunities surrounding climate change.
                        </p>
                        <p>
                          The Network for Greening the Financial System (NGFS),
                          a group of over 100 central banks, financial
                          regulatory supervisors, and observers, have developed
                          guidance and methodologies to support scenario
                          analysis and stress testing for financial
                          institutions.
                        </p>
                      </div>
                      <div class="help-text margin-top-50">
                        <h3>What are physical climate risks?</h3>
                        <p class="margin-bottom-40">
                          Physical risks refer to the potential physical impacts
                          arising from climate change.
                        </p>
                        <p class="margin-bottom-40">
                          Scientists project that a global average temperature
                          warming of 1.5°C will pose unprecedented yet
                          potentially manageable climatic challenges to
                          ecosystems and societies. Further increases are
                          expected to lead to fully disruptive impacts,
                          including significant sea level rise, species
                          extinction, increased impacts on human health from
                          heat stress and vector-borne diseases, and higher
                          risks of droughts and flooding.
                        </p>
                        <p>
                          These risks, such as the increased frequency and
                          intensity of extreme weather events, can have severe
                          repercussions for companies, affecting their own
                          operations or their supply chains. For example
                          companies’ operations that are located in an area
                          frequently affected by tropical cyclones or floods may
                          face staff safety concerns or potential damages to
                          facilities, and business interruptions and repair
                          costs
                        </p>
                      </div>
                      <div class="help-text margin-top-50">
                        <h3>What are transition climate risks?</h3>
                        <p class="margin-bottom-40">
                          Transition risks refer to the potential impacts to an
                          organization as it adjusts (or does not adjust) toward
                          a low emission economy.
                        </p>
                        <p class="margin-bottom-40">
                          Government policy and regulatory actions aimed at
                          decarbonising global economic activity are likely to
                          impose significant uncertainty and costs in key areas
                          of the economy, with those costs likely to rise
                          considerably as action is delayed.
                        </p>
                        <p class="margin-bottom-40">
                          Emerging climate policy and low-carbon technologies
                          have already begun to significantly affect companies’
                          financial performance, particularly in the power and
                          transport sectors. Examples include the introduction
                          of carbon pricing such carbon tax or emissions trading
                          schemes, or the falling costs of technologies such as
                          electric vehicles and renewables.
                        </p>
                        <p>
                          However, the different pace and scale of policy and
                          technology advancement in different countries and
                          regiona are likely to bring differing impacts for
                          companies operating in different jurisdictions.
                        </p>
                      </div>
                    </div>
                  </div>
                </v-card-text>
              </v-card>
              <div
                class="nextBtn"
                @click="handleOpen(3)"
              >
                Next:
                <span>What are the assumptions behind this tool?</span>
                <img
                  :src="getResource('right_circle.svg')"
                  alt=""
                />
              </div>
            </v-tab-item>
            <v-tab-item>
              <v-card flat>
                <v-card-text>
                  <div class="box-card">
                    <div
                      slot="header"
                      class="clearfix header-line"
                    >
                      <h2>What are the assumptions behind this tool?</h2>
                      <p>
                        The tool has been developed based on the scenarios and
                        methodologies developed by the Network for Greening the
                        Financial System (NGFS), which is a group of over 100
                        central banks, financial regulatory supervisors, and
                        observers.
                      </p>
                    </div>
                    <div>
                      <div class="help-text">
                        <h3>What are the NGFS scenarios?</h3>
                        <p class="margin-bottom-40">
                          The NGFS Scenarios have been developed to provide a
                          common starting point for analysing climate risks to
                          the economy and financial system. While developed
                          primarily for use by central banks and supervisors
                          they may also be useful to the broader private sector,
                          government and academia.
                        </p>
                        <p>
                          The NGFS Scenarios are not forecasts, but rather
                          explore risks in a range of future states of the
                          world.
                        </p>
                      </div>
                      <div class="help-text margin-top-50">
                        <h3>How were they derived?</h3>
                        <p class="margin-bottom-40">
                          The NGFS scenarios and methodologies were produced
                          jointly with a consortium of leading research
                          institutions.
                        </p>
                        <p class="margin-bottom-40">
                          Multiple models were used to produce the scenarios to
                          capture a range of uncertainty in the results.
                        </p>
                        <p class="margin-bottom-40">
                          The transition pathways were generated by three
                          different integrated assessment models (GCAM,
                          REMIND-MAgPIE, and MESSAGEix-GLOBIOM) to provide
                          different views of how the economy responds to
                          mitigation policy.
                        </p>
                        <p>
                          The climate model MAGICC9 was also used to simulate
                          the temperature response to the NGFS scenarios and
                          provide an uncertainty band to a change in emissions.
                        </p>
                      </div>
                      <div class="help-text margin-top-50">
                        <div
                          class="float-left"
                          style="width:607px;"
                        >
                          <h3>
                            What scenarios are available?
                          </h3>
                          <p class="margin-bottom-40">
                            The NGFS scenarios explore a set of six scenarios,
                            each reflecting the pace and scale of the transition
                            to a low carbon economy. For example, Orderly
                            scenarios assume climate policies are introduced early
                            and become gradually more stringent, Disorderly
                            scenarios explore higher transition risk due to
                            policies being delayed or divergent across countries
                            and sectors, and Hot house world scenarios assume that
                            some climate policies are implemented in some
                            jurisdictions, but globally efforts are insufficient
                            to halt significant global warming.
                          </p>
                        </div>
                        <div class="float-right margin-top-50">
                          <img
                            width="205"
                            height="210"
                            :src="getResource('home_pic.png')"
                            alt=""
                          />
                        </div>

                      </div>
                      <div class="help-text margin-top-50">
                        <h3>How is the probability of default (PD) calculated?</h3>
                        <p>
                          In practice, each bank has its own methodologies to calculate the PD. Within this tool,
                          the baseline methodology represents a simplified approach based on the Zmijewski model*,
                          calculated over a longer time horizon to reflect the long term risks posed by
                          climate-related physical and transition risks. </p>
                        <p>
                          The Zmijewski model is a bankruptcy model used to predict a firm's bankruptcy in two years.
                          Zmijewski’s model uses ratio analysis that measures the performance,
                          leverage and liquidity of a company for its prediction model.
                          The ratio uses in the Zmijewski score were determined by probit analysis.
                          The analysis was based on 40 bankrupt and 800 nonbankrupt firms.
                          Zmijewski’s Probability of Default<br />

                          <img
                            :src="getResource('formula.png')"
                            alt=""
                          />
                          <br />
                          Where<br />
                          PDt = Probability of default at time t<br />
                          NIt = Net Income at time t<br />
                          TA = Total Assets<br />
                          TL = Total Liabilities<br />
                          CA = Current Assets<br />
                          CL = Current Liabilities<br />
                          The PD is calculated over the timeframe of the loan tenure, at five-yearly intervals.<br />
                          * Zmijewski, M. (1984). Methodological Issues Related to the Estimation of Financial Distress Prediction Models. 
                          Journal of Accounting Research, 22, 59-82. doi:10.2307/2490859

                        </p>
                      </div>
                      <div class="help-text margin-top-50">
                        <h3>How is the climate-adjusted probability of default (PD) calculated?</h3>
                        <p>
                          Our tool assumes that climate risks affect the factors of PD through the following ways.<br />
                          <span style="font-weight:bold">Net Income (at time t) </span>may be affected by transition risks
                          and physical risks through impacts on revenue or impacts on carbon costs and energy costs (proxied by electricity costs).
                          This impact varies by sectors and geographies.
                          This in turn affects the ability of the company to repay its liability obligations,
                          affecting <span style="font-weight:bold">Current Liabilities</span> and <span style="font-weight:bold">Total Liabilities (at time t)</span>.<br />
                          <span style="font-weight:bold"> Current Assets</span> may be affected by physical risks through impacts on liquidity (cash and receivables) of the company. This takes into account the potential annual expected damages from climate events.

                        </p>
                      </div>
                    </div>
                  </div>
                </v-card-text>
              </v-card>
              <div
                class="lastBtn"
                @click="handleOpen(2)"
              >
                <img
                  :src="getResource('right_circle.svg')"
                  alt=""
                />
                Next:
                <span>What are the assumptions behind this tool?</span>
              </div>
            </v-tab-item>
          </v-tabs>
        </v-card>
      </div>
    </div>
  </div>
</template>
        
        <script>
export default {
  data () {
    return {
      tables: [
        { title: "How to use this tool for assessing  climate risk to a new loan?", id: 1 },
        { title: "What is climate risks and why do I  need to assess them?", id: 2 },
        { title: "What are the assumptions behind  this tool?", id: 3 }
      ]
    };
  },
  methods: {
    getQueryString (name) {
      let reg = `(^|&)${name}=([^&]*)(&|$)`
      let r = window.location.search.substr(1).match(reg);
      if (r != null) return unescape(r[2]); return null;
    },
    handleOpen (num) {
      let tag = document.getElementById(num);
      tag.click();
    },
  },
  mounted () {
    var _this = this;
    var type = this.getQueryString("type");
    if (type != undefined && type != "") {
      if (type == "risk") {
        _this.handleOpen(2);
      }
    }
  },
};
    </script>