import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '@/views/movies/MovieView'
import DetailView from '@/views/movies/DetailView'
import SearchView from '@/views/movies/SearchView'
import GenreView from '@/views/genres/GenreView'
import LoginView from '@/views/accounts/LoginView'
import SignupView from '@/views/accounts/SignupView'
import MyPageView from '@/views/accounts/MyPageView'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movies',
    component: MovieView
  },
  {
    path: '/movies/content/:id',
    name: 'detail',
    component: DetailView
  },
  {
    path: '/movies/search',
    name: 'search',
    component: SearchView
  },
  {
    path: '/genres/:category',
    name: 'genre',
    component: GenreView
  },
  {
    path: '/accounts/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/accounts/signup',
    name: 'signup',
    component: SignupView
  },
  {
    path: '/accounts/mypage',
    name: 'mypage',
    component: MyPageView
  },

]

const router = new VueRouter({
  scrollBehavior() { 
    return { x: 0, y: 0 } 
  },
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
