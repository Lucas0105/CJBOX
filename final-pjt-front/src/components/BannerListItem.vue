<template>
  <div class="movie" :style="{ backgroundImage: 'url(' + image + ')' }" @click="toUrl">
    <div class="content">
    </div>
  </div>
</template>

<script>
export default {
    name:'BannerListItem',
    props : [
    'image',
    'id',
  ],
  methods: {
    toUrl() {
      this.$router.push({name:'detail', params:{id: this.id}})
      this.$router.go(this.$router.currentRoute)
    }
  },
}
</script>

<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.movie{
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: flex-end;
  text-align: left;
  width : 100%;
  height : 800px;
  /* background-color: rgba(255, 255, 255, 0.7); */
  background-repeat: no-repeat;
  background-blend-mode: overlay;
  background-size: contain;
  background-position: center;
}
.content {
  padding: 10px;
}
</style>
