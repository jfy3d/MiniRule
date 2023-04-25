<template>
  <div class="q-pa-sm">
    <q-table
      class="ll-shadow-2"
      square
      flat

      title="规则方案"
      :rows="rows"
      :columns="columns"
      row-key="id"

    >
      <template v-slot:top>
        <div class="q-gutter-md">
          <q-btn color="green" icon="add" label="新建" unelevated rounded class="l-shadow-2" @click="openAdd"/>

        </div>
        <q-space/>

        <q-input dense outlined debounce="300" color="primary">
          <template v-slot:append>
            <q-icon name="search"/>
          </template>
        </q-input>
      </template>
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
                 color="primary"
                 icon="o_edit"
                 size="md"
                 @click="openEdit(props.row)"
          ></q-btn>
          <q-btn flat
                 dense
                 round
                 color="green"
                 icon="o_fact_check"
                 size="md"
                 @click="$router.push({name:'rule', params:{case_id:props.row.id}})"
          ></q-btn>
          <q-btn flat
                 dense
                 round
                 color="red"
                 icon="o_delete_forever"
                 size="md"
                 @click="doDelete(props.row.id)"
          ></q-btn>
        </q-td>
      </template>
    </q-table>
    <q-dialog v-model="dialogEdit">
      <q-card>
        <q-card-section>
          <div class="text-h6">规则方案</div>
        </q-card-section>

        <q-separator/>

        <q-card-section style="max-height: 50vh;min-width: 600px" class="scroll">
          <div class="q-gutter-md">
            <div class="row items-center q-col-gutter-sm">
              <div class="col-3">方案名称
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-input
                  v-model="model.case_name" filled square placeholder="请输入用户名" dense/>
              </div>

            </div>
            <div class="row items-center q-col-gutter-sm">

              <div class="col-3">短路

              </div>
              <div class="col-8">
                <q-toggle
                  v-model="model.short_circuit"
                  checked-icon="check"
                  color="green"
                  unchecked-icon="clear"

                  :true-value="1"
                  :false-value="model.short_circuit==null?null:0"
                  :indeterminate-value="-1"
                />
              </div>
            </div>
            <div class="row items-center q-col-gutter-sm">
              <div class="col-3">空值跳过

              </div>
              <div class="col-8">
                <q-toggle
                  v-model="model.blank_skip"
                  checked-icon="check"
                  color="green"
                  unchecked-icon="clear"
                  :true-value="1"
                  :false-value="model.blank_skip==null?null:0"
                  :indeterminate-value="-1"
                />

              </div>

            </div>
          </div>


        </q-card-section>

        <q-separator/>

        <q-card-actions align="right">
          <div class="q-gutter-x-lg q-pa-sm">
            <q-btn color="white" unelevated text-color="black" rounded label="取消" style="min-width: 100px" icon="reply"
                   v-close-popup
                   class="l-shadow-2"/>

            <q-btn color="primary" unelevated label="保存" rounded style="min-width: 100px" icon="save"
                   class="l-shadow-2" @click="saveItem(model)"/>
          </div>
        </q-card-actions>
      </q-card>
    </q-dialog>

  </div>
</template>

<script lang="ts" setup>
import { useQuasar } from 'quasar'

import {Case} from '../services/case';
import {onMounted, reactive, ref} from 'vue';
import {CaseModel} from '../models/model';

const model = ref<any>({})

const {dialogEdit, columns, rows, loadList, saveItem, deleteItem} = Case();

const openAdd = () => {
  model.value = {
    short_circuit: 0,
    blank_skip: 0
  }
  dialogEdit.value = true;
};

const openEdit = (item: any) => {
  model.value = {...item};
  dialogEdit.value = true;
}
onMounted(() => {
  loadList();
});
const q = useQuasar();
const doDelete = (id:number)=>{


  q.dialog({
    title: '操作确认',
    message: '确认要删除本条记录',
    cancel: '取消',
    persistent: true,
    ok:'确定'
  }).onOk(() => {
    deleteItem(id);
  });
};

</script>
<style scoped>

</style>

