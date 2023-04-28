<template>
  <div class="q-pa-sm full-width full-height">


        <q-table
          title="规则"
          :rows="rows"
          :columns="columns"
          row-key="id"
        :visible-columns="['id','case_name','blank_skip','short_circuit', 'update_time','handle']"
          square
          flat
          class="ll-shadow-2"
        >
          <template v-slot:body-cell-short_circuit="props">
            <q-td :props="props">

              <q-badge :color="props.row.short_circuit==1?'green':'red'" rounded>
                <q-icon :name="props.row.short_circuit==1?'check':'clear'" color="white"/>
              </q-badge>
            </q-td>
          </template>
          <template v-slot:body-cell-blank_skip="props">
            <q-td :props="props">

              <q-badge :color="props.row.blank_skip==1?'green':'red'" rounded>
                <q-icon :name="props.row.blank_skip==1?'check':'clear'" color="white"/>
              </q-badge>
            </q-td>
          </template>

          <template v-slot:body-cell-handle="props">
            <q-td :props="props">

              <q-btn flat
                     dense
                     round
                     color="green"
                     icon="o_play_circle"
                     size="md"
                     @click="openTest(props.row)"
              ></q-btn>

            </q-td>
          </template>
        </q-table>
    <q-dialog v-model="dialog" persistent full-width>
      <q-card>
        <q-card-section>
          <div class="text-h6">规则方案</div>
        </q-card-section>

        <q-separator/>

        <q-card-section class="scroll" style="height: 70vh">
          <q-splitter
            v-model="splitterModel"

          >

            <template v-slot:before>
              <div class="q-pa-md q-gutter-md">
                <q-input dense filled square v-model="fmodel[item.field]" v-for="item in fields"  :label="item.field" :key="item.id"/>
              </div>
            </template>

            <template v-slot:after>
              <div class="q-pa-md">
              </div>
            </template>

          </q-splitter>

        </q-card-section>

        <q-separator/>

        <q-card-actions align="right">
          <div class="q-gutter-x-lg q-pa-sm">
            <q-btn color="white" unelevated text-color="black" rounded label="关闭" style="min-width: 100px" icon="reply"
                   v-close-popup
                   @click="showValue"
                   class="l-shadow-2"/>

            <q-btn color="primary" unelevated label="调用" rounded style="min-width: 100px" icon="send"

                   class="l-shadow-2"/>
          </div>
        </q-card-actions>
      </q-card>
    </q-dialog>
  </div>
</template>

<script lang="ts" setup>
import {defineComponent, onMounted, ref} from 'vue';
import {Case, CaseField} from '../services/case'
const splitterModel = ref(40)
const dialog = ref(false)
const selectItem = ref();
const {dialogEdit, columns, rows, loadList, saveItem, deleteItem} = Case();

const {fields, loadFieldsList} = CaseField()


const fmodel = ref({})

const showValue = ()=>{
  console.log(fmodel);
};

const openTest = (item:any) => {
  selectItem.value = item;
  dialog.value = true;
  loadFieldsList(item.id);

}

onMounted(() => {
  loadList();
});
</script>

<style scoped>

</style>
