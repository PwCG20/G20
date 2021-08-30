<template>
  <div class="home-module">
    <v-card
      class="mx-auto home-title-module"
      height="360"
      :style="{
        background:
          'url(' +
          getResource('gettyimages.png') +
          ') center center no-repeat !important',
      }"
    >
      <v-card-title>
        <span class="header-wrap-title">Climate Smart - Risk Assessment of Lending</span>
      </v-card-title>

      <v-card-text class="header-wrap-detail">
        PwC AirTrace Climate Smart supports the climate risk assessment of new
        loan applicants for your financial institution.
      </v-card-text>
    </v-card>
    <v-row class="content-title">
      <v-col cols="7">
        <p>Climate risk assessment - Portfolio Summary</p>
      </v-col>
      <v-col cols="1"> </v-col>
      <v-col
        cols="4"
        class="content-help"
      >
        <a
          class="help-title"
          @click="helpPage"
        >
          <div class="circle">?</div>
          <span>Help me learn</span>
        </a>
      </v-col>
    </v-row>
    <div class="content-module">
      <v-card
        class="mx-auto report-module"
        height="430"
      >
        <v-row style="header-row">
          <v-col
            cols="12"
            sm="2"
            class="header-chart"
          >
            <div class="weeklyDigestChart">
              <div class="title">No. of assessment submission</div>
              <div class="weekly-digest-box custom-scrollbar">
                <div class="weekly-digest-item">
                  <div class="weekly-digest-item-img">
                    <div>
                      <svg
                        id="teamSvg"
                        xmlns="http://www.w3.org/2000/svg"
                        width="55"
                        height="55"
                        viewBox="0 0 45 55"
                        fill="#D04A02"
                      >
                        <path
                          class="a"
                          d="M36.953-13.422a3.044,3.044,0,0,0,2.188-1.172,6.232,6.232,0,0,0,1.016-3.828,3.4,3.4,0,0,0-3.2-3.516,3.345,3.345,0,0,0-3.2,3.516,5.755,5.755,0,0,0,1.016,3.828A2.9,2.9,0,0,0,36.953-13.422Zm0-6.719a1.591,1.591,0,0,1,1.406,1.719c0,1.25-.391,3.2-1.406,3.2s-1.406-1.953-1.406-3.2A1.591,1.591,0,0,1,36.953-20.141ZM8.047-13.422a2.9,2.9,0,0,0,2.188-1.172,5.755,5.755,0,0,0,1.016-3.828,3.345,3.345,0,0,0-3.2-3.516,3.4,3.4,0,0,0-3.2,3.516,6.232,6.232,0,0,0,1.016,3.828A3.044,3.044,0,0,0,8.047-13.422Zm0-1.8c-1.016,0-1.406-1.953-1.406-3.2a1.591,1.591,0,0,1,1.406-1.719,1.591,1.591,0,0,1,1.406,1.719C9.453-17.172,9.063-15.219,8.047-15.219ZM0-36V9H7.031L8.281-3.266a5.855,5.855,0,0,1,3.594-3.594l6.719-2.266c.078-.078.156,0,.234,0l.547.547A4.249,4.249,0,0,0,22.5-7.25a4.249,4.249,0,0,0,3.125-1.328l.547-.547c.078,0,.156-.078.234,0l6.719,2.266a5.674,5.674,0,0,1,3.594,3.594L37.969,9H45V-36ZM11.25-8.656A7.546,7.546,0,0,0,6.484-3.812L5.313,7.047H1.953V-7.172l.156-1.484A2.232,2.232,0,0,1,3.438-9.984l2.813-.937.078.078a2.424,2.424,0,0,0,1.719.7,2.475,2.475,0,0,0,1.8-.7l.078-.078,2.813.938a2.806,2.806,0,0,1,.781.547Zm13.516-1.8-.469.547a2.543,2.543,0,0,1-1.8.781,2.543,2.543,0,0,1-1.8-.781l-.469-.547A2.424,2.424,0,0,0,17.969-11l-2.656.938A3.839,3.839,0,0,0,13.281-11.7l-3.047-1.016a1.533,1.533,0,0,0-1.484.391l-.234.234a.713.713,0,0,1-.937,0l-.234-.234a1.488,1.488,0,0,0-1.484-.391L2.813-11.7a8.522,8.522,0,0,0-.859.469V-34.047H43.047v22.813a8.522,8.522,0,0,0-.859-.469l-3.047-1.016a1.488,1.488,0,0,0-1.484.391l-.234.234a.713.713,0,0,1-.937,0l-.234-.234a1.533,1.533,0,0,0-1.484-.391L31.719-11.7a3.839,3.839,0,0,0-2.031,1.641L27.031-11A2.424,2.424,0,0,0,24.766-10.453Zm14.922,17.5L38.594-3.578l-.078-.234A7.546,7.546,0,0,0,33.75-8.656l-2.266-.781a2.806,2.806,0,0,1,.781-.547l2.813-.937.078.078a2.475,2.475,0,0,0,1.8.7,2.424,2.424,0,0,0,1.719-.7l.078-.078,2.813.938a2.232,2.232,0,0,1,1.328,1.328l.156,1.484V7.047ZM22.5-28.656c-3.359,0-6.094,2.969-6.094,6.719,0,3.594.7,6.172,2.031,7.656,1.094,1.25,2.188,2.266,4.063,2.266s2.969-1.016,4.063-2.266c1.328-1.484,2.031-4.062,2.031-7.656C28.594-25.687,25.859-28.656,22.5-28.656Zm2.656,13.125c-1.172,1.25-1.719,1.641-2.656,1.641s-1.484-.391-2.656-1.641c-.937-1.094-1.484-3.437-1.484-6.406,0-2.656,1.875-4.844,4.141-4.844s4.141,2.188,4.141,4.844C26.641-18.969,26.094-16.625,25.156-15.531Z"
                          transform="translate(0 36)"
                        ></path>
                      </svg>
                    </div>
                  </div>
                  <div class="weekly-digest-item-right">
                    <div class="digest-title-num">
                      <span
                        title="14"
                        style="color: #d04a02"
                      >{{
                        loanAppStatusStat["Draft"]
                      }}</span>
                    </div>
                    <div class="digest-title">Draft</div>
                  </div>
                </div>
                <div class="weekly-digest-item">
                  <div class="weekly-digest-item-img">
                    <div>
                      <svg
                        id="taskSvg"
                        xmlns="http://www.w3.org/2000/svg"
                        width="55"
                        height="55"
                        viewBox="0 0 45 55"
                        fill="#E0301E"
                      >
                        <path
                          class="a"
                          d="M33.878-36V3.072L37.649,9l3.835-5.928v-37.1h1.534v14.15H45V-36ZM39.5-34.024V-20.83H35.859V-34.024ZM37.649,5.494l-1.79-2.932V-18.854H39.5V2.562ZM22.5-24.654H7.479V-26.5H22.5Zm0,8.095H7.479v-1.912H22.5Zm0,8.159H7.479v-1.976H22.5Zm0,8.031H7.479V-2.218H22.5ZM29.979,9H0V-36H29.979ZM1.854,7.152H28.061V-34.024H1.854Z"
                          transform="translate(0 36)"
                        ></path>
                      </svg>
                    </div>
                  </div>
                  <div class="weekly-digest-item-right">
                    <div class="digest-title-num">
                      <span
                        title="38"
                        style="color: #e0301e"
                      >{{
                        loanAppStatusStat["Under consideration"]
                      }}</span>
                    </div>
                    <div class="digest-title">Under consideration</div>
                  </div>
                </div>
                <div class="weekly-digest-item">
                  <div class="weekly-digest-item-img">
                    <div>
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        id="documentSvg"
                        width="55"
                        height="55"
                        viewBox="0 0 45 55"
                        fill="#000000"
                      >
                        <path
                          class="a"
                          d="M16.3-16.623H8.374v-1.912H16.3Zm0,6.183H8.374v1.912H16.3ZM8.374-.37H16.3V-2.346H8.374ZM27.486-8.528H37.777v-1.912H27.486Zm0,8.159H37.777V-2.346H27.486ZM20.646-18.535H45V9H20.646ZM22.564,7.024H43.018V-16.559H22.564ZM27.486-26.63H8.374v1.976H27.486ZM45-26.5v4.844H43.018v-3.123H34.07v-9.37H1.854V7.024H17.514V9H0V-36H35.412Zm-9.013-.191H42l-6.009-6.055Z"
                          transform="translate(0 36)"
                        ></path>
                      </svg>
                    </div>
                  </div>
                  <div class="weekly-digest-item-right">
                    <div class="digest-title-num">
                      <span
                        title="2"
                        style="color: #000000"
                      >{{
                        loanAppStatusStat["Approved"]
                      }}</span>
                    </div>
                    <div class="digest-title">Approved</div>
                  </div>
                </div>
                <div class="weekly-digest-item">
                  <div class="weekly-digest-item-img">
                    <div>
                      <svg
                        id="messageSvg"
                        xmlns="http://www.w3.org/2000/svg"
                        width="55"
                        height="55"
                        viewBox="0 0 45 55"
                        fill="#7D7D7D"
                      >
                        <defs></defs>
                        <path
                          class="a"
                          d="M45.5-36v14.773H43.445v-12.7H2.055V-.25H8.219V5.068L13.5-.25h2.935V1.523H14.384L6.165,9.5V1.523H0V-36Zm-8.513,9.75H8.513v1.773H36.987ZM8.513-16.2h7.926v-2.068H8.513Zm0,8.273h7.926V-9.7H8.513ZM38.161-9.7H27.594v1.773H38.161ZM20.842-18.273H45.5v19.8H39.629V9.5L31.41,1.523H20.842ZM22.6-.25H32.29l5.284,5.318V-.25h5.871V-16.2H22.6Z"
                          transform="translate(0 36)"
                        ></path>
                      </svg>
                    </div>
                  </div>
                  <div class="weekly-digest-item-right">
                    <div class="digest-title-num">
                      <span
                        title="1"
                        style="color: #7d7d7d"
                      >{{
                        loanAppStatusStat["Drawdown"]
                      }}</span>
                    </div>
                    <div class="digest-title">Drawdown</div>
                  </div>
                </div>
              </div>
            </div>
            <!-- <div class="helppage">
              <button
                type="button"
                class="btn"
                @click="helpPage"
              >
                <i class="mdi pwc_helpquestionicon"></i>Help me learn
              </button>
            </div> -->
          </v-col>
          <v-col
            cols="12"
            sm="5"
            class="header-chart"
          >
            <div class="weeklyDigestChart">
              <div class="title">Unadjusted Probability of default (PD)</div>
              <vcc_echart_middle
                ref="secondChart"
                style="
                  border-left: 1px solid rgb(221, 221, 221);
                  border-right: 1px solid rgb(221, 221, 221);
                "
                :model="model"
                :schema="echartMiddleSchema"
                :options="options"
              />
            </div>
          </v-col>
          <v-col
            cols="12"
            sm="5"
            class="header-chart"
          >
            <div class="weeklyDigestChart">
              <div class="title">
                Sector average: change in climate-adjusted probability of
                default (PD)
              </div>
              <vcc_echart_pdindustry
                ref="thirdChart"
                :model="model"
                :schema="pdindustrySchema"
                :options="options"
              />
            </div>
          </v-col>
        </v-row>
      </v-card>

      <v-card class="datatable-module">
        <v-row class="mt-4 pl-4 pr-4 table-title">
          <v-col
            class="d-flex justify-start pb-0"
            cols="12"
            sm="7"
          >
            <div class="title">Loan Portfolio</div>
            <v-text-field
              class="mr-2"
              style="max-width: 300px"
              color="#E0301E"
              dense
              outlined
              v-model="loanApplication"
              label="Loan application"
              single-line
              hide-details
            >
            </v-text-field>
            <v-select
              class="mr-2"
              color="#E0301E"
              style="max-width: 300px"
              dense
              outlined
              @change="chooseLoanType"
              v-model="loanType"
              :items="statusItems"
              item-text="itemText"
              item-value="itemValue"
              label="Loan status"
            >
            </v-select>
          </v-col>
          <v-col
            class="d-flex justify-end pb-0"
            cols="12"
            sm="5"
          >
            <button
              type="button"
              class="newloan-button btn"
              @click="newLoan"
            >
              <i class="mdi pwc_plusicon"></i>New loan
            </button>
          </v-col>
        </v-row>
        <div class="datatable_module">
          <v-data-table
            ref="vcDataTable"
            @dblclick:row="dblclickRow"
            :height="height"
            item-key="_id"
            :loading="loadingData"
            :headers="headers"
            :items="desserts"
            fixed-header
            hide-default-footer
            disable-pagination
            :no-data-text="noDataText"
          >
            <template v-slot:item.CompanyName="{ item }">
              <a
                :href="exportEnvUrl(formHref + 'edit/' + item._id)"
                target="_blank"
                color="#E0301E"
              >
                {{ item.CompanyName }}
              </a>
            </template>
            <template v-slot:item.CloseDate="{ item }">
              {{
                item.CloseDate
                  ? $options.filters["dateformat"](item.CloseDate, "YYYY/MM/DD")
                  : ""
              }}
            </template>
            <template v-slot:item.StartDate="{ item }">
              {{ $options.filters["dateformat"](item.StartDate, "YYYY/MM/DD") }}
            </template>
            <template v-slot:item.EndDate="{ item }">
              {{ $options.filters["dateformat"](item.EndDate, "YYYY/MM/DD") }}
            </template>
            <template v-slot:item.RiskAssessment="{ item }">
              <v-chip
                :color="getRiskColor(item.RiskAssessment)"
                dark
              >
                {{ getRiskContent(item.RiskAssessment) }}
              </v-chip>
            </template>
            <template v-slot:item.CompanyHashCode="{ item }">
              <a
                v-if="item.CompanyHashCode"
                :href="exportEnvUrl(blockChainHref + '?id=' + item._id)"
                target="_blank"
                color="#4dacf1"
              >
                View on blockchain
              </a>
            </template>
          </v-data-table>
        </div>
        <v-divider></v-divider>
      </v-card>
    </div>
  </div>
