import { createRouter, createWebHistory } from 'vue-router'
import Device from '../pages/device.vue'
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/dashboard' },
    {
      path: '/',
      component: () => import('../layouts/default.vue'),
      children: [
        {
          path: 'dashboard',
          component: () => import('../pages/dashboard.vue'),
        },
        {
          path: 'models',
          component: () => import('../pages/models.vue'),
        },
        {
          path: 'scrapper',
          component: () => import('../pages/scrapper.vue'),
        },
        {
          path: 'details',
          component: () => import('../pages/scrapper.vue'),
        },
        {
          path: 'compte',
          component: () => import('../pages/compte.vue'),
        },
        {
          path: 'typography',
          component: () => import('../pages/typography.vue'),
        },
        {
          path: 'icons',
          component: () => import('../pages/icons.vue'),
        },
        {
          path: '/device/:id', // :id is the dynamic route parameter
          name: 'DeviceDetails',
          component: Device,
          props: true, // Pass route params as props to the component
        },
        {
          path: 'form-layouts',
          component: () => import('../pages/form-layouts.vue'),
        },
      ],
    },
    {
      path: '/',
      component: () => import('../layouts/blank.vue'),
      children: [
        {
          path: 'login',
          component: () => import('../pages/login.vue'),
        },
        {
          path: 'register',
          component: () => import('../pages/register.vue'),
        },
        {
          path: '/:pathMatch(.*)*',
          component: () => import('../pages/[...all].vue'),
        },
      ],
    },
  ],
})

export default router
