<template>
  <div class="q-pa-sm">

    <q-card class="ll-shadow-2" square>
      <div class="row">
        <div class="col">
          <q-table
            square
            flat
            title="规则"
            :rows="item_rows"
            :columns="columnsItem"
            row-key="id"
          >
            <template v-slot:top>
              <div class="q-gutter-md q-pt-sm">
                <q-btn color="green" icon="add" label="新建规则" unelevated rounded class="l-shadow-2" @click="openItemAdd"/>

              </div>
              <q-space/>

            </template>

            <template v-slot:body-cell-handle="props">
              <q-td :props="props">
                <q-btn flat
                       dense
                       round
                       color="primary"
                       icon="o_edit"
                       size="md"
                       @click="openItemEdit(props.row)"
                ></q-btn>
                <q-btn flat
                       dense
                       round
                       color="green"
                       icon="o_rule"
                       @click="openMatch(props.row)"
                       size="md"></q-btn>
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
      </div>
    </q-card>

    <q-dialog v-model="dialogItemEdit" persistent>
      <q-card>
        <q-card-section>
          <div class="text-h6">规则</div>
        </q-card-section>

        <q-separator/>

        <q-card-section style="max-height: 50vh;min-width: 600px" class="scroll">
          <div class="q-gutter-md">
            <div class="row items-center q-col-gutter-sm">
              <div class="col-3">规则名称
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-input
                  v-model="itemModel.rule_name" filled square placeholder="请输入规则名称" dense/>
              </div>

            </div>
            <div class="row items-center q-col-gutter-sm">
              <div class="col-3">返回值
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-input
                         v-model.number="itemModel.return_value" filled square placeholder="返回值" dense/>
              </div>

            </div>

            <div class="row items-center q-col-gutter-sm">
              <div class="col-3">最少匹配数
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-input
                  v-model.number="itemModel.min_match_amount" filled square placeholder="最少匹配数" dense/>
              </div>

            </div>

            <div class="row items-center q-col-gutter-sm">
              <div class="col-3">序号
                <q-badge rounded color="red"/>
              </div>
              <div class="col-8">
                <q-input type="number"
                         v-model.number="itemModel.flag_index" filled square placeholder="返回值" dense/>
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
                   class="l-shadow-2" @click="saveItem(itemModel)"/>
          </div>
        </q-card-actions>
      </q-card>
    </q-dialog>
    <q-dialog v-model="dialogMatch" persistent full-width>
      <item-match :select="selectItem"/>
    </q-dialog>
  </div>
</template>

<script lang="ts" setup>
import { useRouter, useRoute } from 'vue-router'

import {Rule} from '../services/rule';
import {onMounted, ref, watch} from 'vue';
import {showErrorNotify} from 'src/common/utils';
import ItemMatch from 'components/ItemMatch.vue';
import {useQuasar} from 'quasar';

const dialogMatch = ref<boolean>(false)
const router = useRouter()
const route = useRoute()
const selected = ref<any>([]);
const model = ref<any>({})
const itemModel = ref<any>({})
const selectItem = ref<any>({})

const {dialogItemEdit, columnsItem, item_rows, loadItemList, saveItem, deleteItem} = Rule();
const handleSelect = (evt:any, row:object, index:number) => {
  selected.value = [];
  selected.value.push(row);
};
const openAdd = () => {
  model.value = {
    version_default: 0
  }

};


const openEdit = (item: any) => {
  model.value = {...item};

}


const openItemAdd = () => {

  itemModel.value = {
    case:route.params.case_id,
    flag_index: 0
  }
  dialogItemEdit.value = true;
};


const openItemEdit = (item: any) => {
  itemModel.value = {...item};
  dialogItemEdit.value = true;
}

const openMatch = (item:any) =>{
  selectItem.value = item;
  dialogMatch.value = true;
};

onMounted(() => {
  loadItemList({case_id:route.params.case_id});
});
// watch(selected,(newValue,oldValue)=>{
//   loadItemList()
// })
const q = useQuasar();
const doDelete = (id:any)=>{


  q.dialog({
    title: '操作确认',
    message: '确认要删除本条记录',
    cancel: '取消',
    persistent: true,
    ok:'确定'
  }).onOk(() => {
    deleteItem(route.params.case_id,id);
  });
};
</script>

