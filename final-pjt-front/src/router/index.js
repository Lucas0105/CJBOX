import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/movies/MovieView'
import DetailView from '@/views/movies/DetailView'
import SearchView from '@/views/movies/SearchView'
import GenreView from '@/views/genres/GenreView'
import LoginView from '@/views/accounts/LoginView'
import SignupView from '@/views/accounts/SginupView'
import MyPageView from '@/views/accounts/MyPageView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/movies',
    name: 'MovieView',
    component: MovieView
  },
  {
    path: '/movies/:id',
    name: 'DetailView',
    component: DetailView
  },
  {
    path: '/movies/search',
    name: 'SearchView',
    component: SearchView
  },
  {
    path: '/genres',
    name: 'GenreView',
    component: GenreView
  },
  {
    path: '/accounts/login',
    name: 'LoginView',
    component: LoginView
  },
  {
    path: '/accounts/SignupView',
    name: 'SignupView',
    component: SignupView
  },
  {
    path: '/accounts/MyPageView',
    name: 'MyPageView',
    component: MyPageView
  },


]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
