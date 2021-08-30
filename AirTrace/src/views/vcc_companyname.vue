<template>
  <div>
    <div class="company-name-show">
      Company:
      <span style="padding-left: 10px">{{ model["CompanyName"] }}</span>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      pageIndex: 1,
    };
  },
  mounted() {
    let _self = this;
    _self.bus.$on("showPage", (page) => {
      //在第一页时候不显示
      if (page != _self.pageIndex) {
        _self.schema.show = true;
      } else _self.schema.show = false;
    });
  },
};
</script>
<style>
.company-name-show {
  padding-top: 74px;
  font-size: 24px;
  margin-left: 20px;
  margin-bottom: 10px;
}
</style>