</template>
<script>
export default {
  data () {
    return {
      pageIndex: 1,
      loadMoreData: false,
      totalDesserts: 0,
      loanApplication: "",
      loanType: "",
      selectedStatus: "all",
      height: "500",
      statusItems: [
        {
          itemValue: "All",
          itemText: "All",
        },
        {
          itemValue: "Draft",
          itemText: "Draft",
        },
        {
          itemValue: "Under consideration",
          itemText: "Under consideration",
        },
        {
          itemValue: "Approved",
          itemText: "Approved",
        },
        {
          itemValue: "Drawdown",
          itemText: "Drawdown",
        },
      ],
      noDataText: "No data",
      search: "",
      loadingData: false,
      pageCode: "airtrace",
      tenantId: "g20",
      headers: [
        {
          text: "Loan Application",
          align: "start",
          sortable: true,
          value: "CompanyName",
          width: "10%",
          class: "headerCSS",
        },
        {
          text: "Stage",
          align: "start",
          sortable: true,
          value: "Stage",
          width: "8%",
          class: "headerCSS",
        },
        {
          text: "Close Date",
          align: "start",
          sortable: true,
          value: "CloseDate",
          width: "9%",
          class: "headerCSS",
        },
        {
          text: "Loan Start Date",
          align: "start",
          sortable: true,
          value: "StartDate",
          width: "10%",
          class: "headerCSS",
        },
        {
          text: "Loan End Date",
          align: "start",
          sortable: true,
          value: "EndDate",
          width: "10%",
          class: "headerCSS",
        },
        {
          text: "Owner Full Name",
          align: "start",
          sortable: true,
          value: "Owner",
          width: "10%",
          class: "headerCSS",
        },
        {
          text: "Loan Amount",
          align: "start",
          sortable: true,
          value: "LoanValue",
          width: "11%",
          class: "headerCSS",
        },
        {
          text: "Climate Risk Assessment",
          align: "start",
          sortable: true,
          value: "RiskAssessment",
          width: "17%",
          class: "headerCSS",
        },
        {
          text: "",
          align: "start",
          sortable: false,
          value: "CompanyHashCode",
          width: "17%",
          class: "headerCSS",
        },
      ],
      desserts: [],
      enableMock: false,
      mockData: {
        statusCode: 200,
        info: "Request (or process) succeeded",
        data: {
          totalCount: 8,
          items: [
            {
              _id: "092ce0b2-18d1-497e-9592-28132653358d",
              Ng_SysCreationTime: 1627378735179,
              Ng_SysCreatorId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysCreatorName: "Eason Dong",
              Ng_SysLastModificationTime: 1627378735179,
              Ng_SysLastModifierId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysLastModifierName: "Eason Dong",
              CompanyName: "ExxonMobil Test",
              ProductType: ["Business Expansion credit line"],
              StartDate: 1609948800000,
              EndDate: 1615046400000,
              LoanValue: "666",
              CloseDate: null,
              Stage: "Draft",
              Owner: "Eason Dong",
              RiskAssessment: 0,
              Ng_ConcurrencyStamp: "092ce0b2-18d1-497e-9592-28132653358d",
            },
            {
              _id: "092ce0b2-18d1-497e-9592-281326533500",
              Ng_SysCreationTime: 1627378735179,
              Ng_SysCreatorId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysCreatorName: "Eason Dong",
              Ng_SysLastModificationTime: 1627378735179,
              Ng_SysLastModifierId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysLastModifierName: "Eason Dong",
              CompanyName: "ExxonMobil",
              ProductType: ["Business Expansion credit line"],
              StartDate: 1609948800000,
              EndDate: 1615046400000,
              LoanValue: "666",
              CloseDate: null,
              Stage: "Under consideration",
              Owner: "Eason Dong",
              RiskAssessment: 1,
              Ng_ConcurrencyStamp: "092ce0b2-18d1-497e-9592-28132653358d",
            },
            {
              _id: "092ce0b2-18d1-497e-9592-281326533501",
              Ng_SysCreationTime: 1627378735179,
              Ng_SysCreatorId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysCreatorName: "Eason Dong",
              Ng_SysLastModificationTime: 1627378735179,
              Ng_SysLastModifierId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysLastModifierName: "Eason Dong",
              CompanyName: "ExxonMobil",
              ProductType: ["Business Expansion credit line"],
              StartDate: 1609948800000,
              EndDate: 1615046400000,
              LoanValue: "666",
              CloseDate: null,
              Stage: "Draft",
              Owner: "Eason Dong",
              RiskAssessment: 0,
              Ng_ConcurrencyStamp: "092ce0b2-18d1-497e-9592-28132653358d",
            },
            {
              _id: "092ce0b2-18d1-497e-9592-281326533503",
              Ng_SysCreationTime: 1627378735179,
              Ng_SysCreatorId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysCreatorName: "Eason Dong",
              Ng_SysLastModificationTime: 1627378735179,
              Ng_SysLastModifierId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysLastModifierName: "Eason Dong",
              CompanyName: "ExxonMobil",
              ProductType: ["Business Expansion credit line"],
              StartDate: 1609948800000,
              EndDate: 1615046400000,
              LoanValue: "666",
              CloseDate: null,
              Stage: "Draft",
              Owner: "Eason Dong",
              RiskAssessment: 0,
              Ng_ConcurrencyStamp: "092ce0b2-18d1-497e-9592-28132653358d",
            },
            {
              _id: "092ce0b2-18d1-497e-9592-281326533502",
              Ng_SysCreationTime: 1627378735179,
              Ng_SysCreatorId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysCreatorName: "Eason Dong",
              Ng_SysLastModificationTime: 1627378735179,
              Ng_SysLastModifierId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysLastModifierName: "Eason Dong",
              CompanyName: "ExxonMobil",
              ProductType: ["Business Expansion credit line"],
              StartDate: 1609948800000,
              EndDate: 1615046400000,
              LoanValue: "666",
              CloseDate: null,
              Stage: "Draft",
              Owner: "Eason Dong",
              RiskAssessment: 0,
              Ng_ConcurrencyStamp: "092ce0b2-18d1-497e-9592-28132653358d",
            },
            {
              _id: "092ce0b2-18d1-497e-9592-281326533504",
              Ng_SysCreationTime: 1627378735179,
              Ng_SysCreatorId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysCreatorName: "Eason Dong",
              Ng_SysLastModificationTime: 1627378735179,
              Ng_SysLastModifierId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysLastModifierName: "Eason Dong",
              CompanyName: "ExxonMobil",
              ProductType: ["Business Expansion credit line"],
              StartDate: 1609948800000,
              EndDate: 1615046400000,
              LoanValue: "666",
              CloseDate: null,
              Stage: "Draft",
              Owner: "Eason Dong",
              RiskAssessment: 0,
              Ng_ConcurrencyStamp: "092ce0b2-18d1-497e-9592-28132653358d",
            },
            {
              _id: "092ce0b2-18d1-497e-9592-281326533505",
              Ng_SysCreationTime: 1627378735179,
              Ng_SysCreatorId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysCreatorName: "Eason Dong",
              Ng_SysLastModificationTime: 1627378735179,
              Ng_SysLastModifierId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysLastModifierName: "Eason Dong",
              CompanyName: "ExxonMobil",
              ProductType: ["Business Expansion credit line"],
              StartDate: 1609948800000,
              EndDate: 1615046400000,
              LoanValue: "666",
              CloseDate: null,
              Stage: "Draft",
              Owner: "Eason Dong",
              RiskAssessment: 0,
              Ng_ConcurrencyStamp: "092ce0b2-18d1-497e-9592-28132653358d",
            },
            {
              _id: "092ce0b2-18d1-497e-9592-281326533506",
              Ng_SysCreationTime: 1627378735179,
              Ng_SysCreatorId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysCreatorName: "Eason Dong",
              Ng_SysLastModificationTime: 1627378735179,
              Ng_SysLastModifierId: "700fc180-fc50-4368-82ac-f89294e599dc",
              Ng_SysLastModifierName: "Eason Dong",
              CompanyName: "ExxonMobil",
              ProductType: ["Business Expansion credit line"],
              StartDate: 1609948800000,
              EndDate: 1615046400000,
              LoanValue: "666",
              CloseDate: null,
              Stage: "Draft",
              Owner: "Eason Dong",
              RiskAssessment: 0,
              Ng_ConcurrencyStamp: "092ce0b2-18d1-497e-9592-28132653358d",
            },
          ],
        },
      },
      companyResultList: [],
      formHref: "/g20/AirTrace/form/loanapplication/",
      blockChainHref: "/g20/AirTrace/page/blockchain",
      echartMiddleSchema: {
        component: "vcc_echart_middle",
        name: "vcc_echart_middle",
      },
      pdindustrySchema: {
        component: "vcc_echart_pdindustry",
        name: "vcc_echart_pdindustry",
      },
      loanAppStatusStat: {},
    };
  },
  watch: {
    loanApplication () {
      this.pageIndex = 1;
      this.getDataList("reset");
    },
  },
  methods: {
    enableBlockChain (val) {
      console.log("enableBlockChain: ", val);
      if (val) {
        return true;
      } else {
        return false;
      }
    },
    getRiskColor (value) {
      let color = "#22992E";
      switch (value) {
        case 0:
          color = "#22992E";
          break;
        case 1:
          color = "#C52A1A";
          break;
        case 2:
          color = "#FFBF1F";
          break;
      }
      return color;
    },
    getRiskContent (value) {
      let content = "No material climate-related risks";
      switch (value) {
        case 0:
          content = "No material climate-related risks";
          break;
        case 1:
          content = "Material climate risks";
          break;
        case 2:
          content = "Significant climate-related risks";
          break;
      }
      return content;
    },
    helpPage () {
      var href = "/g20/airtrace/page/helpmelearnpage";
      window.open(href, "_blank");
    },
    /* DataTable Function */
    dblclickRow: function (item, row) {
      window.open(
        this.exportEnvUrl(this.formHref + "edit/" + row.item._id),
        "_blank"
      );
    },
    // getCompanyStatistics() {
    //   this.statusItems.forEach((item)=>{
    //     if(item.itemValue != 'All'){
    //       getCompanyCountByStatus(item.itemValue);
    //     }
    //   });
    // },
    getCompanyCountByStatus (status) {
      var _self = this;
      // console.log("status: ", status);
      var requestPara = {
        pageCode: "loanapplication",
        searchItems: [
          {
            name: "Stage",
            value: status,
            operator: "Equal",
            method: "And",
            subSearchItems: [],
          },
        ],
        order: {
          CompanyName: 1,
        },
      };
      _self.callApi("GetDocsCount", requestPara).then((data) => {
        console.log(status + "status_count: ", data);
        if (data.statusCode == 200) {
          _self.$set(_self.loanAppStatusStat, status, data.data);
        } else {
          _self.$set(_self.loanAppStatusStat, status, 0);
        }
      });
    },
    initScroll () {
      var dataTable = this.$refs.vcDataTable;
      if (dataTable !== undefined) {
        var dt = dataTable.$el.querySelector(".v-data-table__wrapper");
        if (dt != undefined) {
          dt.addEventListener("scroll", this.onScroll);
        }
      }
    },
    onScroll (e) {
      let _self = this;
      var dataTable = _self.$refs.vcDataTable;
      if (dataTable !== undefined) {
        var dt = dataTable.$el.querySelector(".v-data-table__wrapper");
        var viewH = dt.offsetHeight,
          contentH = dt.scrollHeight,
          scrollTop = e.target.scrollTop;

        if (scrollTop / (contentH - viewH) >= 0.95 && _self.loadMoreData) {
          _self.loadMoreData = false;
          if (_self.totalDesserts > _self.desserts.length) {
            _self.pageIndex = _self.pageIndex + 1;
            _self.getDataList();
          }
        }
      }
    },
    getDataList (type) {
      let _self = this;
      let filterData = [];
      if (_self.loanApplication) {
        filterData.push({
          name: "CompanyName",
          value: _self.loanApplication,
          operator: "Contains",
          method: "And",
          subSearchItems: [],
        });
      }
      if (_self.loanType && _self.loanType != "All") {
        filterData.push({
          name: "Stage",
          value: _self.loanType,
          operator: "Equal",
          method: "And",
          subSearchItems: [],
        });
      }
      var requestPara = {
        pageCode: "loanapplication",
        searchItems: filterData,
        order: {
          // Ng_SysLastModificationTime: -1,
          CompanyName: 1
        },
        columns: [
          "CompanyName",
          "ProductType",
          "Stage",
          "CloseDate",
          "StartDate",
          "EndDate",
          "Owner",
          "LoanValue",
          "RiskAssessment",
          // "PDHashCode",
          "CompanyHashCode",
        ],
        withSocialStatus: false,
        index: _self.pageIndex,
        size: 10,
      };
      if (_self.enableMock) {
        _self.desserts = _self.desserts.concat(_self.mockData.data.items);
        _self.loadMoreData = true;
        _self.totalDesserts = 100;
      } else {
        _self.callApi("GetDocs", requestPara).then((data) => {
          let newData = data.data;
          newData.items.map((m) => {
            if (m.LoanValue) {
              // m.LoanValue = "HK$" + m.LoanValue + "(US$" + m.LoanValue + ")"; //需要换算公式
              m.LoanValue = "US$" + _self.format_money(m.LoanValue) + "M";
            }
          });
          if (type == "reset") {
            _self.desserts = newData.items;
          } else {
            _self.desserts = _self.desserts.concat(newData.items);
          }
          _self.loadMoreData = true;
          _self.totalDesserts = newData.totalCount;
        });
      }
    },
    format_money (val) {
      var num = val.replaceAll(",", "");
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
      return newvalue.toString();
    },
    chooseLoanType () {
      this.pageIndex = 1;
      this.getDataList("reset");
    },
    getEnv () {
      var env = null;
      if (window.top.location.search.indexOf("env=") > -1) {
        env =
          window.top.location.search.split("env=")[1] === "dev" ||
            window.top.location.search.split("env=")[1] === "stage"
            ? window.top.location.search.split("env=")[1]
            : null;
      }
      return env;
    },
    exportEnvUrl (url) {
      let env = this.getEnv();
      if (env && env.toLowerCase() != "prod") {
        var newUrl = url;
        var idx = url.indexOf("?");
        if (idx < 0) {
          newUrl += "?";
        } else if (idx >= 0 && idx != url.length - 1) {
          newUrl += "&";
        }
        newUrl = newUrl + "env=" + env;
        return newUrl;
      } else {
        return url;
      }
    },
    newLoan () {
      window.open(this.exportEnvUrl(this.formHref + "add"), "_blank");
    },
    getResourceDemo (name) {
      let url = "";
      switch (name) {
        case "icon-search.svg":
          url = require("../assets/g20/icon-search.svg");
          break;
        case "gettyimages.png":
          url = require("../assets/g20/GettyImages.png");
          break;
      }
      return url;
    },
    resize () {
      let _self = this;
      _self.$refs.secondChart.resize();
      _self.$refs.thirdChart.resize();
    },
  },
  created () {
    var _self = this;
    _self.statusItems.forEach((item) => {
      if (item.itemValue != "All") {
        _self.getCompanyCountByStatus(item.itemValue);
      }
    });
  },
  mounted () {
    let _self = this;
    this.getDataList("init");
    this.initScroll();
    window.onresize = () => {
      _self.resize();
    };
  },
};
</script>
<style>
html body {
  background-color: #fff;
}
.header-row {
  margin-left: 0px;
  margin-right: 0px;
}

