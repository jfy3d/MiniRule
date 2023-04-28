import { defineStore } from 'pinia';

export const appMenu = defineStore('menus', {
  state: () => ({
    menus: [

      {
        icon: 'o_settings',
        label: '配置工具',
        children: [
          {
            label: '规则配置',
            page: 'index'
          },
          {
            label: '测试工具',
            page: 'tool'
          }
        ]
      }


    ],
  }),
  // getters: {
  //   menus: (state) => state.menus,
  // },
  actions: {
    // increment() {
    // },
  },
});
