import Vue from 'vue'
import Vuex from 'vuex'
import movie from './modules/movie'
import user from './modules/user'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    movie: movie,
    user : user
  },
  plugins:[
    createPersistedState({
      paths: ["user"]
    })
  ]
})