.header-chart {
  padding: 0 12px !important;
}

.vc-toolbar + div {
  padding-top: 64px !important;
}

.home-module {
  padding-top: 64px !important;
}

.home-module .home-title-module {
  background: url('../assets/g20/GettyImages.png') center center no-repeat !important;
}

.home-module .header-wrap-title {
  font-family: 'ITC Charter Com';
  background-color: #ffb600;
  color: #000;
  font-size: 40px;
  width: 870px;
  height: 95px;
  margin-left: 177px;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  left: -15px;
  top: 50px;
}

.home-module .header-wrap-detail {
  font-family: 'Helvetica Neue LT Pro';
  background-color: #000000;
  color: #ffffff !important;
  font-size: 24px;
  line-height: 26px;
  width: 771px;
  height: 91px;
  margin-left: 235px;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 0 50px 0 30px;
  position: absolute;
  top: 145px;
}

@media screen and (min-width: 320px) {
  .home-module .header-wrap-title {
    width: 270px;
    height: 75px;
    padding: 20px;
    font-size: 20px;
    margin-left: 57px;
  }

  .home-module .header-wrap-detail {
    width: 234px;
    height: 125px;
    font-size: 14px;
    margin-left: 75px;
    top: 125px;
  }
}

@media screen and (min-width: 700px) {
  .home-module .header-wrap-title {
    width: 570px;
    height: 75px;
    padding: 20px;
    margin-left: 137px;
    font-size: 25px;
  }

  .home-module .header-wrap-detail {
    width: 450px;
    height: 85px;
    font-size: 14px;
    margin-left: 175px;
    top: 125px;
  }
}

