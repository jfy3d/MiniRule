<template>
  <q-card style="max-height: 80vh;min-width: 900px;">
    <q-card-section class="row items-center ">
      <div class="text-h6">匹配项</div>
      <q-space />
      <q-btn icon="close" flat round dense v-close-popup />
    </q-card-section>

    <q-separator/>

    <q-card-section class="scroll q-pa-none">
      <div class="row">
        <div class="col-8">
          <q-table
            square
            flat
            :visible-columns="['field', 'description', 'match_type', 'target_type', 'target_value', 'update_time']"
            :rows="rows"
            :columns="columns"
            row-key="id"

            selection="single"
            v-model:selected="selected"
            @row-click="handleSelect"
            class="my-sticky-table-handle"
          >

            <template v-slot:top>
              <div class="">
                <q-btn color="secondary" icon="add" label="新建匹配" unelevated rounded class="l-shadow-2" @click="selected=[];model={}"/>

              </div>
              <q-space/>

            </template>

            <template v-slot:body-cell-handle="props">
              <q-td :props="props">


                <q-btn flat
                       dense
                       round
                       color="red"
                       icon="o_delete_forever"
                       @click="doDelete(props.row.id)"
                       size="md"></q-btn>
              </q-td>
            </template>
          </q-table>
        </div>
        <q-separator vertical/>
        <div class="col q-pl-sm">
          <div class=" q-col-gutter-md">
            <div class="row items-center q-col-gutter-sm">
              <div class="col-4">字段
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-input
                  v-model="model.field" filled square placeholder="请输入字段" dense/>
              </div>

            </div>
            <div class="row items-center q-col-gutter-sm">
              <div class="col-4">描述
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-input
                  v-model="model.description" filled square placeholder="描述" dense/>
              </div>

            </div>
            <div class="row items-center q-col-gutter-sm">
              <div class="col-4">匹配类型
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-select
                  @update:model-value="model.target_type=''"
                  map-options emit-value
                  :options="match_type_option"
                  v-model="model.match_type"
                  filled square placeholder="匹配类型" dense/>
              </div>

            </div>
            <div class="row items-center q-col-gutter-sm">
              <div class="col-4">匹配目标
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-select
                  emit-value
                  map-options
                  :options="model.match_type?target_type_option[model.match_type]:[]"
                  v-model="model.target_type"
                  filled square placeholder="匹配目标" dense/>
              </div>

            </div>
            <div class="row items-center q-col-gutter-sm">
              <div class="col-4">目标值
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-input v-if="model.target_type&&model.target_type=='value'"
                         v-model="model.target_value" filled square placeholder="目标值" dense/>
                <q-input v-if="model.target_type&&model.target_type=='array'"
                         v-model="model.target_value" filled square placeholder="目标数组" dense/>
                <q-input v-if="model.target_type&&model.target_type=='range'"
                         v-model="model.target_value" filled square placeholder="目标范围" dense/>
              </div>

            </div>

            <div class="row items-center q-col-gutter-sm">
              <div class="col-4">序号
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-input type="number"
                         v-model.number="model.flag_index" filled square placeholder="输入序号" dense/>
              </div>

            </div>

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
               @click="doSave"
               class="l-shadow-2"/>
      </div>
    </q-card-actions>
  </q-card>
</template>

<script setup lang="ts">
import {ItemMatch} from '../services/match';
import {onMounted, reactive, ref} from 'vue';
import {useQuasar} from 'quasar';



const match_type_option = reactive([
  {
    label: '存在', value: 'in',
    children: [
      {label: '范围', value: 'range'}
    ]
  },
  {
    label: '不存在', value: 'notin',
    children: [
      {label: '范围', value: 'range'}
    ]
  },
  {
    label: '等于', value: 'equal',
    children: [
      {label: '值', value: 'value'}
    ]
  },
  {
    label: '不等于', value: 'notequal',
    children: [
      {label: '值', value: 'value'}
    ]
  },
  {
    label: '大于等于', value: 'gte',
    children: [
      {label: '值', value: 'value'}
    ]
  },
  {
    label: '大于', value: 'gt',
    children: [
      {label: '值', value: 'value'}
    ]
  },
  {
    label: '小于等于', value: 'lte',
    children: [
      {label: '值', value: 'value'}
    ]
  },
  {
    label: '小于', value: 'lt',
    children: [
      {label: '值', value: 'value'}
    ]
  },
  {
    label: '范围', value: 'range',
    children: [
      {label: '范围', value: 'range'}
    ]
  },
  {
    label: '包含', value: 'contain',
    children: [
      {label: '值', value: 'value'}
    ]
  }
]);
const target_type_option = {
  'in':[{label: '数组', value: 'array'}],
  'notin':[{label: '范围', value: 'range'}],
  'equal':[{label: '值', value: 'value'}],
  'notequal':[{label: '值', value: 'value'}],
  'gte':[{label: '值', value: 'value'}],
  'gt':[{label: '值', value: 'value'}],
  'lte':[{label: '值', value: 'value'}],
  'lt':[{label: '值', value: 'value'}],
  'range':[{label: '范围', value: 'range'}],
  'contain':[{label: '值', value: 'value'}]
};
const selected = ref<any>([]);

const props = defineProps({
  select: Object
});


const model = ref<any>({});
const handleSelect = (evt: any, row: object, index: number) => {
  selected.value = [];
  selected.value.push(row);
  model.value = row;
};

const doSave = ()=>{
  model.value.rule = props.select.id;
  saveItem(model.value)
};

const {columns, rows, loadList, saveItem, deleteItem} = ItemMatch();
onMounted(() => {
  console.log(props)
  loadList({rule_id:props.select.id});
});
const q = useQuasar();
const doDelete = (id:any)=>{


  q.dialog({
    title: '操作确认',
    message: '确认要删除本条记录',
    cancel: '取消',
    persistent: true,
    ok:'确定'
  }).onOk(() => {
    deleteItem(props.select.id,id);
  });
};
</script>

<style scoped>

</style>
