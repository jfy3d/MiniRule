import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    redirect: '/index',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '/index', name:'index', component: () => import('pages/IndexPage.vue') },
      { path: '/rule/:case_id', name:'rule', component: () => import('pages/RulePage.vue') },
      { path: '/tool', name:'tool', component: () => import('pages/BusinessConfigPage.vue') },
      // { path: '/customer_list', name:'customer_list', component: () => import('pages/CustomerList.vue') },
      // { path: '/order', name:'order', component: () => import('pages/OrderPage.vue') }
    ]
  },


  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