@media screen and (min-width: 1000px) {
  .home-module .header-wrap-title {
    background-color: #ffb600;
    color: #000;
    font-size: 40px;
    width: 870px;
    height: 95px;
    margin-left: 177px;
    display: flex;
    align-items: center;
    justify-content: center;
    position: absolute;
    left: -15px;
    top: 50px;
    padding: 0px;
  }

  .home-module .header-wrap-detail {
    background-color: #000;
    color: #fff !important;
    font-size: 24px;
    line-height: 26px;
    width: 771px;
    height: 91px;
    margin-left: 235px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 50px 0 30px;
    position: absolute;
    top: 145px;
  }
}

/* .home-module .search-wrap-box {
        min-width: 80%;
        margin: 0 auto;
        position: relative;
    }

    .home-module .search-wrap {
        width: 60%;
        height: 120px;
        background-color: #fff;
        border-bottom: solid #FFB600 5px;
        position: absolute;
        top: -50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 9;
        padding: 20px 20px 5px;
    }

    .home-module .search-button {
        border-radius: 0px;
    }

    .home-module .search-wrap-content {
        display: flex;
    } */

.report-module {
  margin-top: 20px !important;
  box-shadow: 0px 0px 4px #0000001a !important;
}

/* datatable css */
.datatable-module {
  background-color: #f3f3f3 !important;
}

