import {api} from 'boot/axios'
import {ref} from 'vue';
import {showSuccessNotify, showErrorNotify} from '../common/utils';

function Rule() {

  const path = '/api/rule/';

  const dialogItemEdit = ref<boolean>(false);

  const columnsItem = [
    {name: 'id', label: 'ID', field: 'id'},
    {name: 'rule_name', label: '规则名', field: 'rule_name', align: 'left'},
    {name: 'return_value', label: '返回值', field: 'return_value'},
    {name: 'min_match_amount', label: '最少匹配数', field: 'min_match_amount'},
    {name: 'flag_index', label: '序号', field: 'flag_index'},
    {name: 'create_time', label: '创建时间', field: 'create_time'},
    {name: 'update_time', label: '修改时间', field: 'update_time'},
    {name: 'handle', label: '操作', field: 'handle'},
  ];
  const item_rows = ref<Array<object>>();
  const loadItemList = (params?: any) => {
    console.log('loadItemList');
    api.get(`${path}?case_id=${params.case_id}`).then(
      res => {
        item_rows.value = res.data
      }
    ).catch(error=>{
      console.log('loadItemList error');
    });
  };
  const saveItem = (params: any) => {
    if ('id' in params) {
      api.put(`${path}${params.id}/`, params).then((res) => {
        showSuccessNotify('保存成功');
        // console.log("oooooooo")
        loadItemList({case_id:params.case});
        dialogItemEdit.value = false;
      }).catch(error => {
        // console.log("eeeeeeee",error)
        showErrorNotify(error.response.data);

      });
    } else {
      api.post(path, params).then((res) => {
        showSuccessNotify('保存成功');
        loadItemList({case_id:params.case})
        dialogItemEdit.value = false;
      }).catch(error => {
        showErrorNotify(error.response.data);
      });
    }

  };

  const deleteItem = (parent_id:any, id:any) => {
    api.delete(`${path}${id}/`).then((res) => {
      showSuccessNotify('保存成功');
      loadItemList({case_id:parent_id})
    }).catch(error => {
      showErrorNotify(error.response.data.blank_skip);
    });
  };

  return {dialogItemEdit, columnsItem, item_rows, loadItemList, saveItem,deleteItem}
}

export {Rule}
