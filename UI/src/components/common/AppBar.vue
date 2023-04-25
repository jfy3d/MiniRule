<template>
  <q-toolbar>
    <q-btn
      flat
      dense
      round
      icon="menu"
      aria-label="Menu"
      @click="doSwitchL"
    />

    <q-toolbar-title style="max-width: 160px">
      MiniRule
    </q-toolbar-title>

    <q-space/>

    <q-btn flat round dense class="q-mr-xs" :icon="$q.fullscreen.isActive ? 'fullscreen_exit' : 'fullscreen'"
           @click="$q.fullscreen.toggle()"/>

    <q-btn flat round dense class="q-mr-xs" icon="o_settings"
           @click="doSwitchR"/>
  </q-toolbar>
</template>

<script lang="ts" setup>
const emit = defineEmits(['switch-left', 'switch-right']);
const doSwitchR = () => {
  emit('switch-right')
}

const doSwitchL = () => {
  emit('switch-left')
}
</script>