.justify-start > .title {
  font-size: 18px !important;
  font-weight: bold;
  color: #000;
  padding-right: 115px;
}

.table-title {
  height: 79px;
  padding-top: 20px;
}
.home-module .datatable-module .headerCSS {
  color: #2d2d2d !important;
  font-size: 14px !important;
}

.home-module .newloan-button {
  background-color: #e0301e !important;
  color: #fff !important;
  cursor: pointer !important;
  width: 160px;
  height: 40px;
}

.home-module .newloan-button:hover {
  background-color: #fff !important;
  color: #e0301e !important;
  border: solid #e0301e 1px !important;
}

.home-module .newloan-button span:hover {
  color: #e0301e !important;
}

/* report css */
.weeklyDigestChart {
  width: 100%;
  position: relative;
}

.weeklyDigestChart .title {
  font-size: 18px !important;
  font-family: 'Helvetica Neue' !important;
  font-weight: bold;
  padding-left: 15px;
  padding-top: 22px;
  line-height: 22px;
}

.weeklyDigestChart .weekly-digest-box {
  display: flex;
  flex-wrap: wrap;
  overflow-x: auto;
  margin-top: 51px;
}

.weeklyDigestChart .weekly-digest-box .weekly-digest-item {
  display: flex;
  padding: 10px 5px 30px 5px;
  width: 50%;
  align-items: center;
  justify-content: center;
  flex-direction: column;
}

