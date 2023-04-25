import {api} from 'boot/axios'
import {ref} from 'vue';
import {showSuccessNotify, showErrorNotify} from '../common/utils';

function ItemMatch() {

  const path = '/api/match/';

  const columns = [
    {name: 'id', label: 'ID', field: 'id', hidden:true},
    {name: 'field', label: '字段', field: 'field', align: 'left'},
    {name: 'description', label: '描述', field: 'description'},
    {name: 'match_type', label: '匹配类型', field: 'match_type'},
    {name: 'target_type', label: '目标类型', field: 'target_type'},
    {name: 'target_value', label: '目标值', field: 'target_value'},
    {name: 'flag_index', label: '序号', field: 'flag_index'},
    {name: 'create_time', label: '创建时间', field: 'create_time'},
    {name: 'update_time', label: '修改时间', field: 'update_time'},
    {name: 'handle', label: '操作', field: 'handle', required:true},
  ];
  const rows = ref<Array<object>>();
  const loadList = (params?: any) => {
    api.get(`${path}?rule_id=${params.rule_id}`).then(
      res => {
        rows.value = res.data
      }
    );
  };
  const saveItem = (params: any) => {
    if ('id' in params) {
      api.put(`${path}${params.id}/`, params).then((res) => {
        showSuccessNotify('保存成功');
        loadList({rule_id:params.rule});

      }).catch(error => {

        showErrorNotify(error.response.data);

      });
    } else {
      api.post(path, params).then((res) => {
        showSuccessNotify('保存成功');
        loadList({rule_id:params.rule});

      }).catch(error => {
        showErrorNotify(error.response.data);
      });
    }

  };

  const deleteItem = (parent_id:any, id:any) => {
    api.delete(`${path}${id}/`).then((res) => {
      showSuccessNotify('保存成功');
      loadList({rule_id:parent_id})
    }).catch(error => {
      showErrorNotify(error.response.data.blank_skip);
    });
  };

  return { columns, rows, loadList, saveItem, deleteItem}
}

export {ItemMatch}
