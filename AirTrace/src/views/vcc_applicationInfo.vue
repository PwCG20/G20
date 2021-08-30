<template>
  <div>
    <div class="application-info-show">Fill in loan application info</div>
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
      if (page == _self.pageIndex) {
        _self.schema.show = true;
      } else _self.schema.show = false;
    });
  },
};
</script>
<style>
.application-info-show {
  padding-top: 74px;
  font-size: 24px;
  margin-left: 10px;
  margin-bottom: 10px;
}
</style>