.weeklyDigestChart
  .weekly-digest-box
  .weekly-digest-item
  .weekly-digest-item-img {
  min-width: 56px;
  text-align: center;
}

.weeklyDigestChart
  .weekly-digest-box
  .weekly-digest-item
  .weekly-digest-item-img
  svg {
  width: 55px !important;
  height: 55px !important;
}

.weeklyDigestChart
  .weekly-digest-box
  .weekly-digest-item
  .weekly-digest-item-right {
  line-height: 1.3;
  padding-left: 5px;
  text-align: center;
}

.weeklyDigestChart
  .weekly-digest-box
  .weekly-digest-item
  .weekly-digest-item-right
  .digest-title {
  font-size: 18px;
  padding-top: 5px;
  padding-bottom: 5px;
  color: #000;
  height: 40px;
  font-family: 'Helvetica Neue';
}

.weeklyDigestChart
  .weekly-digest-box
  .weekly-digest-item
  .weekly-digest-item-right
  .digest-title-num {
  display: flex;
  align-items: flex-end;
  font-size: 36px;
  justify-content: center;
  font-family: 'Helvetica Neue LT Pro';
}

.weeklyDigestChart
  .weekly-digest-box
  .weekly-digest-item
  .weekly-digest-item-right
  .digest-title-num
  > span:first-child {
  line-height: 0.8;
  overflow: hidden;
  max-width: 85px;
  text-align: right;
  text-overflow: ellipsis;
}

.weeklyDigestChart
  .weekly-digest-box
  .weekly-digest-item
  .weekly-digest-item-right
  .digest-title-num
  > span:nth-child(2) {
  font-size: 14px;
  color: #2d2d2d;
  margin-left: 5px;
}

.weeklyDigestChart
  .weekly-digest-box
  .weekly-digest-item
  .weekly-digest-item-right
  .digest-tip {
  font-size: 12px;
  color: #7d7d7d;
}

.home-module {
  padding-bottom: 60px !important;
}

.content-module {
  margin: 0 auto;
  margin-left: 30px;
  margin-right: 20px;
}

.content-module .v-data-table {
  padding-top: 0px;
}

.v-data-table > .v-data-table__wrapper > table > tbody > tr > td {
  font-size: 14px !important;
}
.content-module .helppage button {
  width: 180px;
  height: 40px;
  background-color: #d04a02;
  color: #fff;
  font-size: 18px;
}

.content-module .helppage {
  margin: 10px auto;
  display: flex;
  align-items: center;
  justify-content: center;
}

.content-module .helppage button:hover {
  background-color: #fff;
  color: #d04a02;
  border: solid 1px #d04a02;
}

.content-module .helppage button:focus {
  background-color: #fff;
  color: #d04a02;
  border: solid 1px #d04a02;
}

.content-title {
  border-bottom: 1px solid #dedede;
  color: #000000;
  margin-left: 30px;
  margin-right: 30px;
}
.content-title > .col {
  padding-left: 0 !important;
  padding-bottom: 0 !important;
}

.content-title > .col p {
  font-family: 'ITC Charter Com';
  font-size: 28px;
  text-align: left;
  border-bottom: 4px solid #d04a02;
  display: table-cell;
}

.content-help {
  text-align: end;
  color: #2d2d2d;
  font-size: 18px;
  display: flex;
  justify-content: flex-end;
}

.circle {
  width: 24px;
  height: 24px;
  background-color: #2d2d2d;
  border-radius: 50%;
  display: inline-block;
  margin-right: 5px;
  color: #fff;
  text-align: center;
}

.help-title {
  display: flex;
  align-items: center;
}
.help-title span {
  color: #2d2d2d;
}
</style>